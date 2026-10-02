"""カードから表・勝敗・索引・未反映一覧を生成する(Q6/Q12/Q14)。

数値はカードからそのまま転記し、AIや人が手で書かない。出力先:
- generated/papers/<card-id>.md   論文ごとの結果表(比較条件ごとの列)と論文内の勝敗
- generated/index.md              タグ別のカード一覧・比較条件一覧
- generated/stale.md              記事ごとの未反映カード
- 記事本文の <!-- generated:stale --> ... <!-- /generated:stale --> ブロック

使い方: uv run python scripts/generate.py [--root PATH] [--check]
  --check: 生成物が最新か確認だけする(差分があれば終了コード1)
"""

import argparse
import itertools
import re
import sys
from collections import defaultdict
from pathlib import Path

from validate import FRONT_MATTER, _StrDateLoader, load_yaml

import yaml

STALE_BLOCK = re.compile(r"(<!-- generated:stale -->\n).*?(<!-- /generated:stale -->)", re.DOTALL)
HEADER = "<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->\n\n"


def fmt(v: float) -> str:
    return f"{v:g}"


def load_all(root: Path):
    cards = {}
    for kind, folder in (("paper", "papers"), ("experiment", "experiments")):
        for path in sorted((root / folder).glob("*.yaml")):
            card = load_yaml(path)
            card["_kind"] = kind
            cards[card["id"]] = card
    benchmarks = {b["id"]: b for b in load_yaml(root / "registry" / "benchmarks.yaml").get("benchmarks") or []}
    tags = load_yaml(root / "registry" / "tags.yaml")
    articles = []
    for path in sorted((root / "articles").glob("*/*.md")):
        text = path.read_text(encoding="utf-8")
        m = FRONT_MATTER.match(text)
        articles.append((path, text, yaml.load(m.group(1), Loader=_StrDateLoader) if m else {}))
    return cards, benchmarks, tags, articles


def card_tags(card) -> set[str]:
    return {t for values in card.get("tags", {}).values() for t in values}


def result_tables(card, benchmarks) -> list[str]:
    """比較条件ごとの列。指標と繰り返しプロトコルが同じ比較条件だけを1つの表にまとめる。"""
    by_bench = defaultdict(dict)
    for r in card.get("results") or []:
        by_bench[(r["benchmark"], r["metric"])][r["method"]] = r
    groups = defaultdict(list)
    for (bid, metric) in by_bench:
        b = benchmarks[bid]
        groups[(metric, b["protocol"].get("repetitions", ""))].append((bid, metric))
    out = []
    for (metric, reps), cols in groups.items():
        hib = next(m["higher_is_better"] for m in benchmarks[cols[0][0]]["metrics"] if m["name"] == metric)
        methods = list(dict.fromkeys(m for c in cols for m in by_bench[c]))
        best = {}
        for c in cols:
            vals = [r["value"] for r in by_bench[c].values()]
            best[c] = max(vals) if hib else min(vals)
        out.append(f"#### {metric}({'大きいほど良い' if hib else '小さいほど良い'})\n")
        if reps:
            out.append(f"繰り返し: {reps}\n")
        out.append("| method | " + " | ".join(f"`{c[0]}`" for c in cols) + " |")
        out.append("|---|" + "---|" * len(cols))
        for m in methods:
            cells = []
            for c in cols:
                r = by_bench[c].get(m)
                if r is None:
                    cells.append("–")
                    continue
                s = fmt(r["value"]) + (f" ± {fmt(r['std'])}" if "std" in r else "")
                cells.append(f"**{s}**" if r["value"] == best[c] else s)
            out.append(f"| {m} | " + " | ".join(cells) + " |")
        out.append("")
    return out


def pairwise(card, benchmarks) -> dict[tuple[str, str], list[int]]:
    """同じ比較条件・同じ指標の結果から、手法の組ごとの [勝ち, 引き分け, 負け] を数える。"""
    by_bench = defaultdict(dict)
    for r in card.get("results") or []:
        by_bench[(r["benchmark"], r["metric"])][r["method"]] = r["value"]
    counts = defaultdict(lambda: [0, 0, 0])
    for (bid, metric), vals in by_bench.items():
        hib = next(m["higher_is_better"] for m in benchmarks[bid]["metrics"] if m["name"] == metric)
        for a, b in itertools.combinations(sorted(vals), 2):
            diff = (vals[a] - vals[b]) * (1 if hib else -1)
            idx = 0 if diff > 0 else 1 if diff == 0 else 2
            counts[(a, b)][idx] += 1
    return counts


def paper_page(card, benchmarks) -> str:
    lines = [HEADER + f"# {card['title']}\n",
             f"- カード: [`{card['id']}`](../../{'papers' if card['_kind'] == 'paper' else 'experiments'}/{card['id']}.yaml)",
             f"- 著者: {', '.join(card.get('authors', []))}" if card.get("authors") else "",
             f"- 年・掲載: {card.get('year', '')} {card.get('venue', '')}".rstrip(),
             f"- タグ: {', '.join(sorted(card_tags(card)))}",
             f"- 人手レビュー: {'済' if card['card']['reviewed'] else '未'}\n"]
    if card.get("claims"):
        lines.append("## 主張\n")
        lines += [f"- **{c['id']}** {c['statement']}({c['location']})" for c in card["claims"]]
        lines.append("")
    if card.get("results"):
        lines.append("## 結果表\n")
        lines.append("列ごとに比較条件が異なる。**同じ列の中だけ**比較できる。太字は列内の最良値。\n")
        lines += result_tables(card, benchmarks)
        lines.append("## 論文内の勝敗(結果から導出)\n")
        lines.append("同じ比較条件での数値の大小だけを数えたもの。**統計的有意性は考慮していない**。\n")
        lines.append("| A | B | A勝ち | 引き分け | B勝ち |")
        lines.append("|---|---|---|---|---|")
        for (a, b), (w, t, l) in sorted(pairwise(card, benchmarks).items()):
            lines.append(f"| {a} | {b} | {w} | {t} | {l} |")
        lines.append("")
    if card.get("relations"):
        lines.append("## 論文内の勝敗(本文の記述)\n")
        lines.append("| 勝ち | 負け | 根拠 | 比較条件 | 出典 |")
        lines.append("|---|---|---|---|---|")
        for r in card["relations"]:
            lines.append(f"| {r['winner']} | {r['loser']} | {r['basis']} | {('`' + r['benchmark'] + '`') if r.get('benchmark') else '–'} | {r['location']} |")
        lines.append("")
    return "\n".join(l for l in lines if l is not None) + "\n"


def index_page(cards, benchmarks, tags) -> str:
    lines = [HEADER + "# 索引\n", "## タグ別のカード\n"]
    for kind in ("tasks", "method_families", "paradigms"):
        lines.append(f"### {kind}\n")
        for t in tags.get(kind) or []:
            ids = [c for c in cards if t["id"] in card_tags(cards[c])]
            if ids:
                lines.append(f"- **{t['id']}**: " + ", ".join(f"[{i}](papers/{i}.md)" for i in ids))
        lines.append("")
    lines.append("## 比較条件\n")
    lines.append("| id | scope | task | dataset | 定義した論文 | 結果・勝敗の数 |")
    lines.append("|---|---|---|---|---|---|")
    n_results = defaultdict(int)
    for c in cards.values():
        for r in (c.get("results") or []) + (c.get("relations") or []):
            if r.get("benchmark"):
                n_results[r["benchmark"]] += 1
    for b in benchmarks.values():
        lines.append(f"| `{b['id']}` | {b['scope']} | {b['task']} | {b['dataset']} | {b['defined_in']} | {n_results[b['id']]} |")
    return "\n".join(lines) + "\n"


def stale_for(article_fm, cards) -> list[str]:
    covered = set(article_fm.get("tags") or [])
    deps = set(article_fm.get("depends_on") or [])
    return [cid for cid, c in cards.items() if cid not in deps and card_tags(c) & covered]


def generate(root: Path) -> dict[Path, str]:
    cards, benchmarks, tags, articles = load_all(root)
    out: dict[Path, str] = {}
    for cid, card in cards.items():
        out[root / "generated" / "papers" / f"{cid}.md"] = paper_page(card, benchmarks)
    out[root / "generated" / "index.md"] = index_page(cards, benchmarks, tags)

    lines = [HEADER + "# 未反映カード\n", "記事の `depends_on` に入っていない、記事のタグと重なるカード(Q14)。\n"]
    for path, text, fm in articles:
        stale = stale_for(fm, cards)
        rel = path.relative_to(root)
        lines.append(f"- [{rel}](../{rel}): " + (", ".join(f"`{s}`" for s in stale) if stale else "なし"))
        if STALE_BLOCK.search(text):
            note = (f"> ⚠ この記事の執筆後({fm.get('written_at')})に、関連カードが {len(stale)} 件追加されています(未反映): "
                    + ", ".join(f"`{s}`" for s in stale) + "\n") if stale else "> 未反映のカードはありません。\n"
            out[path] = STALE_BLOCK.sub(lambda m: m.group(1) + note + m.group(2), text)
    out[root / "generated" / "stale.md"] = "\n".join(lines) + "\n"
    return out


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parent.parent)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()

    changed = []
    for path, content in generate(args.root).items():
        if not path.exists() or path.read_text(encoding="utf-8") != content:
            changed.append(path.relative_to(args.root))
            if not args.check:
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(content, encoding="utf-8")
    for p in changed:
        print(f"{'OUTDATED' if args.check else 'wrote'} {p}")
    print(f"{len(changed)} file(s) {'outdated' if args.check else 'written'}")
    return 1 if args.check and changed else 0


if __name__ == "__main__":
    sys.exit(main())
