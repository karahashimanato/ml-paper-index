---
title: AutoML システムとアーキテクチャ探索 — 何を探し、どう探し、どう比べるのか
kind: method
tags: [automl-systems, neural-architecture-search]
depends_on: [arxiv-1208.3719, arxiv-1603.06212, arxiv-2003.06505, arxiv-1911.04706, arxiv-2006.13799, arxiv-1907.00909, arxiv-2207.12560, arxiv-1908.00709, arxiv-1611.01578, arxiv-1802.01548, arxiv-1802.03268, arxiv-1806.09055, arxiv-1808.05377, arxiv-1902.09635, arxiv-1902.08142, arxiv-1909.09656, arxiv-2007.04074, arxiv-1907.10902, arxiv-1810.05934, arxiv-1902.07638, arxiv-2005.02960, arxiv-1810.03548]
written_at: 2026-10-10
written_by: claude-opus-5-5 via Claude Code
---

# AutoML システムとアーキテクチャ探索 — 何を探し、どう探し、どう比べるのか

<!-- generated:stale -->
> 未反映のカードはありません。
<!-- /generated:stale -->

## この記事の読み方

**AutoML**(機械学習の自動化)は、データを渡すと、前処理、モデルの種類、ハイパーパラメータの選択までを自動で行う仕組みである。ニューラルネットワークの構造そのものを自動で探す**アーキテクチャ探索**(NAS)も、その一部として扱われることが多い。
この記事は16本の新しいカードと既存の6本のカードから、次の点を整理する。

1. 何を探すのか:CASH 問題とパイプライン
2. 表データの AutoML システム:Auto-WEKA、TPOT、auto-sklearn、AutoGluon、FLAML、Auto-PyTorch
3. AutoML の比べ方:AMLB ベンチマークとその注意
4. アーキテクチャ探索の手法:強化学習、進化、重み共有、微分可能な探索
5. アーキテクチャ探索の評価:ランダム探索との比較、重み共有の順位、ベンチマーク

性能の数値は書かない。各論文のページの結果表を参照のこと(カードは結果表を記録せず、主張だけを記録している)。
探索のアルゴリズム(ベイズ最適化、多忠実度の最適化、ランダム探索)そのものは [ベイズ最適化とハイパーパラメータ最適化](bayesian-optimization.md) の記事で扱った。

## 1. 何を探すのか

### CASH 問題

Auto-WEKA は、「どのアルゴリズムを使うか」と「そのハイパーパラメータをどうするか」を同時に決める問題を **CASH**(Combined Algorithm Selection and Hyperparameter optimization)と名付けた。アルゴリズムの選択を、最上位の1つのハイパーパラメータとみなすことで、全体を1つの階層的なハイパーパラメータ最適化の問題に書き直せる [arxiv-1208.3719#c1](https://arxiv.org/pdf/1208.3719v2#page=2 "We note that this problem can be reformulated as a single combined hierarchical hyperparameter optimization problem")。
探索空間は、基本の分類器かアンサンブルか、特徴選択を使うかどうかといった条件付きの選択からなる、4層の階層構造である [arxiv-1208.3719#c4](https://arxiv.org/pdf/1208.3719v2#page=5 "This results in a very wide tree that captures all the hierarchical nature of the model hyperparameters, and allows the creation of a single hyperparameter optimization problem with four hierarchical layers of a total of 786 parameters.")。

### パイプライン全体

He らのサーベイは、AutoML のパイプラインを、データの準備、特徴エンジニアリング、モデルの生成、モデルの評価に分け、モデルの生成を「探索空間」と「最適化の方法」に分けて整理している [arxiv-1908.00709#c1](https://arxiv.org/pdf/1908.00709v6#page=1 "As Figure 1 shows, the AutoML pipeline consists of several processes: data preparation, feature engineering, model generation, and model evaluation.")。
TPOT は、前処理・特徴選択・モデルをつなげた**パイプライン**を木で表し、その木を遺伝的プログラミングで進化させる [arxiv-1603.06212#c1](https://arxiv.org/pdf/1603.06212v1#page=4 "In TPOT, we use GP to evolve the sequence of pipeline operators as well as each operator’s parameters (e.g., the number of trees in a random forest or the number of feature pairs to select during feature selection) to maximize the classiﬁcation accuracy of the pipeline.") [arxiv-1603.06212#c2](https://arxiv.org/pdf/1603.06212v1#page=3 "Each time a data set is passed through a modeling operator, the resulting classiﬁcations are stored such that the most recent classiﬁer to process the data overrides any previous predictions, and the earlier classiﬁer’s predictions are stored as a new feature.")。

## 2. 表データの AutoML システム

システムの部品になる探索の道具には、実行しながら探索空間を組み立てられる Optuna [arxiv-1907.10902#c1](https://arxiv.org/pdf/1907.10902v1#page=2 "Following the original deﬁnition, we use the term deﬁne-by-run in the context of optimization framework to refer to a design that allows the user to dynamically construct the search space.") や、多数の並列の作業者で早期打ち切りを行う ASHA [arxiv-1810.05934#c3](https://arxiv.org/pdf/1810.05934v5#page=4 "Intuitively, ASHA promotes conﬁgurations to the next rung whenever possible instead of waiting for a rung to complete before proceeding to the next rung.") などがある。以下は、それらを組み込んだ「データを渡せば動く」システムである。

| システム | 探し方の中心 | 特徴 |
|---|---|---|
| Auto-WEKA | ベイズ最適化(SMAC、TPE)で CASH を解く | 階層的な探索空間 |
| TPOT | 遺伝的プログラミングでパイプラインを進化 | 正確さと単純さの両立も試みる |
| auto-sklearn 2.0 | メタ学習による設定の組合せ(ポートフォリオ) | 過去のデータセットでの経験を使う |
| AutoGluon-Tabular | ハイパーパラメータ探索をせず、多層のスタッキング | 既定値で多数のモデルを組み合わせる |
| FLAML | 試行のコストを考えた探索 | 計算資源が少ない状況向け |
| Auto-PyTorch Tabular | 多忠実度のベイズ最適化(BOHB)とポートフォリオ | ニューラルネットの構造とハイパーパラメータを同時に探す |

### ベイズ最適化で探す(Auto-WEKA)

Auto-WEKA は、SMAC と TPE という2つのベイズ最適化の手法で CASH を解いた。SMAC は、交差検証の分割を1つずつ評価し、現在の最良の設定に負けた時点で打ち切ることで計算を節約する [arxiv-1208.3719#c2](https://arxiv.org/pdf/1208.3719v2#page=3 "This means that a poorly performing conﬁguration can be discarded after considering as little as a single fold.")。
著者らは、交差検証での改善がテストデータでの改善より大きいことを認め、過学習を検出し避けるもっと良い方法が必要だと述べている [arxiv-1208.3719#c9](https://arxiv.org/pdf/1208.3719v2#page=9 "First, Auto-WEKA still shows larger improvements in cross-validation performance than on test data, suggesting the investigation of more sophisticated methods for detecting and avoiding overﬁtting than our simple correlation-based approach.")。

### 進化で探す(TPOT)

TPOT の論文では、遺伝的プログラミングで導かれた探索と、同じ数のパイプラインをランダムに作る方法とを比べ、多くの場合で平均的に同程度だった。著者らは、導かれた探索は必須ではないかもしれないと示唆している [arxiv-1603.06212#c7](https://arxiv.org/pdf/1603.06212v1#page=7 "This result suggests that guided search may not be vital for the automated design of pipelines because random search generally performs as well as guided search.")。
ランダムに作ったパイプラインは不必要に複雑になりがちだった [arxiv-1603.06212#c8](https://arxiv.org/pdf/1603.06212v1#page=7 "Furthermore, even though TPOT-Random pipelines perform nearly as well as regular TPOT pipelines, TPOT-Random pipelines tend to be needlessly complex and contain 6 pipeline operators on average (Figure 5).")。パイプラインの適合度はテスト用に分けた25%のデータの正確さで評価され、結果も25%の取り置きのデータで報告されている [arxiv-1603.06212#c3](https://arxiv.org/pdf/1603.06212v1#page=4 "In this paper, TPOT pipelines are evaluated based on their classiﬁcation accuracy on the testing set.")。

### メタ学習で始める(auto-sklearn 2.0)

auto-sklearn 2.0 は、多数の過去のデータセットでうまくいった設定の組合せ(**ポートフォリオ**)を用意し、新しいデータセットの大きさなど単純な特徴から、どの方針を使うかを選ぶ [arxiv-2007.04074#c1](https://arxiv.org/pdf/2007.04074v3#page=9 "Under the assumption that we apply the portfolio to datasets from the same distribution of datasets, we have a strong set of default ML pipelines.") [arxiv-2007.04074#c2](https://arxiv.org/pdf/2007.04074v3#page=19 "for each pair of AutoML policies, we ﬁt a random forest to predict whether policy πA outperforms policy πB given the current dataset’s meta-features.")。
Vanschoren のサーベイは、メタ学習は過去のタスクが新しいタスクに似ているほど役立つと述べ、タスクの類似性をどう定義するかを重要な課題に挙げている [arxiv-1810.03548#c2](https://arxiv.org/pdf/1810.03548v1#page=1 "When a new task represents completely unrelated phenomena, or random noise, leveraging prior experience will not be eﬀective.")。

### 探索せずに組み合わせる(AutoGluon-Tabular)

AutoGluon-Tabular の著者らは、それまでの研究が CASH に偏っており、その探索は高価で、性能の悪い設定に多くの計算を使う、と主張した [arxiv-2003.06505#c1](https://arxiv.org/pdf/2003.06505v1#page=1 "Their brute-force search expends signiﬁcant compute evaluating poor model/hyperparameter conﬁgurations that no reasonable data scientist would consider.")。
AutoGluon は、ハイパーパラメータを探索せず、既定値の多様なモデルを**多層にスタッキング**する。上の層のモデルは、元の特徴と下の層の予測を入力にする [arxiv-2003.06505#c2](https://arxiv.org/pdf/2003.06505v1#page=4 "AutoGluon instead simply reuses all of its base layer model types (with the same hyperparameter values) as stackers.")。著者らは、ベンチマークで CASH をまったく使わずに高精度な AutoML が実現できることを初めて示したと述べている [arxiv-2003.06505#c4](https://arxiv.org/pdf/2003.06505v1#page=7 "This demonstrates for the ﬁrst time that high-accuracy AutoML is achievable entirely without CASH.")。
ただし、スタッキングに使う「交差検証の外側の予測」も、早期打ち切りなどを通じて少し過学習しうる、と注意している [arxiv-2003.06505#c3](https://arxiv.org/pdf/2003.06505v1#page=4 "While k-fold bagging efﬁciently reuses training data, it remains susceptible to a subtle form of over-ﬁtting.")。

### コストを考えて探す(FLAML)

FLAML は、1回の試行のコストが、学習器の種類、ハイパーパラメータ、学習データの量、検証の方法で決まることに注目し、良いモデルが見つかるまでの総コストを小さくすることを目標にする [arxiv-1911.04706#c1](https://arxiv.org/pdf/1911.04706v3#page=1 "We recognize that the cost of one trial is jointly decided by the following variables: the choice of learner, a subset of the hyperparameters for the chosen learner, the size of the training data, and the resampling strategy.")。小さなデータ量から始めて、必要に応じてデータ量を増やしていく [arxiv-1911.04706#c5](https://arxiv.org/pdf/1911.04706v3#page=7 "Speciﬁcally, we begin with a small sample size (10K) for each l.")。
使いやすさのために、メタ学習やアンサンブルにはあえて頼らない設計にしている [arxiv-1911.04706#c2](https://arxiv.org/pdf/1911.04706v3#page=3 "FLAML is designed to perform efﬁciently and robustly without relying on meta-learning or ensemble at ﬁrst order, for several usability reasons.")。

### 構造とハイパーパラメータを同時に探す(Auto-PyTorch Tabular)

Auto-PyTorch Tabular は、ニューラルネットの構造と学習のハイパーパラメータは相互に影響するので、同時に最適化すべきだと主張する [arxiv-2006.13799#c1](https://arxiv.org/pdf/2006.13799v3#page=1 "Since there are interaction effects between the best architecture and the best hyperparameter conﬁguration for it, AutoDL systems have to jointly optimize both [9].")。学習のエポック数を予算とする多忠実度のベイズ最適化(BOHB)で探索し [arxiv-2006.13799#c2](https://arxiv.org/pdf/2006.13799v3#page=4 "We choose the number of training epochs as our budgets over the runtime because of its generality and interpretability.")、ポートフォリオで初期化する [arxiv-2006.13799#c4](https://arxiv.org/pdf/2006.13799v3#page=5 "This approach assumes (as all meta-learning approaches) that we have access to a reasonable set of meta-training datasets that are representative of meta-test datasets.")。

## 3. AutoML の比べ方:AMLB

### なぜ共通のベンチマークが必要か

Gijsbers らは、それまでの AutoML の比較は、少数の小さく古いデータセットを使い、システムがうまくいくデータセットを選んでしまう危険があると指摘した [arxiv-1907.00909#c1](https://arxiv.org/pdf/1907.00909v1#page=1 "Authors may even knowingly or unknowingly select datasets on which current systems perform well.")。そこで、事前に決めた基準でデータセットを選ぶ公開のベンチマーク(AMLB)を作った [arxiv-1907.00909#c2](https://arxiv.org/pdf/1907.00909v1#page=3 "We excluded datasets which were too easily solved with AutoML or did not represent typical AutoML scenario’s (e.g. artiﬁcial datasets).")。

### AMLB の設計と、そこから言えないこと

- 各システムは既定の設定で動かす。多くの利用者がそう使うからである [arxiv-1907.00909#c4](https://arxiv.org/pdf/1907.00909v1#page=4 "The AutoML tools were all used with their default hyperparameter values and search spaces, since most users will use them in this way.")。後の版では、システムの開発者が選んだ「モード」だけを指定している [arxiv-2207.12560#c5](https://arxiv.org/pdf/2207.12560v2#page=17 "The modes used to evaluate each AutoML framework is chosen by their developers.")。
- システムの統合は、各システムの開発者と一緒に行い、正しく動くようにしている [arxiv-2207.12560#c1](https://arxiv.org/pdf/2207.12560v2#page=3 "The AutoML frameworks are integrated with the benchmarking tool in direct agreement and jointly with the framework’s developers to ensure correctness.")。
- 失敗した実行はランダムに起きるのではなく、データの大きさなどと関係する。失敗を無視すると難しいタスクで失敗するシステムが得をするので、定数を予測するモデルの結果で埋める [arxiv-2207.12560#c4](https://arxiv.org/pdf/2207.12560v2#page=16 "Ignoring missing values thus means that AutoML frameworks may fail on harder tasks or folds and consequently obtain higher average performance estimates.")。
- GPU のない環境で実行するので、GPU で大きく得をするシステムは評価していない [arxiv-2207.12560#c2](https://arxiv.org/pdf/2207.12560v2#page=6 "As our experiments are run on machines without GPU, we focus on AutoML frameworks which are not significantly affected by the lack thereof.")。

著者らは、結論の範囲も明記している。

- 探索空間も最適化の方法も共通でないので、どの探索空間・どの最適化の方法がよいかについての結論は出せない [arxiv-1907.00909#c5](https://arxiv.org/pdf/1907.00909v1#page=4 "It is important to realize that no two tools share the exact same search space or optimization method, so from this benchmark no conclusions can be drawn about those.")。性能の差を、どの設計の要素によるものかに帰することもできない [arxiv-2207.12560#c6](https://arxiv.org/pdf/2207.12560v2#page=18 "Perhaps the biggest limitation of the design is the inability to attribute the performance of an AutoML framework to any one aspect of its design, as is often done with ablation studies.")。
- ベンチマークのデータは公開されて有名なので、メタ学習に使ったデータと重なっている可能性が高い。その場合、メタ学習を使うシステムの結果は楽観的になりうる [arxiv-2207.12560#c7](https://arxiv.org/pdf/2207.12560v2#page=19 "This ultimately means that the result of AUTO-SKLEARN 2 must be considered very carefully and are likely optimistic") [arxiv-1907.00909#c6](https://arxiv.org/pdf/1907.00909v1#page=4 "An AutoML framework which used datasets of the benchmark in its meta-learning process will have an unfair advantage on them.")。

結果について、初版では、どのシステムも他を一貫して上回ることはなかった [arxiv-1907.00909#c7](https://arxiv.org/pdf/1907.00909v1#page=4 "There is no AutoML system which consistently outperforms all others.")。後の版では、失敗の主な原因はデータセットの大きさで、予測にかかる時間にも大きな差があった [arxiv-2207.12560#c9](https://arxiv.org/pdf/2207.12560v2#page=31 "and found that the main cause for failure was data set size.")。

### 利益相反

AutoML のシステムの論文は、ほとんどが開発者自身による評価である。Auto-WEKA の SMAC、auto-sklearn、Auto-PyTorch、BOHB は同じ研究グループの成果で、AutoGluon は Amazon、FLAML は Microsoft の研究者による。AMLB の著者にも、評価対象のシステム(H2O AutoML、GAMA)の開発者が含まれる(各カードの notes 参照)。

## 4. アーキテクチャ探索の手法

Elsken らのサーベイは、NAS を**探索空間**、**探索戦略**、**性能の推定方法**の3つの軸で整理している [arxiv-1808.05377#c1](https://arxiv.org/pdf/1808.05377v3#page=1 "categorize them according to three dimensions: search space, search strategy, and performance estimation strategy.")。

### 強化学習で探す

Zoph と Le は、ネットワークの構造を記述する文字列を RNN の「制御器」で生成し、その構造を学習した検証の正確さを報酬として、方策勾配(REINFORCE)で制御器を更新した [arxiv-1611.01578#c1](https://arxiv.org/pdf/1611.01578v2#page=2 "Using this accuracy as the reward signal, we can compute the policy gradient to update the controller.") [arxiv-1611.01578#c2](https://arxiv.org/pdf/1611.01578v2#page=4 "In this work, our baseline b is an exponential moving average of the previous architecture accuracies.")。
計算は膨大で、多数の GPU で多数のネットワークを同時に学習した [arxiv-1611.01578#c4](https://arxiv.org/pdf/1611.01578v2#page=7 "which means there are 800 networks being trained on 800 GPUs concurrently at any time.")。Elsken らは、この研究が NAS を主流の話題にし、その後、計算を減らす多くの方法が提案されたと述べている [arxiv-1808.05377#c4](https://arxiv.org/pdf/1808.05377v3#page=6 "While Zoph and Le (2017) used vast computational resources to achieve this result (800 GPUs for three to four weeks), after their work, a wide variety of methods have been published in quick succession to reduce the computational costs and achieve further improvements in performance.")。

### 進化で探す

Real らは、母集団から「最も悪いもの」ではなく「最も古いもの」を取り除く**年齢による進化**を提案した [arxiv-1802.01548#c1](https://arxiv.org/pdf/1802.01548v7#page=3 "in this paper we prefer a novel approach: killing the oldest model in the population")。同じコードと条件で、進化、強化学習、ランダム探索を比べた [arxiv-1802.01548#c2](https://arxiv.org/pdf/1802.01548v7#page=4 "To avoid selection bias, plots do not include optimization runs, as was decided a priori.")。進化は探索の初期により良いモデルを見つけ、最後まで走らせると強化学習と同程度だった [arxiv-1802.01548#c4](https://arxiv.org/pdf/1802.01548v7#page=4 "At the later stages, if we allow to run for the full 20k models (as in the baseline study), evolution produced models with similar accuracy.")。
著者らは、慎重に調整すれば強化学習のほうが良くなるかもしれないと認め [arxiv-1802.01548#c8](https://arxiv.org/pdf/1802.01548v7#page=8 "It is possible that through careful tuning, RL could be made to produce even better models than evolution, but such tuning would likely involve running many experiments, making it more costly.")、結果は使った探索空間とデータセットに限られるかもしれないとも述べている [arxiv-1802.01548#c7](https://arxiv.org/pdf/1802.01548v7#page=6 "Some of our ﬁndings may be restricted to the search spaces and datasets we used.")。

### 重みを共有する(ENAS)

ENAS は、候補の構造を毎回ゼロから学習する代わりに、すべての候補が1つの大きなネットワークの重みを**共有**する [arxiv-1802.03268#c1](https://arxiv.org/pdf/1802.03268v2#page=1 "We observe that the computational bottleneck of NAS is the training of each child model to convergence, only to measure its accuracy whilst throwing away all the trained weights.") [arxiv-1802.03268#c3](https://arxiv.org/pdf/1802.03268v2#page=3 "Nevertheless – and this is perhaps surprising – we ﬁnd that M = 1 works just ﬁne, i.e. we can update ω using the gradient from any single model m sampled from π(m; θ).")。これで探索の計算は大幅に減った [arxiv-1802.03268#c2](https://arxiv.org/pdf/1802.03268v2#page=1 "Compared to NAS, this is a reduction of GPU-hours by more than 1000x.")。
最終的な構造は、共有した重みのまま検証データの1つのミニバッチで評価し、最も良いものだけを再学習して選ぶ [arxiv-1802.03268#c4](https://arxiv.org/pdf/1802.03268v2#page=3 "We then take only the model with the highest reward to re-train from scratch.")。

### 微分可能にする(DARTS)

DARTS は、各辺でどの演算を使うかという離散的な選択を、すべての演算のソフトマックスで重み付けした和に置き換え、構造のパラメータを勾配で最適化する [arxiv-1806.09055#c1](https://arxiv.org/pdf/1806.09055v2#page=3 "To make the search space continuous, we relax the categorical choice of a particular operation to a softmax over all possible operations:")。構造のパラメータは検証損失を、重みは学習損失を最小にする**二段階の最適化**として定式化する [arxiv-1806.09055#c2](https://arxiv.org/pdf/1806.09055v2#page=3 "This implies a bilevel optimization problem (Anandalingam & Friesz, 1992; Colson et al., 2007) with α as the upper-level variable and w as the lower-level variable:")。
内側の最適化は1ステップの学習で近似し、著者らはこの近似の収束の保証は知られていないと述べている [arxiv-1806.09055#c3](https://arxiv.org/pdf/1806.09055v2#page=4 "While we are not currently aware of the convergence guarantees for our optimization algorithm, in practice it is able to reach a ﬁxed point with a suitable choice of")。連続的な表現から取り出した離散的な構造との食い違いも、限界として挙げている [arxiv-1806.09055#c9](https://arxiv.org/pdf/1806.09055v2#page=9 "For example, the current method may suffer from discrepancies between the continuous architecture encoding and the derived discrete architecture.")。

## 5. アーキテクチャ探索の評価

### ランダム探索との比較

いくつかの研究は、NAS の手法がランダム探索と大差ないことを示した。

- DARTS の論文自身が、ランダム探索が競争力のある結果を出すことを認め、それは探索空間の設計が重要であることを反映していると述べている [arxiv-1806.09055#c7](https://arxiv.org/pdf/1806.09055v2#page=8 "It is also interesting to note that random search is competitive for both convolutional and recurrent models, which reﬂects the importance of the search space design.")。
- Yu らは、評価した手法が平均するとランダムな方策と同程度だったと報告した [arxiv-1902.08142#c1](https://arxiv.org/pdf/1902.08142v3#page=1 "On average, the state-of-the-art NAS algorithms perform similarly to the random policy;")。ただし、それは手法が悪いというより、探索空間が十分に絞られていて、ランダムな構造でも良い性能が出るからだ、と解釈している [arxiv-1902.08142#c5](https://arxiv.org/pdf/1902.08142v3#page=2 "Note that this does not necessarily mean that these algorithms perform poorly, but rather that the search space has been sufﬁciently constrained so that even a random architecture in this space provides good results.")。
- Li と Talwalkar も、早期打ち切りを使うランダム探索は、公表されていたランダム探索のベースラインよりずっと強いと示した [arxiv-1902.07638#c4](https://arxiv.org/pdf/1902.07638v3#page=2 "While SOTA NAS methods like DARTS still outperform this baseline, our results demonstrate that the gap is not nearly as large as that suggested by published random search baselines on these tasks [34, 41].")。
- 以前の比較では、ランダム探索に公平な機会を与えていなかった(ランダムな構造を1つしか試していない、など)という指摘もある [arxiv-1902.08142#c4](https://arxiv.org/pdf/1902.08142v3#page=3 "While some works have provided partial comparisons to random search, these comparisons unfortunately did not give a fair chance to the random policy.")。

Elsken らも、引用した研究から、強化学習と進化はランダム探索に勝つが差はかなり小さい、と述べている [arxiv-1808.05377#c5](https://arxiv.org/pdf/1808.05377v3#page=7 "Both approaches consistently perform better than RS in their experiments, but with a rather small margin:")。

### 重み共有は順位を保つか

重み共有で評価した構造の順位が、ゼロから学習したときの順位と一致しなければ、探索は正しい構造を選べない。

- Yu らは、重み共有で得た順位と、共有せずに得た順位がほとんど相関しなかったと報告した [arxiv-1902.08142#c7](https://arxiv.org/pdf/1902.08142v3#page=2 "the architecture rankings obtained with and without weight sharing are entirely uncorrelated in RNN space")。
- Elsken らのサーベイは、重み共有は大きな偏りを生み、最良の構造の性能を大きく過小評価すると述べている [arxiv-1808.05377#c7](https://arxiv.org/pdf/1808.05377v3#page=10 "However, it is currently not clear if this is actually the case (Bender et al., 2018; Sciuto et al., 2019).")。
- He らのサーベイも、重み共有が候補の順位に悪影響を与えると、引用した研究に基づいて述べている [arxiv-1908.00709#c6](https://arxiv.org/pdf/1908.00709v6#page=22 "Yu et al. [11] experimentally showed that the weight-sharing strat-egy degrades the individual architecture’s performance and negatively impacts the real performance ranking of the candidate architectures.")。

### DARTS の失敗

Zela らは、DARTS が劣化した構造を生む12の設定を見つけた [arxiv-1909.09656#c1](https://arxiv.org/pdf/1909.09656v2#page=1 "We identify 12 NAS benchmarks based on four search spaces in which standard DARTS yields degenerate architectures with poor test performance across several datasets (Section 3).")。パラメータを持たないスキップ接続が、ほとんどの辺を占めてしまう [arxiv-1909.09656#c2](https://arxiv.org/pdf/1909.09656v2#page=4 "the parameter-less skip connections dominate in almost all the edges for spaces S1-S3, and for S4 even the harmful Noise operation was selected for ﬁve out of eight operations.")。これらの設定の多くは、意図的に作ったものではなく、元の探索空間の自然な部分空間である [arxiv-1909.09656#c3](https://arxiv.org/pdf/1909.09656v2#page=4 "We emphasize that search spaces S1-S3 are very natural, and, as strict subspaces of the original space, should merely be easier to search than that.")。
著者らは、構造のパラメータについての検証損失のヘッセ行列の最大固有値(損失の谷の鋭さの目安)が、テスト誤差と一緒に増えることを示し [arxiv-1909.09656#c5](https://arxiv.org/pdf/1909.09656v2#page=5 "indeed strongly correlates with test error (with a Pearson correlation coefﬁcient of 0.867).")、これを使った早期打ち切りや正則化を提案した [arxiv-1909.09656#c6](https://arxiv.org/pdf/1909.09656v2#page=6 "To implement this idea, we use a simple heuristic that worked off-the-shelf without any tuning.") [arxiv-1909.09656#c7](https://arxiv.org/pdf/1909.09656v2#page=7 "We emphasize that we do not alter the regularization of the ﬁnal training and evaluation phase, but solely that of the search phase.")。一方、DARTS がよく調整された元の2つのベンチマークでは、改良版は DARTS と同程度だった [arxiv-1909.09656#c9](https://arxiv.org/pdf/1909.09656v2#page=9 "RobustDARTS performed similarly to DARTS for the two original benchmarks from the DARTS paper (PTB and CIFAR-10), on which DARTS was developed and is well tuned;")。

### ベンチマークと再現性

NAS-Bench-101 は、約42万の構造をすべて学習・評価した表を公開し、探索を表の参照だけで行えるようにした [arxiv-1902.09635#c2](https://arxiv.org/pdf/1902.09635v2#page=3 "After de-duplication, there are approximately 423k unique graphs in the search space.") [arxiv-1902.09635#c4](https://arxiv.org/pdf/1902.09635v2#page=3 "We repeat the train-ing and evaluation of all architectures 3 times to ob-tain a measure of variance.")。研究の再現が難しく、手法どうしを比べにくいことが動機である [arxiv-1902.09635#c1](https://arxiv.org/pdf/1902.09635v2#page=1 "different methods are not compa-rable to each other due to different training procedures and different search spaces, which make it difﬁcult to attribute the success of each method to the search algorithm itself.")。
ただし、すべての構造に1つの固定したハイパーパラメータを使い [arxiv-1902.09635#c3](https://arxiv.org/pdf/1902.09635v2#page=3 "We utilize a single, ﬁxed set of hyperparameters for all NAS-Bench-101 models.")、重み共有の手法は直接評価できない [arxiv-1902.09635#c7](https://arxiv.org/pdf/1902.09635v2#page=6 "NAS algorithms based on weight sharing (Pham et al., 2018; Liu et al., 2018b) or network morphisms (Cai et al., 2018; Elsken et al., 2018) cannot be directly evaluated on the dataset, so we did not include them.")。計算を抑えるために、最先端の性能には届かない探索空間になっている [arxiv-1902.09635#c9](https://arxiv.org/pdf/1902.09635v2#page=8 "Unfortunately, this means that the models we evaluate do not reach current state-of-the-art performance on CIFAR-10.")。

再現性については、次の指摘がある。

- 多くの NAS の論文は、探索のコード、評価のコード、乱数のシードを公開しておらず、厳密な再現ができない [arxiv-1902.07638#c1](https://arxiv.org/pdf/1902.07638v3#page=2 "For example, of the 12 papers published since 2018 at NeurIPS, ICML, and ICLR that introduce novel NAS methods (see Table 1), none are exactly reproducible.")。NAS の結果は1回の実行のことが多いが、ハイパーパラメータ最適化では10回の独立な実行で報告するのが標準である [arxiv-1902.07638#c9](https://arxiv.org/pdf/1902.07638v3#page=18 "Consequently, we conclude that either significantly more computational resources need to be devoted to evaluating NAS methods and/or more computationally tractable benchmarks need to be developed to lower the barrier for performing adequate empirical evaluations.")。
- 実験によって、探索空間、計算予算、データ拡張、学習の工夫が違い、学習の工夫そのものが報告される数値に大きく影響する [arxiv-1808.05377#c9](https://arxiv.org/pdf/1808.05377v3#page=13 "It is therefore conceivable that improvements in these ingredients have a larger impact on reported performance numbers than the better architectures found by NAS.")。He らも、異なる設定の結果を集めた比較は公平でないと注意している [arxiv-1908.00709#c4](https://arxiv.org/pdf/1908.00709v6#page=20 "In other words, the comparison is not quite fair.")。
- ベンチマークのノイズを減らすと、最も単純な山登り法が多くの手法を上回る、という報告もある [arxiv-2005.02960#c1](https://arxiv.org/pdf/2005.02960v3#page=1 "In this work, we show that (1) the simplest hill-climbing algorithm is a powerful baseline for NAS, and (2), when the noise in popular NAS benchmark datasets is reduced to a minimum, hill-climbing to outperforms many popular state-of-the-art algorithms.")。

## 設計への示唆(本記事の整理)

- **AutoML の比較は、既定の設定・計算予算・ハードウェアをそろえた共通のベンチマークで読む** [arxiv-1907.00909#c4](https://arxiv.org/pdf/1907.00909v1#page=4 "The AutoML tools were all used with their default hyperparameter values and search spaces, since most users will use them in this way.") [arxiv-2207.12560#c5](https://arxiv.org/pdf/2207.12560v2#page=17 "The modes used to evaluate each AutoML framework is chosen by their developers.")。メタ学習とベンチマークのデータの重なりにも注意する [arxiv-2207.12560#c7](https://arxiv.org/pdf/2207.12560v2#page=19 "This ultimately means that the result of AUTO-SKLEARN 2 must be considered very carefully and are likely optimistic")。
- **探索よりも、多様なモデルの組合せ(アンサンブル、スタッキング)が効く場合がある** [arxiv-2003.06505#c4](https://arxiv.org/pdf/2003.06505v1#page=7 "This demonstrates for the ﬁrst time that high-accuracy AutoML is achievable entirely without CASH.")。ただし、組合せも過学習しうる [arxiv-2003.06505#c3](https://arxiv.org/pdf/2003.06505v1#page=4 "While k-fold bagging efﬁciently reuses training data, it remains susceptible to a subtle form of over-ﬁtting.") [arxiv-2006.13799#c9](https://arxiv.org/pdf/2006.13799v3#page=10 "First of all, while the ensem-bles improve performance overall, it is also known that they can lead to overﬁtting.")。
- **NAS の手法は、同じ探索空間・同じ学習条件のランダム探索と比べる** [arxiv-1902.08142#c2](https://arxiv.org/pdf/1902.08142v3#page=2 "To reduce randomness, the search using each policy, i.e., random and NAS ones, is repeated several times, with different random seeds.") [arxiv-1806.09055#c7](https://arxiv.org/pdf/1806.09055v2#page=8 "It is also interesting to note that random search is competitive for both convolutional and recurrent models, which reﬂects the importance of the search space design.")。探索空間の設計そのものが結果を大きく左右する [arxiv-1902.08142#c5](https://arxiv.org/pdf/1902.08142v3#page=2 "Note that this does not necessarily mean that these algorithms perform poorly, but rather that the search space has been sufﬁciently constrained so that even a random architecture in this space provides good results.")。
- **重み共有を使う場合は、得られる順位が真の順位とどれだけ一致するかを確かめる** [arxiv-1902.08142#c7](https://arxiv.org/pdf/1902.08142v3#page=2 "the architecture rankings obtained with and without weight sharing are entirely uncorrelated in RNN space")。
- **複数の乱数シードで実行し、コードを公開する** [arxiv-1902.07638#c9](https://arxiv.org/pdf/1902.07638v3#page=18 "Consequently, we conclude that either significantly more computational resources need to be devoted to evaluating NAS methods and/or more computationally tractable benchmarks need to be developed to lower the barrier for performing adequate empirical evaluations.")。

## わかっていないこと

- 性能の差を、探索空間、探索の方法、前処理などのどの要素に帰すべきかは、共通のベンチマークでも答えられない [arxiv-2207.12560#c6](https://arxiv.org/pdf/2207.12560v2#page=18 "Perhaps the biggest limitation of the design is the inability to attribute the performance of an AutoML framework to any one aspect of its design, as is often done with ablation studies.")。
- 重み共有がどのような偏りを生むのかは、よくわかっていない [arxiv-1808.05377#c8](https://arxiv.org/pdf/1808.05377v3#page=11 "it is currently not well understood which biases they introduce into the search if the sampling distribution of architectures is optimized along with the one-shot model instead of ﬁxing it")。
- DARTS の近似の収束は保証されていない [arxiv-1806.09055#c3](https://arxiv.org/pdf/1806.09055v2#page=4 "While we are not currently aware of the convergence guarantees for our optimization algorithm, in practice it is able to reach a ﬁxed point with a suitable choice of")。
- AutoML の過学習を検出し避ける方法は、Auto-WEKA の時点から課題として残されている [arxiv-1208.3719#c9](https://arxiv.org/pdf/1208.3719v2#page=9 "First, Auto-WEKA still shows larger improvements in cross-validation performance than on test data, suggesting the investigation of more sophisticated methods for detecting and avoiding overﬁtting than our simple correlation-based approach.")。

## 参照カード

- [arxiv-1208.3719](../../papers/arxiv-1208.3719.yaml) Thornton et al., "Auto-WEKA: Combined Selection and Hyperparameter Optimization of Classification Algorithms"
- [arxiv-1603.06212](../../papers/arxiv-1603.06212.yaml) Olson et al., "Evaluation of a Tree-based Pipeline Optimization Tool for Automating Data Science"
- [arxiv-2007.04074](../../papers/arxiv-2007.04074.yaml) Feurer et al., "Auto-Sklearn 2.0: Hands-free AutoML via Meta-Learning"
- [arxiv-2003.06505](../../papers/arxiv-2003.06505.yaml) Erickson et al., "AutoGluon-Tabular: Robust and Accurate AutoML for Structured Data"
- [arxiv-1911.04706](../../papers/arxiv-1911.04706.yaml) Wang et al., "FLAML: A Fast and Lightweight AutoML Library"
- [arxiv-2006.13799](../../papers/arxiv-2006.13799.yaml) Zimmer, Lindauer & Hutter, "Auto-PyTorch Tabular"
- [arxiv-1810.03548](../../papers/arxiv-1810.03548.yaml) Vanschoren, "Meta-Learning: A Survey"
- [arxiv-1907.00909](../../papers/arxiv-1907.00909.yaml) Gijsbers et al., "An Open Source AutoML Benchmark"
- [arxiv-2207.12560](../../papers/arxiv-2207.12560.yaml) Gijsbers et al., "AMLB: an AutoML Benchmark"
- [arxiv-1908.00709](../../papers/arxiv-1908.00709.yaml) He, Zhao & Chu, "AutoML: A Survey of the State-of-the-Art"
- [arxiv-1808.05377](../../papers/arxiv-1808.05377.yaml) Elsken, Metzen & Hutter, "Neural Architecture Search: A Survey"
- [arxiv-1611.01578](../../papers/arxiv-1611.01578.yaml) Zoph & Le, "Neural Architecture Search with Reinforcement Learning"
- [arxiv-1802.01548](../../papers/arxiv-1802.01548.yaml) Real et al., "Regularized Evolution for Image Classifier Architecture Search"
- [arxiv-1802.03268](../../papers/arxiv-1802.03268.yaml) Pham et al., "Efficient Neural Architecture Search via Parameter Sharing"
- [arxiv-1806.09055](../../papers/arxiv-1806.09055.yaml) Liu, Simonyan & Yang, "DARTS: Differentiable Architecture Search"
- [arxiv-1902.08142](../../papers/arxiv-1902.08142.yaml) Yu et al., "Evaluating the Search Phase of Neural Architecture Search"
- [arxiv-1902.07638](../../papers/arxiv-1902.07638.yaml) Li & Talwalkar, "Random Search and Reproducibility for Neural Architecture Search"
- [arxiv-1909.09656](../../papers/arxiv-1909.09656.yaml) Zela et al., "Understanding and Robustifying Differentiable Architecture Search"
- [arxiv-1902.09635](../../papers/arxiv-1902.09635.yaml) Ying et al., "NAS-Bench-101: Towards Reproducible Neural Architecture Search"
- [arxiv-2005.02960](../../papers/arxiv-2005.02960.yaml) White et al., "Exploring the Loss Landscape in Neural Architecture Search"
- [arxiv-1907.10902](../../papers/arxiv-1907.10902.yaml) Akiba et al., "Optuna: A Next-generation Hyperparameter Optimization Framework"
- [arxiv-1810.05934](../../papers/arxiv-1810.05934.yaml) Li et al., "A System for Massively Parallel Hyperparameter Tuning"
