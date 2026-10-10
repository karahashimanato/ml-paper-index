---
title: 数式の解説 5 — 線形モデルとカーネル:最小二乗、Lasso と最良部分集合、カーネルリッジ回帰、SVM、GP-UCB
kind: math
tags: [linear-models, kernel-methods, gaussian-processes]
depends_on: [arxiv-1507.03133, arxiv-1305.5029, arxiv-1311.0914, arxiv-0912.3995, arxiv-1807.02811, arxiv-1206.2944]
written_at: 2026-10-10
written_by: claude-opus-5-5 via Claude Code
---

# 数式の解説 5 — 線形モデルとカーネル:最小二乗、Lasso と最良部分集合、カーネルリッジ回帰、SVM、GP-UCB

<!-- generated:stale -->
> ⚠ この記事の執筆日(2026-10-10)以降に作成された関連カードが 2 件あります(未反映。執筆日と同じ日に作成されたカードを含む): `arxiv-1811.05868`, `arxiv-1902.07153`
<!-- /generated:stale -->

## この記事の読み方

多くの手法の土台になる**線形モデル**と、それを曲線や複雑な形に広げる**カーネル法**の式を解説する。
[数式の解説 4](04-bayes.md) のガウス過程は、カーネル法の一種でもある。この記事の最後で、両者のつながりを見る。

使う道具(Σ、ベクトルと行列、偏微分、正規分布)は [準備の記事](00-preliminaries.md) で説明している。

- 式は論文から取り、根拠のカード(論文の該当ページへのリンク)を付けている。
- 「**補足**」と書いた計算は、論文には書かれていない、この記事による説明である。

## 1. 線形モデルと最小二乗

### 線形モデル

$n$ 個のデータそれぞれに、$p$ 個の特徴量と、予測したい値(応答)があるとする。応答を並べたベクトルを $y$($n$ 次元)、特徴量を並べた行列を $X$($n$ 行 $p$ 列)とすると、**線形回帰モデル**は

$$
y = X\beta + \epsilon
$$

と書ける [arxiv-1507.03133#c8](https://arxiv.org/pdf/1507.03133v1#page=2 "The cardinality constraint makes Problem (1) NP-hard [41].")。$\beta$ は $p$ 個の係数を並べたベクトル、$\epsilon$ は誤差である。
1つのデータについて書けば、$y_i = \beta_1 x_{i1} + \beta_2 x_{i2} + \cdots + \beta_p x_{ip} + \epsilon_i$。特徴量に係数を掛けて足すだけのモデルである。

### 最小二乗

係数は、予測の誤差の2乗の和が最小になるように決める。

$$
\min_\beta \ \frac{1}{2} \Vert y - X\beta \Vert_2^2 = \min_\beta \ \frac{1}{2} \sum_{i=1}^{n} \big( y_i - (X\beta)_i \big)^2
$$

$\Vert \cdot \Vert_2$ はベクトルの長さ(成分の2乗の和の平方根)で、その2乗は成分の2乗の和である。

**補足(例:特徴量が1つのとき)**:$y_i \approx \beta x_i$ で、データが $(x, y) = (1, 1), (2, 2), (3, 2)$ だとする。
$g(\beta) = \frac{1}{2}\sum_i (y_i - \beta x_i)^2$ を $\beta$ で微分して0とおくと、$-\sum_i x_i (y_i - \beta x_i) = 0$ より

$$
\beta = \frac{\sum_i x_i y_i}{\sum_i x_i^2} = \frac{1 + 4 + 6}{1 + 4 + 9} = \frac{11}{14} \approx 0.786
$$

## 2. 係数を減らす:最良部分集合選択と Lasso

特徴量が多いと、どれが本当に効いているのかわかりにくい。使う特徴量を少数に絞りたい。

### 最良部分集合選択

使う特徴量を $k$ 個以下に制限して、最小二乗を解く [arxiv-1507.03133#c8](https://arxiv.org/pdf/1507.03133v1#page=2 "The cardinality constraint makes Problem (1) NP-hard [41].")。

$$
\min_\beta \ \frac{1}{2} \Vert y - X\beta \Vert_2^2 \quad \text{subject to} \quad \Vert \beta \Vert_0 \le k
$$

$\Vert \beta \Vert_0$ は、$\beta$ の成分のうち0でないものの個数である。
$p$ 個から $k$ 個を選ぶ組合せは非常に多く、この問題は NP 困難である(効率よく解く方法が知られていない問題の仲間)[arxiv-1507.03133#c8](https://arxiv.org/pdf/1507.03133v1#page=2 "The cardinality constraint makes Problem (1) NP-hard [41].")。Bertsimas らは、混合整数最適化(MIO)という方法でこの問題に取り組んでいる [arxiv-1507.03133#c1](https://arxiv.org/pdf/1507.03133v1#page=1 "We develop a discrete extension of modern ﬁrst order continuous optimization methods to ﬁnd high quality feasible solutions that we use as warm starts to a MIO solver that ﬁnds provably optimal solutions.")。

### Lasso

「個数」の代わりに、係数の絶対値の和を罰則として足すのが Lasso である [arxiv-1507.03133#c9](https://arxiv.org/pdf/1507.03133v1#page=3 "shrinks the coeﬃcients towards zero and naturally produces a sparse solution by setting many coeﬃcients to be exactly zero.")。

$$
\min_\beta \ \frac{1}{2} \Vert y - X\beta \Vert_2^2 + \lambda \Vert \beta \Vert_1, \qquad \Vert \beta \Vert_1 = \sum_i |\beta_i|
$$

$\lambda$ は罰則の強さを決める正の数である。論文によれば、この罰則は係数を0に向けて縮め、多くの係数をちょうど0にする [arxiv-1507.03133#c9](https://arxiv.org/pdf/1507.03133v1#page=3 "shrinks the coeﬃcients towards zero and naturally produces a sparse solution by setting many coeﬃcients to be exactly zero.")。
また、この問題は凸な2次の最適化問題で、効率のよい解き方がある [arxiv-1507.03133#c10](https://arxiv.org/pdf/1507.03133v1#page=3 "Problem (2) is a convex quadratic optimization problem and there are several eﬃcient solvers for it, see for example [44, 23, 29].")。

**補足(例:なぜちょうど0になるのか)**:特徴量が1つで、罰則なしの最小二乗の答えが $b$ になる簡単な場合を考える。このとき Lasso は

$$
h(\beta) = \frac{1}{2} (\beta - b)^2 + \lambda |\beta|
$$

の最小化になる。$\beta > 0$ の範囲では $h'(\beta) = \beta - b + \lambda$ なので、$b > \lambda$ なら $\beta = b - \lambda$ で最小になる。$\beta < 0$ の範囲も同様に調べると、答えは

$$
\beta = \begin{cases} b - \lambda & (b > \lambda) \\ 0 & (|b| \le \lambda) \\ b + \lambda & (b < -\lambda) \end{cases}
$$

になる。$|b|$ が $\lambda$ 以下なら係数はちょうど0になり、それより大きくても $\lambda$ だけ0に近づく。たとえば $\lambda = 0.3$ なら、$b = 0.8$ は $0.5$ に、$b = 0.2$ は $0$ になる。

**補足(最良部分集合との違い)**:同じ簡単な場合で最良部分集合選択を考えると、$|b|$ の大きい係数を、縮めずにそのまま残すことになる。
Bertsimas らも、Lasso は大きい係数ほど強く罰するので係数の推定が偏る一方、最良部分集合選択は選んだ変数を縮めずに入れる、と述べている [arxiv-1507.03133#c11](https://arxiv.org/pdf/1507.03133v1#page=3 "Lasso leads to biased regression coef-
ﬁcient estimates, since the ℓ1-norm penalizes the large coeﬃcients more severely than the smaller coeﬃcients.")。

## 3. カーネル:線形モデルを曲線に広げる

### カーネルとは

**補足**:この小節は一般的な説明で、特定の論文の主張ではない。

線形モデルは、特徴量の1次式しか表せない。特徴量を変換して $\varphi(x)$(たとえば $x$ の2乗や積を並べたもの)にしてから線形モデルを使えば、曲線も表せる。
**カーネル** $K(x, x')$ は、この変換後のベクトルどうしの内積 $\varphi(x) \cdot \varphi(x')$ を、変換を経由せずに直接計算する関数である。2点がどれだけ「似ているか」を表す量とも読める。

**補足(例)**:2次元の $x = (x_1, x_2)$ に対して $K(x, x') = (x \cdot x')^2$ とする。$\varphi(x) = (x_1^2,\ \sqrt{2}\, x_1 x_2,\ x_2^2)$ とおくと

$$
\varphi(x) \cdot \varphi(x') = x_1^2 x_1'^2 + 2 x_1 x_2 x_1' x_2' + x_2^2 x_2'^2 = (x_1 x_1' + x_2 x_2')^2 = K(x, x')
$$

で、3次元に変換してから内積をとった結果を、2次元のまま計算できている。

### カーネルリッジ回帰(KRR)

2乗誤差に、関数の「複雑さ」の罰則を足して最小化する [arxiv-1305.5029#c8](https://arxiv.org/pdf/1305.5029v2#page=4 "It is a natural generalization of the ordinary ridge regression estimate [13] to the non-parametric setting.")。

$$
\hat{f} = \arg\min_{f \in \mathcal{H}} \left\{ \frac{1}{N} \sum_{i=1}^{N} \big( f(x_i) - y_i \big)^2 + \lambda \Vert f \Vert_{\mathcal{H}}^2 \right\}
$$

$\mathcal{H}$ はカーネルで決まる関数の集まり(再生核ヒルベルト空間)で、$\Vert f \Vert_{\mathcal{H}}^2$ はそこでの関数の「大きさ」である。論文は、これを通常のリッジ回帰を非線形に広げたものと説明している [arxiv-1305.5029#c8](https://arxiv.org/pdf/1305.5029v2#page=4 "It is a natural generalization of the ordinary ridge regression estimate [13] to the non-parametric setting.")。

**補足(リッジ回帰)**:通常のリッジ回帰は、最小二乗に係数の2乗の和 $\lambda \Vert \beta \Vert_2^2$ を罰則として足したものである。1節の例で、目的関数を $\frac{1}{2}\sum_i (y_i - \beta x_i)^2 + \frac{\lambda}{2} \beta^2$ とすると、同じように微分して

$$
\beta = \frac{\sum_i x_i y_i}{\sum_i x_i^2 + \lambda}
$$

になる。$\lambda = 1$ なら $11/15 \approx 0.733$ で、罰則なしの $11/14$ より0に近い。Lasso と違って、ちょうど0にはならない。

### 解はデータ点のカーネルの和で書ける

**代表定理**により、KRR の解は、データ点でのカーネル関数 $K(\cdot, x_i)$ の線形結合になる [arxiv-1305.5029#c9](https://arxiv.org/pdf/1305.5029v2#page=4 "By the representer theorem for reproducing kernel Hilbert spaces [31], any solution to the KRR program (2) must belong to the linear span of the kernel functions {K(·, xi), i = 1, . . . , N}.")。

$$
\hat{f}(x) = \sum_{i=1}^{N} \alpha_i K(x, x_i)
$$

関数全体を探す問題が、$N$ 個の数 $\alpha_1, \ldots, \alpha_N$ を決める問題に変わる。

**補足(係数の式)**:$K$ を $N \times N$ のカーネル行列($i, j$ 成分が $K(x_i, x_j)$)とすると、$\Vert \hat{f} \Vert_{\mathcal{H}}^2 = \alpha^\top K \alpha$ となる(再生核ヒルベルト空間の性質)。これを目的関数に入れて $\alpha$ で偏微分し0とおくと、$\alpha = (K + N\lambda I)^{-1} y$ が解の1つになる。
1節のリッジ回帰の式の分母に $\lambda$ が足されていたのと同じ形で、行列の対角に $N\lambda$ が足されている。

この式には $N \times N$ の行列の逆行列が出てくる。論文は、標準的な実装では計算時間が $O(N^3)$、メモリが $O(N^2)$ かかると述べている [arxiv-1305.5029#c10](https://arxiv.org/pdf/1305.5029v2#page=1 "the kernel matrix must be inverted, which requires costs O(N 3) and O(N 2) in time and")。$O(N^3)$ は「データ数が2倍になると計算時間がおよそ8倍になる」という意味である。

## 4. カーネル SVM の双対問題

ラベルが $y_i \in \{1, -1\}$ の2値分類で、カーネル SVM の学習は次の2次の最適化問題になる [arxiv-1311.0914#c8](https://arxiv.org/pdf/1311.0914v1#page=3 "the main task in training the kernel SVM is to solve the following quadratic optimization problem:")。

$$
\min_\alpha \ f(\alpha) = \frac{1}{2} \alpha^\top Q \alpha - e^\top \alpha, \qquad \text{subject to} \quad 0 \le \alpha_i \le C, \qquad Q_{ij} = y_i y_j K(x_i, x_j)
$$

- $\alpha$ は $n$ 個の**双対変数**で、データ1つにつき1つある。
- $e$ はすべての成分が1のベクトルなので、$e^\top \alpha = \sum_i \alpha_i$。
- $C$ は、もとの問題(主問題)での損失と正則化の釣り合いを決める定数である。
- 論文はバイアス項(定数項)を省いている。

学習した $\alpha^*$ を使うと、テストデータ $x$ の判定値は次のようになる [arxiv-1311.0914#c9](https://arxiv.org/pdf/1311.0914v1#page=3 "the decision value for a test data x can be computed by")。

$$
\sum_{i=1}^{n} \alpha_i^* \, y_i \, K(x, x_i)
$$

**補足(読み方)**:判定値は「学習データとの似ている度合い $K(x, x_i)$ に、そのラベル $y_i$ と重み $\alpha_i^*$ を掛けて足したもの」である。正のラベルのデータに似ていれば正に、負のラベルのデータに似ていれば負に傾く。$\alpha_i^* = 0$ のデータは判定値に影響しない。
KRR の $\hat{f}(x) = \sum_i \alpha_i K(x, x_i)$ と同じく、解がデータ点のカーネルの和で書けている。

## 5. ガウス過程との関係と GP-UCB

### ノイズがある場合のガウス過程の事後平均

[数式の解説 4](04-bayes.md) では、ノイズのない観測でガウス過程の事後分布を求めた。観測にノイズ $\epsilon_t \sim \mathcal{N}(0, \sigma^2)$ があるとき($y_t = f(x_t) + \epsilon_t$)、事前分布の平均を0とすると、事後分布の平均と分散は次のようになる [arxiv-0912.3995#c9](https://arxiv.org/pdf/0912.3995v4#page=3 "A major advantage of working with GPs is the existence of simple analytic formulae for mean and covariance of the posterior distribution, which allows easy implementation of algorithms.")。

$$
\begin{aligned}
\mu_T(x) &= k_T(x)^\top (K_T + \sigma^2 I)^{-1} y_T \\
\sigma_T^2(x) &= k(x, x) - k_T(x)^\top (K_T + \sigma^2 I)^{-1} k_T(x)
\end{aligned}
$$

$k_T(x) = (k(x_1, x), \ldots, k(x_T, x))$ は、新しい点 $x$ と観測した各点とのカーネルを並べたベクトル、$K_T$ は観測した点どうしのカーネル行列である [arxiv-0912.3995#c9](https://arxiv.org/pdf/0912.3995v4#page=3 "A major advantage of working with GPs is the existence of simple analytic formulae for mean and covariance of the posterior distribution, which allows easy implementation of algorithms.")。

**補足(KRR との一致)**:事後平均は $\mu_T(x) = \sum_t \alpha_t\, k(x, x_t)$($\alpha = (K_T + \sigma^2 I)^{-1} y_T$)と書ける。これは3節の KRR の解で、$N\lambda$ を $\sigma^2$ に置き換えたものと同じ形である。
つまり、ノイズの分散 $\sigma^2$ が、KRR の罰則の強さの役目をしている。ガウス過程はさらに、分散 $\sigma_T^2(x)$ によって「どれだけ不確かか」も与える。

### GP-UCB

Srinivas らの GP-UCB は、次に評価する点を次の規則で選ぶ [arxiv-0912.3995#c10](https://arxiv.org/pdf/0912.3995v4#page=4 "it implicitly negotiates the exploration–exploitation tradeoﬀ.")。

$$
x_t = \arg\max_{x} \ \mu_{t-1}(x) + \beta_t^{1/2} \, \sigma_{t-1}(x)
$$

- $\mu_{t-1}(x)$ が大きい点(よい値が期待できる点)と、$\sigma_{t-1}(x)$ が大きい点(不確かな点)の両方を好む。論文は、これが探索と活用の釣り合いを暗に取っていると述べている [arxiv-0912.3995#c10](https://arxiv.org/pdf/0912.3995v4#page=4 "it implicitly negotiates the exploration–exploitation tradeoﬀ.")。
- 平均が最大の点だけを選ぶと、欲張りすぎて浅い局所解にとどまりやすい、と論文は述べている [arxiv-0912.3995#c2](https://arxiv.org/pdf/0912.3995v4#page=4 "However, this rule is too greedy too soon and tends to get stuck in shallow local optima.")。
- $\beta_t$ は定数で、論文の理論では状況に応じて決める [arxiv-0912.3995#c10](https://arxiv.org/pdf/0912.3995v4#page=4 "it implicitly negotiates the exploration–exploitation tradeoﬀ.")。

[数式の解説 4](04-bayes.md) で見た Snoek らの「信頼下限」$\mu - \kappa\sigma$ は、これを最小化の向きに書いたものにあたる [arxiv-1206.2944#c13](https://arxiv.org/pdf/1206.2944v2#page=3 "with a tunable κ to balance exploitation against exploration.")。

## まとめ

| 式 | 何を表すか | 根拠 |
|---|---|---|
| $y = X\beta + \epsilon$、$\min \frac{1}{2}\Vert y - X\beta \Vert_2^2$ | 線形モデルと最小二乗 | [arxiv-1507.03133#c8](https://arxiv.org/pdf/1507.03133v1#page=2 "The cardinality constraint makes Problem (1) NP-hard [41].") |
| $\Vert \beta \Vert_0 \le k$ | 最良部分集合選択(NP 困難) | [arxiv-1507.03133#c8](https://arxiv.org/pdf/1507.03133v1#page=2 "The cardinality constraint makes Problem (1) NP-hard [41].") |
| $+ \lambda \Vert \beta \Vert_1$ | Lasso(係数をちょうど0にする) | [arxiv-1507.03133#c9](https://arxiv.org/pdf/1507.03133v1#page=3 "shrinks the coeﬃcients towards zero and naturally produces a sparse solution by setting many coeﬃcients to be exactly zero.") |
| $\frac{1}{N}\sum (f(x_i) - y_i)^2 + \lambda \Vert f \Vert_{\mathcal{H}}^2$ | カーネルリッジ回帰 | [arxiv-1305.5029#c8](https://arxiv.org/pdf/1305.5029v2#page=4 "It is a natural generalization of the ordinary ridge regression estimate [13] to the non-parametric setting.") |
| $\hat{f}(x) = \sum_i \alpha_i K(x, x_i)$ | 代表定理 | [arxiv-1305.5029#c9](https://arxiv.org/pdf/1305.5029v2#page=4 "By the representer theorem for reproducing kernel Hilbert spaces [31], any solution to the KRR program (2) must belong to the linear span of the kernel functions {K(·, xi), i = 1, . . . , N}.") |
| $\frac{1}{2}\alpha^\top Q \alpha - e^\top \alpha$、$0 \le \alpha \le C$ | カーネル SVM の双対問題 | [arxiv-1311.0914#c8](https://arxiv.org/pdf/1311.0914v1#page=3 "the main task in training the kernel SVM is to solve the following quadratic optimization problem:") |
| $\mu_T(x) = k_T(x)^\top (K_T + \sigma^2 I)^{-1} y_T$ | ノイズありのガウス過程の事後平均 | [arxiv-0912.3995#c9](https://arxiv.org/pdf/0912.3995v4#page=3 "A major advantage of working with GPs is the existence of simple analytic formulae for mean and covariance of the posterior distribution, which allows easy implementation of algorithms.") |
| $\mu_{t-1}(x) + \beta_t^{1/2}\sigma_{t-1}(x)$ | GP-UCB | [arxiv-0912.3995#c10](https://arxiv.org/pdf/0912.3995v4#page=4 "it implicitly negotiates the exploration–exploitation tradeoﬀ.") |

## 参照カード

- [arxiv-1507.03133](../../papers/arxiv-1507.03133.yaml) Bertsimas, King & Mazumder, "Best Subset Selection via a Modern Optimization Lens"
- [arxiv-1305.5029](../../papers/arxiv-1305.5029.yaml) Zhang, Duchi & Wainwright, "Divide and Conquer Kernel Ridge Regression"
- [arxiv-1311.0914](../../papers/arxiv-1311.0914.yaml) Hsieh, Si & Dhillon, "A Divide-and-Conquer Solver for Kernel Support Vector Machines"
- [arxiv-0912.3995](../../papers/arxiv-0912.3995.yaml) Srinivas, Krause, Kakade & Seeger, "Gaussian Process Optimization in the Bandit Setting"
- [arxiv-1807.02811](../../papers/arxiv-1807.02811.yaml) Frazier, "A Tutorial on Bayesian Optimization"
- [arxiv-1206.2944](../../papers/arxiv-1206.2944.yaml) Snoek, Larochelle & Adams, "Practical Bayesian Optimization of Machine Learning Algorithms"
