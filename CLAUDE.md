# ml-paper-index で作業するときのルール

設計の背景は README.md の「原則」を参照。ここにはカード・記事を作る作業手順だけを書く。

## 論文カード(papers/)を作るとき

- 論文PDFを取得して `cache/pdfs/<id>.pdf` に保存し、**その本文を読んでから**書く。記憶・要旨・検索スニペットだけで書かない
  (過去に検索スニペットだけで要約を書いて誤引用した事例がある: ssd-anomaly-detection の README「訂正」)。
- `source.pdf_sha256` は `sha256sum cache/pdfs/<id>.pdf` の値をそのまま入れる。
- `quote` はPDFからの逐語コピー(一文以内・300文字以内)。言い換えたものを quote に入れない。言い換えは `statement` に書く。
- `results` の数値は表からそのまま転記し、`quote` には該当する行・セルの文字列を入れる。丸めや単位変換をしない。
- 比較条件が `registry/benchmarks.yaml` の既存IDに**完全に**当てはまらない場合、近いIDを流用せず、新しいIDを提案してユーザーに確認する。
  非公開データや一回限りの設定は `scope: paper-private` にする。
- 新しいタグが必要なら、`registry/tags.yaml` への追加をユーザーに提案してから使う。
- `card.reviewed` は人が本文と照合するまで `false` のまま。
- 作成後は `uv run python scripts/validate.py` がエラー0であることを確認する。

## 記事(articles/)を書くとき

- 地の文は日本語。カード・ID・タグ・引用は英語のまま。
- 地の文に数値を書かない(比較表は生成物を参照する)。
- 論文に由来する主張には `[card-id#c1]` 形式で根拠を付け、そのカードを `depends_on` に入れる。
- 条件の違う論文の数値を比べる文章を書かない。論文をまたぐ優劣は「論文内の勝敗の関係」で述べる。
- `written_at` は書いた日。既存記事を更新したら、反映したカードを `depends_on` に足して `written_at` を更新する。

## 実験カード(experiments/)を作るとき

- `commit` は40文字のハッシュ。値はそのコミット時点のファイルから転記する。
- 新しい実験は `results.json` を出力させて `json_pointer` で指す。既存のREADMEやnotebookからは `locator` に逐語テキストを入れる。
