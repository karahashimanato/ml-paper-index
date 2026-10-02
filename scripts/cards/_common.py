"""カード生成スクリプトの共通処理。リポジトリのルートから実行する前提。"""

import hashlib
import sys

import pymupdf
import yaml

sys.path.insert(0, "scripts")
from verify_quotes import match, variants  # noqa: E402


class Paper:
    def __init__(self, card_id: str):
        self.id = card_id
        self.pdf = f"cache/pdfs/{card_id}.pdf"
        doc = pymupdf.open(self.pdf)
        self._raw = [p.get_text() for p in doc]
        self._pages = [variants(t) for t in self._raw]

    def text(self, page: int) -> str:
        """空白を1つに正規化したページテキスト(1始まり)。"""
        return " ".join(self._raw[page - 1].split())

    def lines(self, page: int) -> list[str]:
        return [l.strip() for l in self._raw[page - 1].splitlines() if l.strip()]

    def page_of(self, quote: str, page: int | None = None) -> int:
        """引用がちょうど1ページで完全一致することを確認してページ番号を返す。
        本文と付録に同じ文があるときは page で明示する(そのページにあることは確認する)。"""
        hits = [i + 1 for i, p in enumerate(self._pages) if match(quote, [p]) == "exact"]
        if page is not None:
            assert page in hits, (quote, page, hits)
            return page
        assert len(hits) == 1, (quote, hits)
        return hits[0]

    def sha256(self) -> str:
        return hashlib.sha256(open(self.pdf, "rb").read()).hexdigest()

    def claims(self, items) -> list[dict]:
        """(statement, location, quote[, page]) のリストから claims を作る。順番が ID(c1, c2, ...) になるので、追加は末尾にだけ行う。"""
        return [{"id": f"c{i}", "statement": it[0], "location": it[1], "page": self.page_of(it[2], *it[3:]), "quote": it[2]}
                for i, it in enumerate(items, 1)]


def write_card(card: dict) -> None:
    yaml.safe_dump(card, open(f"papers/{card['id']}.yaml", "w"), sort_keys=False, allow_unicode=True, width=200)


def register(card_id: str, entries: list[dict]) -> None:
    """registry/benchmarks.yaml から card_id が定義したエントリを置き換える(先頭のコメントは保持)。"""
    path = "registry/benchmarks.yaml"
    doc = yaml.safe_load(open(path)) or {}
    doc["benchmarks"] = [b for b in (doc.get("benchmarks") or []) if b["defined_in"] != card_id] + entries
    header = "".join(l for l in open(path) if l.startswith("#"))
    open(path, "w").write(header + yaml.safe_dump(doc, sort_keys=False, allow_unicode=True, width=200))
