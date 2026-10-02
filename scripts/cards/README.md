# カード生成スクリプト

論文ごとに、キャッシュしたPDF(`cache/pdfs/<id>.pdf`)のテキストから表の数値を機械的に読み取り、
`papers/<id>.yaml` と `registry/benchmarks.yaml` の該当エントリを生成する。主張(claims)の要約は本文を読んで書いたもの。

```bash
uv run python scripts/cards/arxiv_2106_03253.py   # リポジトリのルートで実行
```

表の行が想定どおりに読めない場合は assert で止まる(黙って誤った値を入れない)。
