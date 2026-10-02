"""GitHub Pages 用のサイトのソース(site_src/)を組み立てる。

README.md -> index.md、articles/ と generated/ をコピーし、Markdown 以外のリポジトリ内ファイル
(papers/*.yaml、registry/、scripts/ など)へのリンクを GitHub 上の URL に書き換える。
サイトの生成は mkdocs.yml を使う:  uvx --with mkdocs-material mkdocs build
"""

import re
import shutil
from pathlib import Path

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


def main() -> None:
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir()
    for folder in ("articles", "generated"):
        for src in sorted((ROOT / folder).rglob("*.md")):
            dst = OUT / src.relative_to(ROOT)
            dst.parent.mkdir(parents=True, exist_ok=True)
            dst.write_text(rewrite(src.read_text(encoding="utf-8"), src), encoding="utf-8")
    readme = rewrite((ROOT / "README.md").read_text(encoding="utf-8"), ROOT / "README.md")
    (OUT / "index.md").write_text(readme, encoding="utf-8")
    print(f"site sources written to {OUT}")


if __name__ == "__main__":
    main()
