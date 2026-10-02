"""新着論文の候補を集めて Markdown の一覧にする(Q8-D)。AIは使わない。

候補の出どころ:
- arXiv: registry/watch.yaml のテーマごとの検索式に合う、直近 lookback_days 日の新着
- Semantic Scholar: 既存カードの論文を引用している、直近 citation_lookback_days 日の論文

既存カードと、過去の候補 Issue に載せた論文は除外する。既存カードを多く引用している候補を上に並べる。
API の失敗はジョブを止めずに一覧の末尾に書く。

使い方:
  uv run python scripts/find_candidates.py                    # 一覧を標準出力へ
  uv run python scripts/find_candidates.py --seen-from-gh --out body.md   # Actions 用
"""

import argparse
import datetime as dt
import json
import os
import re
import subprocess
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from collections import defaultdict
from pathlib import Path

from validate import load_yaml

ATOM = {"a": "http://www.w3.org/2005/Atom"}
UA = "ml-paper-index candidate finder (https://github.com/karahashimanato/ml-paper-index)"
ARXIV_ID = re.compile(r"(\d{4}\.\d{4,5})")


def http_get(url: str, retries: int = 3, wait: float = 5.0) -> bytes:
    headers = {"User-Agent": UA}
    # Semantic Scholar の API キー(任意)。キーなしの共有枠は混雑すると 429 になりやすい。
    if "semanticscholar.org" in url and os.environ.get("S2_API_KEY"):
        headers["x-api-key"] = os.environ["S2_API_KEY"]
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=60) as r:
                return r.read()
        except urllib.error.HTTPError as e:
            if e.code in (429, 500, 502, 503) and attempt + 1 < retries:
                time.sleep(wait * (attempt + 1))
                continue
            raise
    raise RuntimeError("unreachable")


def card_keys(root: Path) -> dict[str, dict]:
    """既存カード: キー(arXiv ID か DOI) -> カード。"""
    keys = {}
    for path in sorted((root / "papers").glob("*.yaml")):
        card = load_yaml(path)
        links = card.get("links") or {}
        if links.get("arxiv"):
            keys["arxiv:" + ARXIV_ID.search(links["arxiv"]).group(1)] = card
        if links.get("doi"):
            keys["doi:" + links["doi"].split("doi.org/")[-1].lower()] = card
    return keys


def seen_from_gh() -> set[str]:
    """過去の候補 Issue(ラベル paper-candidates)に載せた論文のキー。"""
    out = subprocess.run(["gh", "issue", "list", "--label", "paper-candidates", "--state", "all", "--limit", "500", "--json", "body"],
                         capture_output=True, text=True, check=True).stdout
    seen = set()
    for issue in json.loads(out):
        seen |= {"arxiv:" + m for m in re.findall(r"arXiv:(\d{4}\.\d{4,5})", issue["body"])}
        seen |= {"doi:" + m.lower() for m in re.findall(r"doi:(10\.[^\s\]\)]+)", issue["body"])}
    return seen


def arxiv_search(query: str, max_results: int, since: dt.date) -> list[dict]:
    url = "https://export.arxiv.org/api/query?" + urllib.parse.urlencode(
        {"search_query": query, "sortBy": "submittedDate", "sortOrder": "descending", "max_results": max_results})
    root = ET.fromstring(http_get(url))
    out = []
    for e in root.findall("a:entry", ATOM):
        published = dt.date.fromisoformat(e.find("a:published", ATOM).text[:10])
        if published < since:
            continue
        aid = ARXIV_ID.search(e.find("a:id", ATOM).text).group(1)
        out.append({"key": "arxiv:" + aid, "title": " ".join(e.find("a:title", ATOM).text.split()),
                    "authors": [a.find("a:name", ATOM).text for a in e.findall("a:author", ATOM)], "date": published.isoformat()})
    return out


def citing_papers(card_key: str, since: dt.date) -> list[dict]:
    kind, ident = card_key.split(":", 1)
    pid = f"arXiv:{ident}" if kind == "arxiv" else f"DOI:{ident}"
    url = (f"https://api.semanticscholar.org/graph/v1/paper/{urllib.parse.quote(pid)}/citations?"
           + urllib.parse.urlencode({"fields": "title,externalIds,publicationDate,authors", "limit": 1000}))
    data = json.loads(http_get(url, wait=10.0))
    out = []
    for item in data.get("data") or []:
        p = item.get("citingPaper") or {}
        date = p.get("publicationDate")
        if not date or dt.date.fromisoformat(date) < since:
            continue
        ext = p.get("externalIds") or {}
        key = ("arxiv:" + ext["ArXiv"]) if ext.get("ArXiv") else ("doi:" + ext["DOI"].lower()) if ext.get("DOI") else None
        if key:
            out.append({"key": key, "title": " ".join((p.get("title") or "").split()),
                        "authors": [a.get("name", "") for a in p.get("authors") or []], "date": date})
    return out


def link(key: str) -> str:
    kind, ident = key.split(":", 1)
    return f"[arXiv:{ident}](https://arxiv.org/abs/{ident})" if kind == "arxiv" else f"[doi:{ident}](https://doi.org/{ident})"


def collect(root: Path, seen: set[str], today: dt.date):
    cfg = load_yaml(root / "registry" / "watch.yaml")
    cards = card_keys(root)
    excluded = set(cards) | seen
    candidates = defaultdict(dict)  # theme -> key -> candidate
    errors = []

    for theme in cfg["themes"]:
        for q in theme["arxiv_queries"]:
            try:
                for p in arxiv_search(q, cfg["max_per_query"], today - dt.timedelta(days=cfg["lookback_days"])):
                    if p["key"] not in excluded:
                        c = candidates[theme["name"]].setdefault(p["key"], {**p, "cites": [], "keyword": False})
                        c["keyword"] = True
            except Exception as e:  # noqa: BLE001 - 1件の失敗で全体を止めない
                errors.append(f"arXiv 検索に失敗 ({theme['name']}): {e}")
            time.sleep(3.5)  # arXiv API の利用規約: 3秒に1リクエスト

        theme_cards = {k: c for k, c in cards.items() if set(theme["tags"]) & {t for v in c["tags"].values() for t in v}}
        for key, card in theme_cards.items():
            try:
                for p in citing_papers(key, today - dt.timedelta(days=cfg["citation_lookback_days"])):
                    if p["key"] not in excluded:
                        c = candidates[theme["name"]].setdefault(p["key"], {**p, "cites": [], "keyword": False})
                        if card["id"] not in c["cites"]:
                            c["cites"].append(card["id"])
            except Exception as e:  # noqa: BLE001
                errors.append(f"Semantic Scholar の引用取得に失敗 ({card['id']}): {e}")
            time.sleep(1.5)
    # 引用経由の候補は、既存カードを min_citations 本以上引用しているものだけ残す(キーワード一致は常に残す)
    for theme in candidates:
        candidates[theme] = {k: c for k, c in candidates[theme].items() if c["keyword"] or len(c["cites"]) >= cfg["min_citations"]}
    return candidates, errors


def render(candidates, errors, today: dt.date, show: int) -> str:
    total = sum(len(v) for v in candidates.values())
    lines = [f"自動で集めた論文の候補です({today.isoformat()}、AIは使っていません)。",
             "カード化したいものにチェックを付けてください。チェック済みのものは、ローカルの Claude Code で "
             "`uv run python scripts/list_approved.py` を実行して一覧し、カード化します。",
             "",
             "並び順: 既存カードを引用している数が多い順 → 新しい順。「引用」は既存カードの論文を引用していること(2本以上のものだけ)、"
             "「キーワード」は registry/watch.yaml の検索式に合ったことを示します。", ""]
    for theme, cands in candidates.items():
        if not cands:
            continue
        lines.append(f"## {theme}({len(cands)}件)\n")
        ordered = sorted(cands.values(), key=lambda c: (len(c["cites"]), c["date"]), reverse=True)
        for i, c in enumerate(ordered):
            if i == show:
                lines.append(f"\n<details><summary>残り {len(ordered) - show} 件</summary>\n")
            who = ", ".join(c["authors"][:3]) + (" ほか" if len(c["authors"]) > 3 else "")
            why = []
            if c["cites"]:
                why.append(f"引用 {len(c['cites'])}本: " + ", ".join(f"`{x}`" for x in c["cites"]))
            if c["keyword"]:
                why.append("キーワード")
            lines.append(f"- [ ] {link(c['key'])} **{c['title']}** — {who}({c['date']})— {' / '.join(why)}")
        if len(ordered) > show:
            lines.append("\n</details>")
        lines.append("")
    if errors:
        lines.append("## 取得できなかったもの\n")
        lines += [f"- {e}" for e in errors]
        lines.append("")
    return ("\n".join(lines) + "\n") if total or errors else ""


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parent.parent)
    parser.add_argument("--seen-from-gh", action="store_true", help="過去の候補 Issue に載せた論文を除外する(gh CLI が必要)")
    parser.add_argument("--out", type=Path, help="全テーマをまとめた Markdown の出力先(候補が無ければ空ファイル)")
    parser.add_argument("--out-dir", type=Path, help="テーマごとの Markdown を出力するディレクトリ(Issue 本文の文字数上限対策。候補の無いテーマは出力しない)")
    args = parser.parse_args()

    today = dt.date.today()
    seen = seen_from_gh() if args.seen_from_gh else set()
    candidates, errors = collect(args.root, seen, today)
    body = render(candidates, errors, today, load_yaml(args.root / "registry" / "watch.yaml")["show_per_theme"])
    if args.out_dir:
        args.out_dir.mkdir(parents=True, exist_ok=True)
        show = load_yaml(args.root / "registry" / "watch.yaml")["show_per_theme"]
        nonempty = [(t, c) for t, c in candidates.items() if c]
        for i, (theme, cands) in enumerate(nonempty, 1):
            part = render({theme: cands}, errors if i == len(nonempty) else [], today, show)
            assert len(part) < 65000, f"issue body too long for {theme}: {len(part)} chars"
            (args.out_dir / f"{i:02d}.md").write_text(f"<!-- theme: {theme} -->\n" + part, encoding="utf-8")
        if errors and not any(candidates.values()):
            (args.out_dir / "99.md").write_text(render({}, errors, today, show), encoding="utf-8")
    if args.out:
        args.out.write_text(body, encoding="utf-8")
    else:
        sys.stdout.write(body or "候補はありません。\n")
    print(f"{sum(len(v) for v in candidates.values())} candidate(s), {len(errors)} error(s)", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
