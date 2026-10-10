---
title: 数式の解説 6 — 近似推論:変分推論の ELBO と CAVI、メトロポリス法と HMC、R-hat、重要度比と診断
kind: math
tags: [mcmc, variational-inference, posterior-inference]
depends_on: [arxiv-1601.00670, arxiv-1401.0118, arxiv-1701.02434, arxiv-1903.08008, arxiv-1507.02646, arxiv-1802.02538, arxiv-1804.06788]
written_at: 2026-10-10
written_by: claude-opus-5-5 via Claude Code
---

# 数式の解説 6 — 近似推論:変分推論の ELBO と CAVI、メトロポリス法と HMC、R-hat、重要度比と診断

<!-- generated:stale -->
> 未反映のカードはありません。
<!-- /generated:stale -->

## この記事の読み方

[近似ベイズ推論とその診断](../methods/approximate-inference-and-diagnostics.md) の記事で扱った手法の、中心にある式を解説する。

ベイズの定理で事後分布 $p(z \mid x)$ を求めたいが、分母の $p(x)$(エビデンス)が計算できないことが多い。そこで次の2つの方向で近似する。

- **変分推論**:扱いやすい分布 $q(z)$ を、事後分布に最も近くなるように**最適化**する。
- **MCMC**:事後分布に従うサンプルを、確率的な手順で**順に生成**する。

そして、どちらの近似がうまくいったかを**診断**する式がある。

使う道具(期待値、ベイズの定理、対数、偏微分)は [準備の記事](00-preliminaries.md)、KL ダイバージェンスは [数式の解説 2](02-generative-models.md) の1節で説明している。

- 式は論文から取り、根拠のカード(論文の該当ページへのリンク)を付けている。
- 「**補足**」と書いた計算は、論文には書かれていない、この記事による説明である。

## 1. 変分推論

### KL は計算できないが、ELBO は計算できる

近似分布 $q(z)$ と事後分布 $p(z \mid x)$ の近さを KL ダイバージェンスで測る。期待値はすべて $q(z)$ についてとる [arxiv-1601.00670#c10](https://arxiv.org/pdf/1601.00670v9#page=6 "This reveals its dependence on log p(x).")。

$$
\mathrm{KL}\big(q(z) \,\Vert\, p(z \mid x)\big) = E[\log q(z)] - E[\log p(z \mid x)] = E[\log q(z)] - E[\log p(z, x)] + \log p(x)
$$

**補足**:2つ目の等号は、条件付き確率の定義 $p(z \mid x) = p(z, x)/p(x)$ の対数をとって $\log p(z \mid x) = \log p(z, x) - \log p(x)$ とし、$\log p(x)$ が $z$ によらない定数なので期待値の外に出したものである。

最後の項 $\log p(x)$ が計算できないので、KL そのものは計算できない [arxiv-1601.00670#c10](https://arxiv.org/pdf/1601.00670v9#page=6 "This reveals its dependence on log p(x).")。そこで、計算できる部分だけを取り出した **ELBO**(エビデンスの下界)を最大化する [arxiv-1601.00670#c11](https://arxiv.org/pdf/1601.00670v9#page=7 "The bound then follows from the fact that KL (·) ≥0 (Kullback and Leibler, 1951).")。

$$
\mathrm{ELBO}(q) = E[\log p(z, x)] - E[\log q(z)], \qquad
\log p(x) = \mathrm{KL}\big(q(z) \,\Vert\, p(z \mid x)\big) + \mathrm{ELBO}(q)
$$

- $\log p(x)$ は $q$ によらない定数なので、ELBO を大きくすることは KL を小さくすることと同じである。
- KL は負にならないので、どんな $q$ でも $\log p(x) \ge \mathrm{ELBO}(q)$。これが「下界」という名前の由来である [arxiv-1601.00670#c11](https://arxiv.org/pdf/1601.00670v9#page=7 "The bound then follows from the fact that KL (·) ≥0 (Kullback and Leibler, 1951).")。

ELBO は「データをよく説明する項」と「事前分布に近づける項」に分けて書くこともできる [arxiv-1601.00670#c12](https://arxiv.org/pdf/1601.00670v9#page=7 "Thus the variational objective mirrors the usual balance between likelihood and prior.")。これは VAE の目的関数([数式の解説 2](02-generative-models.md) の2節)と同じ形である。

### 平均場近似と座標上昇(CAVI)

**平均場近似**では、潜在変数 $z = (z_1, \ldots, z_m)$ が $q$ のもとで互いに独立だと仮定し、$q(z) = \prod_j q_j(z_j)$ とする。
この近似は各変数の周辺分布は表せるが、変数どうしの相関は表せない。相関のある2次元正規分布を近似すると、周辺の分散を小さく見積もる [arxiv-1601.00670#c6](https://arxiv.org/pdf/1601.00670v9#page=9 "Further, the marginal variances of the approximation under-represent those of the target density.")。

CAVI は、1つの因子 $q_j$ だけを動かし、ほかを固定して ELBO を最大にする操作を、順に繰り返す。そのときの最適な $q_j$ は次の形になる [arxiv-1601.00670#c13](https://arxiv.org/pdf/1601.00670v9#page=9 "The optimal qj(zj) is then proportional to the exponentiated expected log of the complete conditional,")。

$$
q_j^*(z_j) \propto \exp\Big\{ E_{-j}\big[ \log p(z_j, z_{-j}, x) \big] \Big\}
$$

$z_{-j}$ は $z_j$ 以外の変数、$E_{-j}$ は固定した他の因子 $\prod_{\ell \ne j} q_\ell$ についての期待値、$\propto$ は「定数倍を除いて等しい」という意味である。

**補足(読み方)**:もし他の変数の値がわかっていれば、$z_j$ の条件付き分布は $p(z_j, z_{-j}, x)$ に比例する。他の変数の値はわからないので、その対数を他の変数について**平均**してから指数に戻している。

ELBO は一般に凸ではなく、CAVI は局所的な最適解に収束することしか保証されない [arxiv-1601.00670#c7](https://arxiv.org/pdf/1601.00670v9#page=11 "Each initialization reaches a different value, indicating the presence of many local optima in the ELBO.")。

### 勾配を使う:ブラックボックス変分推論

モデルが複雑だと、CAVI の期待値を式で計算できない。Ranganath らは、$q$ のパラメータ $\lambda$ についての ELBO の勾配を、次の期待値で書いた [arxiv-1401.0118#c2](https://arxiv.org/pdf/1401.0118v1#page=3 "We emphasize that the score function and sampling algorithms depend only on the variational distribution, not the underlying model.")。

$$
\nabla_\lambda \mathrm{ELBO} = E_q\Big[ \nabla_\lambda \log q(z \mid \lambda) \, \big( \log p(x, z) - \log q(z \mid \lambda) \big) \Big]
$$

この期待値は、$q$ から $S$ 個のサンプルを引いて平均すれば近似できる。モデルについて必要なのは、同時分布 $\log p(x, z)$ を計算できることだけである [arxiv-1401.0118#c2](https://arxiv.org/pdf/1401.0118v1#page=3 "We emphasize that the score function and sampling algorithms depend only on the variational distribution, not the underlying model.")。

**補足(なぜこう書けるか)**:中心にあるのは $\nabla_\lambda q = q\, \nabla_\lambda \log q$ という関係(対数の微分 $(\log q)' = q'/q$ の言い換え)である。これを使うと、「期待値の勾配」が「勾配を含む量の期待値」に書き換わり、サンプルの平均で近似できるようになる。

ただし、この推定量はばらつき(分散)が大きすぎて役に立たないことがある、と論文は述べている [arxiv-1401.0118#c3](https://arxiv.org/pdf/1401.0118v1#page=3 "In practice, the high variance gradients would require very small steps which would lead to slow convergence.")。

### 変分推論の弱点

論文は、変分推論が一般に事後分布の分散を小さく見積もることを、目的関数(KL の向き)の結果として述べている [arxiv-1601.00670#c5](https://arxiv.org/pdf/1601.00670v9#page=3 "We do know that variational inference generally underestimates the variance of the posterior density; this is a consequence of its objective function.")。

## 2. MCMC

### メトロポリス・ヘイスティングス法

現在の点 $q$ から、提案分布 $Q(q' \mid q)$ で新しい点 $q'$ を提案し、次の確率で受け入れる。受け入れなければ $q$ にとどまる [arxiv-1701.02434#c10](https://arxiv.org/pdf/1701.02434v2#page=15 "The Metropolis-Hastings algorithm is comprised of two steps: a proposal and a correction.")。

$$
a(q' \mid q) = \min\left( 1,\ \frac{Q(q \mid q')\, \pi(q')}{Q(q' \mid q)\, \pi(q)} \right)
$$

$\pi$ は目標の分布(事後分布)の密度である。提案分布が正規分布のように対称($Q(q' \mid q) = Q(q \mid q')$)なら、比の $Q$ が消えて次の形になる(ランダムウォーク・メトロポリス法)[arxiv-1701.02434#c11](https://arxiv.org/pdf/1701.02434v2#page=16 "density cancels in the acceptance probability, leaving the simple form")。

$$
a(q' \mid q) = \min\left( 1,\ \frac{\pi(q')}{\pi(q)} \right)
$$

**補足(例)**:提案先の密度が今の点より高ければ、比は1以上なので必ず受け入れる。半分なら確率 $0.5$ で受け入れる。
比だけを使うので、$\pi$ が定数倍を除いてしかわからなくてもよい。事後分布の分母 $p(x)$ がわからなくても、分子 $p(x \mid z)\, p(z)$ だけで計算できる。

論文は、高次元では、ランダムウォーク・メトロポリス法の提案はほとんどが棄却され、提案を小さくすると今度は動きが小さくなり、どう調整しても探索が非常に遅いと述べている [arxiv-1701.02434#c2](https://arxiv.org/pdf/1701.02434v2#page=16 "Regardless of how we tune the covariance of the Random Walk Metropolis proposal or the particular details of the target distribution, the resulting Markov chain will explore the typical set extremely slowly in all but the lowest dimensional spaces.")。

### ハミルトニアン・モンテカルロ(HMC)

HMC は、位置 $q$(パラメータ)に、運動量 $p$ という補助の変数を加え、物理の運動のように動かして遠くの点を提案する。
2つを合わせた分布を、**ハミルトニアン** $H$ で表す [arxiv-1701.02434#c12](https://arxiv.org/pdf/1701.02434v2#page=25 "Appealing to the physical analogy, the value of the Hamiltonian at any point in phase space is called the energy at that point.")。

$$
\pi(q, p) = e^{-H(q, p)}, \qquad H(q, p) = \underbrace{-\log \pi(p \mid q)}_{K:\ \text{運動エネルギー}} + \underbrace{(-\log \pi(q))}_{V:\ \text{位置エネルギー}}
$$

- 位置エネルギー $V(q) = -\log \pi(q)$ は、目標の分布で決まる。密度が高い点ほど $V$ は低い(谷になる)。
- 運動エネルギー $K$ は、実装する側が選ぶ [arxiv-1701.02434#c12](https://arxiv.org/pdf/1701.02434v2#page=25 "Appealing to the physical analogy, the value of the Hamiltonian at any point in phase space is called the energy at that point.")。

点は**ハミルトンの方程式**に従って動く [arxiv-1701.02434#c13](https://arxiv.org/pdf/1701.02434v2#page=25 "Recognizing ∂V/∂q as the gradient of the logarithm of the target density, we see that Hamilton’s equations fulﬁll exactly the intuition introduced in Section 3.1.")。

$$
\frac{dq}{dt} = +\frac{\partial H}{\partial p}, \qquad \frac{dp}{dt} = -\frac{\partial H}{\partial q}
$$

**補足(読み方)**:よく使われる $K = \frac{1}{2} p^2$ では、1つ目の式は $\frac{dq}{dt} = p$(位置は運動量の向きに動く)、2つ目は $\frac{dp}{dt} = -\frac{dV}{dq}$(運動量は谷の方向に加速される)になる。斜面を転がる球のように、谷(密度の高い所)の周りを勢いをつけて動き回る。

### リープフロッグ法

ハミルトンの方程式はそのままでは解けないので、刻み幅 $\epsilon$ で区切って近似的に動かす。論文はリープフロッグ法を次のように書いている [arxiv-1701.02434#c14](https://arxiv.org/pdf/1701.02434v2#page=37 "Given a time discretization, or step size, ϵ, the leapfrog integrator simulates the exact trajectory as")。

$$
\begin{aligned}
p_{n+1/2} &= p_n - \frac{\epsilon}{2} \frac{\partial V}{\partial q}(q_n) \\
q_{n+1} &= q_n + \epsilon\, p_{n+1/2} \\
p_{n+1} &= p_{n+1/2} - \frac{\epsilon}{2} \frac{\partial V}{\partial q}(q_{n+1})
\end{aligned}
$$

運動量を半歩、位置を1歩、運動量をまた半歩、と交互に進める。論文は、この交互の更新によって、位相空間の体積が正確に保たれると述べている [arxiv-1701.02434#c14](https://arxiv.org/pdf/1701.02434v2#page=37 "Given a time discretization, or step size, ϵ, the leapfrog integrator simulates the exact trajectory as")。

**補足(例)**:目標を標準正規分布とすると $V(q) = q^2/2$、$\partial V/\partial q = q$。$K = p^2/2$、$\epsilon = 0.5$、$q_0 = 1$、$p_0 = 0$ から1歩進めると

$$
p_{1/2} = 0 - 0.25 \times 1 = -0.25, \quad q_1 = 1 + 0.5 \times (-0.25) = 0.875, \quad p_1 = -0.25 - 0.25 \times 0.875 = -0.46875
$$

となる。$H = q^2/2 + p^2/2$ は、出発点で $0.5$、1歩後で約 $0.383 + 0.110 = 0.493$ で、ほぼ保たれている。正確な運動なら $H$ は変わらない。一般的な HMC の実装では、近似の誤差で $H$ がずれた分を、メトロポリス法と同じ考え方の受け入れ判定で補正する。

曲率の大きい領域では、この近似の軌道が発散することがある。論文は、発散した遷移が1つでもあれば推定を疑うべきだと述べている [arxiv-1701.02434#c7](https://arxiv.org/pdf/1701.02434v2#page=45 "In particular, any divergent transitions encountered in a Hamiltonian Markov chain should prompt suspicion of the validity of any Markov chain Monte Carlo estimators.")。

## 3. MCMC がうまくいったかを調べる:R-hat

複数の鎖(チェーン)を別々の初期値から走らせ、「鎖どうしの違い」と「鎖の中のばらつき」を比べる。$M$ 本の鎖に $N$ 個ずつのサンプルがあるとき、次を計算する [arxiv-1903.08008#c10](https://arxiv.org/pdf/1903.08008v5#page=5 "For each scalar summary of interest θ, we compute B and W, the between- and within-chain variances:")。

$$
B = \frac{N}{M - 1} \sum_{m=1}^{M} \big( \bar{\theta}^{(\cdot m)} - \bar{\theta}^{(\cdot\cdot)} \big)^2, \qquad
W = \frac{1}{M} \sum_{m=1}^{M} s_m^2
$$

- $\bar{\theta}^{(\cdot m)}$ は鎖 $m$ の平均、$\bar{\theta}^{(\cdot\cdot)}$ は全体の平均。$B$ は**鎖の平均どうしのばらつき**(鎖間分散)である。
- $s_m^2$ は鎖 $m$ の中の分散($N - 1$ で割る)。$W$ はその平均(鎖内分散)である。

この2つを混ぜて事後分散を推定し、$W$ との比の平方根をとる [arxiv-1903.08008#c11](https://arxiv.org/pdf/1903.08008v5#page=5 "Meanwhile, for any ﬁnite N, the within-chain variance W should underestimate var(θ/y) because the individual chains haven’t had the time to explore all of the target distribution and, as a result, will have less variability.") [arxiv-1903.08008#c12](https://arxiv.org/pdf/1903.08008v5#page=6 "Without splitting, bR would get fooled by non-stationary chains as in Figure 1b.")。

$$
\widehat{\mathrm{var}}^{+} = \frac{N - 1}{N} W + \frac{1}{N} B, \qquad
\hat{R} = \sqrt{ \frac{\widehat{\mathrm{var}}^{+}}{W} }
$$

論文によれば、有限の $N$ では、鎖がまだ分布全体を探索していないため $W$ は事後分散を小さく見積もる [arxiv-1903.08008#c11](https://arxiv.org/pdf/1903.08008v5#page=5 "Meanwhile, for any ﬁnite N, the within-chain variance W should underestimate var(θ/y) because the individual chains haven’t had the time to explore all of the target distribution and, as a result, will have less variability.")。$\hat{R}$ は、うまく混ざる過程では $N \to \infty$ で1に近づく [arxiv-1903.08008#c12](https://arxiv.org/pdf/1903.08008v5#page=6 "Without splitting, bR would get fooled by non-stationary chains as in Figure 1b.")。

**補足(例)**:$M = 2$、$N = 3$ で、鎖1が $1, 2, 3$、鎖2が $3, 4, 5$ だったとする。鎖の平均は $2$ と $4$、全体の平均は $3$、どちらの鎖も $s_m^2 = 1$ である。

$$
B = \frac{3}{1} \big( (2-3)^2 + (4-3)^2 \big) = 6, \quad W = 1, \quad
\widehat{\mathrm{var}}^{+} = \frac{2}{3} \times 1 + \frac{1}{3} \times 6 = \frac{8}{3}, \quad
\hat{R} = \sqrt{8/3} \approx 1.63
$$

2本の鎖が違う場所にいるので、$\hat{R}$ は1より大きくなる。2本の平均が等しければ $B = 0$ となり、$\hat{R}$ は1以下になる。

- 鎖を半分に分けて計算する(split-$\hat{R}$)のは、分けないと、定常になっていない鎖を見逃すからである [arxiv-1903.08008#c12](https://arxiv.org/pdf/1903.08008v5#page=6 "Without splitting, bR would get fooled by non-stationary chains as in Figure 1b.")。
- 論文は、順位で正規化した $\hat{R}$ が $1.01$ 未満の場合にだけサンプルを使うことを推奨している [arxiv-1903.08008#c3](https://arxiv.org/pdf/1903.08008v5#page=4 "This threshold is much tighter than the one recommended by Gelman and Rubin (1992), reﬂecting lessons learnt over more than 25 years of use, as well as the simulation results in Appendix A.")。

## 4. 重要度比と変分推論の診断

### 重要度サンプリング

目標の分布 $p$ から直接サンプルを引けないとき、別の分布 $g$ から引いたサンプルに重みを付けて期待値を推定する [arxiv-1507.02646#c10](https://arxiv.org/pdf/1507.02646v9#page=2 "When the proposal distribution is a poor approximation to the target distribution, the distribution of importance ratios can have a heavy right tail.")。

$$
E_p[h] \approx \frac{\sum_{s=1}^{S} r_s\, h(\theta_s)}{\sum_{s=1}^{S} r_s}, \qquad r_s = \frac{p(\theta_s)}{g(\theta_s)}
$$

$r_s$ を**重要度比**という。$p$ で出やすいのに $g$ で出にくい点ほど、大きな重みが付く。
$g$ が $p$ の近似として悪いと、重要度比の分布の右の裾が重くなり、少数のサンプルが推定を支配して不安定になる [arxiv-1507.02646#c10](https://arxiv.org/pdf/1507.02646v9#page=2 "When the proposal distribution is a poor approximation to the target distribution, the distribution of importance ratios can have a heavy right tail.")。

### パレート $\hat{k}$ 診断

PSIS は、大きな重要度比の分布を一般化パレート分布で近似し、その形のパラメータ $\hat{k}$ を診断に使う [arxiv-1507.02646#c1](https://arxiv.org/pdf/1507.02646v9#page=4 "We propose a new method to stabilize the importance weights by replacing the M largest weights above the threshold u by a set of well-spaced values that are consistent with the tails of the importance distribution,")。$\hat{k}$ が大きいほど裾が重い。論文の推奨は、サンプル数 $S$ に応じたしきい値で判断するものである [arxiv-1507.02646#c7](https://arxiv.org/pdf/1507.02646v9#page=25 "If ˆk > 1, it is expected that the mean does not exist and any estimate for the mean is invalid.")。

Yao らは、これを変分推論の診断に使った。$q$ をサンプルを引く分布、$p$ を事後分布として重要度比をとり、$\hat{k}$ が大きければ $q$ は事後分布の近似として不十分だと判断する [arxiv-1802.02538#c2](https://arxiv.org/pdf/1802.02538v2#page=3 "ˆk is invariant under any constant multiplication of p or q, which explains why we can suppress the marginal likelihood (normalizing constant) p(y) and replace the intractable p(θ/y) with p(θ, y) in (2).") [arxiv-1802.02538#c3](https://arxiv.org/pdf/1802.02538v2#page=3 "If ˆk > 0.7, the PSIS convergence rate becomes impractically slow, leading to a large mean square error, and a even larger error for plain VI estimate.")。
重要度比は $p$ や $q$ の定数倍で $\hat{k}$ が変わらないので、正規化されていない同時分布 $p(z, x)$ をそのまま使える [arxiv-1802.02538#c2](https://arxiv.org/pdf/1802.02538v2#page=3 "ˆk is invariant under any constant multiplication of p or q, which explains why we can suppress the marginal likelihood (normalizing constant) p(y) and replace the intractable p(θ/y) with p(θ, y) in (2).")。

### シミュレーションに基づく較正(SBC)

推論の**計算**が正しいかを確かめる方法である。個々の観測で事後分布が真の値を含むことを保証するものではない [arxiv-1804.06788#c4](https://arxiv.org/pdf/1804.06788v2#page=4 "Importantly, this calibration is limited exclusively to the computational aspect of our analysis.")。

1. 事前分布からパラメータ $\tilde{\theta}$ を引く。
2. その $\tilde{\theta}$ でデータを生成する。
3. そのデータで推論を行い、事後分布のサンプルを $L$ 個得る。
4. $L$ 個の事後サンプルのうち、$\tilde{\theta}$ より小さいものの個数(順位)を数える。

これを何度も繰り返す。推論が正確なら、順位は $0, 1, \ldots, L$ の上で一様に分布する [arxiv-1804.06788#c3](https://arxiv.org/pdf/1804.06788v2#page=4 "SBC requires just one assumption: that we have a generative model for our data.")。
順位のヒストグラムの形から、ずれの種類を読み取れる。山形なら計算した事後分布が広すぎ、谷形なら狭すぎ、左右非対称なら偏りがある [arxiv-1804.06788#c5](https://arxiv.org/pdf/1804.06788v2#page=7 "Conversely, an algorithm that computes posteriors that are, on average, under-dispersed relative to the true posterior produces a histogram of rank statistics with a characteristic ∪ shape (Figure 6).")。

**補足(なぜ一様か)**:$\tilde{\theta}$ は事前分布から引かれ、データはそれから生成されている。このとき $\tilde{\theta}$ は、そのデータのもとでの事後分布から引いたサンプルと同じ分布に従う。$\tilde{\theta}$ と $L$ 個の事後サンプルは同じ分布から出た $L + 1$ 個の値になるので、$\tilde{\theta}$ が何番目に来るかは等しく確からしい。[数式の解説 3](03-uncertainty-and-calibration.md) の共形予測の「$n+1$」と同じ考え方である。

## まとめ

| 式 | 何を表すか | 根拠 |
|---|---|---|
| $\log p(x) = \mathrm{KL}(q \Vert p(z \mid x)) + \mathrm{ELBO}(q)$ | ELBO はエビデンスの下界 | [arxiv-1601.00670#c10](https://arxiv.org/pdf/1601.00670v9#page=6 "This reveals its dependence on log p(x).") [arxiv-1601.00670#c11](https://arxiv.org/pdf/1601.00670v9#page=7 "The bound then follows from the fact that KL (·) ≥0 (Kullback and Leibler, 1951).") |
| $q_j^* \propto \exp\{E_{-j}[\log p(z_j, z_{-j}, x)]\}$ | 平均場近似の座標上昇(CAVI) | [arxiv-1601.00670#c13](https://arxiv.org/pdf/1601.00670v9#page=9 "The optimal qj(zj) is then proportional to the exponentiated expected log of the complete conditional,") |
| $E_q[\nabla \log q \,(\log p - \log q)]$ | ELBO の勾配(スコア関数) | [arxiv-1401.0118#c2](https://arxiv.org/pdf/1401.0118v1#page=3 "We emphasize that the score function and sampling algorithms depend only on the variational distribution, not the underlying model.") |
| $\min(1, \frac{Q(q \mid q')\pi(q')}{Q(q' \mid q)\pi(q)})$ | メトロポリス・ヘイスティングスの受け入れ確率 | [arxiv-1701.02434#c10](https://arxiv.org/pdf/1701.02434v2#page=15 "The Metropolis-Hastings algorithm is comprised of two steps: a proposal and a correction.") |
| $H = K + V$、ハミルトンの方程式 | HMC の運動 | [arxiv-1701.02434#c12](https://arxiv.org/pdf/1701.02434v2#page=25 "Appealing to the physical analogy, the value of the Hamiltonian at any point in phase space is called the energy at that point.") [arxiv-1701.02434#c13](https://arxiv.org/pdf/1701.02434v2#page=25 "Recognizing ∂V/∂q as the gradient of the logarithm of the target density, we see that Hamilton’s equations fulﬁll exactly the intuition introduced in Section 3.1.") |
| 半歩・1歩・半歩の更新 | リープフロッグ法 | [arxiv-1701.02434#c14](https://arxiv.org/pdf/1701.02434v2#page=37 "Given a time discretization, or step size, ϵ, the leapfrog integrator simulates the exact trajectory as") |
| $\hat{R} = \sqrt{\widehat{\mathrm{var}}^{+}/W}$ | 鎖間と鎖内のばらつきの比 | [arxiv-1903.08008#c10](https://arxiv.org/pdf/1903.08008v5#page=5 "For each scalar summary of interest θ, we compute B and W, the between- and within-chain variances:") [arxiv-1903.08008#c12](https://arxiv.org/pdf/1903.08008v5#page=6 "Without splitting, bR would get fooled by non-stationary chains as in Figure 1b.") |
| $r_s = p(\theta_s)/g(\theta_s)$ | 重要度比 | [arxiv-1507.02646#c10](https://arxiv.org/pdf/1507.02646v9#page=2 "When the proposal distribution is a poor approximation to the target distribution, the distribution of importance ratios can have a heavy right tail.") |
| 順位が $0, \ldots, L$ で一様 | SBC | [arxiv-1804.06788#c3](https://arxiv.org/pdf/1804.06788v2#page=4 "SBC requires just one assumption: that we have a generative model for our data.") |

## 参照カード

- [arxiv-1601.00670](../../papers/arxiv-1601.00670.yaml) Blei, Kucukelbir & McAuliffe, "Variational Inference: A Review for Statisticians"
- [arxiv-1401.0118](../../papers/arxiv-1401.0118.yaml) Ranganath, Gerrish & Blei, "Black Box Variational Inference"
- [arxiv-1701.02434](../../papers/arxiv-1701.02434.yaml) Betancourt, "A Conceptual Introduction to Hamiltonian Monte Carlo"
- [arxiv-1903.08008](../../papers/arxiv-1903.08008.yaml) Vehtari et al., "Rank-normalization, folding, and localization: An improved R-hat for assessing convergence of MCMC"
- [arxiv-1507.02646](../../papers/arxiv-1507.02646.yaml) Vehtari et al., "Pareto Smoothed Importance Sampling"
- [arxiv-1802.02538](../../papers/arxiv-1802.02538.yaml) Yao, Vehtari, Simpson & Gelman, "Yes, but Did It Work?: Evaluating Variational Inference"
- [arxiv-1804.06788](../../papers/arxiv-1804.06788.yaml) Talts et al., "Validating Bayesian Inference Algorithms with Simulation-Based Calibration"
