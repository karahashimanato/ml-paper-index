"""GitHub Pages 用のサイトのソース(site_src/)を組み立てる。

README.md -> index.md、articles/ と generated/ をコピーし、Markdown 以外のリポジトリ内ファイル
(papers/*.yaml、registry/、scripts/ など)へのリンクを GitHub 上の URL に書き換える。
サイトの生成は mkdocs.yml を使う:  uvx --with mkdocs-material mkdocs build
"""

import json
import re
import shutil
from pathlib import Path

from generate import CITATION_LINK, item_url, load_all

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "site_src"
REPO_URL = "https://github.com/karahashimanato/ml-paper-index/blob/main/"
LINK = re.compile(r"\]\((?!https?://|#|mailto:)([^)\s]+?)((?:\s+\"[^\"]*\")?)\)")


def rewrite(text: str, src: Path) -> str:
    """src(リポジトリ内のパス)からの相対リンクのうち、サイトに含まれないものを GitHub の URL にする。"""
    def sub(m):
        target, title = m.group(1), m.group(2)
        path_part, _, anchor = target.partition("#")
        resolved = (src.parent / path_part).resolve()
        try:
            rel = resolved.relative_to(ROOT)
        except ValueError:
            return m.group(0)
        in_site = rel.suffix == ".md" and (rel.parts[0] in ("articles", "generated") or str(rel) == "README.md")
        if in_site:
            return m.group(0)
        return f"]({REPO_URL}{rel.as_posix()}{('#' + anchor) if anchor else ''}{title})"
    return LINK.sub(sub, text)


def item_summary(item) -> str:
    """ホバーカードに出す1行。主張は statement、結果表の値は「手法 / ベンチマーク / 指標 = 値」。"""
    if item.get("statement"):
        return item["statement"]
    parts = [item.get("method"), item.get("benchmark")]
    head = " / ".join(p for p in parts if p)
    return f"{head} / {item.get('metric', '')} = {item.get('value', '')}".strip(" /")


def embed_citation_cards(text: str, src: Path, cards) -> str:
    """記事が引用している主張だけを JSON にしてページ末尾に埋め込み、サイトでは title 属性を外す。
    表示は site_assets/citation-cards.js が行う(記事ごとに必要な分だけ持つので、全カードを読み込まない)。"""
    depth = len(src.relative_to(ROOT).with_suffix("").parts)  # use_directory_urls: articles/x/y.md -> /articles/x/y/
    to_root = "../" * depth
    data = {}

    def sub(m):
        cid, iid = m.group(1), m.group(2)
        card = cards.get(cid)
        items = {i["id"]: i for i in (card.get("claims") or []) + (card.get("results") or [])} if card else {}
        item = items.get(iid)
        if not item:
            return m.group(0)
        url = item_url(card, item)
        authors = card.get("authors") or []
        data[f"{cid}#{iid}"] = {
            "title": card.get("title", ""),
            "authors": authors[0] + (" et al." if len(authors) > 1 else "") if authors else "",
            "year": card.get("year", ""),
            "version": (card.get("source") or {}).get("version") or card.get("venue") or "",
            "location": item.get("location", ""),
            "page": item.get("page"),
            "summary": item_summary(item),
            "quote": item.get("quote") or item.get("locator") or "",
            "url": url,
            "card": f"{to_root}generated/papers/{cid}/" if card["_kind"] == "paper" else None,
        }
        return f"[{cid}#{iid}]({url})" if url else f"[{cid}#{iid}]"

    text = CITATION_LINK.sub(sub, text)
    if not data:
        return text
    payload = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
    return text.rstrip("\n") + f'\n\n<script id="citation-data" type="application/json">{payload}</script>\n'


def main() -> None:
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir()
    cards = load_all(ROOT)[0]
    for folder in ("articles", "generated"):
        for src in sorted((ROOT / folder).rglob("*.md")):
            dst = OUT / src.relative_to(ROOT)
            dst.parent.mkdir(parents=True, exist_ok=True)
            text = rewrite(src.read_text(encoding="utf-8"), src)
            if folder == "articles":
                text = embed_citation_cards(text, src, cards)
            dst.write_text(text, encoding="utf-8")
    assets = OUT / "assets"
    assets.mkdir()
    for f in (ROOT / "site_assets").iterdir():
        shutil.copy(f, assets / f.name)
    readme = rewrite((ROOT / "README.md").read_text(encoding="utf-8"), ROOT / "README.md")
    (OUT / "index.md").write_text(readme, encoding="utf-8")
    print(f"site sources written to {OUT}")


if __name__ == "__main__":
    main()
