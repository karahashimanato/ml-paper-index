"""論文カードの quote が、ローカルにキャッシュしたPDFに実在するかを照合する(Q10)。

- cache/pdfs/<id>.pdf の sha256 がカードの source.pdf_sha256 と一致するか
- 各 claim / result / relation の quote が本文に存在するか(page があればそのページに)

PDF抽出テキストの揺れ(合字・行末ハイフン・引用符・空白)は正規化して吸収する。
空白の違いまで無視しないと一致しないもの(表のセルなど)は "loose" として区別して報告する。
PDF が無いカードはスキップする(公開リポジトリにはPDFを置かないため、CIでは照合できない)。

使い方: uv run python scripts/verify_quotes.py [--root PATH] [card-id ...]
"""

import argparse
import hashlib
import re
import sys
import unicodedata
from pathlib import Path

import pymupdf

from validate import load_yaml

_PUNCT = str.maketrans({"‘": "'", "’": "'", "“": '"', "”": '"', "–": "-", "—": "-", "−": "-"})


def normalize(text: str, keep_hyphen: bool, join_hyphen: bool = True) -> str:
    text = unicodedata.normalize("NFKC", text).translate(_PUNCT)
    # 行末ハイフンは「単語の分割」「複合語のハイフン」「並列のハイフン(attention- and)」がありうるので、呼び出し側で全て試す
    if join_hyphen:
        text = re.sub(r"(?<=[A-Za-z])-\s*\n\s*", "-" if keep_hyphen else "", text)
    return re.sub(r"\s+", " ", text).strip()


def variants(text: str) -> list[str]:
    return [normalize(text, keep_hyphen=False), normalize(text, keep_hyphen=True), normalize(text, keep_hyphen=True, join_hyphen=False)]


def match(quote: str, pages: list[list[str]]) -> str | None:
    """'exact' / 'hyphen' / 'loose' / None を返す。pages は各ページの正規化テキストの候補。
    'hyphen': ハイフンの有無だけが違う(1つの引用に「単語分割の行末ハイフン」と「複合語の行末ハイフン」が混在する場合)。"""
    q = normalize(quote, keep_hyphen=True)
    if any(q in v for page in pages for v in page):
        return "exact"
    q_nohyphen = q.replace("-", "")
    if any(q_nohyphen in v.replace("-", "") for page in pages for v in page):
        return "hyphen"
    q_loose = re.sub(r"\s", "", q)
    if any(q_loose in re.sub(r"\s", "", v) for page in pages for v in page):
        return "loose"
    return None


def verify_card(root: Path, card: dict) -> tuple[list[str], dict[str, int]]:
    errors: list[str] = []
    stats = {"exact": 0, "hyphen": 0, "loose": 0, "missing": 0}
    pdf = root / "cache" / "pdfs" / f"{card['id']}.pdf"
    sha = hashlib.sha256(pdf.read_bytes()).hexdigest()
    if sha != card["source"]["pdf_sha256"]:
        errors.append(f"{card['id']}: cached PDF sha256 {sha[:12]}… != card {card['source']['pdf_sha256'][:12]}… (different version?)")
        return errors, stats

    with pymupdf.open(pdf) as doc:
        pages = [variants(p.get_text()) for p in doc]

    items = [("claim", c) for c in card.get("claims") or []]
    items += [("result", r) for r in card.get("results") or []]
    items += [("relation", r) for r in card.get("relations") or []]
    for kind, item in items:
        label = f"{card['id']}: {kind} {item.get('id', item.get('winner', '?'))}"
        page = item.get("page")
        if page is not None and not 1 <= page <= len(pages):
            errors.append(f"{label}: page {page} out of range (1-{len(pages)})")
            continue
        found = match(item["quote"], [pages[page - 1]] if page else pages)
        if found is None:
            where = f"page {page}" if page else "the PDF"
            hint = " (found on another page)" if page and match(item["quote"], pages) else ""
            errors.append(f"{label}: quote not found on {where}{hint}: {item['quote']!r}")
            stats["missing"] += 1
        else:
            stats[found] += 1
    return errors, stats


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parent.parent)
    parser.add_argument("ids", nargs="*", help="card ids to check (default: all)")
    args = parser.parse_args()

    errors: list[str] = []
    for path in sorted((args.root / "papers").glob("*.yaml")):
        if args.ids and path.stem not in args.ids:
            continue
        card = load_yaml(path)
        if not (args.root / "cache" / "pdfs" / f"{path.stem}.pdf").exists():
            print(f"SKIP  {path.stem}: no cached PDF")
            continue
        card_errors, stats = verify_card(args.root, card)
        errors += card_errors
        status = "FAIL" if card_errors else "OK  "
        print(f"{status}  {path.stem}: exact={stats['exact']} hyphen={stats['hyphen']} loose={stats['loose']} missing={stats['missing']}")
    for e in errors:
        print(f"ERROR {e}")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
