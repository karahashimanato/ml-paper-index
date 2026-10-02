"""候補 Issue でチェックが付いた(承認された)論文のうち、まだカードになっていないものを一覧する。

使い方: uv run python scripts/list_approved.py   (gh CLI でこのリポジトリにアクセスできること)
"""

import json
import re
import subprocess
import sys
from pathlib import Path

from find_candidates import card_keys

CHECKED = re.compile(r"^- \[[xX]\] \[(arXiv:\d{4}\.\d{4,5}|doi:10\.[^\]]+)\]\(([^)]+)\) \*\*(.+?)\*\*", re.M)


def main() -> int:
    root = Path(__file__).resolve().parent.parent
    carded = set(card_keys(root))
    issues = json.loads(subprocess.run(
        ["gh", "issue", "list", "--label", "paper-candidates", "--state", "all", "--limit", "500", "--json", "number,title,body"],
        capture_output=True, text=True, check=True).stdout)
    rows, seen = [], set()
    for issue in issues:
        for ident, url, title in CHECKED.findall(issue["body"]):
            key = ident.replace("arXiv:", "arxiv:").lower() if ident.startswith("doi:") else ident.replace("arXiv:", "arxiv:")
            if key in carded or key in seen:
                continue
            seen.add(key)
            rows.append(f"#{issue['number']}  {ident}  {title}  {url}")
    print("\n".join(rows) if rows else "承認済みでカード未作成の候補はありません。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
