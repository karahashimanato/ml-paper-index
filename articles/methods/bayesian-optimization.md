---
title: ベイズ最適化とハイパーパラメータ最適化 — 代理モデル、多忠実度、ランダム探索との比較
kind: method
tags: [bayesian-optimization, multi-fidelity-optimization, hyperparameter-optimization]
depends_on: [arxiv-1206.2944, arxiv-1012.2599, arxiv-1807.02811, arxiv-0912.3995, arxiv-1603.06560, arxiv-1807.01774, arxiv-1810.05934, arxiv-1605.07079, arxiv-1502.05700, arxiv-1910.01739, arxiv-1910.06403, arxiv-1907.10902, arxiv-2012.03826, arxiv-2104.10201, arxiv-2107.05847, arxiv-2109.06716, arxiv-1902.07638, arxiv-1802.09596, arxiv-1911.01914, arxiv-2305.02997, arxiv-2407.04491, arxiv-2506.16791, arxiv-2007.04074]
written_at: 2026-10-07
written_by: claude-opus-5-5 via Claude Code
---

# ベイズ最適化とハイパーパラメータ最適化 — 代理モデル、多忠実度、ランダム探索との比較

<!-- generated:stale -->
> ⚠ この記事の執筆日(2026-10-07)以降に作成された関連カードが 6 件あります(未反映。執筆日と同じ日に作成されたカードを含む): `arxiv-1208.3719`, `arxiv-1603.06212`, `arxiv-1902.09635`, `arxiv-1908.00709`, `arxiv-1911.04706`, `arxiv-2006.13799`
<!-- /generated:stale -->

## この記事の読み方

ベイズ最適化は、評価に時間やお金のかかる関数(たとえば「このハイパーパラメータで学習したときの検証誤差」)を、少ない評価回数で最適化する方法である。
これまでに評価した点から目的関数の**代理モデル**(ガウス過程など)を作り、その予測の不確実さを使って次に評価する点を**獲得関数**で選ぶ、という手順を繰り返す。

この記事は、ハイパーパラメータ最適化(HPO)を中心に次の5点を整理する。

1. ベイズ最適化の仕組みと前提
2. 多忠実度: 安い評価で候補を絞る方法(Hyperband など)
3. 規模を上げる工夫とフレームワーク
4. **ランダム探索と比べて本当に良いのか**、ベンチマークは何を示したか
5. 実務での注意(過剰な調整、探索空間の設計、予算)

これまでの記事([勾配ブースティング木](gradient-boosted-trees.md)、[自己教師あり学習](self-supervised-representation-learning.md)、[異常検知](../topics/anomaly-detection-classical-vs-deep.md))で繰り返し出てきた「チューニングの公平さ」の問題も、ここで扱う。

性能の数値は書かない。各論文のページの結果表を参照のこと(カードは結果表を記録せず、主張だけを記録している)。

## 1. ベイズ最適化の仕組みと前提

### 代理モデルと獲得関数

- 獲得関数は、不確実なところを調べる(探索)と、良さそうなところを調べる(活用)の間で自動的に釣り合いを取る [arxiv-1012.2599#c1](https://arxiv.org/pdf/1012.2599v1#page=3 "This optimization technique has the nice property that it aims to minimize the number of objective function evaluations.")。
- 最もよく使われる獲得関数は期待改善量(EI)である [arxiv-1807.02811#c5](https://arxiv.org/pdf/1807.02811v1#page=7 "These alternate acquisition functions are most useful in exotic problems where an assumption made by expected improvement, that the primary beneﬁt of sampling occurs through an improvement at the point sampled, is no longer true.")。Snoek らは、改善確率より振る舞いが良く、GP-UCB のように別の調整パラメータが要らないことから EI を選んでいる [arxiv-1206.2944#c1](https://arxiv.org/pdf/1206.2944v2#page=3 "In this work we will focus on the expected improvement criterion, as it has been shown to be better-behaved than probability of improvement, but unlike the method of GP upper conﬁdence bounds (GP-UCB), it does not require its own tuning parameter.")。
- 知識勾配やエントロピー探索は、「サンプルした点での改善」という EI の前提が成り立たない場合(ノイズが大きいときなど)に有用である [arxiv-1807.02811#c5](https://arxiv.org/pdf/1807.02811v1#page=7 "These alternate acquisition functions are most useful in exotic problems where an assumption made by expected improvement, that the primary beneﬁt of sampling occurs through an improvement at the point sampled, is no longer true.") [arxiv-1807.02811#c6](https://arxiv.org/pdf/1807.02811v1#page=11 "When such phenomenon are ﬁrst-order, KG tends to signiﬁcantly outperform EI (Wu et al., 2017; Poloczek et al., 2017; Wu and Frazier, 2016; Toscano-Palmerin and Frazier, 2018).")。ただし、この利点を示した研究の多くは、チュートリアルの著者自身が関わったものである(カードの notes に記録)。

### ガウス過程の設定が結果を左右する

- **カーネルの選択は決定的に重要**で、サンプル関数の滑らかさを決める [arxiv-1012.2599#c3](https://arxiv.org/pdf/1012.2599v1#page=9 "The choice of covariance function for the Gaussian Process is crucial, as it determines the smoothness properties of samples drawn from it.")。よく使われる二乗指数カーネルは、実際の最適化問題には滑らかすぎるとされる [arxiv-1206.2944#c2](https://arxiv.org/pdf/1206.2944v2#page=4 "However, sample functions with this covariance function are unrealistically smooth for practical optimization problems.")。実験でも、カーネルの選択が性能に大きく影響した [arxiv-1206.2944#c7](https://arxiv.org/pdf/1206.2944v2#page=10 "The assumption of the inﬁnite diﬀerentiability of the underlying function as imposed by the commonly used squared exponential is too restrictive for this problem.")。
- GP 自体のハイパーパラメータは、最尤推定・MAP 推定・完全なベイズ推定(MCMC で積分する)で決める [arxiv-1807.02811#c4](https://arxiv.org/pdf/1807.02811v1#page=6 "To choose the hyperparameters, three approaches are typically considered.")。Snoek らは点推定ではなく積分を勧めている [arxiv-1206.2944#c3](https://arxiv.org/pdf/1206.2944v2#page=5 "As both optimization and Markov chain Monte Carlo are computationally dominated by the cubic cost of solving an N-dimensional linear system")。
- ノイズは、評価ごとに独立で分散一定のガウス分布と仮定されることがほとんどである [arxiv-1807.02811#c3](https://arxiv.org/pdf/1807.02811v1#page=1 "In almost all work on Bayesian optimization, noise is assumed independent across evaluations and Gaussian with constant variance.")。

### 時間と並列化

- 評価にかかる時間は設定によって違うので、「1秒あたりの期待改善量」が提案されている [arxiv-1206.2944#c4](https://arxiv.org/pdf/1206.2944v2#page=6 "In this work, we assume that these functions are independent of each other, although their coupling may be usefully captured using GP variants of multi-task learning (e.g., Teh et al. (2005); Bonilla et al. (2008)).")。評価1回あたりでは劣るが、実時間では速くなる場合がある [arxiv-1206.2944#c8](https://arxiv.org/pdf/1206.2944v2#page=10 "In this case, GP EI MCMC is superior to GP EI per Second in terms of function evaluations but GP EI per Second ﬁnds better parameters faster than GP EI MCMC as it learns to use a less strict convergence tolerance early on while exploring the other parameters.")。
- 並列に評価するときは、まだ結果の出ていない評価の結果を仮に想定し、その平均で次の点を選ぶ [arxiv-1206.2944#c5](https://arxiv.org/pdf/1206.2944v2#page=6 "Instead we propose a sequential strategy that takes advantage of the tractable inference properties of the Gaussian process to compute Monte Carlo estimates of the acquisiton function under diﬀerent possible results from pending function evaluations.")。

### 理論的な保証と、その前提

GP-UCB には、累積の後悔(regret)の上界が示されている [arxiv-0912.3995#c1](https://arxiv.org/pdf/0912.3995v4#page=1 "We formalize this task as a multi-armed bandit problem, where the payoﬀfunction is either sampled from a Gaussian process (GP) or has low RKHS norm.")。ただし、その前提は強い。

- 目的関数が既知のカーネルを持つ GP から生成されているか、RKHS のノルムが小さいことを仮定する [arxiv-0912.3995#c3](https://arxiv.org/pdf/0912.3995v4#page=5 "This theorem shows that, with high probability over samples from the GP, the cumulative regret is bounded in terms of the maximum information gain, forging a novel connection between GP optimization and experimental design.") [arxiv-0912.3995#c5](https://arxiv.org/pdf/0912.3995v4#page=6 "Note that we still run the same GP-UCB algorithm, whose prior and noise model are misspeciﬁed in this case.")。カーネルとノイズは既知とされる。
- 実験では、理論が指示する探索の強さより小さい値の方が良く働いた [arxiv-0912.3995#c7](https://arxiv.org/pdf/0912.3995v4#page=7 "While the choice of βt as recommended by Theorem 1 leads to competitive performance of GP-UCB, we ﬁnd (using cross-validation) that the algorithm is improved by scaling βt down by a factor 5.")。
- 実際に使われる獲得関数の良い性能を説明する有限時間の上界はなく、収束の速さもほとんどわかっていない [arxiv-1807.02811#c9](https://arxiv.org/pdf/1807.02811v1#page=16 "It is also possible that new acquisition functions may provide substantial value in high dimensional problems.")。

### 向いている問題、向かない問題

- ベイズ最適化は、20次元未満の連続の領域に最も向いている [arxiv-1807.02811#c1](https://arxiv.org/pdf/1807.02811v1#page=1 "It is best-suited for optimization over continuous domains of less than 20 dimensions, and tolerates stochastic noise in function evaluations.")。評価回数が数百回程度に限られる問題を想定している [arxiv-1807.02811#c2](https://arxiv.org/pdf/1807.02811v1#page=1 "f is “expensive to evaluate” in the sense that the number of evaluations that may be performed is limited, typically to a few hundred.")。
- 次元が増えると問題は悪化する [arxiv-1012.2599#c9](https://arxiv.org/pdf/1012.2599v1#page=43 "In order to deal with this problem eﬀectively, it may be necessary to do automatic feature selection, or assume independence and optimize each dimension individually.")。事前分布の設計が決定的に重要で、GP がいつも最良とは限らない [arxiv-1012.2599#c8](https://arxiv.org/pdf/1012.2599v1#page=43 "A particular issue is that the design of the prior is absolutely critical to eﬃcient Bayesian optimization.")。
- HPO のレビューは、基本的な GP は条件付きのハイパーパラメータや数値でないハイパーパラメータを扱えず、次元が高いと性能が落ち、評価回数の3乗で計算量が増えるとまとめている [arxiv-2107.05847#c2](https://arxiv.org/pdf/2107.05847v3#page=12 "Most importantly, standard GPs have runtime complexity that is cubic in the number of samples, which can result in a signiﬁcant overhead when the archive A becomes large.")。

## 2. 多忠実度 — 安い評価で候補を絞る

学習の途中経過や、データの一部での学習のような「安い評価」を使って、見込みのない設定を早めに打ち切る方法である。

| 方法 | 仕組み | 前提・限界 |
|---|---|---|
| Hyperband | ランダムに選んだ設定に少しずつ資源を配り、悪い半分を落とすこと(successive halving)を、打ち切りの強さを変えて繰り返す [arxiv-1603.06560#c2](https://arxiv.org/pdf/1603.06560v4#page=6 "However, for a ﬁxed B, it is not clear a priori whether we should (a) consider many conﬁgurations (large n) with a small average training time; or (b) consider a small number of conﬁgurations (small n) with longer average training times.") [arxiv-1603.06560#c3](https://arxiv.org/pdf/1603.06560v4#page=8 "Hence, Hyperband performs a geometric search in the average budget per conﬁguration and removes the need to select n for a ﬁxed budget at the cost of approximately smax + 1 times more work than running SuccessiveHalving for a single value of n.") | 最適な設定が資源の量によって変わると、少ない資源での性能は多い資源での性能の目安にならない [arxiv-1603.06560#c5](https://arxiv.org/pdf/1603.06560v4#page=21 "In these situations, the rate of convergence to the true loss is usually slow because the performance on a smaller resource is not indicative of that on a larger resource.")。ゆっくり収束するが最終的に良い設定を落としうる [arxiv-1603.06560#c6](https://arxiv.org/pdf/1603.06560v4#page=33 "The core issue arises when conﬁgurations with drastically slower convergence rates ultimately result in better models.") |
| BOHB | Hyperband の候補をランダムではなく、TPE に似たモデルで選ぶ [arxiv-1807.01774#c2](https://arxiv.org/pdf/1807.01774v1#page=3 "Due to the nature of kernel density estimators, TPE easily supports mixed continuous and discrete spaces, and model construction scales linearly in the number of data points (in contrast to the cubic-time Gaussian processes (GPs) predominant in the BO literature).") | 最小の予算での評価に、大きな予算での良さについての情報が含まれている必要がある [arxiv-1807.01774#c6](https://arxiv.org/pdf/1807.01774v1#page=14 "To get substantial speedups, an evaluation with a budget of bmin should contain some information about the quality of a conﬁguration with larger budgets; for example, when subsampling the data, the smallest subset should not be one datum, but rather enough points to ﬁt a meaningful model.")。安い評価が誤解を招く場合に備えて、一部はランダムに選ぶ [arxiv-1807.01774#c5](https://arxiv.org/pdf/1807.01774v1#page=4 "This means, that in the worst case (when the lower ﬁdelities are misleading), BOHB is at most this factor times slower than RS, but it is still guaranteed to converge eventually.") |
| ASHA | 段の完了を待たずに昇格させる非同期版 [arxiv-1810.05934#c3](https://arxiv.org/pdf/1810.05934v5#page=4 "Intuitively, ASHA promotes conﬁgurations to the next rung whenever possible instead of waiting for a rung to complete before proceeding to the next rung.") | 非同期のため、後から見ると誤った昇格が少数起きる [arxiv-1810.05934#c4](https://arxiv.org/pdf/1810.05934v5#page=5 "ASHA is able to remove the bottleneck associated with synchronous promotions by incurring a small number of incorrect promotions, i.e. conﬁgurations that were promoted early on but are not in the top 1/η of conﬁgurations in hindsight.") |
| FABOLAS | データの部分集合の大きさを、最適化の入力の1つとして扱う [arxiv-1605.07079#c1](https://arxiv.org/pdf/1605.07079v2#page=1 "We treat the size of a randomly subsampled dataset Nsub as an additional input to the blackbox function, and allow the optimizer to actively choose it at each function evaluation.") | 小さい部分集合でも最適な設定の位置がだいたい保たれる、という観察に基づく [arxiv-1605.07079#c3](https://arxiv.org/pdf/1605.07079v2#page=4 "Additionally, there are no deceiving local optima on smaller subsets.")。学習時間がデータ量に比例するモデルでは利点が小さい [arxiv-1605.07079#c8](https://arxiv.org/pdf/1605.07079v2#page=8 "For the same reason of linear scaling, Hyperband was substantially slower than vanilla Bayesian optimization to make a recommendation, but it did ﬁnd good hyperparameter settings when given enough time.") |

**読むときの注意**: 多忠実度の論文どうしの比較には、食い違いがある。

- Hyperband の論文自身、ほとんどの実験で最も攻撃的な打ち切りの段だけの方が Hyperband より良かったと書き、「振り返れば、それだけを走らせればよかった」と述べている [arxiv-1603.06560#c9](https://arxiv.org/pdf/1603.06560v4#page=21 "In hindsight, we should have just run bracket s = 4, since aggressive early-stopping provides massive speedups on many of these benchmarking tasks.")。
- ASHA の論文は、FABOLAS の論文の「Hyperband より速い」という結果に、評価の枠組みを揃えると異議を唱えている [arxiv-1810.05934#c7](https://arxiv.org/pdf/1810.05934v5#page=13 "Interestingly, by leveraging these intermediate losses, we observe that Hyperband actually outperforms Fabolas.")。
- BOHB の比較の多くは、代理モデルによるベンチマーク上の検証誤差で、テストの性能は示されていない [arxiv-1807.01774#c9](https://arxiv.org/pdf/1807.01774v1#page=16 "There is no test performance that could indicate overﬁtting.")。
- BOHB は、高次元の人工問題では TPE や SMAC に負けた [arxiv-1807.01774#c7](https://arxiv.org/pdf/1807.01774v1#page=6 "However, we note that with as many as 64 dimensions, TPE and SMAC started to perform better than BOHB since the noise grows and evaluating conﬁgurations on a smaller budget does not help to build better models for the full budget.")。

## 3. 規模を上げる工夫とフレームワーク

### 計算量と高次元

- **GP の計算量**: 推論の時間が評価回数の3乗で増える [arxiv-1502.05700#c1](https://arxiv.org/pdf/1502.05700v2#page=1 "inference time grows cubically in the number of observations")。ニューラルネットワークの最終層にベイズ線形回帰を載せる方法(DNGO)は、評価回数に線形の計算量にする [arxiv-1502.05700#c2](https://arxiv.org/pdf/1502.05700v2#page=3 "we take a pragmatic approach and add a Bayesian linear regressor to the last hidden layer of a deep neural network") [arxiv-1502.05700#c3](https://arxiv.org/pdf/1502.05700v2#page=3 "scales linearly in the number of observations, and cubically in the basis function dimensionality")。ただし、活性化関数の選択で不確実性の推定が大きく変わる [arxiv-1502.05700#c4](https://arxiv.org/pdf/1502.05700v2#page=4 "the commonly used rectiﬁed linear (ReLU) function can lead to very poor estimates of uncertainty, which causes the Bayesian optimization routine to explore excessively")。
- **高次元・多数の評価**: 大域的な GP は、長さのスケールなどが探索空間全体で一定だと暗に仮定している [arxiv-1910.01739#c2](https://arxiv.org/pdf/1910.01739v4#page=2 "implicitly suppose that characteristic lengthscales and signal variances of the function are constant in the search space")。TuRBO は、良い点の周りの信頼領域で局所的な GP を使う [arxiv-1910.01739#c3](https://arxiv.org/pdf/1910.01739v4#page=3 "We choose our TR to be a hyperrectangle centered at the best solution found so far")。

### フレームワーク

- **BoTorch**: 解析的に書けない獲得関数をモンテカルロで近似し、乱数を固定して決定的な最適化問題として解く [arxiv-1910.06403#c1](https://arxiv.org/pdf/1910.06403v3#page=3 "Instead, MC integration can be used to approximate the expectation (1) using samples from the posterior.") [arxiv-1910.06403#c2](https://arxiv.org/pdf/1910.06403v3#page=3 "and hold it ﬁxed between evaluations throughout the course of optimization")。
- **Optuna**: 探索空間を目的関数の実行中に動的に組み立てる(define-by-run)[arxiv-1907.10902#c1](https://arxiv.org/pdf/1907.10902v1#page=2 "Following the original deﬁnition, we use the term deﬁne-by-run in the context of optimization framework to refer to a design that allows the user to dynamically construct the search space.")。見込みのない試行を途中で打ち切る機能(ASHA の変種)を持つ [arxiv-1907.10902#c4](https://arxiv.org/pdf/1907.10902v1#page=5 "our implementation does not allow repechage")。
- **HEBO**: 多数の HPO の課題で、出力のばらつきが一様でないことと非定常性を確かめ、出力の変換と入力の歪みを加えた [arxiv-2012.03826#c1](https://arxiv.org/pdf/2012.03826v6#page=8 "In 58/108 tasks, the gain is signiﬁcant at the 95% level of conﬁdence (p-value < 0.025).") [arxiv-2012.03826#c2](https://arxiv.org/pdf/2012.03826v6#page=7 "In 79/108 tasks, the gain is signiﬁcant at the 95% level of conﬁdence (p-value < 0.025).") [arxiv-2012.03826#c3](https://arxiv.org/pdf/2012.03826v6#page=9 "We observe that the well-known Box-Cox (Box & Cox, 1964) and Yeo-Jonhson (Yeo & Johnson, 2000) output transformations in conjunction with the Kumaraswamy (Kumaraswamy, 1980) input transformation, oﬀer a balance between simplicity of implementation and empirical performance.")。

**読むときの注意**: フレームワークの論文は、いずれも開発者が自分のフレームワークを評価している。

- BoTorch は他のライブラリを既定の設定で比べた [arxiv-1910.06403#c6](https://arxiv.org/pdf/1910.06403v3#page=9 "First, we ﬁnd that BOTORCH’s algorithms tend to achieve greater sample efﬁciency compared to those of other packages (all packages use their default models and settings).")。
- Optuna の比較では、GP に基づく他のライブラリの方が多くの場合良かったが、1試行あたりの時間がずっと長かった [arxiv-1907.10902#c6](https://arxiv.org/pdf/1907.10902v1#page=6 "Meanwhile, GPyOpt performed better than TPE+CMA-ES in 34/56 cases in terms of the best-attained loss value.")。
- HEBO は、設計の根拠にした分析と評価に、同じ課題群を使っている [arxiv-2012.03826#c6](https://arxiv.org/pdf/2012.03826v6#page=12 "Each experiment is repeated for 20 random seeds.")。

## 4. ランダム探索と比べて本当に良いのか

### ランダム探索が強い理由

HPO のレビューは先行研究を引いて、多くの HPO の問題は実質的な次元が低い(効くハイパーパラメータが少ない)ので、ランダム探索の方がグリッド探索より効くハイパーパラメータをよく調べられると説明している [arxiv-2107.05847#c1](https://arxiv.org/pdf/2107.05847v3#page=9 "Altogether, this makes RS preferable to GS and a surprisingly strong baseline for HPO in many practical settings.")。

### ベイズ最適化が勝った報告

Black-Box Optimization Challenge 2020 の分析は、ベイズ最適化がランダム探索より優れることを決定的に示した、としている [arxiv-2104.10201#c8](https://arxiv.org/pdf/2104.10201v2#page=11 "The top submissions showed over 100× sample efﬁciency gains compared to random search.")。ただし、条件は次のとおりである。

- 問題はモデル×データセット×損失関数の組み合わせで、検証データでの指標を最適化する [arxiv-2104.10201#c1](https://arxiv.org/pdf/2104.10201v2#page=4 "The search space varied by ML model and was provided to the algorithm by the benchmark.")。
- 予算は、少数の並列の提案を少ない回数だけ繰り返す設定である [arxiv-2104.10201#c2](https://arxiv.org/pdf/2104.10201v2#page=5 "The optimizers had a total of 640 seconds compute time for making suggestions on each problem (16 iterations with batch size of 8); or 40 seconds per iteration.")。
- ランダム探索は、対数尺度などで歪めた空間で一様に選ぶ。そのため、素朴なランダム探索よりすでに強い [arxiv-2104.10201#c7](https://arxiv.org/pdf/2104.10201v2#page=7 "Note also that the baseline random search samples uniformly in the warped space from the search conﬁguration.")。
- 比較の対象は各パッケージの既定の設定で、著者らは「パッケージではなく既定の方法の比較」だと注意している [arxiv-2104.10201#c5](https://arxiv.org/pdf/2104.10201v2#page=6 "Note that this comparison does not necessarily show that one package is better than another; it rather compares the performance of their default methods.")。
- 単純なアンサンブル(2つの方法の提案を半分ずつ使う)が、それぞれ単独より大きく良かった [arxiv-2104.10201#c9](https://arxiv.org/pdf/2104.10201v2#page=9 "This analysis hints that ensembling may be useful in avoiding failed models where an individual BO algorithm makes little progress.")。

### ベンチマークは何を示したか

HPOBench は、代理モデルや表引きで安く評価できる、再現可能なベンチマーク集である [arxiv-2109.06716#c2](https://arxiv.org/pdf/2109.06716v3#page=4 "While surrogate benchmarks are similarly cheap to query, the surrogate’s internal ML model adds extra complexity and the benchmark’s quality crucially depends on the quality of this model and its training data.")。

- 高度な方法の多くはランダム探索を上回ったが、多忠実度の方法で Hyperband を上回ったものは一部だった [arxiv-2109.06716#c7](https://arxiv.org/pdf/2109.06716v3#page=8 "We can observe that four out of ﬁve black-box methods are signiﬁcantly better than RS.")。
- 予算が小さいときは多忠実度の方法が有利で、予算が十分あれば多忠実度を使わない方法が追いつく [arxiv-2109.06716#c8](https://arxiv.org/pdf/2109.06716v3#page=9 "Overall, multi-ﬁdelity optimizers outperform black-box optimizers for relatively small compute budgets.")。
- 個々のベンチマークでは、ランダム探索が勝つこともある [arxiv-2109.06716#c9](https://arxiv.org/pdf/2109.06716v3#page=10 "By exploring a very broad range of benchmarks, we also found an existence proof that black-box methods can outperform multi-ﬁdelity methods for very high budgets and that even advanced methods can be outperformed by RS in individual benchmarks.")。
- 比較した方法はすべて既定の設定で動かしている [arxiv-2109.06716#c6](https://arxiv.org/pdf/2109.06716v3#page=24 "We note that we used the default settings for all tools and implementations.")。

### NAS でのランダム探索

ニューラルアーキテクチャ探索(NAS)では、Li と Talwalkar が、公表されていたランダム探索のベースラインは弱く、早期打ち切り付きのランダム探索は、同程度の計算量でずっと競争力があると示した [arxiv-1902.07638#c2](https://arxiv.org/pdf/1902.07638v3#page=4 "Some works either compare to random search given a budget of just of few evaluations [34, 41] or Bayesian optimization methods without efficient architecture evaluation schemes [23].") [arxiv-1902.07638#c4](https://arxiv.org/pdf/1902.07638v3#page=2 "While SOTA NAS methods like DARTS still outperform this baseline, our results demonstrate that the gap is not nearly as large as that suggested by published random search baselines on these tasks [34, 41].")。
また、調べた NAS の論文に完全に再現できるものはなかった [arxiv-1902.07638#c1](https://arxiv.org/pdf/1902.07638v3#page=2 "For example, of the 12 papers published since 2018 at NeurIPS, ICML, and ICLR that introduce novel NAS methods (see Table 1), none are exactly reproducible.")。試行間のばらつきが大きいので、複数の独立な実行で報告するよう勧めている [arxiv-1902.07638#c9](https://arxiv.org/pdf/1902.07638v3#page=18 "Consequently, we conclude that either significantly more computational resources need to be devoted to evaluating NAS methods and/or more computationally tractable benchmarks need to be developed to lower the barrier for performing adequate empirical evaluations.")。

### 既存の表データのカードとのつながり

- **アルゴリズムによって効き目が違う**: Probst らの Tunability の研究では、チューニングの効き目はアルゴリズムで大きく違い、ランダムフォレストでは小さかった [arxiv-1802.09596#c5](https://arxiv.org/pdf/1802.09596v3#page=8 "Clearly, some algorithms such as glmnet and svm are much more tunable than the others, while ranger is the algorithm with the smallest tunability, which is in line with common knowledge in the web community.")。
- **探索の規模がアルゴリズムで違う比較**: 比較研究の中には、グリッドの大きさがアルゴリズムごとに大きく違うものがある [arxiv-1911.01914#c3](https://arxiv.org/pdf/1911.01914v1#page=11 "Since the size of the grid is diﬀerent for diﬀerent classiﬁers (i.e. 3840, 256 and 1920 for XGB, RF and GB respectively), the time dedicated to ﬁnding the best parameters is not directly comparable between classiﬁers.")。
- **軽い調整で十分なことが多い**: 表データでは、GBDT の軽いランダム探索の方が、手法の選択より効くことが多い [arxiv-2305.02997#c2](https://arxiv.org/pdf/2305.02997v4#page=1 "light hyperparameter tuning on a GBDT is more important than choosing between NNs and GBDTs")。
- **調整した既定値という選択肢**: 多数のデータで調整した既定値を使い、複数のアルゴリズムを既定値のまま試す方が、1つのアルゴリズムを素朴に HPO するより速く、良いことが多かった [arxiv-2407.04491#c6](https://arxiv.org/pdf/2407.04491v3#page=10 "Simply trying all default algorithms is faster and very often better than (naive) single-algorithm HPO.")。ただし、単一の検証データでの HPO は、交差検証より検証データに過学習しやすい [arxiv-2407.04491#c20](https://arxiv.org/pdf/2407.04491v3#page=10 "This means that HPO can overfit the validation set more easily than in a cross-validation setup.")。
- **ベンチマークの固定された候補**: 大規模な表データのベンチマークでも、ハイパーパラメータの候補をランダムな固定の集合にしていて、HPO の手法やばらつきは調べていない [arxiv-2506.16791#c18](https://arxiv.org/pdf/2506.16791v4#page=10 "We use a fixed set of 200 random hyperparameter configurations to enable the study of ensemble pipelines.")。

## 5. 実務での注意

- **過剰な調整(overtuning)**: 入れ子の再標本化(外側の評価と内側の HPO を分ける)は、偏りのない評価を保証するが、より良いモデルを作るわけではない。多数の評価の後の過剰な調整は、十分に分析されていない [arxiv-2107.05847#c4](https://arxiv.org/pdf/2107.05847v3#page=24 "This eﬀect has been called either overtuning, meta-overﬁtting or oversearching (Ng, 1997; Quinlan & Cameron-Jones, 1995).")。Hyperband の論文でも、多数のデータセットでベイズ的な方法が検証データに過学習する兆候が見られた [arxiv-1603.06560#c8](https://arxiv.org/pdf/1603.06560v4#page=16 "Bayesian methods outperform Hyperband and random search in test error performance but also exhibit signs of overﬁtting to the validation set, as they outperform Hyperband by a larger margin on the validation error rank.")。
- **内側の評価は粗くてよい**: 内側で必要なのは正確な推定ではなく、設定の正しい順位である [arxiv-2107.05847#c5](https://arxiv.org/pdf/2107.05847v3#page=27 "Hence, it might be appropriate to use a 10-fold CV on the outside to ensure proper generalization error estimation of the tuned learner, but to use only 2 folds or simple holdout on the inside.")。
- **探索空間の設計**: カテゴリのハイパーパラメータを整数で表すのはよくある間違いで、距離に基づく最適化を悪くする [arxiv-2107.05847#c6](https://arxiv.org/pdf/2107.05847v3#page=28 "Encoding categorical values as integers is a common mistake that degrades the performance of optimizers that rely on information about distances between HPCs, such as BO.")。
- **単純な方法で足りる場合**: 評価が安く探索空間が小さいときは、ランダム探索や Hyperband に戻るのがよい [arxiv-2107.05847#c7](https://arxiv.org/pdf/2107.05847v3#page=29 "When performance evaluations are cheap and the search space is small, it may therefore be beneﬁcial to fall back on simple and robust approaches such as RS, Hyperband, or any tuner with minimal inference overhead.")。
- **予算**: いつ止めるかは未解決の実務上の課題で、実際には事前に決めた時間がほとんどである [arxiv-2107.05847#c9](https://arxiv.org/pdf/2107.05847v3#page=30 "A simple rule-of-thumb might be scaling the budget of HPC evaluations with search space dimensionality in a linear fashion like 50 × l or 100 × l, which would also deﬁne the number of full budget units in a multi-ﬁdelity setup.")。
- **ベンチマークの一般化**: どのベンチマークもすべての状況を代表しない [arxiv-2107.05847#c8](https://arxiv.org/pdf/2107.05847v3#page=29 "However, no single benchmark exists which includes all relevant scenarios and whose results generalize to all possible applications.")。

AutoML の文脈では、Auto-sklearn 2.0 がデータセットごとに探索の方針自体を選ぶ方法をとっている [arxiv-2007.04074#c2](https://arxiv.org/pdf/2007.04074v3#page=19 "for each pair of AutoML policies, we ﬁt a random forest to predict whether policy πA outperforms policy πB given the current dataset’s meta-features.")。詳しくは [フォールバックとモデル選択の記事](../topics/model-fallback-and-selection.md) を参照。

## 設計への示唆(本記事の整理)

論文の主張そのものではなく、本記事のまとめである。

1. **まず歪めた空間でのランダム探索を基準にする**: ランダム探索は強い基準で、対数尺度などの設計だけで大きく変わる [arxiv-2104.10201#c7](https://arxiv.org/pdf/2104.10201v2#page=7 "Note also that the baseline random search samples uniformly in the warped space from the search conﬁguration.") [arxiv-2107.05847#c1](https://arxiv.org/pdf/2107.05847v3#page=9 "Altogether, this makes RS preferable to GS and a surprisingly strong baseline for HPO in many practical settings.")。
2. **評価が高価で次元が低ければベイズ最適化**: 20次元未満、数百回の評価が目安とされる [arxiv-1807.02811#c1](https://arxiv.org/pdf/1807.02811v1#page=1 "It is best-suited for optimization over continuous domains of less than 20 dimensions, and tolerates stochastic noise in function evaluations.") [arxiv-1807.02811#c2](https://arxiv.org/pdf/1807.02811v1#page=1 "f is “expensive to evaluate” in the sense that the number of evaluations that may be performed is limited, typically to a few hundred.")。
3. **安い評価が本番の性能を予測するなら多忠実度**: 予算が小さいときに有利だが、予測しない場合は誤った打ち切りが起きる [arxiv-2109.06716#c8](https://arxiv.org/pdf/2109.06716v3#page=9 "Overall, multi-ﬁdelity optimizers outperform black-box optimizers for relatively small compute budgets.") [arxiv-1603.06560#c5](https://arxiv.org/pdf/1603.06560v4#page=21 "In these situations, the rate of convergence to the true loss is usually slow because the performance on a smaller resource is not indicative of that on a larger resource.")。
4. **評価の外側と内側を分ける**: 検証データへの過学習に注意する [arxiv-2107.05847#c4](https://arxiv.org/pdf/2107.05847v3#page=24 "This eﬀect has been called either overtuning, meta-overﬁtting or oversearching (Ng, 1997; Quinlan & Cameron-Jones, 1995).") [arxiv-2407.04491#c20](https://arxiv.org/pdf/2407.04491v3#page=10 "This means that HPO can overfit the validation set more easily than in a cross-validation setup.")。
5. **論文の比較では、既定値か調整か・誰が実装したかを見る** [arxiv-2104.10201#c5](https://arxiv.org/pdf/2104.10201v2#page=6 "Note that this comparison does not necessarily show that one package is better than another; it rather compares the performance of their default methods.") [arxiv-1910.06403#c6](https://arxiv.org/pdf/1910.06403v3#page=9 "First, we ﬁnd that BOTORCH’s algorithms tend to achieve greater sample efﬁciency compared to those of other packages (all packages use their default models and settings).")。

## わかっていないこと

- **過剰な調整の大きさと対策**: 十分に分析されておらず、知られている対策も少ない [arxiv-2107.05847#c4](https://arxiv.org/pdf/2107.05847v3#page=24 "This eﬀect has been called either overtuning, meta-overﬁtting or oversearching (Ng, 1997; Quinlan & Cameron-Jones, 1995).")。
- **実際の獲得関数の理論**: 有限時間の保証がない [arxiv-1807.02811#c9](https://arxiv.org/pdf/1807.02811v1#page=16 "It is also possible that new acquisition functions may provide substantial value in high dimensional problems.")。
- **予算の決め方**: 未解決 [arxiv-2107.05847#c9](https://arxiv.org/pdf/2107.05847v3#page=30 "A simple rule-of-thumb might be scaling the budget of HPC evaluations with search space dimensionality in a linear fashion like 50 × l or 100 × l, which would also deﬁne the number of full budget units in a multi-ﬁdelity setup.")。
- **多忠実度の前提が成り立つかの判定**: 安い評価が本番の性能を予測するかを事前に知る方法は、この範囲では示されていない [arxiv-1807.01774#c6](https://arxiv.org/pdf/1807.01774v1#page=14 "To get substantial speedups, an evaluation with a budget of bmin should contain some information about the quality of a conﬁguration with larger budgets; for example, when subsampling the data, the smallest subset should not be one datum, but rather enough points to ﬁt a meaningful model.") [arxiv-1603.06560#c5](https://arxiv.org/pdf/1603.06560v4#page=21 "In these situations, the rate of convergence to the true loss is usually slow because the performance on a smaller resource is not indicative of that on a larger resource.")。

## 現時点での整理

- **ベイズ最適化は、代理モデルと獲得関数で評価回数を節約する方法で、低次元・高価な評価に向く** [arxiv-1012.2599#c1](https://arxiv.org/pdf/1012.2599v1#page=3 "This optimization technique has the nice property that it aims to minimize the number of objective function evaluations.") [arxiv-1807.02811#c1](https://arxiv.org/pdf/1807.02811v1#page=1 "It is best-suited for optimization over continuous domains of less than 20 dimensions, and tolerates stochastic noise in function evaluations.")。
- **理論的な保証は強い仮定のもとのもので、実際の設定とはずれている** [arxiv-0912.3995#c3](https://arxiv.org/pdf/0912.3995v4#page=5 "This theorem shows that, with high probability over samples from the GP, the cumulative regret is bounded in terms of the maximum information gain, forging a novel connection between GP optimization and experimental design.") [arxiv-0912.3995#c7](https://arxiv.org/pdf/0912.3995v4#page=7 "While the choice of βt as recommended by Theorem 1 leads to competitive performance of GP-UCB, we ﬁnd (using cross-validation) that the algorithm is improved by scaling βt down by a factor 5.")。
- **多忠実度の方法は、安い評価が本番を予測するという前提に依存する** [arxiv-1603.06560#c5](https://arxiv.org/pdf/1603.06560v4#page=21 "In these situations, the rate of convergence to the true loss is usually slow because the performance on a smaller resource is not indicative of that on a larger resource.") [arxiv-1807.01774#c6](https://arxiv.org/pdf/1807.01774v1#page=14 "To get substantial speedups, an evaluation with a budget of bmin should contain some information about the quality of a conﬁguration with larger budgets; for example, when subsampling the data, the smallest subset should not be one datum, but rather enough points to ﬁt a meaningful model.")。
- **ベイズ最適化はランダム探索を上回るという報告がある一方、ランダム探索が勝つ場合もあり、比較の条件に注意が要る** [arxiv-2104.10201#c8](https://arxiv.org/pdf/2104.10201v2#page=11 "The top submissions showed over 100× sample efﬁciency gains compared to random search.") [arxiv-2109.06716#c9](https://arxiv.org/pdf/2109.06716v3#page=10 "By exploring a very broad range of benchmarks, we also found an existence proof that black-box methods can outperform multi-ﬁdelity methods for very high budgets and that even advanced methods can be outperformed by RS in individual benchmarks.") [arxiv-1902.07638#c4](https://arxiv.org/pdf/1902.07638v3#page=2 "While SOTA NAS methods like DARTS still outperform this baseline, our results demonstrate that the gap is not nearly as large as that suggested by published random search baselines on these tasks [34, 41].")。
- **実務では、過剰な調整、探索空間の設計、予算の決め方が、手法の選択と同じくらい重要である** [arxiv-2107.05847#c4](https://arxiv.org/pdf/2107.05847v3#page=24 "This eﬀect has been called either overtuning, meta-overﬁtting or oversearching (Ng, 1997; Quinlan & Cameron-Jones, 1995).") [arxiv-2107.05847#c6](https://arxiv.org/pdf/2107.05847v3#page=28 "Encoding categorical values as integers is a common mistake that degrades the performance of optimizers that rely on information about distances between HPCs, such as BO.") [arxiv-2107.05847#c9](https://arxiv.org/pdf/2107.05847v3#page=30 "A simple rule-of-thumb might be scaling the budget of HPC evaluations with search space dimensionality in a linear fashion like 50 × l or 100 × l, which would also deﬁne the number of full budget units in a multi-ﬁdelity setup.")。

**この整理に含まれていないもの**: TPE と SMAC の原論文(arXiv にない)、ランダム探索の原論文(Bergstra と Bengio 2012。レビューを通してだけ触れている)、メタ学習による初期化、多目的のベイズ最適化、制約付きのベイズ最適化、進化戦略(CMA-ES)、NAS の個別の手法。

## 参照カード

- [arxiv-1206.2944](../../papers/arxiv-1206.2944.yaml) Snoek, Larochelle & Adams, "Practical Bayesian Optimization of Machine Learning Algorithms"
- [arxiv-1012.2599](../../papers/arxiv-1012.2599.yaml) Brochu, Cora & de Freitas, "A Tutorial on Bayesian Optimization of Expensive Cost Functions, with Application to Active User Modeling and Hierarchical Reinforcement Learning"
- [arxiv-1807.02811](../../papers/arxiv-1807.02811.yaml) Frazier, "A Tutorial on Bayesian Optimization"
- [arxiv-0912.3995](../../papers/arxiv-0912.3995.yaml) Srinivas et al., "Gaussian Process Optimization in the Bandit Setting: No Regret and Experimental Design"
- [arxiv-1603.06560](../../papers/arxiv-1603.06560.yaml) Li et al., "Hyperband: A Novel Bandit-Based Approach to Hyperparameter Optimization"
- [arxiv-1807.01774](../../papers/arxiv-1807.01774.yaml) Falkner, Klein & Hutter, "BOHB: Robust and Efficient Hyperparameter Optimization at Scale"
- [arxiv-1810.05934](../../papers/arxiv-1810.05934.yaml) Li et al., "A System for Massively Parallel Hyperparameter Tuning"
- [arxiv-1605.07079](../../papers/arxiv-1605.07079.yaml) Klein et al., "Fast Bayesian Optimization of Machine Learning Hyperparameters on Large Datasets"
- [arxiv-1502.05700](../../papers/arxiv-1502.05700.yaml) Snoek et al., "Scalable Bayesian Optimization Using Deep Neural Networks"
- [arxiv-1910.01739](../../papers/arxiv-1910.01739.yaml) Eriksson et al., "Scalable Global Optimization via Local Bayesian Optimization"
- [arxiv-1910.06403](../../papers/arxiv-1910.06403.yaml) Balandat et al., "BoTorch: A Framework for Efficient Monte-Carlo Bayesian Optimization"
- [arxiv-1907.10902](../../papers/arxiv-1907.10902.yaml) Akiba et al., "Optuna: A Next-generation Hyperparameter Optimization Framework"
- [arxiv-2012.03826](../../papers/arxiv-2012.03826.yaml) Cowen-Rivers et al., "HEBO Pushing The Limits of Sample-Efficient Hyperparameter Optimisation"
- [arxiv-2104.10201](../../papers/arxiv-2104.10201.yaml) Turner et al., "Bayesian Optimization is Superior to Random Search for Machine Learning Hyperparameter Tuning: Analysis of the Black-Box Optimization Challenge 2020"
- [arxiv-2107.05847](../../papers/arxiv-2107.05847.yaml) Bischl et al., "Hyperparameter Optimization: Foundations, Algorithms, Best Practices and Open Challenges"
- [arxiv-2109.06716](../../papers/arxiv-2109.06716.yaml) Eggensperger et al., "HPOBench: A Collection of Reproducible Multi-Fidelity Benchmark Problems for HPO"
- [arxiv-1902.07638](../../papers/arxiv-1902.07638.yaml) Li & Talwalkar, "Random Search and Reproducibility for Neural Architecture Search"
- [arxiv-1802.09596](../../papers/arxiv-1802.09596.yaml) Probst, Bischl & Boulesteix, "Tunability: Importance of Hyperparameters of Machine Learning Algorithms"
- [arxiv-1911.01914](../../papers/arxiv-1911.01914.yaml) Bentéjac et al., "A Comparative Analysis of XGBoost"
- [arxiv-2305.02997](../../papers/arxiv-2305.02997.yaml) McElfresh et al., "When Do Neural Nets Outperform Boosted Trees on Tabular Data?"
- [arxiv-2407.04491](../../papers/arxiv-2407.04491.yaml) Holzmüller et al., "Better by Default: Strong Pre-Tuned MLPs and Boosted Trees on Tabular Data"
- [arxiv-2506.16791](../../papers/arxiv-2506.16791.yaml) Erickson et al., "TabArena: A Living Benchmark for Machine Learning on Tabular Data"
- [arxiv-2007.04074](../../papers/arxiv-2007.04074.yaml) Feurer et al., "Auto-Sklearn 2.0: Hands-free AutoML via Meta-Learning"
