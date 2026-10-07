---
title: ベイズ変化点検知 — BOCPD とその拡張、オフラインの事後分析、評価の作法
kind: topic
tags: [online-change-point-detection, bayesian-changepoint-models]
depends_on: [arxiv-0710.3742, arxiv-1805.05383, arxiv-1902.04524, arxiv-1710.03276, arxiv-2103.14224, arxiv-1806.02261, arxiv-2302.04759, arxiv-1302.3721, arxiv-2304.00232, arxiv-2405.09330, arxiv-1011.2932, arxiv-2006.15532, arxiv-2211.14097, arxiv-2102.12938, arxiv-2003.06222, arxiv-1801.00718, arxiv-2306.05265, arxiv-2507.01558]
written_at: 2026-10-07
written_by: claude-opus-5-5 via Claude Code
---

# ベイズ変化点検知 — BOCPD とその拡張、オフラインの事後分析、評価の作法

<!-- generated:stale -->
> 未反映のカードはありません。
<!-- /generated:stale -->

## この記事の読み方

変化点検知は、時系列の性質(平均、分散、分布)が変わる時点を見つける問題である。ベイズ的な方法は、変化点の位置や数について**事後分布**を出し、不確実さも併せて扱う。
この記事は、ベイズ変化点検知を2つの流れに分けて整理する。

1. **オンライン**: データが届くたびに、直近の変化点からの経過時間(run length)の事後分布を更新する BOCPD とその拡張
2. **オフライン**: 系列全体を見て、変化点の数と位置の事後分布を求める方法

あわせて、**頑健さ**(外れ値で偽の変化点を出さないか)、**応用**(バンディット、強化学習、障害の原因分析)、**評価の作法**を扱う。

モデルの性能劣化を見つける用途としてのドリフト検知は、[ドリフト検知の記事](../tasks/drift-detection.md) で扱っている。この記事は変化点そのものの推定に焦点を当てる。性能の数値は書かない。各論文のページの結果表を参照のこと(カードは結果表を記録せず、主張だけを記録している)。

## 1. BOCPD — オンラインのベイズ変化点検知

### 前提と仕組み

Adams と MacKay の BOCPD は、次を仮定する。系列は重ならない区間(product partition)に分かれ、区間の中ではデータが独立同分布で、区間ごとのパラメータも独立である [arxiv-0710.3742#c1](https://arxiv.org/pdf/0710.3742v1#page=1 "We further assume that for each partition ρ, the data within it are i.i.d. from some probability distribution")。
多くのベイズ変化点の研究が系列全体を事後的に区切るのに対し、BOCPD はオンラインで因果的に予測することを目指す [arxiv-0710.3742#c2](https://arxiv.org/pdf/0710.3742v1#page=1 "Rather than retrospective segmentation, we focus on causal predictive ﬁltering; generating an accurate distribution of the next unseen datum in the sequence, given only data already observed.")。

- **run length の再帰**: 直近の変化点からの経過時間と、これまでのデータの同時分布を、メッセージパッシングで再帰的に計算する [arxiv-0710.3742#c3](https://arxiv.org/pdf/0710.3742v1#page=2 "We can thus generate a recursive message-passing algorithm for the joint distribution over the current run length and the data")。
- **ハザード関数**: 次の時点で変化点が起きる事前確率である。区間の長さに幾何分布を仮定すると、一定のハザードになる [arxiv-0710.3742#c4](https://arxiv.org/pdf/0710.3742v1#page=2 "is a discrete exponential (geometric) distribution with timescale λ, the process is memoryless and the hazard function is constant")。
- **予測モデル**: 共役な指数型分布族を使うと、十分統計量を逐次更新するだけで済む [arxiv-0710.3742#c6](https://arxiv.org/pdf/0710.3742v1#page=3 "We will only address the exact case in this paper")。
- **計算量**: 1ステップあたりの計算量は、それまでに観測した点の数に比例する。確率の小さい run length を切り捨てれば、平均的には一定になる [arxiv-0710.3742#c7](https://arxiv.org/pdf/0710.3742v1#page=4 "This yields a constant average complexity per iteration on the order of the expected run length E[r], although the worst-case complexity is still linear in the data.")。

### 変化点をどう「宣言」するか

BOCPD が出すのは run length の分布で、「ここが変化点」という答えそのものではない。宣言の仕方は論文によって違う。

- 原論文の評価は、run length の事後分布の図を見て、実際の出来事と照らし合わせる定性的なものである [arxiv-0710.3742#c9](https://arxiv.org/pdf/0710.3742v1#page=4 "Notice that the drops to zero run-length correspond well with the abrupt changes in the mean of the data.")。
- ラグ付きの拡張の論文も、変化点の宣言は実務家に委ね、事後分布の質量が0に大きく移ったときなどを目安にしている [arxiv-1710.03276#c2](https://arxiv.org/pdf/1710.03276v3#page=4 "For instance, if the concentration of the mass of the run length’s distribution shifts greatly toward 0 at time t + 1 after being mostly concentrated around the max possible run length at time t, then this would indicate a change in the regime.")。
- モデル選択付きの拡張(BOCPDMS)は、事後分布から MAP の区切りを出す [arxiv-1805.05383#c3](https://arxiv.org/pdf/1805.05383v2#page=3 "Eq. (6e) is arrived at directly in FL and used for on-line MAP segmentation.")。
- 大規模な評価(TCPDBench)では、他の手法と比べるために MAP の区切りを使っている [arxiv-2003.06222#c5](https://arxiv.org/pdf/2003.06222v3#page=11 "To allow for comparisons to the other methods we use the maximum a posteriori (MAP) segmentation of the series (see, e.g., Fearnhead and Liu, 2007).")。
- 障害の原因分析(BARO)は、最も確率の高い run length が減った時点を変化点としている [arxiv-2405.09330#c3](https://arxiv.org/pdf/2405.09330v1#page=8 "Finally, note that following the assumptions in Section 3.1, we use Latency and Errors to detect anomalies, and we only output the first detected change point as the detected anomaly.")。

### 拡張

- **モデル選択(BOCPDMS)**: 区間ごとに、複数の予測モデルから1つを選ぶ。変化点で新しいモデルが事前分布から選ばれる [arxiv-1805.05383#c2](https://arxiv.org/pdf/1805.05383v2#page=2 "Eq. (1b) implies that the model at time t will be equal to the model at time")。ハイパーパラメータは、オンラインの勾配降下で決める [arxiv-1805.05383#c5](https://arxiv.org/pdf/1805.05383v2#page=5 "Firstly, inference and type-II ML are executed simultaneously (rather than sequentially) and thus enable cold-starts of BOCPDMS.")。
- **ラグ付きの推論**: 少し遅れて、過去の時点の run length を正確に計算し直す [arxiv-1710.03276#c4](https://arxiv.org/pdf/1710.03276v3#page=8 "Our algorithm remains online in the sense that once a new datum is observed the past data need not be reused to update the model.")。ただし、変化点の直前では、ラグが次の区間の点を含んでしまい、パラメータの推定が悪くなることがある [arxiv-1710.03276#c8](https://arxiv.org/pdf/1710.03276v3#page=15 "A reasonable solution is to use as higher order a lag as possible for the detection of changepoints, while using a smaller lag for moment calculations.")。
- **変化点の予測**: 現在の区間がいつ終わるか(残りの時間)を予測する。一定のハザードでは、予測はデータによらなくなるので、変化点の予測が意味を持つのは一定でないハザードを使う場合である [arxiv-1902.04524#c1](https://arxiv.org/pdf/1902.04524v2#page=4 "Note the assumption of independence of the observation model with respect to the residual time and the segment duration.") [arxiv-1902.04524#c2](https://arxiv.org/pdf/1902.04524v2#page=4 "This suggests that online prediction of CPs is more meaningful for non-constant hazard settings.")。ハザードは区間の長さの分布を決める [arxiv-1902.04524#c3](https://arxiv.org/pdf/1902.04524v2#page=2 "induces a geometric distribution over the segment duration")。
- **能動的な多忠実度**: 安いセンサーと高価なセンサーのどちらで観測するかを、情報の得られ方と費用で選ぶ [arxiv-2103.14224#c4](https://arxiv.org/pdf/2103.14224v2#page=5 "Note that the weights can be tuned on held-out data to achieve a desired expected budget.")。

### ハザードとハイパーパラメータの決め方

ハザード(変化点の起きやすさ)の事前分布は、結果を大きく左右する。しかし、多くの論文でその決め方が明記されていない。

- 原論文の実験は、データセットごとに区間の長さの事前の値を設定しているが、その選び方は本文に見当たらない [arxiv-0710.3742#c8](https://arxiv.org/pdf/0710.3742v1#page=4 "In each of the three examples, we use a discrete exponential prior over the interval between changepoints.")。
- ラグ付きの論文も、幾何分布の事前分布を仮定し、一定のハザードを使っている [arxiv-1710.03276#c3](https://arxiv.org/pdf/1710.03276v3#page=5 "this prior distribution is chosen to be the geometric distribution")。
- 能動的な多忠実度の論文も、一定のハザードを仮定している [arxiv-2103.14224#c1](https://arxiv.org/pdf/2103.14224v2#page=2 "We model the arrival of changepoints as a discrete time Bernoulli process with hazard rate 1/β")。
- 変化点の予測の論文は、ハイパーパラメータをラベル付きの系列から最尤推定で学ぶ [arxiv-1902.04524#c5](https://arxiv.org/pdf/1902.04524v2#page=5 "We adopt a data-driven approach by using labeled observation sequences where the change point locations have been marked.")。そのため、変化点のラベルが必要になる。

## 2. 外れ値への頑健さ

### 標準の BOCPD は外れ値で変化点を出しやすい

BOCPD は、次の観測の予測密度が低いと変化点だと判断する。そのため、外れ値で偽の変化点が多く出やすい [arxiv-1806.02261#c1](https://arxiv.org/pdf/1806.02261v2#page=1 "Naturally, this leads to a high false CP discovery rate in the presence of outliers and as they run on-line, pre-processing is not an option.")。
裾の重い分布(Student の t 分布)に替えても解決しない。外れ値の後の run length の比較では、現在の区間での予測密度と事前の予測密度が両方とも変わるからである [arxiv-1806.02261#c3](https://arxiv.org/pdf/1806.02261v2#page=5 "In fact, the perhaps unintuitive consequence is that Student’s t error models will yield CP inference that very closely resembles that of the corresponding normal model.")。

### 一般化ベイズによる頑健化

- **β ダイバージェンス(β-BOCPD)**: run length の事後分布とパラメータの事後分布の両方を、β ダイバージェンスに基づく一般化ベイズの事後分布に置き換える [arxiv-1806.02261#c2](https://arxiv.org/pdf/1806.02261v2#page=4 "This form of robustness is easy to implement and retains the closed forms of BOCPD:")。1つの外れ値で変化点が宣言されないことが、条件付きで示されている [arxiv-1806.02261#c4](https://arxiv.org/pdf/1806.02261v2#page=5 "Theorem 1 provides very mild conditions for the β-D robustiﬁed BLR model ensuring that the odds never favor a CP after any single outlying observation")。β の選び方には原理的な枠組みがなく、オンラインで調整している [arxiv-1806.02261#c6](https://arxiv.org/pdf/1806.02261v2#page=7 "We remedy this by minimizing the expected predictive loss with respect to β on-line.")。
- **拡散スコアマッチング(DSM-BOCD)**: β-BOCPD は β の調整が難しく、各ステップで変分近似が要ると批判し [arxiv-2302.04759#c2](https://arxiv.org/pdf/2302.04759v2#page=3 "Numerically, this makes the loss extremely sensitive to even very minor changes in β, which makes it very difﬁcult to tune β and counteracts the very robustness one hopes to achieve.")、共役な形で計算できる頑健な事後分布を提案した [arxiv-2302.04759#c3](https://arxiv.org/pdf/2302.04759v2#page=6 "This is also the complexity of standard BOCD with the Gaussian likelihood and conjugate prior (Adams & MacKay, 2007).")。頑健さの保証には条件がある [arxiv-2302.04759#c4](https://arxiv.org/pdf/2302.04759v2#page=6 "Note also that m is only applicable to models with support X = Rd, as the expansion in (3) is otherwise not valid without additional boundary conditions.")。

**読むときの注意**:

- β-BOCPD の比較では、標準の BOCPD に、より情報量の多い事前分布を使っている。平らな事前分布だと偽の変化点が多すぎたためである [arxiv-1806.02261#c8](https://arxiv.org/pdf/1806.02261v2#page=34 "If priors are too ﬂat, the standard version declares far too many changepoints.")。
- DSM-BOCD は、重みの基準点をデータ全体の最尤推定値に設定していて、未来のデータを使っている [arxiv-2302.04759#c5](https://arxiv.org/pdf/2302.04759v2#page=6 "In all experiments, we thus picked θ⋆as the maximum likelihood estimate computed on the full data set.")。
- 頑健な変化点検知は、本物の変化点の検出が遅れることが知られている。DSM-BOCD の著者らは、自分たちの実験ではそれを観察しなかったと述べている [arxiv-2302.04759#c7](https://arxiv.org/pdf/2302.04759v2#page=7 "known issue with robust CP detection method is that they can experience a latency when it comes to detecting actual CPs.")。
- DSM-BOCD の論文の最後の著者は、β-BOCPD の第一著者でもある(カードの notes に記録)。

## 3. 応用 — 意思決定の中の変化点検知

- **非定常なバンディット**: 報酬が突然切り替わる環境で、run length を潜在変数にして Thompson sampling に組み込む [arxiv-1302.3721#c2](https://arxiv.org/pdf/1302.3721v1#page=3 "Since we do not know the runlength rt we can introduce it as a latent variable and marginalise it out.")。著者ら自身、適切に調整した他の手法には及ばない環境があり [arxiv-1302.3721#c8](https://arxiv.org/pdf/1302.3721v1#page=16 "However our results suggest that a strategy that just tracks changes in the perceived best arm (Global-CTS2,PA-CTS2), similar to Adapt-EvE, works well.")、後悔の理論的な保証もないと述べている [arxiv-1302.3721#c9](https://arxiv.org/pdf/1302.3721v1#page=16 "however steps still need to be taken to provide any theoretic justiﬁcation for their performance.")。パラメータは、テスト環境の1つで調整している [arxiv-1302.3721#c5](https://arxiv.org/pdf/1302.3721v1#page=10 "The parameters for all experiments shown were tuned based on the PASCAL challenge.")。
- **非定常な MDP**: 再起動型の BOCPD を強化学習に組み込み、誤警報と検出遅れについての保証を示した [arxiv-2304.00232#c3](https://arxiv.org/pdf/2304.00232v1#page=6 "In this section, we provide sufﬁcient conditions on the parameter ηr,s,t that guarantee the false alarm rate control")。ただし、この再起動型は標準の BOCPD の run length の再帰とは別物である [arxiv-2304.00232#c2](https://arxiv.org/pdf/2304.00232v1#page=6 "Recall that in the work of Alami et al. (2020), instead of dealing with a run-length, they deal with the notion of forecaster that is a product of successive Laplace predictors.")。実験は人工的な環境だけで、現実的な環境で変化をどう模擬するかは不明だとしている [arxiv-2304.00232#c8](https://arxiv.org/pdf/2304.00232v1#page=30 "it is unclear to us at the moment of writing this manuscript how to control the process of changing these variables and relate it to the rather latent changes in the underlying state-transition distributions and rewards.")。比較手法には、探索で選んだ値や真の値が与えられている [arxiv-2304.00232#c7](https://arxiv.org/pdf/2304.00232v1#page=30 "The diameter maximizing the cumulative rewards was chosen.")。
- **マイクロサービスの障害の原因分析(BARO)**: 多変量の BOCPD で障害の発生時刻を推定し、その前後の指標の変化で原因を順位付けする [arxiv-2405.09330#c2](https://arxiv.org/pdf/2405.09330v1#page=7 "We then propose to use Multivariate BOCPD, a combination of BOCPD [22] and MultivariateCPD [75], to model the dependency and correlation among metrics to detect anomalies effectively.") [arxiv-2405.09330#c5](https://arxiv.org/pdf/2405.09330v1#page=10 "Note that we do not use the p-value to reject/accept a possible root cause as in standard hypothesis testing.")。最初に検出した変化点を障害の発生時刻と仮定している [arxiv-2405.09330#c4](https://arxiv.org/pdf/2405.09330v1#page=6 "In this work, based on this failure propagation chain, we assume the first anomaly corresponds to the time when the failure first occurs.")。評価は、人工的に注入した障害で行っている [arxiv-2405.09330#c6](https://arxiv.org/pdf/2405.09330v1#page=12 "For each combination of fault type and targeted service, we repeat the operation (i.e. fault injection and metrics data collection) five times, resulting in 100 failure cases for each benchmark microservice system.")。

## 4. オフラインのベイズ変化点解析

系列全体を見て、変化点の数と位置の事後分布を求める。

- **MCMC で探す**: 共役な事前分布で区間のパラメータを積分消去し、変化点の数と位置だけを MCMC で探す [arxiv-1011.2932#c2](https://arxiv.org/pdf/1011.2932v1#page=4 "Noting this, it becomes apparent that sampling k and z is equivalent to a model search over large model space.") [arxiv-1011.2932#c3](https://arxiv.org/pdf/1011.2932v1#page=5 "In this situation a local random walk update may be preferred.")。
- **厳密な再帰の弱点**: 厳密なフィルタリングの再帰は独立なサンプルを素早く出せるが、ハイパーパラメータを固定した条件付きのサンプルになる [arxiv-1011.2932#c5](https://arxiv.org/pdf/1011.2932v1#page=7 "The main weakness of this approach is that the generated samples are dependent on a ﬁxed value of the hyperparameters γ.")。
- **スケーラブルな多重変化点**: 補助的な一様化で、計算量を観測の数ではなく一様な時刻の数の2乗にする [arxiv-2006.15532#c3](https://arxiv.org/pdf/2006.15532v1#page=11 "Firstly, both the computational cost and the memory cost of this version of FFBS algorithm are only quadratic to the number of uniform times K, instead of the number of observations, which is otherwise prohibitive when the ﬁltering probabilities are computed and stored in an event-by-event scale.")。ただし、近い変化点が別々に推定される「結び目」が生じ [arxiv-2006.15532#c5](https://arxiv.org/pdf/2006.15532v1#page=13 "This straightforward approach to pruning knots among changepoints will possibly lead to slightly biased estimation of the locations of changepoints, see simulation studies in the following sections.")、解像度のパラメータが精度と計算量を引き換える [arxiv-2006.15532#c6](https://arxiv.org/pdf/2006.15532v1#page=15 "The tuning parameter needs to be carefully selected for a tradeoﬀbetween the accuracies and eﬃciencies.")。

### 事前分布への敏感さ

- 区間の長さの事前分布(幾何分布)のパラメータの選び方で、結果が変わりうる。小さすぎると小さな変化を検出できず、大きすぎると偽の変化点が出る [arxiv-1011.2932#c4](https://arxiv.org/pdf/1011.2932v1#page=6 "If too large, then spurious changepoints are inferred.")。
- 実データでは、厳密な再帰の変化点の数が、この事前分布に敏感だった [arxiv-1011.2932#c8](https://arxiv.org/pdf/1011.2932v1#page=12 "Only ten unique changepoint conﬁgurations were sampled in the 50,000 iterations of the MCMC scheme.")。

### 不確実性の定量化と理論

- **信用集合**: 分散の変化点について、変化点の位置の事後分布から MAP の推定値と信用集合を作る [arxiv-2211.14097#c1](https://arxiv.org/pdf/2211.14097v3#page=6 "We highlight that the credible set built through the above is not necessarily an interval.")。ただし、理論は変化点が1つの場合だけで [arxiv-2211.14097#c2](https://arxiv.org/pdf/2211.14097v3#page=8 "However, in the scenario of independent Gaussian data, it remains unknown whether our estimator is minimax optimal as the Wild Binary Segmentation algorithm from Wang et al. (2021b).") [arxiv-2211.14097#c9](https://arxiv.org/pdf/2211.14097v3#page=30 "This challenge can explain the relatively small literature on theoretical results for Bayesian change point methodologies.")、変化点を検出したとみなす閾値は「やや恣意的」と著者自身が書いている [arxiv-2211.14097#c5](https://arxiv.org/pdf/2211.14097v3#page=12 "Thus, for typical datasets Algorithm 1 has an effective overall computational complexity of O(TL).")。
- **不確実性の定量化の枠組み(MICH)**: 著者らは、ベイズ変化点検知は最新の手法より一桁遅く、理論が乏しく、結果の要約が難しいと指摘する [arxiv-2507.01558#c1](https://arxiv.org/pdf/2507.01558v2#page=2 "In practice, the majority of BCPD methods simply return the marginal posterior probability that any given index t is a change-point.")。単一の変化点で、最小最大の速さ(対数因子まで)の保証を示した [arxiv-2507.01558#c3](https://arxiv.org/pdf/2507.01558v2#page=1 "In the case of a single change in the mean and/or the variance of an independent sub-Gaussian sequence, we prove that our method attains a localization rate that is minimax optimal up to a log T factor.")。検出の基準は、先行研究の基準を場当たり的だとして改めた [arxiv-2507.01558#c5](https://arxiv.org/pdf/2507.01558v2#page=9 "This rule is somewhat ad hoc and can lead to an inflated false positive rate in practice.")。
- **事後一致性**: 変化点の数と位置について事後分布の一致性を示したが、いくつかの定理は本文で定義されていない仮定に依存している [arxiv-2102.12938#c2](https://arxiv.org/pdf/2102.12938v1#page=4 "We also prove that the minimax rate of O(n−1) (Frick et al., 2014) is attained by the Bayes estimators for change point recovery.") [arxiv-2102.12938#c6](https://arxiv.org/pdf/2102.12938v1#page=9 "Theorem 7. Under A1 −A7, for (2.1) , for the empirical estimator of σ2,")。

### 頻度論の方法とのつながり

最小記述長(MDL)の基準は、特定の事前分布の下でのベイズの周辺尤度に一致する [arxiv-2306.05265#c1](https://arxiv.org/pdf/2306.05265v1#page=3 "Our paper addresses this gap by showing that the MDL criterion corresponds to the marginal likelihood of a Bayesian model with a specific class of prior distributions.")。ただし、その事前分布は各区間のデータ自身から決める、データ依存のものである [arxiv-2306.05265#c4](https://arxiv.org/pdf/2306.05265v1#page=9 "Proposition 2 formally establishes the link between a class of Bayesian CP models and the MDL criterion.")。
頻度論とベイズの変化点の方法は、これまでほぼ独立に発展してきた、と著者らは述べている [arxiv-2306.05265#c2](https://arxiv.org/pdf/2306.05265v1#page=3 "most criteria used by frequentists consistently estimate the number and locations of the breaks, this is rarely investigated in the Bayesian framework.")。オフラインの手法のレビューも、ベイズ的な手法を範囲外にしている [arxiv-1801.00718#c2](https://arxiv.org/pdf/1801.00718v3#page=6 "In particular, Bayesian approaches are not considered in the remainder of this article, even though they provide state-of-the-art results in several domains, such as speech and sound processing.")。

## 5. 評価の作法

### 評価が定性的な論文が多い

- BOCPD の原論文は、事後分布の図を見る定性的な評価だけである [arxiv-0710.3742#c9](https://arxiv.org/pdf/0710.3742v1#page=4 "Notice that the drops to zero run-length correspond well with the abrupt changes in the mean of the data.")。
- ラグ付きの論文の実データの評価も、検出した変化点を歴史的な出来事と照らし合わせる定性的なものである [arxiv-1710.03276#c9](https://arxiv.org/pdf/1710.03276v3#page=19 "For EXO, we ignore random jumps that appear to be mistakes from the procedure.")。
- オフラインの分析の論文には、変化点の正解がない実データで探索的に分析するものや [arxiv-2102.12938#c9](https://arxiv.org/pdf/2102.12938v1#page=16 "As it is impossible to know if there should be any “true” change-points in 2017 data in the absence of additional information, this can be regarded as a preliminary exploratory analysis.")、他の変化点の手法と比較していないものがある [arxiv-2006.15532#c9](https://arxiv.org/pdf/2006.15532v1#page=21 "From the ﬁgure, it is observed that large uncertainties appear for the number of changepoints and their locations.")。
- 能動的な多忠実度の論文の指標は、真の変化点ではなく、高精度のセンサーだけを使った BOCPD との差である [arxiv-2103.14224#c7](https://arxiv.org/pdf/2103.14224v2#page=6 "In other words, we compare the evaluated model to the best it could have done in practice.")。

### 大規模な評価(TCPDBench)

van den Burg と Williams は、人が注釈を付けた実際の時系列で、変化点検知のアルゴリズムを比べた [arxiv-2003.06222#c1](https://arxiv.org/pdf/2003.06222v3#page=8 "In total, eight annotators provided annotations for the 42 time series, with ﬁve annotators assigned to each time series.")。

- **指標**: 区間の重なり(covering)と、許容幅付きの F1 を使う [arxiv-2003.06222#c2](https://arxiv.org/pdf/2003.06222v3#page=6 "In the experiments we use a margin of error of M = 5.")。注釈者の間でも一致は完全ではない [arxiv-2003.06222#c3](https://arxiv.org/pdf/2003.06222v3#page=9 "The ﬁgures show that on average there is a high degree of agreement between annotators, with the median annotator score approximately 0.8 for the covering metric and 0.9 for the F1-score")。
- **2つの設定**: 既定の設定と、各系列でのグリッド探索の最良値(Oracle)で評価した [arxiv-2003.06222#c4](https://arxiv.org/pdf/2003.06222v3#page=10 "It should be emphasized that while the Oracle experiment is important from a theoretical point of view, it is not necessarily a realistic measure of practical algorithm performance.")。
- **既定の設定**: 常に「変化点なし」と答える基準が、多くの手法を上回った [arxiv-2003.06222#c7](https://arxiv.org/pdf/2003.06222v3#page=13 "We also see that in our experiments no method performs signiﬁcantly better than the zero method on the Default experiment, while this does not hold for the Oracle experiment.")。
- **最良値の設定**: 単純な BOCPD が最も高い平均順位だったが、他の多くの手法と統計的に有意な差はなかった [arxiv-2003.06222#c8](https://arxiv.org/pdf/2003.06222v3#page=13 "It is noteworthy that even though bocpd assumes a simple Gaussian model with constant mean for each segment, it outperforms methods that allow for more complex time series behavior such as trend and seasonality (prophet), or autoregressive structures (bocpdms).")。
- **結論**: 著者らは、既定の設定では二分割法が最も良かったが有意差はなく、ハイパーパラメータを調整すると BOCPD が良くなると述べている [arxiv-2003.06222#c9](https://arxiv.org/pdf/2003.06222v3#page=14 "However, the diﬀerences between it and some other algorithms (binseg, segneigh, and rfpop, among others) have been shown to not be statistically signiﬁcantly diﬀerent.")。

**ここから読み取れること(本記事の整理)**: ベイズの変化点検知の強みは、ハイパーパラメータ(ハザードと事前分布)をうまく決められたときに発揮される。しかし、その決め方が多くの論文で明記されていない。

### 評価の指標

オフラインの手法のレビューは、変化点の数の差、最悪の時間誤差(Hausdorff)、Rand 指数、許容幅付きの F1 などの指標を整理している [arxiv-1801.00718#c5](https://arxiv.org/pdf/1801.00718v3#page=11 "A breakpoint is considered detected up to a user-deﬁned margin of error M > 0; true positives Tp are true change points for which there is an estimated one at less than M samples, i.e.")。どの指標を使うかで、評価の意味が変わる。

## 使い方への示唆(本記事の整理)

論文の主張そのものではなく、本記事のまとめである。

1. **ハザードと事前分布は、結果を左右するハイパーパラメータとして扱う**: 決め方を明記し、敏感さを確かめる [arxiv-1011.2932#c4](https://arxiv.org/pdf/1011.2932v1#page=6 "If too large, then spurious changepoints are inferred.") [arxiv-2003.06222#c8](https://arxiv.org/pdf/2003.06222v3#page=13 "It is noteworthy that even though bocpd assumes a simple Gaussian model with constant mean for each segment, it outperforms methods that allow for more complex time series behavior such as trend and seasonality (prophet), or autoregressive structures (bocpdms).")。
2. **外れ値があるなら、頑健化した BOCPD を検討する**: 標準の BOCPD は外れ値で偽の変化点を出しやすい [arxiv-1806.02261#c1](https://arxiv.org/pdf/1806.02261v2#page=1 "Naturally, this leads to a high false CP discovery rate in the presence of outliers and as they run on-line, pre-processing is not an option.")。ただし、本物の変化点の検出が遅れないかを確かめる [arxiv-2302.04759#c7](https://arxiv.org/pdf/2302.04759v2#page=7 "known issue with robust CP detection method is that they can experience a latency when it comes to detecting actual CPs.")。
3. **変化点の宣言の規則を明記する**: BOCPD の出力は分布で、宣言の規則は論文ごとに違う [arxiv-2003.06222#c5](https://arxiv.org/pdf/2003.06222v3#page=11 "To allow for comparisons to the other methods we use the maximum a posteriori (MAP) segmentation of the series (see, e.g., Fearnhead and Liu, 2007).") [arxiv-1710.03276#c2](https://arxiv.org/pdf/1710.03276v3#page=4 "For instance, if the concentration of the mass of the run length’s distribution shifts greatly toward 0 at time t + 1 after being mostly concentrated around the max possible run length at time t, then this would indicate a change in the regime.")。
4. **既定の設定と「変化点なし」の基準と比べる**: 既定の設定では、何もしない基準に負ける手法が多い [arxiv-2003.06222#c7](https://arxiv.org/pdf/2003.06222v3#page=13 "We also see that in our experiments no method performs signiﬁcantly better than the zero method on the Default experiment, while this does not hold for the Oracle experiment.")。
5. **不確実性の保証の範囲を確認する**: 信用集合の理論は単一の変化点に限られることが多い [arxiv-2211.14097#c9](https://arxiv.org/pdf/2211.14097v3#page=30 "This challenge can explain the relatively small literature on theoretical results for Bayesian change point methodologies.") [arxiv-2507.01558#c3](https://arxiv.org/pdf/2507.01558v2#page=1 "In the case of a single change in the mean and/or the variance of an independent sub-Gaussian sequence, we prove that our method attains a localization rate that is minimax optimal up to a log T factor.")。

## わかっていないこと

- **ハイパーパラメータの決め方**: ハザードと事前分布をラベルなしでどう決めるかについて、論文間で共通の方法はこの範囲にない。
- **複数の変化点の理論**: ベイズの多重変化点の推定量の理論は難しく、多くは単一の変化点に限られる [arxiv-2211.14097#c9](https://arxiv.org/pdf/2211.14097v3#page=30 "This challenge can explain the relatively small literature on theoretical results for Bayesian change point methodologies.")。
- **現実的な環境での評価**: 強化学習の応用では、現実的な環境で変化をどう模擬するかが未解決とされる [arxiv-2304.00232#c8](https://arxiv.org/pdf/2304.00232v1#page=30 "it is unclear to us at the moment of writing this manuscript how to control the process of changing these variables and relate it to the rather latent changes in the underlying state-transition distributions and rewards.")。
- **頑健さと検出の遅れの両立**: 頑健化した方法の検出の遅れは、体系的に調べられていない [arxiv-2302.04759#c7](https://arxiv.org/pdf/2302.04759v2#page=7 "known issue with robust CP detection method is that they can experience a latency when it comes to detecting actual CPs.")。

## 現時点での整理

- **BOCPD は run length の事後分布を逐次更新する方法で、区間内の独立同分布などの仮定に基づく** [arxiv-0710.3742#c1](https://arxiv.org/pdf/0710.3742v1#page=1 "We further assume that for each partition ρ, the data within it are i.i.d. from some probability distribution") [arxiv-0710.3742#c3](https://arxiv.org/pdf/0710.3742v1#page=2 "We can thus generate a recursive message-passing algorithm for the joint distribution over the current run length and the data")。
- **標準の BOCPD は外れ値に弱く、一般化ベイズで頑健化できるが、新たな調整パラメータが加わる** [arxiv-1806.02261#c1](https://arxiv.org/pdf/1806.02261v2#page=1 "Naturally, this leads to a high false CP discovery rate in the presence of outliers and as they run on-line, pre-processing is not an option.") [arxiv-1806.02261#c6](https://arxiv.org/pdf/1806.02261v2#page=7 "We remedy this by minimizing the expected predictive loss with respect to β on-line.") [arxiv-2302.04759#c2](https://arxiv.org/pdf/2302.04759v2#page=3 "Numerically, this makes the loss extremely sensitive to even very minor changes in β, which makes it very difﬁcult to tune β and counteracts the very robustness one hopes to achieve.")。
- **オフラインの解析は事前分布に敏感で、不確実性の理論は単一の変化点に限られることが多い** [arxiv-1011.2932#c4](https://arxiv.org/pdf/1011.2932v1#page=6 "If too large, then spurious changepoints are inferred.") [arxiv-2211.14097#c9](https://arxiv.org/pdf/2211.14097v3#page=30 "This challenge can explain the relatively small literature on theoretical results for Bayesian change point methodologies.")。
- **評価は定性的なものが多く、大規模な比較では既定の設定で何もしない基準に勝てない手法が多い** [arxiv-0710.3742#c9](https://arxiv.org/pdf/0710.3742v1#page=4 "Notice that the drops to zero run-length correspond well with the abrupt changes in the mean of the data.") [arxiv-2003.06222#c7](https://arxiv.org/pdf/2003.06222v3#page=13 "We also see that in our experiments no method performs signiﬁcantly better than the zero method on the Default experiment, while this does not hold for the Oracle experiment.") [arxiv-2003.06222#c8](https://arxiv.org/pdf/2003.06222v3#page=13 "It is noteworthy that even though bocpd assumes a simple Gaussian model with constant mean for each segment, it outperforms methods that allow for more complex time series behavior such as trend and seasonality (prophet), or autoregressive structures (bocpdms).")。

**この整理に含まれていないもの**: Fearnhead と Liu の厳密なオンライン推論の原論文(arXiv にない)、隠れマルコフモデルによる区分、ガウス過程による変化点モデル(Saatçi らの原論文は arXiv にない)、PELT や二分割法などの頻度論の個別の手法(既存の変化点検知のカードとレビューを通してだけ触れている)、多変量・高次元の変化点の個別の手法。

## 参照カード

- [arxiv-0710.3742](../../papers/arxiv-0710.3742.yaml) Adams & MacKay, "Bayesian Online Changepoint Detection"
- [arxiv-1805.05383](../../papers/arxiv-1805.05383.yaml) Knoblauch & Damoulas, "Spatio-temporal Bayesian On-line Changepoint Detection with Model Selection"
- [arxiv-1902.04524](../../papers/arxiv-1902.04524.yaml) Agudelo-España et al., "Bayesian Online Prediction of Change Points"
- [arxiv-1710.03276](../../papers/arxiv-1710.03276.yaml) Byrd, Nghiem & Cao, "Lagged Exact Bayesian Online Changepoint Detection with Parameter Estimation"
- [arxiv-2103.14224](../../papers/arxiv-2103.14224.yaml) Gundersen et al., "Active multi-fidelity Bayesian online changepoint detection"
- [arxiv-1806.02261](../../papers/arxiv-1806.02261.yaml) Knoblauch, Jewson & Damoulas, "Doubly Robust Bayesian Inference for Non-Stationary Streaming Data with β-Divergences"
- [arxiv-2302.04759](../../papers/arxiv-2302.04759.yaml) Altamirano, Briol & Knoblauch, "Robust and Scalable Bayesian Online Changepoint Detection"
- [arxiv-1302.3721](../../papers/arxiv-1302.3721.yaml) Mellor & Shapiro, "Thompson Sampling in Switching Environments with Bayesian Online Change Point Detection"
- [arxiv-2304.00232](../../papers/arxiv-2304.00232.yaml) Alami, Mahfoud & Moulines, "Restarted Bayesian Online Change-point Detection for Non-Stationary Markov Decision Processes"
- [arxiv-2405.09330](../../papers/arxiv-2405.09330.yaml) Pham, Ha & Zhang, "BARO: Robust Root Cause Analysis for Microservices via Multivariate Bayesian Online Change Point Detection"
- [arxiv-1011.2932](../../papers/arxiv-1011.2932.yaml) Wyse & Friel, "Simulation-based Bayesian analysis for multiple changepoints"
- [arxiv-2006.15532](../../papers/arxiv-2006.15532.yaml) Lu, "Scalable Bayesian Multiple Changepoint Detection via Auxiliary Uniformization"
- [arxiv-2211.14097](../../papers/arxiv-2211.14097.yaml) Cappello & Madrid Padilla, "Bayesian variance change point detection with credible sets"
- [arxiv-2102.12938](../../papers/arxiv-2102.12938.yaml) Guha & Datta, "On Posterior consistency of Bayesian Changepoint models"
- [arxiv-2003.06222](../../papers/arxiv-2003.06222.yaml) van den Burg & Williams, "An Evaluation of Change Point Detection Algorithms"
- [arxiv-1801.00718](../../papers/arxiv-1801.00718.yaml) Truong, Oudre & Vayatis, "Selective review of offline change point detection methods"
- [arxiv-2306.05265](../../papers/arxiv-2306.05265.yaml) Ardia, Dufays & Ordas Criado, "Linking Frequentist and Bayesian Change-Point Methods"
- [arxiv-2507.01558](../../papers/arxiv-2507.01558.yaml) Berlind, Cappello & Madrid Padilla, "A Bayesian framework for change-point detection with uncertainty quantification"
