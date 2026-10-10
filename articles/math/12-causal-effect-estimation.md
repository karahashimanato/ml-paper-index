---
title: 数式の解説 12 — 因果効果の推定:潜在的結果、傾向スコアと逆確率重み付け、メタ学習器、R-loss と DML、二重頑健性
kind: math
tags: [causal-effect-estimation, causal-meta-learners]
depends_on: [arxiv-1606.03976, arxiv-1706.03461, arxiv-2101.10943, arxiv-2004.14497, arxiv-1712.04912, arxiv-1608.00060, arxiv-1804.05146, arxiv-1711.02582]
written_at: 2026-10-10
written_by: claude-opus-5-5 via Claude Code
---

# 数式の解説 12 — 因果効果の推定:潜在的結果、傾向スコアと逆確率重み付け、メタ学習器、R-loss と DML、二重頑健性

<!-- generated:stale -->
> ⚠ この記事の執筆日(2026-10-10)以降に作成された関連カードが 8 件あります(未反映。執筆日と同じ日に作成されたカードを含む): `arxiv-1504.01132`, `arxiv-1605.03661`, `arxiv-1705.08821`, `arxiv-1706.09523`, `arxiv-1707.02641`, `arxiv-1906.02120`, `arxiv-2011.04216`, `arxiv-2107.13346`
<!-- /generated:stale -->

## この記事の読み方

[因果効果の推定](../topics/causal-effect-estimation.md) の記事で扱った推定法の式を解説する。

使う道具(期待値、条件付き期待値、条件付き確率、偏微分)は [準備の記事](00-preliminaries.md) で説明している。

- 式は論文から取り、根拠のカード(論文の該当ページへのリンク)を付けている。
- 「**補足**」と書いた計算は、論文には書かれていない、この記事による説明である。

この記事では、1つの小さなデータを最後まで使い、どの推定法もそのデータでは同じ答えになることを確かめる。

## 0. 共通の例(補足)

6人のデータで、特徴 $x$ は 0 か 1、$W = 1$ は処置を受けた人、$Y$ は結果とする。

| 人 | $x$ | $W$ | $Y$ |
|---|---|---|---|
| 1 | 0 | 1 | 5 |
| 2 | 0 | 1 | 6 |
| 3 | 0 | 0 | 3 |
| 4 | 1 | 1 | 8 |
| 5 | 1 | 0 | 4 |
| 6 | 1 | 0 | 4 |

以下、各グループの平均をそのまま「予測」として使う(グループが2つしかないので、どんな回帰でもこうなる)。

## 1. 潜在的結果と推定したい量

各人には、処置を受けた場合の結果 $Y(1)$ と受けなかった場合の結果 $Y(0)$ がある。推定したいのは条件付き平均処置効果

$$
\tau(x) = E\big[ Y(1) - Y(0) \mid X = x \big] = \mu_1(x) - \mu_0(x)
$$

である。$\mu_w(x)$ は、処置 $w$ のもとでの結果の条件付き期待値である [arxiv-1606.03976#c1](https://arxiv.org/pdf/1606.03976v5#page=2 "this is known as the Consistency assumption.")。
観測できるのは、処置を受けた人なら $Y(1)$、受けなかった人なら $Y(0)$ だけである [arxiv-1606.03976#c1](https://arxiv.org/pdf/1606.03976v5#page=2 "this is known as the Consistency assumption.")。交絡なしと重なりの前提のもとで、$\tau(x)$ は観測データから識別できる [arxiv-1606.03976#c2](https://arxiv.org/pdf/1606.03976v5#page=2 "The validity of strong ignorability cannot be assessed from data, and must be determined by domain knowledge and understanding of the causal relationships between the variables.")。

## 2. 傾向スコアと逆確率重み付け

### 傾向スコア

特徴 $x$ の人が処置を受ける確率 $\pi(x) = P(W = 1 \mid X = x)$ を**傾向スコア**という。

**補足(例)**:$x = 0$ の3人のうち2人が処置を受けたので $\pi(0) = 2/3$、$x = 1$ では $\pi(1) = 1/3$。

### 逆確率で重み付けした擬似的な結果

Curth と van der Schaar が PW-learner と呼ぶ方法は、次の**擬似的な結果**を作り、それを $x$ で回帰する [arxiv-2101.10943#c10](https://arxiv.org/pdf/2101.10943v2#page=4 "We prefer the RA-learning strategy here, as it does not require choice of ‘hyper-parameter’ g(x).")。

$$
\tilde{Y}_{PW} = \left( \frac{W}{\pi(X)} - \frac{1 - W}{1 - \pi(X)} \right) Y
$$

処置を受けた人は結果を $1/\pi$ 倍し、受けなかった人は $-1/(1-\pi)$ 倍する。「処置を受けにくい人が処置を受けた」場合ほど大きな重みが付き、処置群が全体を代表するように補正される。

**補足(なぜ効果になるのか)**:交絡なしのもとで $E[W Y \mid X = x] = \pi(x)\, \mu_1(x)$ なので、$E[W Y / \pi(X) \mid X = x] = \mu_1(x)$。同様に第2項の期待値は $-\mu_0(x)$ で、合わせて $\tau(x)$ になる。

**補足(例)**:$x = 0$ では、人1は $5 / (2/3) = 7.5$、人2は $6 / (2/3) = 9$、人3は $-3 / (1/3) = -9$。平均は $(7.5 + 9 - 9)/3 = 2.5$。$x = 1$ では、人4は $8/(1/3) = 24$、人5と人6は $-4/(2/3) = -6$ で、平均は $(24 - 6 - 6)/3 = 4$。

### 重なりが悪いとき

$\pi(x)$ が0や1に近いと、$1/\pi$ や $1/(1-\pi)$ が非常に大きくなる。たとえば $\pi = 0.01$ の人が処置を受けると、重みは100倍になる。Curth と van der Schaar は、逆傾向スコアで重み付けする推定は、特に傾向スコアが極端なとき分散が大きいと述べている [arxiv-2101.10943#c5](https://arxiv.org/pdf/2101.10943v2#page=5 "the pseudo-outcome associated with the PW-learner has a very high variance even when propensity scores are constant and known")。D'Amour らが指摘した高次元での重なりの問題 [arxiv-1711.02582#c1](https://arxiv.org/pdf/1711.02582v4#page=2 "This intuition, however, has the opposite implications for overlap: the richer the set of covariates, the closer these covariates come to perfectly predicting treatment assignment for at least some subgroups.") は、この重みの爆発として現れる。

## 3. メタ学習器

### T-learner と S-learner

- **T-learner**:処置群と対照群で別々に $\hat{\mu}_1$ と $\hat{\mu}_0$ を推定し、$\hat{\tau}(x) = \hat{\mu}_1(x) - \hat{\mu}_0(x)$ とする [arxiv-1706.03461#c1](https://arxiv.org/pdf/1706.03461v6#page=2 "We refer to this meta-algorithm as the S-learner, since it uses a “single” estimator.")。
- **S-learner**:処置 $W$ を特徴の1つとして加えた1つのモデル $\hat{\mu}(x, w)$ を作り、$\hat{\tau}(x) = \hat{\mu}(x, 1) - \hat{\mu}(x, 0)$ とする [arxiv-1706.03461#c1](https://arxiv.org/pdf/1706.03461v6#page=2 "We refer to this meta-algorithm as the S-learner, since it uses a “single” estimator.")。

**補足(例)**:T-learner では、$\hat{\mu}_1(0) = (5 + 6)/2 = 5.5$、$\hat{\mu}_0(0) = 3$ なので $\hat{\tau}(0) = 2.5$。$\hat{\mu}_1(1) = 8$、$\hat{\mu}_0(1) = 4$ なので $\hat{\tau}(1) = 4$。2節の逆確率重み付けと同じ答えになっている。

### X-learner

X-learner は、相手の群のモデルを使って、各人の効果を「代入」する [arxiv-1706.03461#c9](https://arxiv.org/pdf/1706.03461v6#page=4 "and call these the imputed treatment eﬀects.")。

$$
\tilde{D}^1_i = Y^1_i - \hat{\mu}_0(X^1_i) \quad (\text{処置群}), \qquad
\tilde{D}^0_i = \hat{\mu}_1(X^0_i) - Y^0_i \quad (\text{対照群})
$$

それぞれの群で $\tilde{D}$ を $x$ で回帰して $\hat{\tau}_1$ と $\hat{\tau}_0$ を作り、重み $g(x)$ で組み合わせる [arxiv-1706.03461#c9](https://arxiv.org/pdf/1706.03461v6#page=4 "and call these the imputed treatment eﬀects.")。

$$
\hat{\tau}(x) = g(x)\, \hat{\tau}_0(x) + \big(1 - g(x)\big)\, \hat{\tau}_1(x)
$$

重み $g$ には推定した傾向スコアを使うのがよい、と著者らは述べている [arxiv-1706.03461#c4](https://arxiv.org/pdf/1706.03461v6#page=4 "Based on our experience, we observe that it is good to use an estimate of the propensity score for g,")。

**補足(例)**:$x = 0$ の処置群(人1、人2)の代入値は $5 - 3 = 2$ と $6 - 3 = 3$ で、平均 $\hat{\tau}_1(0) = 2.5$。対照群(人3)は $5.5 - 3 = 2.5$ で、$\hat{\tau}_0(0) = 2.5$。どんな $g$ でも $2.5$ になる。

**補足(なぜ $g$ に傾向スコアを使うのか)**:処置群が多い所では $\hat{\mu}_1$ は精度よく推定でき、対照群の代入値 $\tilde{D}^0$(これは $\hat{\mu}_1$ を使う)の信頼性が高い。$g(x) = \pi(x)$ とすると、処置群が多い所ほど $\hat{\tau}_0$ を重視することになり、この考えに合う。

### RA-learner

Curth と van der Schaar は、X-learner の2つの回帰を1つにまとめた形を RA-learner と呼んでいる [arxiv-2101.10943#c10](https://arxiv.org/pdf/2101.10943v2#page=4 "We prefer the RA-learning strategy here, as it does not require choice of ‘hyper-parameter’ g(x).")。

$$
\tilde{Y}_{RA} = W\big(Y - \hat{\mu}_0(X)\big) + (1 - W)\big(\hat{\mu}_1(X) - Y\big)
$$

重み $g$ を選ぶ必要がない点を、彼らは利点に挙げている [arxiv-2101.10943#c10](https://arxiv.org/pdf/2101.10943v2#page=4 "We prefer the RA-learning strategy here, as it does not require choice of ‘hyper-parameter’ g(x).")。

## 4. DR-learner:二重頑健な擬似的な結果

Kennedy の DR-learner は、逆確率重み付けと結果の予測を組み合わせた擬似的な結果を、$x$ で回帰する [arxiv-2004.14497#c4](https://arxiv.org/pdf/2004.14497v5#page=12 "The DR-Learner approach is motivated by the fact that (2) is the (uncentered) efficient influence function for the ATE [Hahn, 1998, Robins and Rotnitzky, 1995]; this drives many of its favorable properties.")。

$$
\tilde{Y}_{DR} = \frac{W - \hat{\pi}(X)}{\hat{\pi}(X)\big(1 - \hat{\pi}(X)\big)} \Big( Y - \hat{\mu}_W(X) \Big) + \hat{\mu}_1(X) - \hat{\mu}_0(X)
$$

$\hat{\mu}_W$ は、その人が実際に受けた処置のほうの予測である。

- 後ろの $\hat{\mu}_1 - \hat{\mu}_0$ は T-learner の推定そのもの。
- 前の項は、予測の誤差 $Y - \hat{\mu}_W$ を逆確率で重み付けした**補正**である。

Kennedy は、この推定とオラクル(真の補助的な量を知っている場合)との差が、傾向スコアの誤差と結果の予測の誤差の**積**で抑えられることを示した [arxiv-2004.14497#c5](https://arxiv.org/pdf/2004.14497v5#page=12 "Importantly the result is agnostic about the methods used, and requires no special tuning or undersmoothing.")。

**補足(二重頑健性の直感)**:結果の予測 $\hat{\mu}$ が正しければ、補正の項は平均0になる。傾向スコア $\hat{\pi}$ が正しければ、補正の項がちょうど $\hat{\mu}$ の偏りを打ち消す。どちらか一方が正しければよいので「二重に頑健」という。誤差が積で効くのはこのためで、たとえば両方の誤差が $0.1$ なら、積は $0.01$ になる。

**補足(例)**:$x = 0$ で $\hat{\pi} = 2/3$ なので、$\hat{\pi}(1 - \hat{\pi}) = 2/9$。

- 人1:$\dfrac{1 - 2/3}{2/9} = 1.5$、$Y - \hat{\mu}_1 = 5 - 5.5 = -0.5$ なので、$1.5 \times (-0.5) + 2.5 = 1.75$
- 人2:$1.5 \times (6 - 5.5) + 2.5 = 3.25$
- 人3:$\dfrac{0 - 2/3}{2/9} = -3$、$Y - \hat{\mu}_0 = 3 - 3 = 0$ なので、$0 + 2.5 = 2.5$

平均は $(1.75 + 3.25 + 2.5)/3 = 2.5$ で、やはり同じ答えになる。

## 5. R-loss と二重機械学習

### Robinson の分解と R-loss

$m(x) = E[Y \mid X = x]$($W$ を使わない結果の予測)、$e(x)$ を傾向スコアとすると、効果 $\tau$ は次の関係を満たす [arxiv-1712.04912#c1](https://arxiv.org/pdf/1712.04912v4#page=2 "This decomposition was originally used by Robinson (1988) to estimate parametric components in partially linear models, and has received considerable attention in recent years.")。

$$
Y - m(X) = \big( W - e(X) \big)\, \tau(X) + \varepsilon
$$

「結果の残差」と「処置の残差」の比例関係として効果を表す形である。R-learner は、これを2乗誤差で当てはめる [arxiv-1712.04912#c9](https://arxiv.org/pdf/1712.04912v4#page=3 "In other words, the ﬁrst step learns an approximation for the oracle objective, and the second step optimizes it.")。

$$
\hat{L}_n(\tau) = \frac{1}{n} \sum_{i=1}^{n} \Big[ \big\{ Y_i - \hat{m}^{(-q(i))}(X_i) \big\} - \big\{ W_i - \hat{e}^{(-q(i))}(X_i) \big\}\, \tau(X_i) \Big]^2
$$

$\hat{m}^{(-q(i))}$ は、$i$ が属するデータの分割を使わずに作った予測(交差フィッティング)である [arxiv-1712.04912#c2](https://arxiv.org/pdf/1712.04912v4#page=3 "We refer to this approach as the R-learner in recognition of the work of Robinson (1988) and to emphasize the role of residualization.")。

**補足(例)**:$x = 0$ では $m(0) = (5 + 6 + 3)/3 \approx 4.667$、$e(0) = 2/3$。$\tau$ を定数とすると、R-loss を最小にする $\tau$ は、$\sum (W - e)(Y - m) \big/ \sum (W - e)^2$(1変数の最小二乗)である。

| 人 | $W - e$ | $Y - m$ | 積 | $(W - e)^2$ |
|---|---|---|---|---|
| 1 | $1/3$ | $0.333$ | $0.111$ | $1/9$ |
| 2 | $1/3$ | $1.333$ | $0.444$ | $1/9$ |
| 3 | $-2/3$ | $-1.667$ | $1.111$ | $4/9$ |

$\tau = 1.667 / (6/9) = 2.5$ で、また同じ答えになる。

### 二重機械学習の部分線形モデル

Chernozhukov らの出発点は、効果が一定の**部分線形モデル**である [arxiv-1608.00060#c10](https://arxiv.org/pdf/1608.00060v7#page=2 "where Y is the outcome variable, D is the policy/treatment variable of interest, vector")。

$$
Y = D\theta_0 + g_0(X) + U, \quad E[U \mid X, D] = 0; \qquad D = m_0(X) + V, \quad E[V \mid X] = 0
$$

$D$ は処置、$\theta_0$ が知りたい効果、$g_0$ と $m_0$ は機械学習で推定する補助的な関数である。
$g_0$ の推定を直接代入すると正則化の偏りが残るので [arxiv-1608.00060#c1](https://arxiv.org/pdf/1608.00060v7#page=3 "Term b is the regularization bias term, which is not centered and diverges in general.")、$D$ からも $X$ の影響を取り除き(直交化)[arxiv-1608.00060#c2](https://arxiv.org/pdf/1608.00060v7#page=4 "We are now solving an auxiliary prediction problem to estimate the conditional mean of D given X, so we are doing “double prediction” or “double machine learning”.")、データを分けて推定する(交差フィッティング)[arxiv-1608.00060#c3](https://arxiv.org/pdf/1608.00060v7#page=6 "We call this sample splitting procedure where we swap the roles of main and auxiliary samples to obtain multiple estimates and then average the results cross-fitting.")。

**補足(R-loss との関係)**:$Y$ と $D$ のそれぞれから $X$ で予測できる部分を引き、残差どうしを回帰して $\theta_0$ を求める操作は、上の R-loss で $\tau$ を定数にした場合と同じ形である。R-learner は、これを $\tau(x)$ が $x$ によって変わる場合に広げたものと読める。

### モデル選択の基準としての R-loss

真の効果は観測できないので、モデルを選ぶ基準も工夫が要る。Schuler らは、R-loss を検証データで計算した値($\tau$-risk$_R$)を、モデル選択の基準として使うことを提案した [arxiv-1804.05146#c5](https://arxiv.org/pdf/1804.05146v2#page=8 "We propose using this same construction to select among models ﬁt by arbitrary means.")。

$$
\frac{1}{n} \sum_i \Big( \big(y_i - \hat{m}(x_i)\big) - \big(w_i - \hat{p}(x_i)\big)\, \hat{\tau}(x_i) \Big)^2
$$

## まとめ

| 式 | 何を表すか | 根拠 |
|---|---|---|
| $\tau(x) = \mu_1(x) - \mu_0(x)$ | 条件付き平均処置効果 | [arxiv-1606.03976#c1](https://arxiv.org/pdf/1606.03976v5#page=2 "this is known as the Consistency assumption.") |
| $(W/\pi - (1-W)/(1-\pi))\, Y$ | 逆確率で重み付けした擬似的な結果 | [arxiv-2101.10943#c10](https://arxiv.org/pdf/2101.10943v2#page=4 "We prefer the RA-learning strategy here, as it does not require choice of ‘hyper-parameter’ g(x).") |
| $\hat{\mu}_1 - \hat{\mu}_0$ | T-learner | [arxiv-1706.03461#c1](https://arxiv.org/pdf/1706.03461v6#page=2 "We refer to this meta-algorithm as the S-learner, since it uses a “single” estimator.") |
| $\tilde{D}^1 = Y^1 - \hat{\mu}_0$、$\tilde{D}^0 = \hat{\mu}_1 - Y^0$、$g\hat{\tau}_0 + (1-g)\hat{\tau}_1$ | X-learner | [arxiv-1706.03461#c9](https://arxiv.org/pdf/1706.03461v6#page=4 "and call these the imputed treatment eﬀects.") |
| $\frac{W - \hat{\pi}}{\hat{\pi}(1-\hat{\pi})}(Y - \hat{\mu}_W) + \hat{\mu}_1 - \hat{\mu}_0$ | DR-learner の擬似的な結果 | [arxiv-2004.14497#c4](https://arxiv.org/pdf/2004.14497v5#page=12 "The DR-Learner approach is motivated by the fact that (2) is the (uncentered) efficient influence function for the ATE [Hahn, 1998, Robins and Rotnitzky, 1995]; this drives many of its favorable properties.") |
| $\frac{1}{n}\sum [\{Y - \hat{m}\} - \{W - \hat{e}\}\tau]^2$ | R-loss | [arxiv-1712.04912#c9](https://arxiv.org/pdf/1712.04912v4#page=3 "In other words, the ﬁrst step learns an approximation for the oracle objective, and the second step optimizes it.") |
| $Y = D\theta_0 + g_0(X) + U$ | DML の部分線形モデル | [arxiv-1608.00060#c10](https://arxiv.org/pdf/1608.00060v7#page=2 "where Y is the outcome variable, D is the policy/treatment variable of interest, vector") |

## 参照カード

- [arxiv-1606.03976](../../papers/arxiv-1606.03976.yaml) Shalit, Johansson & Sontag, "Estimating individual treatment effect: generalization bounds and algorithms"
- [arxiv-1706.03461](../../papers/arxiv-1706.03461.yaml) Künzel et al., "Meta-learners for Estimating Heterogeneous Treatment Effects using Machine Learning"
- [arxiv-2101.10943](../../papers/arxiv-2101.10943.yaml) Curth & van der Schaar, "Nonparametric Estimation of Heterogeneous Treatment Effects"
- [arxiv-2004.14497](../../papers/arxiv-2004.14497.yaml) Kennedy, "Towards optimal doubly robust estimation of heterogeneous causal effects"
- [arxiv-1712.04912](../../papers/arxiv-1712.04912.yaml) Nie & Wager, "Quasi-Oracle Estimation of Heterogeneous Treatment Effects"
- [arxiv-1608.00060](../../papers/arxiv-1608.00060.yaml) Chernozhukov et al., "Double/Debiased Machine Learning for Treatment and Causal Parameters"
- [arxiv-1804.05146](../../papers/arxiv-1804.05146.yaml) Schuler et al., "A comparison of methods for model selection when estimating individual treatment effects"
- [arxiv-1711.02582](../../papers/arxiv-1711.02582.yaml) D'Amour et al., "Overlap in Observational Studies with High-Dimensional Covariates"
