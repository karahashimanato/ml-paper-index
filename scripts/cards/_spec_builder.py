"""仕様(論文ごとの書誌・タグ・主張)のリストから論文カードを作る共通処理。候補 Issue の一括カード化で使う。

各 spec のキー:
  id, title, authors, year, version            必須(書誌は arXiv API / OpenAlex / PDF の値を書き写す。記憶で書かない)
  venue                                        任意(PDF か公式メタデータで確認できたものだけ)
  links                                        dict(arxiv / doi / code / url)
  pdf_url, license                             任意(arXiv 以外の PDF の取得元とライセンス)
  tasks, fam, par                              タグ(registry/tags.yaml に登録済みのものだけ)
  proposes                                     list
  claims                                       [(statement, location, quote[, page])]  quote は PDF からの逐語コピー
  notes                                        任意(カードの注記)
"""

import sys

sys.path.insert(0, "scripts/cards")
from _common import Paper, write_card  # noqa: E402


def build(specs: list[dict], base_note: str, created_at: str = "2026-10-02",
          created_by: str = "claude-opus-5-5 via Claude Code (subagent)") -> None:
    for spec in specs:
        P = Paper(spec["id"])
        source = {"version": spec["version"], "retrieved_at": spec.get("retrieved_at", created_at), "pdf_sha256": P.sha256()}
        for k in ("pdf_url", "license"):
            if spec.get(k):
                source[k] = spec[k]
        card = {
            "id": spec["id"], "title": spec["title"], "authors": spec["authors"], "year": spec["year"],
            **({"venue": spec["venue"]} if spec.get("venue") else {}),
            "links": spec["links"],
            "source": source,
            "tags": {"tasks": spec["tasks"], "method_families": spec["fam"], **({"paradigms": spec["par"]} if spec.get("par") else {})},
            "proposes": spec.get("proposes", []),
            "claims": P.claims(spec["claims"]),
            "results": [], "relations": [],
            "card": {"created_at": created_at, "created_by": created_by, "reviewed": False,
                     "notes": base_note + ((" " + spec["notes"]) if spec.get("notes") else "")},
        }
        write_card(card)
        print(spec["id"], len(card["claims"]), "claims")
