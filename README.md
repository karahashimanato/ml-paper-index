# ml-paper-index

機械学習アルゴリズム(MLOpsのアルゴリズムを含む)の研究動向と手法比較を、**論文を一次情報として**整理するインデックス。

姉妹プロジェクトとの役割分担:

| リポジトリ | 何を引くか | 一次情報 |
|---|---|---|
| [library-dictionary](https://github.com/karahashimanato/library-dictionary) | ライブラリのAPI | 実際に実行した結果 |
| [bayesian-analysis-index](https://github.com/karahashimanato/bayesian-analysis-index) | 自分のベイズ分析で得た手法・失敗パターン | 各プロジェクトのREADME |
| **ml-paper-index**(ここ) | アルゴリズムの比較・系譜・研究動向 | 論文本文(+自分の実験結果を別枠で) |

## 原則

1. **論文本文を読んで書く**。記憶や検索スニペットからは書かない。主張・数値には必ず出典箇所(Table/Section)と短い原文引用(一文以内)を付ける。
2. **同一条件の数値だけを比較する**。比較できる条件は [registry/benchmarks.yaml](registry/benchmarks.yaml) に明示的に登録したものだけ。条件の違う数値は表に並べない。
3. **論文をまたいで比較できないときは、論文内の勝敗の関係で語る**。数値ではなく「論文Xの中でAがBに勝った」という向きを集める。
4. **自分の実験は論文と混ぜない**。`experiments/` に別のカードとして置き、コミットハッシュで固定する。
5. **数値はAIに書かせない**。比較表はカードからスクリプトで生成する(予定)。記事の地の文に数値を書かない。
6. **古さを隠さない**。記事は執筆時に依存したカードと執筆日を記録し、その後に追加されたカードを「未反映」として表示する(予定)。

## 構成

```
papers/            論文カード(唯一の一次情報、英語)        papers/<id>.yaml
experiments/       自分の実験カード(英語)                  experiments/exp-<name>.yaml
registry/
  benchmarks.yaml  比較条件の登録簿
  tags.yaml        タグの統制語彙(課題・手法ファミリー・学習の枠組み)
articles/
  tasks/           課題別の比較記事(日本語)
  methods/         手法ファミリー別の解説・系譜記事(日本語)
schemas/           上記すべてのJSON Schema
templates/         カード・登録簿エントリ・記事のテンプレート
scripts/           検証・生成スクリプト
cache/pdfs/        論文PDFのローカルキャッシュ(gitignore、公開しない)
```

## 使い方

```bash
uv sync
uv run python scripts/validate.py   # スキーマ・参照整合性のチェック
```

`validate.py` が確認すること: スキーマ、ファイル名とIDの一致、未登録のタグ・比較条件・指標の使用、
他論文の paper-private 条件の使用、記事の `depends_on` と本文中の `[card-id#c1]` 参照の実在。

## 現在のテーマ

| テーマ | 状態 |
|---|---|
| 表データの分類・回帰(GBDT vs 深層学習) | パイロット(準備中) |

## 今後の実装予定

- 原文引用の照合(`cache/pdfs/` のPDFに引用文が存在するか、sha256が一致するか)
- 実験カードの照合(指定コミットのファイルに値が存在するか)
- 比較表・勝敗表・タグ別索引・「未反映カード」一覧の生成
- 新着論文の候補検出(GitHub Actions の cron、AI不使用)
- 静的サイト化(GitHub Pages)
