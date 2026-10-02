"""カード・登録簿・記事の整合性チェック。

スキーマ検証に加えて、スキーマでは表せない参照整合性を確認する:
- ファイル名 = カードID
- タグ・比較条件ID・指標名が登録簿に存在する
- paper-private な比較条件は、それを定義した論文カードからしか使えない
- 記事の depends_on と本文中の [card-id#cN] 参照が実在する

使い方: uv run python scripts/validate.py [--root PATH]
"""

import argparse
import json
import re
import sys
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator, FormatChecker


class _StrDateLoader(yaml.SafeLoader):
    """日付を date 型に変換せず文字列のまま読む(スキーマは format: date の文字列を期待するため)。"""


_StrDateLoader.yaml_implicit_resolvers = {
    ch: [(tag, rx) for tag, rx in resolvers if tag != "tag:yaml.org,2002:timestamp"]
    for ch, resolvers in yaml.SafeLoader.yaml_implicit_resolvers.items()
}

FRONT_MATTER = re.compile(r"\A---\n(.*?)\n---\n", re.DOTALL)
CITATION = re.compile(r"\[((?:arxiv|doi|exp)-[^\]#\s]+)#([cr][0-9]+)\]")


def load_yaml(path: Path):
    return yaml.load(path.read_text(encoding="utf-8"), Loader=_StrDateLoader)


def load_schema(root: Path, name: str) -> Draft202012Validator:
    schema = json.loads((root / "schemas" / name).read_text(encoding="utf-8"))
    return Draft202012Validator(schema, format_checker=FormatChecker())


def schema_errors(validator: Draft202012Validator, data, where: str) -> list[str]:
    return [
        f"{where}: {'/'.join(map(str, e.absolute_path)) or '(root)'}: {e.message}"
        for e in validator.iter_errors(data)
    ]


def duplicates(values) -> set:
    seen, dup = set(), set()
    for v in values:
        (dup if v in seen else seen).add(v)
    return dup


def validate(root: Path) -> list[str]:
    errors: list[str] = []

    # --- タグ語彙 ---
    tags_path = root / "registry" / "tags.yaml"
    tags = load_yaml(tags_path)
    errors += schema_errors(load_schema(root, "tags.schema.json"), tags, "registry/tags.yaml")
    tag_ids: dict[str, set[str]] = {}
    for kind in ("tasks", "method_families", "paradigms"):
        entries = (tags or {}).get(kind) or []
        ids = [t.get("id") for t in entries]
        tag_ids[kind] = set(ids)
        for d in duplicates(ids):
            errors.append(f"registry/tags.yaml: duplicate {kind} id '{d}'")
        for t in entries:
            if "parent" in t and t["parent"] not in tag_ids[kind] | set(ids):
                errors.append(f"registry/tags.yaml: {kind} '{t['id']}' has unknown parent '{t['parent']}'")
    all_tags = set().union(*tag_ids.values())

    def check_tags(card_tags: dict, where: str):
        for kind, values in (card_tags or {}).items():
            for v in values:
                if v not in tag_ids.get(kind, set()):
                    errors.append(f"{where}: unknown {kind} tag '{v}' (add it to registry/tags.yaml first)")

    # --- 比較条件の登録簿 ---
    bench_doc = load_yaml(root / "registry" / "benchmarks.yaml")
    errors += schema_errors(load_schema(root, "benchmarks.schema.json"), bench_doc, "registry/benchmarks.yaml")
    benchmarks = {b["id"]: b for b in (bench_doc or {}).get("benchmarks") or [] if "id" in b}
    for d in duplicates(b.get("id") for b in (bench_doc or {}).get("benchmarks") or []):
        errors.append(f"registry/benchmarks.yaml: duplicate id '{d}'")
    for b in benchmarks.values():
        if b.get("task") not in tag_ids["tasks"]:
            errors.append(f"registry/benchmarks.yaml: '{b['id']}' has unknown task tag '{b.get('task')}'")

    def check_result(r: dict, where: str, card_id: str, is_paper: bool):
        b = benchmarks.get(r.get("benchmark"))
        if b is None:
            errors.append(f"{where}: unknown benchmark '{r.get('benchmark')}' (register it in registry/benchmarks.yaml)")
            return
        metric_names = {m["name"] for m in b.get("metrics", [])}
        if r.get("metric") not in metric_names:
            errors.append(f"{where}: metric '{r.get('metric')}' not defined for benchmark '{b['id']}' {sorted(metric_names)}")
        if b.get("scope") == "paper-private" and (not is_paper or b.get("defined_in") != card_id):
            errors.append(f"{where}: benchmark '{b['id']}' is paper-private to '{b.get('defined_in')}'")

    # --- 論文カード ---
    card_items: dict[str, set[str]] = {}  # card id -> {c1, r1, ...}
    paper_schema = load_schema(root, "paper-card.schema.json")
    for path in sorted((root / "papers").glob("*.yaml")):
        where = f"papers/{path.name}"
        card = load_yaml(path)
        errors += schema_errors(paper_schema, card, where)
        if not isinstance(card, dict):
            continue
        if card.get("id") != path.stem:
            errors.append(f"{where}: id '{card.get('id')}' does not match file name")
        check_tags(card.get("tags"), where)
        item_ids = [c.get("id") for c in card.get("claims") or []] + [r.get("id") for r in card.get("results") or []]
        for d in duplicates(item_ids):
            errors.append(f"{where}: duplicate claim/result id '{d}'")
        for r in card.get("results") or []:
            check_result(r, f"{where}: result {r.get('id')}", path.stem, is_paper=True)
        for rel in card.get("relations") or []:
            if "benchmark" in rel and rel["benchmark"] not in benchmarks:
                errors.append(f"{where}: relation uses unknown benchmark '{rel['benchmark']}'")
        card_items[path.stem] = set(item_ids)

    for b in benchmarks.values():
        if b.get("defined_in") not in card_items:
            errors.append(f"registry/benchmarks.yaml: '{b['id']}' defined_in '{b.get('defined_in')}' has no paper card")

    # --- 実験カード ---
    exp_schema = load_schema(root, "experiment-card.schema.json")
    for path in sorted((root / "experiments").glob("*.yaml")):
        where = f"experiments/{path.name}"
        card = load_yaml(path)
        errors += schema_errors(exp_schema, card, where)
        if not isinstance(card, dict):
            continue
        if card.get("id") != path.stem:
            errors.append(f"{where}: id '{card.get('id')}' does not match file name")
        check_tags(card.get("tags"), where)
        item_ids = [r.get("id") for r in card.get("results") or []]
        for d in duplicates(item_ids):
            errors.append(f"{where}: duplicate result id '{d}'")
        for r in card.get("results") or []:
            check_result(r, f"{where}: result {r.get('id')}", path.stem, is_paper=False)
        card_items[path.stem] = set(item_ids)

    # --- 記事 ---
    article_schema = load_schema(root, "article-frontmatter.schema.json")
    for path in sorted((root / "articles").glob("*/*.md")):
        where = str(path.relative_to(root))
        text = path.read_text(encoding="utf-8")
        m = FRONT_MATTER.match(text)
        if not m:
            errors.append(f"{where}: missing YAML front matter")
            continue
        fm = yaml.load(m.group(1), Loader=_StrDateLoader)
        errors += schema_errors(article_schema, fm, where)
        if not isinstance(fm, dict):
            continue
        for t in fm.get("tags") or []:
            if t not in all_tags:
                errors.append(f"{where}: unknown tag '{t}'")
        for dep in fm.get("depends_on") or []:
            if dep not in card_items:
                errors.append(f"{where}: depends_on '{dep}' has no card")
        for card_id, item in CITATION.findall(text[m.end():]):
            if card_id not in card_items:
                errors.append(f"{where}: citation [{card_id}#{item}] refers to a missing card")
            elif item not in card_items[card_id]:
                errors.append(f"{where}: citation [{card_id}#{item}] refers to a missing claim/result")
            elif card_id not in (fm.get("depends_on") or []):
                errors.append(f"{where}: citation [{card_id}#{item}] is not listed in depends_on")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parent.parent)
    args = parser.parse_args()

    errors = validate(args.root)
    for e in errors:
        print(f"ERROR {e}")
    print(f"{len(errors)} error(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
