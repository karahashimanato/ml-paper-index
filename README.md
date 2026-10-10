# ml-paper-index

**サイト**: https://karahashimanato.github.io/ml-paper-index/ (記事・論文ページ・索引を検索付きで閲覧できる)

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
5. **数値はAIに書かせない**。表の数値はPDFのテキストから機械的に読み取ってカードに入れ、比較表はカードからスクリプトで生成する。記事の地の文に結果の数値を書かない。
6. **古さを隠さない**。記事は執筆時に依存したカードと執筆日を記録し、その後に追加されたカードを「未反映」として記事冒頭に自動表示する。

## 構成

```
papers/            論文カード(唯一の一次情報、英語)        papers/<id>.yaml
experiments/       自分の実験カード(英語)                  experiments/exp-<name>.yaml
registry/
  benchmarks.yaml  比較条件の登録簿
  tags.yaml        タグの統制語彙(課題・手法ファミリー・学習の枠組み)
articles/
  tasks/           課題別の比較記事(日本語)
  topics/          テーマを横断する記事(日本語)
  methods/         手法ファミリー別の解説・系譜記事(日本語)
generated/         カードから生成した結果表・勝敗・索引・未反映一覧(手で編集しない)
schemas/           上記すべてのJSON Schema
templates/         カード・登録簿エントリ・記事のテンプレート
scripts/           検証・生成スクリプト
cache/pdfs/        論文PDFのローカルキャッシュ(gitignore、公開しない)
```

## 使い方

```bash
uv sync
uv run python scripts/validate.py        # スキーマ・参照整合性のチェック(CIでも実行)
uv run python scripts/verify_quotes.py   # 引用がPDFに実在するかの照合(ローカルのみ、cache/pdfs/ が必要)
uv run python scripts/generate.py        # generated/ と記事の未反映ブロックを更新(CIでは --check)
```

| スクリプト | 確認・生成するもの |
|---|---|
| `validate.py` | スキーマ、ファイル名とIDの一致、未登録のタグ・比較条件・指標、他論文の paper-private 条件の使用、結果の値が引用中に現れるか、記事の `depends_on` と `[card-id#c1]` 参照の実在 |
| `verify_quotes.py` | キャッシュしたPDFのsha256がカードと一致するか、各引用が(指定ページの)本文に存在するか、`location` の節番号がPDFに見出しか参照として実在するか |
| `generate.py` | 論文ごとの結果表(比較条件ごとの列)、論文内の勝敗(結果からの導出+本文の記述)、タグ別索引、未反映カード |

## 現在のテーマ

| テーマ | 状態 |
|---|---|
| 表データの分類・回帰(GBDT vs 深層学習 vs 基盤モデル) | 論文カード104本(2021〜2026。TabArena 上位モデルの原論文と、候補 Issue #1 で承認した2026年の論文)、記事 [articles/tasks/tabular-gbdt-vs-deep-learning.md](articles/tasks/tabular-gbdt-vs-deep-learning.md) |
| ドリフト検出(概念ドリフト・データシフト・変化点検出、MLOps) | 論文カード19本(2019〜2026、教師なし検出器と候補 Issue #2 の承認分を含む)、記事 [articles/tasks/drift-detection.md](articles/tasks/drift-detection.md) |
| 時系列の異常検知 | 論文カード23本(2020〜2026、評価方法の批判とベンチマーク)、記事 [articles/tasks/time-series-anomaly-detection.md](articles/tasks/time-series-anomaly-detection.md) |
| モデルの解釈可能性 | 論文カード15本(LIME・SHAP・Integrated Gradients・その検証と批判)、記事 [articles/topics/model-interpretability.md](articles/topics/model-interpretability.md) |
| 量子化・モデル圧縮 | 論文カード20本(LLM の量子化手法・その影響の評価・表データ基盤モデルの圧縮)、記事 [articles/topics/quantization-effects.md](articles/topics/quantization-effects.md) |
| 時系列基盤モデルと時系列予測 | 論文カード22本(Chronos・TimesFM・Moirai などの原論文、LLM 転用の検証、GIFT-Eval)、記事 [articles/topics/time-series-foundation-models.md](articles/topics/time-series-foundation-models.md) |
| 学習モデルと計算量 | 論文カード24本(スケーリング則、計算最適な学習とその再検証、創発と逆スケーリング、推論時の計算、計算コストの測り方、効率化アーキテクチャ)、記事 [articles/topics/compute-and-scaling.md](articles/topics/compute-and-scaling.md) |
| 古典アルゴリズムと機械学習 | 論文カード25本(学習済みインデックス、予測つきアルゴリズム、微分可能なソート、アルゴリズムの学習、機械学習の中の貪欲法)、記事 [articles/topics/algorithms-and-ml.md](articles/topics/algorithms-and-ml.md) |
| アルゴリズム設計技法と機械学習 | 論文カード25本+既存4本(分割統治・動的計画・分枝限定・局所探索と機械学習、学習した組合せ最適化の再検証)、記事 [articles/topics/design-techniques-and-ml.md](articles/topics/design-techniques-and-ml.md) |
| 予測モデルのフォールバックとモデル選択 | 論文カード21本+既存3本(メタ学習によるモデル選択、動的選択、予測の保留と委譲、切り替えの引き金、LLM のルーティング、MLOps の監視と入れ替え)、記事 [articles/topics/model-fallback-and-selection.md](articles/topics/model-fallback-and-selection.md) |
| オートエンコーダ | 論文カード24本+既存4本(正則化オートエンコーダの理論、VAE と事後崩壊、KL 項の代わりの正則化、disentanglement の再検証、再構成誤差による異常検知とその信頼性)、記事 [articles/methods/autoencoders.md](articles/methods/autoencoders.md) |
| 勾配ブースティング木 | 論文カード12本+既存6本(関数空間の勾配降下と正則化、XGBoost・CatBoost の設計、サンプリング、DART・区分線形の木・EBM、チューニング、予測分布と不確実性)、記事 [articles/methods/gradient-boosted-trees.md](articles/methods/gradient-boosted-trees.md) |
| ランダムフォレストと決定木 | 論文カード12本+既存6本(最適な決定木、ランダムフォレストの理論の範囲、効く理由の3つの説明、チューニング、変数重要度の偏り、因果フォレスト)、記事 [articles/methods/random-forests-and-decision-trees.md](articles/methods/random-forests-and-decision-trees.md) |
| 拡散モデル | 論文カード21本+既存4本(DDPM・スコアベース・SDE、尤度とサンプルの質、VAE とのつながり、サンプリングの高速化と蒸留、ガイダンス、潜在拡散、FID の問題、学習データの記憶と複製)、記事 [articles/methods/diffusion-models.md](articles/methods/diffusion-models.md) |
| 対照学習・自己教師あり表現学習 | 論文カード22本(対照学習と負例の集め方、負例を使わない方法と崩壊の防止、マスク予測、理論の仮定、線形評価の頑健性と転移の再検証)、記事 [articles/methods/self-supervised-representation-learning.md](articles/methods/self-supervised-representation-learning.md) |
| 不確実性の推定と較正 | 論文カード17本+既存7本(データとモデルの不確実性、MC dropout とアンサンブル、cold posterior、較正の再検証と ECE の測り方、温度スケーリングの先、conformal prediction の保証と分布の変化)、記事 [articles/topics/uncertainty-and-calibration.md](articles/topics/uncertainty-and-calibration.md) |
| 異常検知(古典 vs 深層) | 論文カード15本+既存8本(設定の違い、大規模ベンチマーク、孤立型、自己教師ありの変換型、1クラス・半教師あり・補助の外れ値、事前学習の特徴を使う画像の手法、閾値と評価の落とし穴)、記事 [articles/topics/anomaly-detection-classical-vs-deep.md](articles/topics/anomaly-detection-classical-vs-deep.md) |
| ベイズ最適化とハイパーパラメータ最適化 | 論文カード17本+既存6本(代理モデルと獲得関数、GP-UCB の理論の前提、Hyperband・BOHB・ASHA・FABOLAS、規模を上げる工夫とフレームワーク、ランダム探索との比較とベンチマーク、過剰な調整と探索空間の設計)、記事 [articles/methods/bayesian-optimization.md](articles/methods/bayesian-optimization.md) |
| ベイズ変化点検知 | 論文カード18本(BOCPD とその拡張、ハザードと事前分布、外れ値への頑健化、バンディット・強化学習・障害の原因分析への応用、オフラインの事後分析と信用集合、TCPDBench による評価)、記事 [articles/topics/bayesian-change-point-detection.md](articles/topics/bayesian-change-point-detection.md) |
| 近似ベイズ推論とその診断 | 論文カード18本+既存3本(HMC と NUTS、確率的勾配 MCMC、変分推論とその弱点、正規化フローと Pathfinder、R-hat の改訂、PSIS の k-hat、VI の誤差の上界、SBC とその検定量、ベイズのワークフロー)、記事 [articles/methods/approximate-inference-and-diagnostics.md](articles/methods/approximate-inference-and-diagnostics.md) |

件数はタスクタグで数えたもので、複数のテーマに数えられるカードがある。全体では470本。
自動取得できず未カード化の承認済み論文: [notes/unavailable-pdfs-2026-10.md](notes/unavailable-pdfs-2026-10.md)

手法の記事:

- [表データ基盤モデル(TabPFN 系)— 仕組み、適用範囲、評価の読み方](articles/methods/tabular-foundation-models.md)
- [オートエンコーダ — 正則化、VAE、異常検知での使い方と限界](articles/methods/autoencoders.md)
- [勾配ブースティング木 — 仕組み、実装の設計の違い、チューニングと不確実性](articles/methods/gradient-boosted-trees.md)
- [ランダムフォレストと決定木 — 理論の範囲、効く理由、変数重要度の偏り](articles/methods/random-forests-and-decision-trees.md)
- [拡散モデル — 定式化の系譜、サンプリングの高速化、ガイダンス、評価と記憶の問題](articles/methods/diffusion-models.md)
- [対照学習・自己教師あり表現学習 — 崩壊の避け方、理論の範囲、線形評価の読み方](articles/methods/self-supervised-representation-learning.md)
- [ベイズ最適化とハイパーパラメータ最適化 — 代理モデル、多忠実度、ランダム探索との比較](articles/methods/bayesian-optimization.md)
- [近似ベイズ推論とその診断 — MCMC と変分推論、その近似は信用できるか](articles/methods/approximate-inference-and-diagnostics.md)

横断記事:

- [モデルと評価方法の弱点、それを改善した研究](articles/topics/weaknesses-and-fixes.md) — 3テーマを横断して「問題点 → 改善策 → 検証 → 独立した確認」を整理
- [モデルの解釈可能性 — 説明手法は何を前提にし、どう評価されてきたか](articles/topics/model-interpretability.md)
- [量子化による影響 — 何が失われ、何で測ると見えるのか](articles/topics/quantization-effects.md)
- [時系列基盤モデルと時系列予測 — 「ゼロショット」は何を意味するか](articles/topics/time-series-foundation-models.md)
- [学習モデルと計算量 — スケーリング則、計算の配分、コストの測り方](articles/topics/compute-and-scaling.md)
- [古典アルゴリズムと機械学習 — ソート・二分探索・貪欲法から見る](articles/topics/algorithms-and-ml.md)
- [アルゴリズム設計技法と機械学習 — 分割統治・動的計画・分枝限定・局所探索](articles/topics/design-techniques-and-ml.md)
- [予測モデルのフォールバックとモデル選択 — 運用でモデルを切り替える仕組み](articles/topics/model-fallback-and-selection.md)
- [不確実性の推定と較正 — ベイズ近似、較正の測り方、conformal prediction の保証の範囲](articles/topics/uncertainty-and-calibration.md)
- [異常検知 — 古典的な手法と深層学習、設定の違いと評価の落とし穴](articles/topics/anomaly-detection-classical-vs-deep.md)
- [ベイズ変化点検知 — BOCPD とその拡張、オフラインの事後分析、評価の作法](articles/topics/bayesian-change-point-detection.md)

数式の解説(高校数学Ⅲまでで読めるように、アルゴリズムの式を出典付きで解説するシリーズ):
- [0. 準備 — 記号、ベクトル、偏微分、確率](articles/math/00-preliminaries.md)
- [1. 木モデル — 勾配ブースティングの更新、XGBoost の目的関数、不純度と変数重要度](articles/math/01-tree-models.md)
- [2. 生成モデルと表現学習 — VAE の ELBO、拡散モデルのノイズ、InfoNCE](articles/math/02-generative-models.md)
- [3. 不確実性と較正 — ソフトマックス、温度スケーリング、ECE、分割共形予測](articles/math/03-uncertainty-and-calibration.md)

生成物の入口: [generated/index.md](generated/index.md)

## 新着論文の候補

毎週月曜 9:00(日本時間)に GitHub Actions が新着論文の候補を集め、テーマごとに Issue(ラベル `paper-candidates`)を作る。AIは使わない。

- 候補の出どころ: [registry/watch.yaml](registry/watch.yaml) のキーワードでの arXiv 検索と、既存カードを2本以上引用している新しい論文(Semantic Scholar)
- カード化したい候補にチェックを付け、ローカルで `uv run python scripts/list_approved.py` を実行してカード化する
- 既存カードと、過去の Issue に載せた論文は再度出さない
- 既知の問題: RealMLP の論文(arxiv-2407.04491)は Semantic Scholar で 404 になり、引用の追跡ができていない
- Semantic Scholar の API キー(無料)をリポジトリの Secret `S2_API_KEY` に登録すると、レート制限で失敗しにくくなる

## 今後の実装予定

- 実験カードの照合(指定コミットのファイルに値が存在するか)
- RealMLP 論文付録(Table D.1-D.12)のデータセット別数値の機械抽出
- TabICL・ModernNCA・TabDPT などその他の TabArena 参加モデルの原論文
- ドリフト検出: 表データのデータシフト検出、ラベルシフト推定
- 時系列の異常検知: TSB-AD などの他のベンチマーク、個々の手法の原論文
