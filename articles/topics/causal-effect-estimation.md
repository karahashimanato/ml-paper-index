---
title: 因果効果の推定 — 前提、メタ学習器と二重機械学習、木と森、ニューラルネット、正解のない評価
kind: topic
tags: [causal-effect-estimation, causal-meta-learners, treatment-effect-networks]
depends_on: [arxiv-1706.03461, arxiv-1608.00060, arxiv-1712.04912, arxiv-2004.14497, arxiv-1605.03661, arxiv-1606.03976, arxiv-1906.02120, arxiv-1705.08821, arxiv-1504.01132, arxiv-1706.09523, arxiv-1711.02582, arxiv-2011.04216, arxiv-2101.10943, arxiv-2107.13346, arxiv-1707.02641, arxiv-1804.05146, arxiv-1510.04342, arxiv-1610.01271, arxiv-2609.03003, arxiv-2609.06941, arxiv-2609.36881, arxiv-2609.39523]
written_at: 2026-10-10
written_by: claude-opus-5-5 via Claude Code
---

# 因果効果の推定 — 前提、メタ学習器と二重機械学習、木と森、ニューラルネット、正解のない評価

<!-- generated:stale -->
> 未反映のカードはありません。
<!-- /generated:stale -->

## この記事の読み方

「この薬を飲んだら、飲まなかった場合と比べてどれだけ良くなるか」のように、**処置**(介入)の効果を、観察データから機械学習で推定する研究を整理する。
予測とは違い、知りたい量そのもの(処置した場合としなかった場合の差)は、どの個人についても観測できない。この点が、手法と評価の両方を難しくしている。

この記事は16本の新しいカードと既存の6本のカードから、次の点を整理する。

1. 何を推定するのか、そのために何を仮定するのか
2. メタ学習器(S/T/X/R/DR-learner)と二重機械学習(DML)
3. 木と森(因果木、因果フォレスト、BCF)
4. ニューラルネットワーク(表現の釣り合い、TARNet/CFR、Dragonnet、CEVAE)
5. 正解のない評価:半合成ベンチマーク、競技会、モデル選択
6. 因果の基盤モデル

性能の数値は書かない。各論文のページの結果表を参照のこと(カードは結果表を記録せず、主張だけを記録している)。

## 1. 何を推定するのか、何を仮定するのか

### 推定したい量

各個人には、処置を受けた場合の結果 $Y(1)$ と受けなかった場合の結果 $Y(0)$ の2つの**潜在的結果**がある。

- **個人の処置効果**(ITE):$Y(1) - Y(0)$ [arxiv-1605.03661#c2](https://arxiv.org/pdf/1605.03661v3#page=2 "The fundamental problem of causal inference is that only one potential outcome is observed for a given context x:")。
- **条件付き平均処置効果**(CATE):特徴 $x$ を持つ人たちでの平均 $\tau(x) = E[Y(1) - Y(0) \mid X = x]$ [arxiv-1706.03461#c2](https://arxiv.org/pdf/1706.03461v6#page=3 "This assumption is, however, not suﬃcient to identify the CATE.")。
- **平均処置効果**(ATE):全体での平均 [arxiv-1605.03661#c2](https://arxiv.org/pdf/1605.03661v3#page=2 "The fundamental problem of causal inference is that only one potential outcome is observed for a given context x:")。

1人について観測できるのはどちらか一方の結果だけである [arxiv-1606.03976#c1](https://arxiv.org/pdf/1606.03976v5#page=2 "this is known as the Consistency assumption.")。これは「因果推論の根本問題」と呼ばれ、通常の交差検証のように、予測と正解を比べて評価することができない [arxiv-1504.01132#c3](https://arxiv.org/pdf/1504.01132v3#page=3 "We address this by proposing approaches for constructing unbiased estimates of the mean-squared error of the causal eﬀect of the treatment.")。
Künzel らは、個人の効果そのものは強い追加の仮定なしには識別できないが、CATE の最良の推定量は、平均二乗誤差の意味で ITE の最良の推定量でもある、と述べている [arxiv-1706.03461#c2](https://arxiv.org/pdf/1706.03461v6#page=3 "This assumption is, however, not suﬃcient to identify the CATE.")。

### 識別のための前提

観察データから CATE を推定するには、多くの論文が次の前提を置く [arxiv-1606.03976#c2](https://arxiv.org/pdf/1606.03976v5#page=2 "The validity of strong ignorability cannot be assessed from data, and must be determined by domain knowledge and understanding of the causal relationships between the variables.") [arxiv-1504.01132#c4](https://arxiv.org/pdf/1504.01132v3#page=4 "Later we show that by using propensity score weighting [19], we can adapt all of the methods to that case.") [arxiv-1706.09523#c1](https://arxiv.org/pdf/1706.09523v4#page=4 "The ﬁrst condition assumes we have no unmeasured confounders, and the second condition (overlap) is necessary to estimate treatment eﬀects everywhere in covariate space.")。

- **交絡なし**(強い無視可能性):特徴 $x$ が与えられれば、処置の割り当ては潜在的結果と独立。つまり、処置と結果の両方に影響する要因(交絡因子)はすべて観測されている。
- **重なり**(正値性):どの $x$ でも、処置を受ける確率(**傾向スコア**)が0でも1でもない。
- **SUTVA**:ある人の処置が他の人の結果に影響しない。

Shalit らは、交絡なしの前提が成り立つかどうかはデータからは確かめられないと強調している [arxiv-1606.03976#c2](https://arxiv.org/pdf/1606.03976v5#page=2 "The validity of strong ignorability cannot be assessed from data, and must be determined by domain knowledge and understanding of the causal relationships between the variables.")。この前提がなければ、DML の推定する量は因果効果ではなく単なる関連の大きさになる、と Chernozhukov らも注意している [arxiv-1608.00060#c8](https://arxiv.org/pdf/1608.00060v7#page=35 "Without unconfoundedness/conditional exogeneity, these quantities measure association, and could be referred to as average predictive effect (APE) and average predictive effect for the exposed (APEX).")。

### 隠れた交絡

交絡因子が観測されていなければ、一般には追加の仮定なしに効果を推定できない [arxiv-1705.08821#c1](https://arxiv.org/pdf/1705.08821v2#page=1 "On the the other hand, if a confounder is hidden or unmeasured, it is impossible in the general case (i.e. without further assumptions) to estimate the effect of the intervention on the outcome [40].")。CEVAE は、隠れた交絡因子のノイズのある**代理変数**(プロキシ)から、変分オートエンコーダで交絡因子を推定しようとする [arxiv-1705.08821#c4](https://arxiv.org/pdf/1705.08821v2#page=3 "We further assume that the joint distribution p (Z, X, t, y) of the latent confounders Z and the observed confounders X can be approximately recovered solely from the observations (X, t, y).")。
ただし著者ら自身、隠れた交絡因子が観測された変数と無関係なら不可能だと述べ [arxiv-1705.08821#c4](https://arxiv.org/pdf/1705.08821v2#page=3 "We further assume that the joint distribution p (Z, X, t, y) of the latent confounders Z and the observed confounders X can be approximately recovered solely from the observations (X, t, y).")、VAE がいつ真のモデルを特定できるかについての理論はほとんどないと認めている [arxiv-1705.08821#c6](https://arxiv.org/pdf/1705.08821v2#page=2 "This has the disadvantage that little theory is currently available to justify when learning with VAEs can identify the true model.")。

### 重なりは高次元で厳しくなる

D'Amour らは、見落とされがちな緊張関係を指摘した。交絡なしの前提をもっともらしくするために特徴を増やすほど、特徴が処置をほぼ完全に予測してしまう部分集団が現れやすくなり、重なりが崩れる [arxiv-1711.02582#c1](https://arxiv.org/pdf/1711.02582v4#page=2 "This intuition, however, has the opposite implications for overlap: the richer the set of covariates, the closer these covariates come to perfectly predicting treatment assignment for at least some subgroups.")。
厳密な重なりのもとでは、特徴の数が増えても処置群と対照群の区別がつく度合いは一定に抑えられることを示している [arxiv-1711.02582#c5](https://arxiv.org/pdf/1711.02582v4#page=8 "Asymptotically, by Proposition 1, strict overlap implies that there exists no consistent classiﬁer of P0 against P1 in the large-p limit.")。機械学習による調整は弱い仮定で良い収束を達成できるが、その代わり重なりの悪さに非常に敏感だ、とも述べている [arxiv-1711.02582#c2](https://arxiv.org/pdf/1711.02582v4#page=3 "On the other hand, the cost of this nonparametric ﬂexibility is that these methods are highly sensitive to poor overlap.")。重なりの悪い部分を除く(トリミング)と、特徴で処置がよく分類できるときは、多くのデータを捨てることになる [arxiv-1711.02582#c7](https://arxiv.org/pdf/1711.02582v4#page=13 "In this case, a trimming procedure must throw away a large proportion of the sample.")。

### 前提を確かめる道具

DoWhy は、因果分析を「モデル化・識別・推定・反証」の4段階に分けるライブラリである [arxiv-2011.04216#c1](https://arxiv.org/pdf/2011.04216v1#page=1 "Speciﬁcally, DoWhy’s API is organized around the four key steps that are required for any causal analysis: Model, Identify, Estimate, and Refute.")。正解のない因果のタスクでは、前提の確認と感度の検定が重要だという立場から [arxiv-2011.04216#c2](https://arxiv.org/pdf/2011.04216v1#page=1 "Unlike supervised machine learning models that can be validated using held-out test data, causal tasks often have no ground truth answer available.")、偽の処置(プラセボ)を入れると効果が0になるか、といった**反証のテスト**を用意している [arxiv-2011.04216#c6](https://arxiv.org/pdf/2011.04216v1#page=3 "Having access to multiple refutation methods to validate an effect estimate from a causal estimator is a key beneﬁt of using DoWhy.")。著者は Microsoft Research の所属で、自分たちのライブラリの紹介である(カードの notes 参照)。

## 2. メタ学習器と二重機械学習

**メタ学習器**は、任意の機械学習の回帰を部品として組み合わせて CATE を推定する方法である。

### S-learner と T-learner

- **T-learner**:処置群と対照群で別々に結果を予測するモデルを作り、その差を取る [arxiv-1706.03461#c1](https://arxiv.org/pdf/1706.03461v6#page=2 "We refer to this meta-algorithm as the S-learner, since it uses a “single” estimator.")。
- **S-learner**:処置の有無を特徴の1つとして加えた1つのモデルを作る [arxiv-1706.03461#c1](https://arxiv.org/pdf/1706.03461v6#page=2 "We refer to this meta-algorithm as the S-learner, since it uses a “single” estimator.")。

Kennedy は、それぞれの回帰が複雑でも、その差(効果)は単純ということがよくあり、別々に推定して差を取ると、差が不必要に複雑で誤差の大きい推定になりうると指摘している [arxiv-2004.14497#c2](https://arxiv.org/pdf/2004.14497v5#page=3 "An interesting but likely common phenomenon occurs in this simple example.")。Nie と Wager も、処置群と対照群に別々に正則化をかけると、真の効果が0でも効果を0から遠ざけてしまうことがあると述べている [arxiv-1712.04912#c4](https://arxiv.org/pdf/1712.04912v4#page=5 "This problem is especially acute when the treated and control samples are of diﬀerent sizes;")。

### X-learner

X-learner は、まず各群で結果を予測し、それを使って観測されていない側の結果を補って個人の効果を「代入」し、その代入値から CATE を学習する [arxiv-1706.03461#c3](https://arxiv.org/pdf/1706.03461v6#page=2 "The X-learner uses the observed outcomes to estimate the unobserved individual treatment eﬀects.")。最後に2つの推定を重みで組み合わせ、重みには推定した傾向スコアを使うのがよいとしている [arxiv-1706.03461#c4](https://arxiv.org/pdf/1706.03461v6#page=4 "Based on our experience, we observe that it is good to use an estimate of the propensity score for g,")。
シミュレーションでは、どのメタ学習器にもそれが最もよい場合があった [arxiv-1706.03461#c5](https://arxiv.org/pdf/1706.03461v6#page=6 "These simulation results lead us to the conclusion that unless one has a strong belief that the CATE is mostly 0, then, as a rule of thumb, one should use the X-learner with BART for small data sets and RF for bigger ones.")。X-learner が速く収束するという理論は線形の CATE などの条件付きで、一般の場合は予想にとどまる [arxiv-1706.03461#c6](https://arxiv.org/pdf/1706.03461v6#page=8 "The following theorem deals carefully with this estimation error when τ is linear, but the response functions can be estimated at any nonparametric rate.") [arxiv-1706.03461#c7](https://arxiv.org/pdf/1706.03461v6#page=8 "It turns out to be mathematically very challenging to give a satisfying statement of the extra conditions needed on P.")。

### R-learner と DR-learner

- **R-learner**:結果と処置のそれぞれから、特徴で予測できる部分を引いた残差どうしの関係として効果を推定する(Robinson の分解)[arxiv-1712.04912#c1](https://arxiv.org/pdf/1712.04912v4#page=2 "This decomposition was originally used by Robinson (1988) to estimate parametric components in partially linear models, and has received considerable attention in recent years.")。前段の予測は交差フィッティングで行う [arxiv-1712.04912#c2](https://arxiv.org/pdf/1712.04912v4#page=3 "We refer to this approach as the R-learner in recognition of the work of Robinson (1988) and to emphasize the role of residualization.")。一定の条件のもとで、前段の予測が真の値を知っている場合(オラクル)と同じ速さで収束する(準オラクル性)[arxiv-1712.04912#c5](https://arxiv.org/pdf/1712.04912v4#page=14 "with penalized kernel regression, the R-learner can match the best available performance guarantees available for the oracle learner (10)")。著者らは、この性質は X-learner には成り立たないと論じている [arxiv-1712.04912#c7](https://arxiv.org/pdf/1712.04912v4#page=14 "We emphasize that our quasi-oracle result depends on a local robustness property of the R-loss function, and does not hold for general meta-learners")。
- **DR-learner**:傾向スコアと結果の予測を組み合わせた「擬似的な結果」を作り、それを特徴で回帰する [arxiv-2004.14497#c4](https://arxiv.org/pdf/2004.14497v5#page=12 "The DR-Learner approach is motivated by the fact that (2) is the (uncentered) efficient influence function for the ATE [Hahn, 1998, Robins and Rotnitzky, 1995]; this drives many of its favorable properties.")。オラクルとの差が、傾向スコアの誤差と結果の予測の誤差の**積**になる(**二重頑健性**)[arxiv-2004.14497#c5](https://arxiv.org/pdf/2004.14497v5#page=12 "Importantly the result is agnostic about the methods used, and requires no special tuning or undersmoothing.")。Kennedy は、Künzel らのメタ学習器はどれも二重頑健でないと指摘している [arxiv-2004.14497#c3](https://arxiv.org/pdf/2004.14497v5#page=10 "further, none of their methods are doubly robust, and so in general would inherit larger error rates from the underlying regression estimators.")。

### 理論と有限サンプルのずれ

Curth と van der Schaar は、メタ学習器を整理し直し、DR-learner は漸近的には最適だが、有限のサンプルでは、結果の予測を使う学習器や、2つの予測の間で情報を共有する学習器のほうがよいことがある、と結論している [arxiv-2101.10943#c9](https://arxiv.org/pdf/2101.10943v2#page=9 "We demonstrated that while the DR-learner is asymptotically optimal in theory, both the RA-learner and plug-in learners sharing information between nuisance estimation tasks can outperform it in ﬁnite samples.")。逆傾向スコアで重み付けする推定は、特に傾向スコアが極端なとき分散が大きい [arxiv-2101.10943#c5](https://arxiv.org/pdf/2101.10943v2#page=5 "the pseudo-outcome associated with the PW-learner has a very high variance even when propensity scores are constant and known")。

### 二重機械学習(DML)

Chernozhukov らは、機械学習の予測をそのまま推定式に代入すると、正則化による偏りのために、通常の $1/\sqrt{n}$ の速さで収束しないことを示した [arxiv-1608.00060#c1](https://arxiv.org/pdf/1608.00060v7#page=3 "Term b is the regularization bias term, which is not centered and diverges in general.")。対策は3つの組合せである。

1. **直交化**:結果だけでなく処置も特徴で予測し、その影響を両方から取り除く(二重の予測が名前の由来)[arxiv-1608.00060#c2](https://arxiv.org/pdf/1608.00060v7#page=4 "We are now solving an auxiliary prediction problem to estimate the conditional mean of D given X, so we are doing “double prediction” or “double machine learning”.")。
2. **ネイマン直交性**:推定式が、補助的な量(傾向スコアや結果の予測)の小さな誤差に一次の意味で影響されないようにする [arxiv-1608.00060#c4](https://arxiv.org/pdf/1608.00060v7#page=12 "The Neyman orthogonality condition requires that the derivative in (2.2) vanishes for all η ∈TN.")。
3. **交差フィッティング**:補助的な量を推定するデータと、効果を推定するデータを分け、入れ替えて平均する。過学習の影響を抑える [arxiv-1608.00060#c3](https://arxiv.org/pdf/1608.00060v7#page=6 "We call this sample splitting procedure where we swap the roles of main and auxiliary samples to obtain multiple estimates and then average the results cross-fitting.")。

これにより、補助的な量の推定に求められる条件は、なめらかな問題の最悪の場合でも「$n^{-1/4}$ より速く推定できる」という大まかなものになる。著者らは、構造についての仮定のもとで多くの機械学習の手法がこれを達成できると述べている [arxiv-1608.00060#c5](https://arxiv.org/pdf/1608.00060v7#page=26 "However, in smooth problems, as discussed below this translates, in the worst cases, to the crude requirement that the nuisance parameters are estimated at the rate")。ATE の場合は、重なりの条件などのもとで、二重頑健な形の推定式を使う [arxiv-1608.00060#c6](https://arxiv.org/pdf/1608.00060v7#page=37 "The scores ψ in (5.3) and (5.4) are efficient, so both estimators are asymptotically efficient, reaching the semi-parametric efficiency bound of Hahn (1998).")。

## 3. 木と森

### 因果木と正直な推定

Athey と Imbens の因果木は、処置効果の違いが大きくなるように特徴の空間を分割する [arxiv-1504.01132#c5](https://arxiv.org/pdf/1504.01132v3#page=11 "The criteria reward a partition for ﬁnding strong heterogeneity in treatment eﬀects, and penalize a partition that creates variance in leaf estimates.")。重要なのは**正直さ**(honesty)で、分割を決めるデータと、各葉で効果を推定するデータを分ける [arxiv-1504.01132#c1](https://arxiv.org/pdf/1504.01132v3#page=2 "We say that a model is “honest” if it does not use the same information for selecting the model structure (in our case, the partition of the covariate space) and for estimation given a model structure.")。データを分ける分だけ精度は落ちるが、偏りが除かれる利点がある [arxiv-1504.01132#c2](https://arxiv.org/pdf/1504.01132v3#page=3 "Although there is a loss of precision due to sample splitting (which reduces sample size in each step of estimation), there is a beneﬁt for ﬁt in terms of eliminating bias that oﬀsets at least part of the cost.")。正直な推定では、通常の信頼区間がそのまま使える [arxiv-1504.01132#c6](https://arxiv.org/pdf/1504.01132v3#page=14 "For the adaptive methods standard approaches to conﬁdence intervals are not generally valid for the reasons discussed above, and below we document through simulations that this can be important in practice.")。

### 因果フォレストと一般化ランダムフォレスト

Wager と Athey の因果フォレストは、正直な木を多数組み合わせ [arxiv-1510.04342#c1](https://arxiv.org/pdf/1510.04342v4#page=8 "a tree is honest if, for each training example i, it only uses the response Yi to estimate the within-leaf treatment eﬀect τ using (5) or to decide where to place the splits, but not both.")、交絡なし・滑らかさ・重なりの前提のもとで、推定値が一致性と漸近正規性を持つことを示した [arxiv-1510.04342#c3](https://arxiv.org/pdf/1510.04342v4#page=7 "This condition eﬀectively guarantees that, for large enough n, there will be enough treatment and control units near any test point x for local methods to work.")。
一般化ランダムフォレスト(GRF)は、これを「森が決める重みで局所的に推定する」方法として一般化した [arxiv-1610.01271#c1](https://arxiv.org/pdf/1610.01271v4#page=2 "To avoid this issue, we cast forests as a type of adaptive locally weighted estimators that ﬁrst use a forest to calculate a weighted set of neighbors for each test point x, and then solve a plug-in version of the estimating equation (1) using these neighbors.")。結果と処置から、特徴で予測できる部分を先に引いておく(R-learner と同じ考え方の)工夫で性能が上がる [arxiv-1610.01271#c6](https://arxiv.org/pdf/1610.01271v4#page=22 "however, a practitioner wanting to use results that are precisely covered by theory may prefer to use cross-ﬁtting for centering.")。信頼区間は偏りを捉えないので、過小平滑化に頼っている [arxiv-1610.01271#c7](https://arxiv.org/pdf/1610.01271v4#page=27 "In particular, as discussed above, our conﬁdence interval construction relies on undersmoothing to get valid asymptotic coverage (without undersmoothing, the conﬁdence intervals account for sampling variability of the forest, but do not capture bias).")。

### BCF:ベイズの回帰木

Hahn らは、処置を受けやすい人ほど処置なしでも結果が悪い(または良い)、という**狙った選択**が現実によくあると考えた [arxiv-1706.09523#c3](https://arxiv.org/pdf/1706.09523v4#page=8 "We suspect this selection process is quite common in practice; for example, in medical contexts where risk factors for adverse outcomes are well-understood physicians are more likely to assign treatment to patients with worse expected outcomes in its absence.")。このとき、正則化が意図しない交絡を生む(**正則化による交絡**)[arxiv-1706.09523#c2](https://arxiv.org/pdf/1706.09523v4#page=8 "The use of a naive regularization prior in the presence of counfounding can unwittingly induce extreme bias in estimation of the target parameter, even when all the confounders are measured and the parametric model is correctly speciﬁed.")。
BCF は、推定した傾向スコアを特徴として加え、処置なしの結果を表す関数と、処置効果を表す関数を別々にモデル化し、効果の関数をより強く正則化する [arxiv-1706.09523#c5](https://arxiv.org/pdf/1706.09523v4#page=13 "Finally, we believe that including an estimated propensity score will be cheap insurance against RIC when estimating treatment eﬀects using outcome models under other nonparametric priors and using more general nonparametric/machine learning approaches.") [arxiv-1706.09523#c6](https://arxiv.org/pdf/1706.09523v4#page=15 "For τ, we prefer stronger regularization.")。著者らは、BCF は二重頑健ではなく、理論はまだ発展途上だと認めている [arxiv-1706.09523#c9](https://arxiv.org/pdf/1706.09523v4#page=27 "We do not claim our approach is doubly robust, however, and in all of our examples above we use the natural Bayesian estimates of (conditional) average treatment eﬀects")。

## 4. ニューラルネットワーク

### 表現の釣り合い

Johansson らは、観察データでの因果推論を、処置群と対照群の分布の違い(ドメイン適応)の問題として捉えた [arxiv-1605.03661#c1](https://arxiv.org/pdf/1605.03661v3#page=3 "The difference between the observed (factual) sample and the sample we must perform inference on lies precisely in the treatment assignment mechanism, P(t/x).")。両群の特徴の**表現**の分布を近づける(釣り合わせる)項を目的関数に加える [arxiv-1605.03661#c3](https://arxiv.org/pdf/1605.03661v3#page=3 "where α, γ > 0 are hyperparameters to control the strength of the imbalance penalties, and disc is the discrepancy measure deﬁned in 4.1.")。

その発展の TARNet/CFR は、共有した表現の上に、処置群と対照群の予測のための2つの出力を置く [arxiv-1606.03976#c5](https://arxiv.org/pdf/1606.03976v5#page=6 "When the dimension of Φ is high, this risks losing the inﬂuence of t on h during training.")。個人の効果の誤差を、2群の予測誤差と、表現の分布の距離(IPM)で上から抑える理論を示した [arxiv-1606.03976#c3](https://arxiv.org/pdf/1606.03976v5#page=5 "We therefore bound the difference ϵCF −ϵF using an IPM.")。ただし、理論の定数は多くの場合計算できず、実際の手法では調整するハイパーパラメータに置き換わっている [arxiv-1606.03976#c4](https://arxiv.org/pdf/1606.03976v5#page=6 "For most IPMs, we cannot compute the factor Bφ in Equation 2, but treat it as part of the hyperparameter α.")。

### Dragonnet

Shi らは、傾向スコアだけで調整に十分だという古典的な結果から、処置の予測に関係しない特徴の情報は調整にとって雑音だと考えた [arxiv-1906.02120#c2](https://arxiv.org/pdf/1906.02120v2#page=3 "In words: it sufﬁces to adjust for only the information in X that is relevant for predicting the treatment.")。Dragonnet は、表現から傾向スコアを予測する出力を加え、表現を傾向スコアに結びつける [arxiv-1906.02120#c3](https://arxiv.org/pdf/1906.02120v2#page=3 "The simple map forces the representation layer to tightly couple to the estimated propensity scores.")。さらに、推定式が成り立つように促す正則化(targeted regularization)を加える [arxiv-1906.02120#c5](https://arxiv.org/pdf/1906.02120v2#page=5 "Consistency is plausible—even with the addition of the targeted regularization term—because the model can choose to set ϵ to 0, which (essentially) recovers the original training objective.")。

## 5. 正解のない評価

### 半合成ベンチマーク

真の効果は観測できないので、実データの特徴に、シミュレーションで作った結果を組み合わせた**半合成データ**で評価することが多い。IHDP がその代表で、ニューラルネットの手法の事実上の標準になっている [arxiv-1606.03976#c7](https://arxiv.org/pdf/1606.03976v5#page=6 "This alleviates, but does not solve, the issue of a completely balanced dataset being unsuited for our method.") [arxiv-1906.02120#c7](https://arxiv.org/pdf/1906.02120v2#page=7 "For the conclusions to be useful, the semi-synthetic data must have good ﬁdelity to the real world.")。
しかし Shi らは、IHDP はサンプルが小さく、シミュレーションの設定も限られているので、結論を出しにくいと注意している [arxiv-1906.02120#c8](https://arxiv.org/pdf/1906.02120v2#page=8 "However, the small sample size and limited simulation settings of IHDP make it difﬁcult to draw conclusions about the methods.")。

Curth らは、ベンチマークの作り方そのものが、特定の手法に有利に働くことを示した [arxiv-2107.13346#c1](https://arxiv.org/pdf/2107.13346v1#page=1 "We identify problems with their current use and highlight that the inherent characteristics of the benchmark datasets favor some algorithms over others – a fact that is rarely acknowledged but of immense relevance for interpretation of empirical results.")。

- IHDP では、効果のばらつきの大きさが繰り返しごとに大きく異なり、平均した誤差では、極端な回でうまくいく手法が有利になる [arxiv-2107.13346#c4](https://arxiv.org/pdf/2107.13346v1#page=4 "The common practice to simply report an average RMSE score across all runs gives algorithms that perform well mainly in the tails a clear advantage; thus it might be more appropriate to consider alternative metrics (e.g. normalized RMSE or paired sample test statistics).")。
- ACIC 2016 では、結果を作る前に一部の特徴が2値化されていて、これはランダムフォレストに自然な形である [arxiv-2107.13346#c6](https://arxiv.org/pdf/2107.13346v1#page=5 "We found that the simulated response surfaces are not created using the raw data as input, instead the 27 count variables are dichotomized by [12] before they are used in the DGP.")。効果に個人差のない設定が少ないため、別々に予測して差を取る学習器が平均的に有利になると予想している [arxiv-2107.13346#c7](https://arxiv.org/pdf/2107.13346v1#page=6 "we would expect that – on average – indirect learners will generally be favoured on this benchmark.")。
- 1つのデータセットでの評価で「最先端」と呼ぶことは見直すべきだ、と述べている [arxiv-2107.13346#c8](https://arxiv.org/pdf/2107.13346v1#page=6 "This means that performance assessments based on a single dataset/DGP (e.g. IHDP) capture only one speciﬁc setting of many conﬁgurations of possible drivers of relative performance.")。

### 競技会:作った人と使う人を分ける

Dorie らは、手法の提案者自身による評価は慎重に解釈すべきだと考え [arxiv-1707.02641#c1](https://arxiv.org/pdf/1707.02641v5#page=2 "Strong performance of a method in a paper written by its inventor is encouraging but should be interpreted cautiously for the reasons discussed in this section.")、データを作る人と手法を提出する人を分けた競技会(ACIC 2016)を開いた [arxiv-1707.02641#c2](https://arxiv.org/pdf/1707.02641v5#page=1 "The researchers creating the data testing grounds were distinct from the researchers submitting methods whose eﬃcacy would be evaluated.")。

- 結果の曲面を柔軟にモデル化する手法が繰り返し好成績を収めた [arxiv-1707.02641#c8](https://arxiv.org/pdf/1707.02641v5#page=24 "This held true even for methods like BART that only modeled the response surface and not the assignment mechanism.")。
- しかし、どの手法が他より良いかを、平均的な成績を超えて予測することはほとんどできなかった [arxiv-1707.02641#c7](https://arxiv.org/pdf/1707.02641v5#page=23 "Overall, we ﬁnd that to a surprising degree we could not go beyond a general recommendation of using ﬂexible non-parametric response surface modeling.")。
- この助言は、交絡なし・重なり・独立同分布が成り立つ設定に限られる [arxiv-1707.02641#c9](https://arxiv.org/pdf/1707.02641v5#page=25 "Of course that advice comes with the caveat that our testing grounds have been restricted a range of settings where ignorability holds, overlap for the inferential group is satisﬁed, the data are i.i.d., etc.; these properties may not hold in practice")。

### モデル選択

真の効果が観測できないので、ハイパーパラメータやモデルを選ぶこと自体が難しい。

- Schuler らは、結果の予測誤差でモデルを選ぶと、効果の推定がよいモデルを選べないことがあると指摘した [arxiv-1804.05146#c2](https://arxiv.org/pdf/1804.05146v2#page=5 "There are many simple examples where minimizing the mean-squared error of predicted outcomes badly fails to select the model with the most accurate treatment eﬀect [24].")。比較した基準の中では、R-learner の損失を検証データで計算する基準が、最も一貫してよいモデルを選んだ [arxiv-1804.05146#c5](https://arxiv.org/pdf/1804.05146v2#page=8 "We propose using this same construction to select among models ﬁt by arbitrary means.") [arxiv-1804.05146#c7](https://arxiv.org/pdf/1804.05146v2#page=12 "This is especially true when treatment assignment is randomized, but also to a large extent when the assignment is biased.")。ただし、この比較はシミュレーションに基づく [arxiv-1804.05146#c9](https://arxiv.org/pdf/1804.05146v2#page=16 "The primary limitation of our work is that it relies on simulations.")。
- 初期の論文では、ハイパーパラメータをシミュレーションした実験で選んでいて、著者自身が実データではできないと認めている [arxiv-1605.03661#c8](https://arxiv.org/pdf/1605.03661v3#page=6 "While not possible for real-world data, this approach gives an indication of the robustness of the parameters.")。TARNet/CFR は、反対の群の最も近い人の結果を代わりに使う近似で選んでいる [arxiv-1606.03976#c8](https://arxiv.org/pdf/1606.03976v5#page=19 "Standard methods for hyperparameter selection, such as cross-validation, are not generally applicable for estimating the PEHE loss since only one potential outcome is observed (unless the outcome is simulated).")。

## 6. 因果の基盤モデル

最近は、表データの基盤モデル([表データ基盤モデル(TabPFN 系)](../methods/tabular-foundation-models.md))と同じ考え方で、多数の合成データで事前学習したモデルに因果効果を推定させる研究も出ている。

- 学習済みのモデルを調整なしで使い、半合成データで従来の推定法と競えると報告する比較がある [arxiv-2609.03003#c4](https://arxiv.org/pdf/2609.03003v1#page=19 "These models are downloaded out-of-the-box from their respective sources and applied without any parameter or hyperparameter tuning.") [arxiv-2609.03003#c5](https://arxiv.org/pdf/2609.03003v1#page=19 "Despite not being trained on the Lalonde data distributions, CFMs are remarkably competitive with classical estimators.")。
- 一方、同じ構造の因果モデルでも、推定器に与える観測の仕方を変えると、どの基盤モデルが良いかが大きく入れ替わる、という評価もある [arxiv-2609.36881#c2](https://arxiv.org/pdf/2609.36881v1#page=1 "Across these matched views, no CFM consistently performs best and model rankings vary substantially.")。
- 事前分布を工夫する研究では、IHDP などの標準のベンチマークで既存手法を上回らなかったと報告している [arxiv-2609.06941#c6](https://arxiv.org/pdf/2609.06941v1#page=23 "We state plainly: on standard causal benchmarks, our injection method is not superior to, and is often inferior to, existing methods.")。
- 観察データと介入的なデータを組み合わせて、介入後の条件付き分布を予測する基盤モデルも研究されている [arxiv-2609.39523#c1](https://arxiv.org/pdf/2609.39523v1#page=1 "This work studies CFMs as a method to combine finite observational and surrogate-interventional datasets in order to predict a target conditional interventional distribution (CID) more accurately than with observational data alone.")。

## 示唆(本記事の整理)

- **まず前提を書き出す。** 交絡なし・重なり・SUTVA のどれに頼っているかを明示する。交絡なしはデータから確かめられない [arxiv-1606.03976#c2](https://arxiv.org/pdf/1606.03976v5#page=2 "The validity of strong ignorability cannot be assessed from data, and must be determined by domain knowledge and understanding of the causal relationships between the variables.")。特徴を増やすと重なりが崩れやすい [arxiv-1711.02582#c1](https://arxiv.org/pdf/1711.02582v4#page=2 "This intuition, however, has the opposite implications for overlap: the richer the set of covariates, the closer these covariates come to perfectly predicting treatment assignment for at least some subgroups.")。
- **予測を差し引くだけの推定に頼らない。** 別々の予測の差は不必要に複雑になりうる [arxiv-2004.14497#c2](https://arxiv.org/pdf/2004.14497v5#page=3 "An interesting but likely common phenomenon occurs in this simple example.")。R-learner、DR-learner、DML のように、補助的な量の誤差に強い推定を検討する [arxiv-1712.04912#c5](https://arxiv.org/pdf/1712.04912v4#page=14 "with penalized kernel regression, the R-learner can match the best available performance guarantees available for the oracle learner (10)") [arxiv-2004.14497#c5](https://arxiv.org/pdf/2004.14497v5#page=12 "Importantly the result is agnostic about the methods used, and requires no special tuning or undersmoothing.") [arxiv-1608.00060#c5](https://arxiv.org/pdf/1608.00060v7#page=26 "However, in smooth problems, as discussed below this translates, in the worst cases, to the crude requirement that the nuisance parameters are estimated at the rate")。ただし有限のサンプルでは理論上の最適が実際の最適とは限らない [arxiv-2101.10943#c9](https://arxiv.org/pdf/2101.10943v2#page=9 "We demonstrated that while the DR-learner is asymptotically optimal in theory, both the RA-learner and plug-in learners sharing information between nuisance estimation tasks can outperform it in ﬁnite samples.")。
- **ベンチマークの結果は、その生成過程とセットで読む。** IHDP や ACIC の設計は特定の手法に有利に働きうる [arxiv-2107.13346#c1](https://arxiv.org/pdf/2107.13346v1#page=1 "We identify problems with their current use and highlight that the inherent characteristics of the benchmark datasets favor some algorithms over others – a fact that is rarely acknowledged but of immense relevance for interpretation of empirical results.")。
- **モデル選択の基準を決めておく。** 結果の予測誤差での選択は危うい [arxiv-1804.05146#c2](https://arxiv.org/pdf/1804.05146v2#page=5 "There are many simple examples where minimizing the mean-squared error of predicted outcomes badly fails to select the model with the most accurate treatment eﬀect [24].")。
- **反証のテストや感度分析を組み込む** [arxiv-2011.04216#c6](https://arxiv.org/pdf/2011.04216v1#page=3 "Having access to multiple refutation methods to validate an effect estimate from a causal estimator is a key beneﬁt of using DoWhy.")。

## わかっていないこと

- 半合成データでの好成績が、実データでの好成績につながるかは、ここで扱った論文では確かめようがない(真の効果が観測できないため)[arxiv-1804.05146#c9](https://arxiv.org/pdf/1804.05146v2#page=16 "The primary limitation of our work is that it relies on simulations.") [arxiv-1707.02641#c9](https://arxiv.org/pdf/1707.02641v5#page=25 "Of course that advice comes with the caveat that our testing grounds have been restricted a range of settings where ignorability holds, overlap for the inferential group is satisﬁed, the data are i.i.d., etc.; these properties may not hold in practice")。
- どのメタ学習器を選ぶべきかをデータから決める方法は確立していない [arxiv-2101.10943#c1](https://arxiv.org/pdf/2101.10943v2#page=1 "Choosing between diﬀerent meta-learners in a data-driven manner is diﬃcult, as it requires access to counterfactual information.")。
- 隠れた交絡がある場合の推定は、強い仮定なしには難しく、VAE による方法の理論も乏しい [arxiv-1705.08821#c6](https://arxiv.org/pdf/1705.08821v2#page=2 "This has the disadvantage that little theory is currently available to justify when learning with VAEs can identify the true model.")。
- BCF などベイズの方法の信用区間が、頻度論的な意味で正しい被覆を持つかは、まだ理論がない [arxiv-1706.09523#c9](https://arxiv.org/pdf/1706.09523v4#page=27 "We do not claim our approach is doubly robust, however, and in all of our examples above we use the natural Bayesian estimates of (conditional) average treatment eﬀects")。

## 参照カード

- [arxiv-1706.03461](../../papers/arxiv-1706.03461.yaml) Künzel et al., "Meta-learners for Estimating Heterogeneous Treatment Effects using Machine Learning"
- [arxiv-1712.04912](../../papers/arxiv-1712.04912.yaml) Nie & Wager, "Quasi-Oracle Estimation of Heterogeneous Treatment Effects"
- [arxiv-2004.14497](../../papers/arxiv-2004.14497.yaml) Kennedy, "Towards optimal doubly robust estimation of heterogeneous causal effects"
- [arxiv-1608.00060](../../papers/arxiv-1608.00060.yaml) Chernozhukov et al., "Double/Debiased Machine Learning for Treatment and Causal Parameters"
- [arxiv-2101.10943](../../papers/arxiv-2101.10943.yaml) Curth & van der Schaar, "Nonparametric Estimation of Heterogeneous Treatment Effects"
- [arxiv-1504.01132](../../papers/arxiv-1504.01132.yaml) Athey & Imbens, "Recursive Partitioning for Heterogeneous Causal Effects"
- [arxiv-1510.04342](../../papers/arxiv-1510.04342.yaml) Wager & Athey, "Estimation and Inference of Heterogeneous Treatment Effects using Random Forests"
- [arxiv-1610.01271](../../papers/arxiv-1610.01271.yaml) Athey, Tibshirani & Wager, "Generalized Random Forests"
- [arxiv-1706.09523](../../papers/arxiv-1706.09523.yaml) Hahn, Murray & Carvalho, "Bayesian regression tree models for causal inference"
- [arxiv-1605.03661](../../papers/arxiv-1605.03661.yaml) Johansson, Shalit & Sontag, "Learning Representations for Counterfactual Inference"
- [arxiv-1606.03976](../../papers/arxiv-1606.03976.yaml) Shalit, Johansson & Sontag, "Estimating individual treatment effect: generalization bounds and algorithms"
- [arxiv-1906.02120](../../papers/arxiv-1906.02120.yaml) Shi, Blei & Veitch, "Adapting Neural Networks for the Estimation of Treatment Effects"
- [arxiv-1705.08821](../../papers/arxiv-1705.08821.yaml) Louizos et al., "Causal Effect Inference with Deep Latent-Variable Models"
- [arxiv-1711.02582](../../papers/arxiv-1711.02582.yaml) D'Amour et al., "Overlap in Observational Studies with High-Dimensional Covariates"
- [arxiv-2011.04216](../../papers/arxiv-2011.04216.yaml) Sharma & Kiciman, "DoWhy: An End-to-End Library for Causal Inference"
- [arxiv-2107.13346](../../papers/arxiv-2107.13346.yaml) Curth et al., "Doing Great at Estimating CATE?"
- [arxiv-1707.02641](../../papers/arxiv-1707.02641.yaml) Dorie et al., "Automated versus do-it-yourself methods for causal inference"
- [arxiv-1804.05146](../../papers/arxiv-1804.05146.yaml) Schuler et al., "A comparison of methods for model selection when estimating individual treatment effects"
- [arxiv-2609.03003](../../papers/arxiv-2609.03003.yaml) Stith et al., "Causal Foundation Models"
- [arxiv-2609.36881](../../papers/arxiv-2609.36881.yaml) Jung et al., "What You Observe Determines How You Identify Causal Effects"
- [arxiv-2609.06941](../../papers/arxiv-2609.06941.yaml) Zhou, "When and Why LLM Causal Priors Help"
- [arxiv-2609.39523](../../papers/arxiv-2609.39523.yaml) Gao et al., "CIDER-FM: Foundation Models for Causal Inference from Diverse Experimental Regimes"
