---
title: 表データ基盤モデル(TabPFN 系)— 仕組み、適用範囲、評価の読み方
kind: method
tags: [tabular-foundation-model]
depends_on: [arxiv-2207.01848, doi-10.1038_s41586-024-08328-6, arxiv-2608.17957, arxiv-2609.22866, arxiv-2608.25774, arxiv-2609.04540, arxiv-2609.36108, arxiv-2609.36337, arxiv-2608.27882, arxiv-2506.16791, arxiv-2609.37959, arxiv-2608.12989, arxiv-2608.16429, arxiv-2608.17856, arxiv-2609.02766, arxiv-2609.18130, arxiv-2609.06912, arxiv-2608.28980, doi-10.70393_6a6374616d.343334, arxiv-2609.38744, arxiv-2609.13202, arxiv-2609.32898, arxiv-2609.36968, arxiv-2609.16091, arxiv-2609.13031, arxiv-2608.10837, arxiv-2609.31306, arxiv-2608.14211, arxiv-2608.20024, arxiv-2609.23223, arxiv-2609.29814, arxiv-2609.05955, arxiv-2609.03003, arxiv-2609.36881, arxiv-2609.07655, arxiv-2609.33114, arxiv-2608.22594, arxiv-2609.29523, doi-10.1007_s40123-026-01482-2, doi-10.1186_s44147-026-01203-3, arxiv-2608.18919, arxiv-2305.02997]
written_at: 2026-10-03
written_by: claude-opus-5-5 via Claude Code
---

# 表データ基盤モデル(TabPFN 系)— 仕組み、適用範囲、評価の読み方

<!-- generated:stale -->
> ⚠ この記事の執筆後(2026-10-03)に、関連カードが 26 件追加されています(未反映): `arxiv-2608.02157`, `arxiv-2608.03565`, `arxiv-2608.05265`, `arxiv-2608.13793`, `arxiv-2608.18849`, `arxiv-2608.24056`, `arxiv-2608.25048`, `arxiv-2608.30337`, `arxiv-2608.30392`, `arxiv-2609.03880`, `arxiv-2609.06080`, `arxiv-2609.06941`, `arxiv-2609.07441`, `arxiv-2609.12105`, `arxiv-2609.16309`, `arxiv-2609.17488`, `arxiv-2609.22154`, `arxiv-2609.23574`, `arxiv-2609.25340`, `arxiv-2609.25541`, `arxiv-2609.27679`, `arxiv-2609.28836`, `arxiv-2609.37989`, `arxiv-2609.38058`, `arxiv-2609.39523`, `arxiv-2610.00388`
<!-- /generated:stale -->

## この記事の読み方

TabPFN に始まる**表データ基盤モデル**(tabular foundation model, TFM)を、手法として整理する。
「GBDT と比べてどちらが強いか」は [表データの記事](../tasks/tabular-gbdt-vs-deep-learning.md) で扱っているので、ここでは次の3点に絞る。

1. どういう仕組みで予測しているか
2. どんなデータなら使えて、どこに限界が報告されているか
3. 評価を読むときに何に注意するか

このリポジトリには、表データ基盤モデルを扱うカードが60本以上ある。2026年の論文が多く、開発元による技術報告と、基盤モデルを部品として使う応用研究が含まれる。
性能の数値は書かない。各論文のページの結果表を参照のこと。

## 仕組み

### 学習しないで予測する(文脈内学習)

TabPFN は、新しいデータセットに対してパラメータを更新しない。**学習データをそのまま入力として与え**、テスト点の予測を1回の順伝播で出す [arxiv-2207.01848#c4](https://arxiv.org/pdf/2207.01848v6#page=1 "TabPFN performs in-context learning (ICL), it learns to make predictions using sequences of labeled examples (x, f(x)) given in the input, without requiring further parameter updates.")。
モデルは事前に一度だけ、オフラインで学習しておき、すべての評価で同じモデルを使う [arxiv-2207.01848#c3](https://arxiv.org/pdf/2207.01848v6#page=3 "we trained a 12-layer Transformer for 18 000 batches of 512 synthetically generated datasets each, which required a total of 20 hours on one machine with 8 GPUs (Nvidia RTX 2080 Ti).")。
また、ハイパーパラメータの調整が要らないとされる [arxiv-2207.01848#c16](https://arxiv.org/pdf/2207.01848v6#page=1 "needs no hyperparameter tuning and is competitive with state-of-the-art classification methods")。ただし TabPFN v2 の著者は、回帰では分類よりもハイパーパラメータの調整が重要になると述べている [doi-10.1038_s41586-024-08328-6#c17](https://www.nature.com/articles/s41586-024-08328-6.pdf#page=6 "For regression tasks, tuning hyperparameters is more important.")。

### 合成データで事前学習する

事前学習には実データを使わず、**構造的因果モデルから生成した合成データ**を使う。単純な構造を好むように設計されている [arxiv-2207.01848#c5](https://arxiv.org/pdf/2207.01848v6#page=1 "This prior incorporates ideas from causal reasoning: It entails a large space of structural causal models with a preference for simple structures.") [doi-10.1038_s41586-024-08328-6#c5](https://www.nature.com/articles/s41586-024-08328-6.pdf#page=4 "we created a massive corpus of around 100 million synthetic datasets per model training")。
TabPFN v2 の著者は、合成データだけで学習することで、プライバシーや著作権の問題と、評価データが学習データに混入する問題を避けられるとしている [doi-10.1038_s41586-024-08328-6#c4](https://www.nature.com/articles/s41586-024-08328-6.pdf#page=3 "By relying on synthetic data instead of large collections of public tabular data, we avoid common problems of foundational models, such as privacy and copyright infringements, contaminating our training data with test data")。

一方、**実データの表で事前学習する**系統もある。1つの実データの表で自己教師あり学習をするだけでも、意外に強い転移が生じうるという報告がある [arxiv-2608.17957#c1](https://arxiv.org/pdf/2608.17957v1#page=1 "In contrast, we show that surprisingly strong transfer can emerge from self-supervised pre-training on just a single real table.")。

### 構造の違い

| モデル・系統 | 特徴(構造・使い方) |
|---|---|
| TabPFN v2 | 各セルが行の中で、次に列の中で注意を向ける2方向の注意機構。サンプルと特徴量の順序に対して不変 [doi-10.1038_s41586-024-08328-6#c6](https://www.nature.com/articles/s41586-024-08328-6.pdf#page=3 "uses a two-way attention mechanism, with each cell attending to the other features in its row (that is, its sample) and then attending to the same feature across its column (that is, all other samples).") |
| TabICL 系(Causilo など) | Causilo は TabICL の「列ごと→行ごと」の構造を踏襲し、行の圧縮の前に行を精緻化するモジュールを加えている [arxiv-2609.22866#c2](https://arxiv.org/pdf/2609.22866v1#page=1 "Causilo follows TabICL’s column-then-row architecture but introduces another row-refinement module before row compression.") |
| EXAONE Tabular | 各層で、項目内の特徴量方向の注意と、特徴量ごとの項目方向の注意(サポート集合で条件づけたもの)を交互に行う [arxiv-2608.25774#c1](https://arxiv.org/pdf/2608.25774v1#page=1 "EXAONE Tabular interleaves feature-axis attention within each item with support-conditioned item-axis attention within each feature at every Transformer layer") |
| Mitra-v2 | 代表的な結果は、微調整と8分割のバギングを組み合わせたもの。著者自身が、順伝播だけのモデルよりはるかに遅く、ゼロショットやパレート優位と呼ぶべきではないとしている [arxiv-2609.04540#c2](https://arxiv.org/pdf/2609.04540v1#page=24 "It is much slower than forward-pass foundation models and should not be described as zero-shot or Pareto-dominant (Figure 6).") |
| LoopICL | 1つの Transformer ブロックを繰り返し使い、パラメータ数と計算の深さを切り離す [arxiv-2609.36108#c1](https://arxiv.org/pdf/2609.36108v1#page=1 "We introduce LoopICL, a looped transformer whose core design decouples parameter count from computational depth.") |
| 線形時間の構造(DeltaNet など) | softmax 注意の代わりに線形時間の系列処理を使う試み。最終状態から読み出す(非因果性を戻す)ことで、条件をそろえた softmax 注意の基準モデルに近い性能になったと報告されている [arxiv-2609.36337#c1](https://arxiv.org/pdf/2609.36337v1#page=1 "Finally, re-introducing non-causality by reading out from the final state allows us to closely match a controlled softmax attention baseline on OpenML-CC18 and TabArena.")。Mamba を使う構造 [arxiv-2608.27882#c1](https://arxiv.org/pdf/2608.27882v1#page=1 "We introduce SOMTab, a Set-Order Mamba architecture for efficient tabular in-context learning.") もある |

## 適用範囲と、報告されている限界

### データの大きさ

- 最初の TabPFN は、小さな数値データ(学習データ・特徴量・クラス数に上限あり)を対象としていた [arxiv-2207.01848#c2](https://arxiv.org/pdf/2207.01848v6#page=2 "tasks (≤1 000 training examples, ≤100 purely numerical features without missing values and ≤10 classes)")。Transformer の構造上、小さなデータにしか拡張できないことを著者自身が限界に挙げていた [arxiv-2207.01848#c12](https://arxiv.org/pdf/2207.01848v6#page=10 "the underlying Transformer architecture only scales to small datasets")。
- TabPFN v2 は、扱えるデータの大きさを大きく広げ、回帰・カテゴリ特徴・欠損値にも対応した [doi-10.1038_s41586-024-08328-6#c3](https://www.nature.com/articles/s41586-024-08328-6.pdf#page=2 "the new TabPFN scales to 50× larger datasets; supports regression tasks, categorical data and missing values; and is robust to unimportant features and outliers.")。ただし著者は、評価した範囲を超えて拡張できる証拠ではないと断っている [doi-10.1038_s41586-024-08328-6#c14](https://www.nature.com/articles/s41586-024-08328-6.pdf#page=6 "these results should not be taken as evidence that TabPFN scales well beyond the 10,000 samples and 500 features considered here.")。
- TabArena は、TabPFN v2 をその制約の範囲内のデータセットでのみ実行している [arxiv-2506.16791#c20](https://arxiv.org/pdf/2506.16791v4#page=3 "This only affects TabPFNv2, which is restricted to datasets with up to 10, 000 training samples, 500 features, and 10 classes for classification tasks")。
- 大きなデータに対しては、学習データを無作為に部分抽出して最初の TabPFN を実行する方法もとられている(TabZilla、3000件を抽出) [arxiv-2305.02997#c15](https://arxiv.org/pdf/2305.02997v4#page=3 "In order to run on datasets of size larger than 3000, we simply take a random sample of size 3000 from the full training dataset.")。
- 2026年のモデルでも、事前学習で扱う表の大きさには上限があり、それより大きな表は長さの汎化か部分抽出に頼る [arxiv-2609.37959#c6](https://arxiv.org/pdf/2609.37959v1#page=11 "Current pretraining covers synthetic numerical and categorical tables of at most 16,384 rows and 100 columns, leaving larger tables to length generalization or subsampling and encoding free text without semantic tokenization.")。線形時間の構造の一つ DeltaNet は、事前学習の文脈長の2〜4倍を超えると性能が落ちた [arxiv-2609.36337#c2](https://arxiv.org/pdf/2609.36337v1#page=1 "However, it degrades beyond 2-4× the pretraining context length, and existing mitigation strategies such as bidirectionality defer the problem at best.")。

**大きなデータへの対処**として、文脈に入れる行を選ぶ研究が多い。

- 情報を保つ少数の代表点を選ぶ [arxiv-2608.12989#c1](https://arxiv.org/pdf/2608.12989v1#page=1 "This paper introduces Balanced Adaptive Prototype Selection (BAPS), a framework for constructing compact, information-preserving contexts for scalable TabPFN inference.")
- テスト点ごとに近傍の学習データだけを使う [arxiv-2608.16429#c1](https://arxiv.org/pdf/2608.16429v1#page=1 "Localized TabICLv2 introduces a method that reduces the inference cost of TabICLv2 by retrieving only the k nearest training neighbours for each test point, measured by similarity in the model’s Stage 2 row-representation space, rather than using the full training context.")。ただし全データを使う場合の精度は超えず [arxiv-2608.16429#c5](https://arxiv.org/pdf/2608.16429v1#page=3 "Overall, the localized method does not surpass the accuracy of Full TabICLv2.")、近傍が有用な情報を取りこぼすと弱くなりうる [arxiv-2608.16429#c6](https://arxiv.org/pdf/2608.16429v1#page=4 "However, localization may underperform when useful evidence is not captured by the retrieved neighbours, and retrieval overhead can reduce speedups on smaller datasets or large query batches.")
- テスト点ごとに文脈の例を選ぶ [arxiv-2608.17856#c1](https://arxiv.org/pdf/2608.17856v1#page=1 "This paper introduces ARASH (Adaptive, query-specific Retrieval And Shot selection), a method that improves TFM efficiency by selecting optimal shots based on local neighborhood analysis within the training set.")

ただし、代表点を選ぶ研究は、GBDT など基盤モデル以外の比較対象を報告していない [arxiv-2608.12989#c5](https://arxiv.org/pdf/2608.12989v1#page=4 "All reduced-context methods are compared under identical data partitions, random seeds, and prototype budgets; hence, observed differences primarily reflect the predictive value of the constructed contexts.")。「大きなデータで使える」と「大きなデータで他の手法より良い」は別の問題である。

### 事前分布が表せないもの

- 物理の方程式から作ったデータでは、基盤モデルの事前分布は、**ノイズのない法則も物理単位も表せない**と著者は述べている [arxiv-2609.02766#c3](https://arxiv.org/pdf/2609.02766v1#page=1 "But we show that their prior can represent neither a noiseless mechanism nor physical units")。
- 進化的最適化の代理モデルとして使うと、候補が学習データの分布から離れたとき、TabPFN は**控えめに外挿**した [arxiv-2609.18130#c6](https://arxiv.org/pdf/2609.18130v1#page=12 "TabPFN exhibits relatively conservative extrapolation behavior when candidate solutions move away from the distribution of the training data.")。
- 4つの基盤モデルの合成データ生成器を復元し、ベンチマークのデータと比べた研究では、合成データがベンチマークのデータをよく覆っているほど、相対的な性能が良い傾向があった [arxiv-2609.06912#c2](https://arxiv.org/pdf/2609.06912v1#page=1 "Moreover, stronger synthetic-to-benchmark support is generally associated with better relative model performance.")。ただし、この分析は記述的なもので、因果を示すものではないと著者自身が述べている [arxiv-2609.06912#c6](https://arxiv.org/pdf/2609.06912v1#page=5 "This analysis is descriptive rather than causal: generator identity is confounded with model architecture, optimization, ensembling, inference, and other model-specific choices.")。

### 分布シフトと時間

- TabArena と TALENT は小〜中規模の独立同分布のデータセットが中心で、時間や群のシフトがある条件では基盤モデルの優位が大きく弱まるという指摘を、レビュー論文が先行研究を引いて紹介している [arxiv-2608.28980#c4](https://arxiv.org/pdf/2608.28980v3#page=18 "TabArena and TALENT are dominated by small-to-medium IID tabular datasets, the regime in which tabular foundation models perform particularly well, whereas Purucker et al. [109]’s purpose-built alternative shows that this advantage weakens substantially under temporal and grouped shift.")。
- 産業の故障検出の研究では、時間順に分けた感度分析で、閾値をそのまま持ち越す方法はどのモデルでも失敗した。著者は、これを順位づけではなく頑健性への警告として扱っている [doi-10.70393_6a6374616d.343334#c5](https://www.suaspress.org/ojs/index.php/JCTAM/article/download/v3n4a01/v3n4a01#page=7 "Threshold transfer failed for every model")。
- 分子の性質の予測では、骨格の違う分子をテストに回す分割で評価している [arxiv-2609.38744#c4](https://arxiv.org/pdf/2609.38744v1#page=6 "The scaffold holdout separates structural groups, while the similarity filter removes close analogues that can remain across different scaffolds.")。ただし、現実のシフトはこの分割では捉えきれない可能性があると著者が限界に挙げている [arxiv-2609.38744#c6](https://arxiv.org/pdf/2609.38744v1#page=9 "Broader real-world distribution shifts may also involve changes that are not captured by scaffold separation and fingerprint-similarity-based splits.")。

### 特徴量エンジニアリングは要らなくなったか

特徴量エンジニアリングの効果は、古い世代の基盤モデルに集中しており、最も強いモデルではほとんどなくなったという報告がある [arxiv-2609.13202#c1](https://arxiv.org/pdf/2609.13202v1#page=1 "We find a consistent pattern: feature engineering gains are concentrated in earlier model generations and become negligible for the strongest models.")。
ただし、分類のデータセットを最初の TabPFN の制約内に絞っており [arxiv-2609.13202#c2](https://arxiv.org/pdf/2609.13202v1#page=3 "all selected classification datasets satisfy the sample and feature limits of TabPFN v1 (at most 1,024 training samples and 100 features), ensuring that every generation is evaluated on the same datasets.")、報告された最良の効果は条件の中の最大値(オラクル)であって、検証データで選んだものではない [arxiv-2609.13202#c5](https://arxiv.org/pdf/2609.13202v1#page=5 "the maximum is oracle, not validation-selected")。

### 文脈が汚れている場合

- 外れ値検出に使う場合、途中の層で出力する(データセットごとに最適な層を選ぶ)と検出性能が改善しうるという研究があり、その主な仕組みとして、文脈の中に外れ値が混ざること(文脈の汚染)が挙げられている [arxiv-2609.32898#c2](https://arxiv.org/pdf/2609.32898v1#page=1 "can also improve detection performance on diverse real-world benchmarks by 4.7–7.3% on average, consistent across three distinct foundation models")。
- 教師なしの異常検知に転用する手法は、正常なデータだけの文脈を前提とし、異常が多く混ざると性能が落ちる [arxiv-2609.36968#c6](https://arxiv.org/pdf/2609.36968v1#page=9 "As shown in our appendix experiments, performance degrades when the context is heavily contaminated with anomalies.")。

### 推論のコスト

学習が不要な代わりに、**推論のたびに学習データ全体を文脈として処理する** [arxiv-2207.01848#c4](https://arxiv.org/pdf/2207.01848v6#page=1 "TabPFN performs in-context learning (ICL), it learns to make predictions using sequences of labeled examples (x, f(x)) given in the input, without requiring further parameter updates.") ため、推論のコストが問題になる。

- 代理モデルとして頻繁に作り直す場面では、TabPFN の文脈の符号化にかかる時間が、従来の代理モデル(RBFN)の学習時間を上回ることがあり、作り直すたびに積み重なる [arxiv-2609.18130#c5](https://arxiv.org/pdf/2609.18130v1#page=12 "Although TabPFN does not involve conventional hyper-parameter optimization, its training process still requires encoding and caching the training context to construct the predictive mapping.")。
- 軽量化の研究:
  - TabPFN を小さな順伝播ネットワークへ蒸留する。エンドツーエンドの遅延の改善は、ほぼ推論経路から TabPFN を外したことによる [arxiv-2609.16091#c2](https://arxiv.org/pdf/2609.16091v1#page=1 "Span-level attribution shows that this wall-clock gain is almost entirely from removing in-context TabPFN from the hot path; fewer cloud round-trips cut token cost (2.1×) rather than latency.")
  - attention の FP8 量子化。テスト行と学習行の量子化誤差をそろえる必要がある [arxiv-2609.13031#c1](https://arxiv.org/pdf/2609.13031v1#page=1 "We find that it is crucial to align the quantization error in the test rows with the quantization error in the training rows, as otherwise the accuracy drops drastically.") [arxiv-2609.13031#c2](https://arxiv.org/pdf/2609.13031v1#page=1 "Our Triton kernel achieves a speedup up to 1.7x over regular 16-bit kernels, and we show that on TabPFN-v3 and TabICLv2 there is no relevant accuracy loss across TabArena and BeyondArena.")
  - 層をアダプタに置き換える枝刈り。最適な構成はデータセットごとに違った [arxiv-2608.10837#c5](https://arxiv.org/pdf/2608.10837v1#page=10 "Notably, we find that layer-importance metrics commonly used in the literature fail to identify good compression configurations.")
  - attention の実装の選択。最適な実装は列方向と行方向で違い、ハードウェアにも依存する [arxiv-2609.31306#c2](https://arxiv.org/pdf/2609.31306v2#page=1 "We find that the optimal backend choice differs between column and row attention and varies across hardware as well as model specifics")

詳しくは [量子化による影響](../topics/quantization-effects.md) の表データの節を参照。

### 公平性

学習段階で公平性を組み込む研究もある [arxiv-2608.14211#c1](https://arxiv.org/pdf/2608.14211v1#page=1 "We propose FairTFM, a scalable training strategy based on synthetic fairness tasks and a fairness-aware architecture using a gradient reversal layer, which encourages the model to learn representations invariant to sensitive attributes.")。ただし、公平性に特化した手法をすべての指標で上回るわけではなく、実験は軽量な版のモデルで行われている [arxiv-2608.14211#c6](https://arxiv.org/pdf/2608.14211v1#page=10 "Second, while FairTFM is broadly competitive, the results also show that it does not dominate specialized fairness-aware baselines on every metric or every task configuration, especially in the stricter settings where age is used as sensitive attribute.")。

## 用途の広がり

表の予測以外にも、基盤モデルを部品として使う研究が増えている。

| 用途 | 例 | 注意点 |
|---|---|---|
| 時系列予測 | 地域熱供給の需要予測で、時系列基盤モデルと比べた [arxiv-2608.20024#c1](https://arxiv.org/pdf/2608.20024v1#page=1 "This study systematically evaluates TabPFN-TS against state-of-the-art time-series foundation models and trained machine-learning baselines for probabilistic heat load forecasting in district heating networks.")。電力価格の予測にゼロショットで使った [arxiv-2609.23223#c3](https://arxiv.org/pdf/2609.23223v1#page=11 "Forecasts are generated in the so-called zero-shot mode, i.e., without task-specific tuning of the model weights or hyperparameters.") | 予測精度が最良のモデルと、利益が最大のモデルは一致しなかった [arxiv-2609.23223#c5](https://arxiv.org/pdf/2609.23223v1#page=21 "although TabPFN is the most accurate model, NARX combined with Spread THieF yields the highest arbitrage profit in every market-efficiency combination") |
| 時系列分類 | 系列の局所的な動きを表に変換し、凍結した TabPFN に入れる [arxiv-2609.29814#c1](https://arxiv.org/pdf/2609.29814v1#page=1 "We propose SwitchPFN, which learns a shared projection and regime codebook from the training sequences, making local dynamic operators and transition features directly comparable across samples.") | — |
| グラフ | ノードの予測で、文脈に入れるノードを選ぶ [arxiv-2609.05955#c1](https://arxiv.org/pdf/2609.05955v1#page=1 "We present LoGIC, which retrieves labeled nodes via structural, feature-based, and coverage channels, shares each context across the queries in a graph-local cluster, incorporates an unlabeled halo for adapter backbones, and chooses the channel and context budget without test labels.") | 著者自身が、精度の面でデータセットごとの学習を常に代替できるものではなく、いくつかのデータセットでは最強の学習済みの比較手法に劣ると述べている [arxiv-2609.05955#c6](https://arxiv.org/pdf/2609.05955v1#page=7 "The contribution consequently does not constitute a universal accuracy substitute for per-dataset training.") |
| 因果効果の推定 | 因果推論用の基盤モデル [arxiv-2609.03003#c5](https://arxiv.org/pdf/2609.03003v1#page=19 "Despite not being trained on the Lalonde data distributions, CFMs are remarkably competitive with classical estimators.") | 別の研究では、観測の見え方(observational views)をそろえて比べると、一貫して最良の因果基盤モデルはなく、順位も大きく変わった [arxiv-2609.36881#c2](https://arxiv.org/pdf/2609.36881v1#page=1 "Across these matched views, no CFM consistently performs best and model rankings vary substantially.")。予測用の基盤モデルと条件ごとの識別手順を組み合わせる方法が、因果基盤モデルと競争力を持った [arxiv-2609.36881#c3](https://arxiv.org/pdf/2609.36881v1#page=1 "A modular approach that pairs a predictive tabular foundation model with regime-specific identification procedures is competitive with CFMs and outperforms several of them.") |
| 最適化の代理モデル | 進化的最適化 [arxiv-2609.18130#c2](https://arxiv.org/pdf/2609.18130v1#page=1 "Results show that the effectiveness of TabPFN is highly problem dependent, and it cannot replace conventional surrogates universally.") | 効果は問題に強く依存し、従来の代理モデルを一律には置き換えられない [arxiv-2609.18130#c2](https://arxiv.org/pdf/2609.18130v1#page=1 "Results show that the effectiveness of TabPFN is highly problem dependent, and it cannot replace conventional surrogates universally.")。別の研究は、TabPFN が全体の予測精度のために学習されており、閉ループ探索の目的(最大リグレット)とずれると論じている [arxiv-2609.07655#c3](https://arxiv.org/pdf/2609.07655v2#page=7 "This is a crucial result because TabArena evaluates global predictive accuracy and TabPFN is trained for global prediction, not maximum regret, creating an objective mismatch with closed-loop discovery (Erickson et al., 2025; Hollmann et al., 2025; Grinsztajn et al., 2026).") |
| 統計的推論 | 信頼区間を1回の順伝播で出す [arxiv-2609.33114#c1](https://arxiv.org/pdf/2609.33114v1#page=1 "The key methodological ingredients of TabCon are a sparse mixture-of-experts architecture and reinforcement-learning-based post-training that calibrate the resulting confidence intervals to a desired coverage level.") | — |
| 表以外のデータ | MNIST などを表の行として表し、空間・系列の構造を与えずに適用。いくつかの場合で専用モデルに匹敵 [arxiv-2608.22594#c2](https://arxiv.org/pdf/2608.22594v1#page=1 "Despite having no explicit access to the spatial or sequential structure characterizing the data, TabPFN v3 in some cases achieves accuracies comparable with that of models or methods geared specifically toward the corresponding tasks.") | 事前学習の入力の上限を外して実行している [arxiv-2608.22594#c3](https://arxiv.org/pdf/2608.22594v1#page=6 "All TabPFN results use model v3 library defaults with a single override") |
| 他のモデルの検査 | 病理画像の基盤モデルの表現から分子の情報を読み出せるかを測る [arxiv-2609.29523#c2](https://arxiv.org/pdf/2609.29523v1#page=1 "TabPFN serves as a pretrained probe to measure how well these molecular programs can be decoded without task-specific gradient updates.") | — |

## 評価を読むときの注意

### 誰が評価しているか

- TabPFN v2 の著者の一部は、表データ基盤モデルの企業(PriorLabs)に所属している [doi-10.1038_s41586-024-08328-6#c18](https://www.nature.com/articles/s41586-024-08328-6.pdf#page=13 "F.H. and N.H. are affiliated with PriorLabs, a company focused on developing tabular foundation models.")。TabArena の著者にも TabPFN v2 の著者が含まれる [arxiv-2506.16791#c23](https://arxiv.org/pdf/2506.16791v4#page=11 "L.P. and F.H. are a subset of the authors of TabPFNv2.")。
- 2026年の基盤モデルの評価の多くは、開発元による技術報告である。計算予算・ベンチマークへの適合・比較対象の結果の転用などの注意点は、[表データの記事](../tasks/tabular-gbdt-vs-deep-learning.md) の「2026年の新しい論文に見る評価の実態」にまとめた。

### 「調整不要」との比べ方

基盤モデルは調整しないで使うのが普通なので、**比較対象をどう扱うか**で結果の意味が変わる。

- **比較対象も既定値にそろえる**: 基盤モデルが調整不要であることに合わせて、GBDT も既定値で比べた研究がある。著者は、調整すれば差は縮まるかもしれないと断っている [doi-10.1007_s40123-026-01482-2#c2](https://link.springer.com/content/pdf/10.1007/s40123-026-01482-2.pdf#page=10 "All gradient-boosting models used default hyperparameters without per-dataset tuning to ensure a fair comparison with TabPFN's zero-tuning design")。
- **比較対象だけ調整する**: 比較対象をグリッドサーチで調整し、TabPFN は既定値のまま比べた研究もある [doi-10.1186_s44147-026-01203-3#c2](https://link.springer.com/content/pdf/10.1186/s44147-026-01203-3.pdf#page=1 "TabPFN was applied using its default configuration and compared with four GridSearchCV-optimized models: support vector regression, k-nearest neighbors, Random Forest, and CatBoost.")。
- **調整した比較対象と比べるべき**: 基盤モデルは、従来の手法を適切に調整したうえで比べないと公平に評価できないという主張がある [arxiv-2608.18919#c4](https://arxiv.org/pdf/2608.18919v1#page=11 "This implies that, even though modern foundation models often perform well by default, they can only be compared adequately when the traditional alternatives are appropriately tuned.")。
- **データの使い方の非対称**: 物理データの研究では、調整・アンサンブルする構成の比較対象がモデル選択用にデータの20%を取り分ける一方、基盤モデルは全データを文脈に使う。著者はこの差をそろえず、開示している [arxiv-2609.02766#c5](https://arxiv.org/pdf/2609.02766v1#page=9 "Under the tuned and ensembled pipelines, the trained baselines carve 20% of nsamples for model selection and so fit on 0.8 nsamples; TFMs condition on all of it, since they have nothing to select.")。
- **計算時間の数え方**: 因果基盤モデルの解説論文では、比較対象は学習・調整・推論の時間を数え、基盤モデルは推論だけを数え、事前学習の時間は含めない [arxiv-2609.03003#c6](https://arxiv.org/pdf/2609.03003v1#page=19 "This means we include training, tuning, and inference for classical baselines, but only inference for CFMs since this is the only step we perform.")。

### 小さなデータでの結論の強さ

応用研究の多くは小さなデータで評価しており、著者自身が結論を限定している例も多い。

- 線形モデルや GBDT との差が小さく、外部検証もないため、TabPFN を決定的な選択肢として推奨はできないと述べる例 [doi-10.1007_s40123-026-01482-2#c5](https://link.springer.com/content/pdf/10.1007/s40123-026-01482-2.pdf#page=2 "the modest margin over linear and gradient-boosting baselines and the absence of external validation preclude any recommendation as the definitive algorithm of choice.")
- テストデータが同じデータベースから取られており、独立した外部検証ではないと断る例 [doi-10.1186_s44147-026-01203-3#c6](https://link.springer.com/content/pdf/10.1186/s44147-026-01203-3.pdf#page=22 "Although the independent test subset was excluded from all model development and contained 34 observations reserved for final evaluation, these observations were drawn from the same experimental database and therefore do not constitute independent external validation.")
- この特定の条件での結果であり、一般的な優位や時間をまたいだ運用での妥当性は示していないと結論する例 [doi-10.70393_6a6374616d.343334#c6](https://www.suaspress.org/ojs/index.php/JCTAM/article/download/v3n4a01/v3n4a01#page=8 "The evidence therefore supports TabICLv2 in this specific low-resource, cost-sensitive setting but does not establish universal superiority or temporal deployment validity.")

## 現時点での整理

- **仕組みの要点**は、合成データで一度だけ事前学習し、新しいデータでは学習せずに文脈として与えて予測すること [arxiv-2207.01848#c4](https://arxiv.org/pdf/2207.01848v6#page=1 "TabPFN performs in-context learning (ICL), it learns to make predictions using sequences of labeled examples (x, f(x)) given in the input, without requiring further parameter updates.") [arxiv-2207.01848#c5](https://arxiv.org/pdf/2207.01848v6#page=1 "This prior incorporates ideas from causal reasoning: It entails a large space of structural causal models with a preference for simple structures.")。
- **使える範囲には上限がある**。各モデルの事前学習の範囲を確かめる [doi-10.1038_s41586-024-08328-6#c14](https://www.nature.com/articles/s41586-024-08328-6.pdf#page=6 "these results should not be taken as evidence that TabPFN scales well beyond the 10,000 samples and 500 features considered here.") [arxiv-2609.37959#c6](https://arxiv.org/pdf/2609.37959v1#page=11 "Current pretraining covers synthetic numerical and categorical tables of at most 16,384 rows and 100 columns, leaving larger tables to length generalization or subsampling and encoding free text without semantic tokenization.")。大きなデータでは文脈の選び方が問題になり、選んだ場合でも全データを使う場合を超えるとは限らない [arxiv-2608.16429#c5](https://arxiv.org/pdf/2608.16429v1#page=3 "Overall, the localized method does not surpass the accuracy of Full TabICLv2.")。
- **事前分布が表せないものがある**。ノイズのない法則や物理単位 [arxiv-2609.02766#c3](https://arxiv.org/pdf/2609.02766v1#page=1 "But we show that their prior can represent neither a noiseless mechanism nor physical units")、分布から離れた外挿 [arxiv-2609.18130#c6](https://arxiv.org/pdf/2609.18130v1#page=12 "TabPFN exhibits relatively conservative extrapolation behavior when candidate solutions move away from the distribution of the training data.") など。
- **独立同分布の小〜中規模データ以外での証拠は少ない**。時間や群のシフトがある場面での優位の弱まりが指摘されている [arxiv-2608.28980#c4](https://arxiv.org/pdf/2608.28980v3#page=18 "TabArena and TALENT are dominated by small-to-medium IID tabular datasets, the regime in which tabular foundation models perform particularly well, whereas Purucker et al. [109]’s purpose-built alternative shows that this advantage weakens substantially under temporal and grouped shift.")。運用で時間をまたぐ場合は、時間順の検証が必要 [doi-10.70393_6a6374616d.343334#c5](https://www.suaspress.org/ojs/index.php/JCTAM/article/download/v3n4a01/v3n4a01#page=7 "Threshold transfer failed for every model")。
- **推論のコストは別に評価する**。学習が不要でも推論は重く、軽量化の研究が続いている [arxiv-2609.18130#c5](https://arxiv.org/pdf/2609.18130v1#page=12 "Although TabPFN does not involve conventional hyper-parameter optimization, its training process still requires encoding and caching the training context to construct the predictive mapping.") [arxiv-2609.16091#c2](https://arxiv.org/pdf/2609.16091v1#page=1 "Span-level attribution shows that this wall-clock gain is almost entirely from removing in-context TabPFN from the hot path; fewer cloud round-trips cut token cost (2.1×) rather than latency.")。
- **評価は比較対象の扱いとセットで読む**。調整の有無、データの使い方、時間の数え方 [arxiv-2609.02766#c5](https://arxiv.org/pdf/2609.02766v1#page=9 "Under the tuned and ensembled pipelines, the trained baselines carve 20% of nsamples for model selection and so fit on 0.8 nsamples; TFMs condition on all of it, since they have nothing to select.") [arxiv-2609.03003#c6](https://arxiv.org/pdf/2609.03003v1#page=19 "This means we include training, tuning, and inference for classical baselines, but only inference for CFMs since this is the only step we perform.")。

**この整理に含まれていないもの**: TabICL・TabDPT・TabPFN-3 などの原論文(このリポジトリにまだカードがない)、表データ基盤モデルと LLM の組み合わせ、文脈内学習の理論的な分析。

## 参照カード

- [arxiv-2207.01848](../../papers/arxiv-2207.01848.yaml) Hollmann et al., "TabPFN: A Transformer That Solves Small Tabular Classification Problems in a Second"
- [doi-10.1038_s41586-024-08328-6](../../papers/doi-10.1038_s41586-024-08328-6.yaml) Hollmann et al., "Accurate predictions on small data with a tabular foundation model"
- [arxiv-2608.17957](../../papers/arxiv-2608.17957.yaml) Shaheen et al., "Understanding the Surprising Generalization Properties of Tabular Foundation Models"
- [arxiv-2609.22866](../../papers/arxiv-2609.22866.yaml) Cho et al., "Causilo Technical Report"
- [arxiv-2608.25774](../../papers/arxiv-2608.25774.yaml) Eo et al., "EXAONE Tabular 1.0 : Technical Report"
- [arxiv-2609.04540](../../papers/arxiv-2609.04540.yaml) Tao et al., "Mitra-v2 Technical Report"
- [arxiv-2609.36108](../../papers/arxiv-2609.36108.yaml) Balef et al., "LoopICL: Looping a single transformer block to solve tabular tasks"
- [arxiv-2609.36337](../../papers/arxiv-2609.36337.yaml) Schnurr et al., "Adapting Linear-Time Architectures for Tabular In-Context Learning"
- [arxiv-2608.27882](../../papers/arxiv-2608.27882.yaml) Wang et al., "SOMTab: Set-Order Mamba for Efficient Tabular In-Context Learning"
- [arxiv-2506.16791](../../papers/arxiv-2506.16791.yaml) Erickson et al., "TabArena: A Living Benchmark for Machine Learning on Tabular Data"
- [arxiv-2609.37959](../../papers/arxiv-2609.37959.yaml) Kong et al., "TabFM: A Zero-Shot Foundation Model for Tabular Data"
- [arxiv-2608.12989](../../papers/arxiv-2608.12989.yaml) Jadid et al., "Balanced Adaptive Prototype Selection for Scalable TabPFN Inference on Large-Scale Tabular Data"
- [arxiv-2608.16429](../../papers/arxiv-2608.16429.yaml) Guta, "Localized TabICLv2: Scaling Tabular In-Context Learning through k-NN"
- [arxiv-2608.17856](../../papers/arxiv-2608.17856.yaml) Jamalidinan et al., "ARASH: Adaptive Retrieval And Shot Selection for Tabular Prediction"
- [arxiv-2609.02766](../../papers/arxiv-2609.02766.yaml) Tenachi et al., "Do Tabular Foundation Models Know Physics? Contamination, Units, and the Deterministic Limit"
- [arxiv-2609.18130](../../papers/arxiv-2609.18130.yaml) Han et al., "Benchmarking Tabular Foundation Models as Surrogates in Expensive Evolutionary Optimization"
- [arxiv-2609.06912](../../papers/arxiv-2609.06912.yaml) Zhao et al., "From Synthetic Priors to Model Behavior: Structural Coverage in Tabular Foundation Models"
- [arxiv-2608.28980](../../papers/arxiv-2608.28980.yaml) Rezaee, "The Illusion of Replacement: Rethinking Specialized Machine Learning Models in the Foundation Model Era"
- [doi-10.70393_6a6374616d.343334](../../papers/doi-10.70393_6a6374616d.343334.yaml) Song, "Tabular In-Context Learning for Low-Resource Rare Industrial Fault Detection: a Cost-Sensitive Comparison on Scania APS and SECOM"
- [arxiv-2609.38744](../../papers/arxiv-2609.38744.yaml) Lee et al., "Molecular Property Prediction under Structural Shift with Tabular Foundation Models"
- [arxiv-2609.13202](../../papers/arxiv-2609.13202.yaml) WU et al., "Do Tabular Foundation Models Still Need Feature Engineering?"
- [arxiv-2609.32898](../../papers/arxiv-2609.32898.yaml) Zhou et al., "When Less Compute Is More: Adaptive Early Exit Improves Pretrained Outlier Detection"
- [arxiv-2609.36968](../../papers/arxiv-2609.36968.yaml) Choi et al., "TaskBridge: Bridging Unsupervised Tabular Anomaly Detection and In-Context Learning via Virtual Tasks"
- [arxiv-2609.16091](../../papers/arxiv-2609.16091.yaml) Dey et al., "Distilling Foundation Models for Agentic What-If Reasoning:Cost, Latency, and Governance in a Hybrid LLM+SLM Architecture"
- [arxiv-2609.13031](../../papers/arxiv-2609.13031.yaml) Kübler et al., "Attention Quantization for Tabular Foundation Models"
- [arxiv-2608.10837](../../papers/arxiv-2608.10837.yaml) Koshil et al., "TACTICL: Task-Aware Compression of Tabular ICL Models"
- [arxiv-2609.31306](../../papers/arxiv-2609.31306.yaml) Schambach et al., "Benchmarking Attention for Tabular Foundation Models"
- [arxiv-2608.14211](../../papers/arxiv-2608.14211.yaml) Kenfack et al., "Training Fair Tabular Foundation Models"
- [arxiv-2608.20024](../../papers/arxiv-2608.20024.yaml) Spoek et al., "Systematic Evaluation of TabPFN-TS for Zero-Shot Probabilistic Heat Load Forecasting in District Heating Networks"
- [arxiv-2609.23223](../../papers/arxiv-2609.23223.yaml) Lipiecki et al., "Stealing profits: Spread-based temporal hierarchy forecasting for day-ahead electricity markets"
- [arxiv-2609.29814](../../papers/arxiv-2609.29814.yaml) Zhu et al., "SwitchPFN: Shared Switching Dynamics for Frozen In-Context Time Series Classification"
- [arxiv-2609.05955](../../papers/arxiv-2609.05955.yaml) Yang et al., "LoGIC: Budgeted Context Construction for Node-Level Graph In-Context Learning with Tabular Foundation Models"
- [arxiv-2609.03003](../../papers/arxiv-2609.03003.yaml) Stith et al., "Causal Foundation Models"
- [arxiv-2609.36881](../../papers/arxiv-2609.36881.yaml) Jung et al., "What You Observe Determines How You Identify Causal Effects: Evaluating Causal Models across Observational Views"
- [arxiv-2609.07655](../../papers/arxiv-2609.07655.yaml) Feng et al., "Online Surrogate Repair: Decoupling High-Fidelity Feedback from Search Length in Closed-Loop Discovery"
- [arxiv-2609.33114](../../papers/arxiv-2609.33114.yaml) Ye et al., "Can Tabular Foundation Models Amortize Statistical Inference?"
- [arxiv-2608.22594](../../papers/arxiv-2608.22594.yaml) Nakerst et al., "Tabular foundation models for non-tabular tasks"
- [arxiv-2609.29523](../../papers/arxiv-2609.29523.yaml) Bhattacharjee et al., "Towards Trustworthy Biological Alignment in TabPFN-Probed Pathology Foundation Models"
- [doi-10.1007_s40123-026-01482-2](../../papers/doi-10.1007_s40123-026-01482-2.yaml) Xia et al., "Machine Learning-Based Prediction of Cycloplegic Refraction Using the Eyerobo Vision Screener: Design—A Cross-Sectional Comparative Device Study"
- [doi-10.1186_s44147-026-01203-3](../../papers/doi-10.1186_s44147-026-01203-3.yaml) Bui et al., "Interpretable TabPFN-Based prediction of unconfined compressive strength in chemically stabilized soft soils for transportation subgrade applications"
- [arxiv-2608.18919](../../papers/arxiv-2608.18919.yaml) Tschalzev et al., "Lost in Aggregation: How Benchmarks Overlook Irreplaceable Model Strengths"
- [arxiv-2305.02997](../../papers/arxiv-2305.02997.yaml) McElfresh et al., "When Do Neural Nets Outperform Boosted Trees on Tabular Data?"
