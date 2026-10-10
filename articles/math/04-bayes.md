---
title: 数式の解説 4 — ベイズ系:ガウス過程の事後分布、期待改善量、ベイズ的オンライン変化点検知
kind: math
tags: [bayesian-optimization, bayesian-changepoint-models]
depends_on: [arxiv-1807.02811, arxiv-1206.2944, arxiv-0710.3742]
written_at: 2026-10-10
written_by: claude-opus-5-5 via Claude Code
---

# 数式の解説 4 — ベイズ系:ガウス過程の事後分布、期待改善量、ベイズ的オンライン変化点検知

<!-- generated:stale -->
> 未反映のカードはありません。
<!-- /generated:stale -->

## この記事の読み方

[ベイズ最適化とハイパーパラメータ最適化](../methods/bayesian-optimization.md) と [ベイズ変化点検知](../topics/bayesian-change-point-detection.md) の記事で扱った手法の、中心にある式を解説する。
どちらも「データを見るたびに、ベイズの定理で考えを更新する」という同じ考え方の上に立っている。

使う道具(ベイズの定理、条件付き確率、正規分布、積分)は [準備の記事](00-preliminaries.md) で説明している。

- 式は論文から取り、根拠のカード(論文の該当ページへのリンク)を付けている。
- 「**補足**」と書いた計算は、論文には書かれていない、この記事による説明である。

## 1. ガウス過程:関数についての「事前の考え」

ベイズ最適化は、評価に時間のかかる関数 $f(x)$ の最大値(または最小値)を、少ない評価回数で探す方法である。
まだ評価していない点で $f$ がどんな値をとりそうかを、**ガウス過程**(GP)という確率モデルで表す。

### 事前分布

点 $x_1, \ldots, x_k$ での関数の値をまとめて $f(x_{1:k}) = (f(x_1), \ldots, f(x_k))$ と書く。ガウス過程では、これが多次元の正規分布に従うと考える [arxiv-1807.02811#c10](https://arxiv.org/pdf/1807.02811v1#page=4 "The kernel is chosen so that points xi, xj that are closer in the input space have a large positive correlation, encoding the belief that they should have more similar function values than points that are far apart.")。

$$
f(x_{1:k}) \sim \mathrm{Normal}\big(\mu_0(x_{1:k}),\ \Sigma_0(x_{1:k}, x_{1:k})\big)
$$

- $\mu_0(x)$(平均関数):データを見る前に「$f(x)$ はこのくらいだろう」と考える値。
- $\Sigma_0(x, x')$(**カーネル**):2点 $x$ と $x'$ の値がどれだけ似ているかを表す。論文によれば、近い2点ほど正の相関が大きくなるように選ぶ。「近い点では関数の値も近いはずだ」という考えを表している [arxiv-1807.02811#c10](https://arxiv.org/pdf/1807.02811v1#page=4 "The kernel is chosen so that points xi, xj that are closer in the input space have a large positive correlation, encoding the belief that they should have more similar function values than points that are far apart.")。

### 事後分布

点 $x_1, \ldots, x_n$ で $f$ を(ノイズなしで)評価したあと、新しい点 $x$ での $f(x)$ は、平均 $\mu_n(x)$、分散 $\sigma_n^2(x)$ の正規分布になる [arxiv-1807.02811#c11](https://arxiv.org/pdf/1807.02811v1#page=5 "The posterior mean µn(x) is a weighted average between the prior µ0(x) and an estimate based on the data f(x1:n), with a weight that depends on the kernel.") [arxiv-1807.02811#c12](https://arxiv.org/pdf/1807.02811v1#page=5 "is equal to the prior covariance Σ0(x, x) less a term that corresponds to the variance removed by observing f(x1:n).")。

$$
\begin{aligned}
\mu_n(x) &= \Sigma_0(x, x_{1:n})\, \Sigma_0(x_{1:n}, x_{1:n})^{-1} \big(f(x_{1:n}) - \mu_0(x_{1:n})\big) + \mu_0(x) \\
\sigma_n^2(x) &= \Sigma_0(x, x) - \Sigma_0(x, x_{1:n})\, \Sigma_0(x_{1:n}, x_{1:n})^{-1}\, \Sigma_0(x_{1:n}, x)
\end{aligned}
$$

$^{-1}$ は逆行列(数の「逆数」にあたるもの)である。論文は、この式を次のように読んでいる。

- 事後平均 $\mu_n(x)$ は、事前の値 $\mu_0(x)$ と、データからの推定値の重み付き平均で、重みはカーネルで決まる [arxiv-1807.02811#c11](https://arxiv.org/pdf/1807.02811v1#page=5 "The posterior mean µn(x) is a weighted average between the prior µ0(x) and an estimate based on the data f(x1:n), with a weight that depends on the kernel.")。
- 事後分散 $\sigma_n^2(x)$ は、事前の分散 $\Sigma_0(x, x)$ から「観測によって減った分」を引いたもの [arxiv-1807.02811#c12](https://arxiv.org/pdf/1807.02811v1#page=5 "is equal to the prior covariance Σ0(x, x) less a term that corresponds to the variance removed by observing f(x1:n).")。

**補足(例:観測が1点だけのとき)**:行列が1×1になり、逆行列はただの逆数になる。$\mu_0(x) = 0$、カーネルを $\Sigma_0(x, x') = e^{-(x - x')^2}$ とし、$x_1 = 0$ で $f(0) = 1$ を観測したとする。$\Sigma_0(0, 0) = 1$ なので

$$
\mu_1(x) = e^{-x^2} \times 1 \times 1 = e^{-x^2}, \qquad
\sigma_1^2(x) = 1 - e^{-x^2} \times 1 \times e^{-x^2} = 1 - e^{-2x^2}
$$

- 観測した点 $x = 0$ では、$\mu_1(0) = 1$(観測値そのもの)、$\sigma_1^2(0) = 0$(不確かさなし)。
- $x = 1$ では、$\mu_1(1) = e^{-1} \approx 0.368$、$\sigma_1^2(1) = 1 - e^{-2} \approx 0.865$。
- 遠く離れた点では、$\mu_1 \to 0$、$\sigma_1^2 \to 1$ と、事前分布に戻る。

観測した点の近くほど「わかっている」、遠くほど「わからない」という状態が、式で表されている。

## 2. 次にどこを評価するか:期待改善量(EI)

事後分布がわかっても、次にどの点を評価すればよいかはすぐには決まらない。
平均 $\mu_n(x)$ が大きい点(良さそうな点)と、分散 $\sigma_n^2(x)$ が大きい点(まだよくわからない点)のどちらも、評価する価値がある。この2つを1つの数にまとめる関数を**獲得関数**という。

### 定義(最大化の場合)

Frazier のチュートリアルは、関数を**最大化**する場合で説明している [arxiv-1807.02811#c13](https://arxiv.org/pdf/1807.02811v1#page=7 "What we can do, however, is to take the expected value of this improvement and choose x to maximize it.")。
これまでの最良の値を $f_n^* = \max_{m \le n} f(x_m)$ とする。点 $x$ を新しく評価したときの「改善量」は、$f(x)$ が $f_n^*$ を超えた分で、超えなければ0である。

$$
[f(x) - f_n^*]^+ \qquad (\text{ただし } a^+ = \max(a, 0))
$$

$f(x)$ は評価するまでわからないので、事後分布での期待値をとる。これが**期待改善量**(Expected Improvement, EI)で、次はこれが最大の点を評価する [arxiv-1807.02811#c13](https://arxiv.org/pdf/1807.02811v1#page=7 "What we can do, however, is to take the expected value of this improvement and choose x to maximize it.") [arxiv-1807.02811#c14](https://arxiv.org/pdf/1807.02811v1#page=7 "The expected improvement can be evaluated in closed form using integration by parts, as described in Jones et al. (1998) or Clark (1961).")。

$$
\mathrm{EI}_n(x) = E_n\big[ [f(x) - f_n^*]^+ \big], \qquad x_{n+1} = \arg\max_x \mathrm{EI}_n(x)
$$

### 閉じた式(最小化の場合)

Snoek らは、関数を**最小化**する場合で、EI を次の形で書いている [arxiv-1206.2944#c12](https://arxiv.org/pdf/1206.2944v2#page=3 "This also has closed form under the Gaussian process:")。$\mu(x)$、$\sigma(x)$ は事後分布の平均と標準偏差、$f(x_{\text{best}})$ はこれまでの最小値である。

$$
a_{\mathrm{EI}}(x) = \sigma(x) \big( \gamma(x)\, \Phi(\gamma(x)) + \phi(\gamma(x)) \big), \qquad
\gamma(x) = \frac{f(x_{\text{best}}) - \mu(x)}{\sigma(x)}
$$

$\Phi$ は標準正規分布の累積分布関数、$\phi$ は標準正規分布の密度関数である [arxiv-1206.2944#c10](https://arxiv.org/pdf/1206.2944v2#page=3 "In the proceeding, we will denote the best current value as xbest = argminxn f(xn), Φ(·) will denote the cumulative distribution function of the standard normal, and φ(·) will denote the standard normal density function.")。
(論文は $\phi(\gamma)$ を $\mathcal{N}(\gamma; 0, 1)$ と書いているが、同じものである。)

**補足(導出)**:数学Ⅲの積分で確かめられる。事後分布で $f(x) = \mu + \sigma u$($u$ は標準正規分布に従う)と書くと、最小化での改善量は

$$
\max\big(f(x_{\text{best}}) - f(x),\ 0\big) = \max\big(\sigma(\gamma - u),\ 0\big)
$$

で、これが正になるのは $u < \gamma$ のときである。したがって

$$
E[\text{改善量}] = \sigma \int_{-\infty}^{\gamma} (\gamma - u)\, \phi(u)\, du
= \sigma \left( \gamma\, \Phi(\gamma) - \int_{-\infty}^{\gamma} u\, \phi(u)\, du \right)
$$

$\phi(u) = \frac{1}{\sqrt{2\pi}} e^{-u^2/2}$ を微分すると $\phi'(u) = -u\, \phi(u)$ なので、$\int_{-\infty}^{\gamma} u\, \phi(u)\, du = \big[ -\phi(u) \big]_{-\infty}^{\gamma} = -\phi(\gamma)$。これを代入すると、上の閉じた式 $\sigma(\gamma \Phi(\gamma) + \phi(\gamma))$ が得られる。

**補足(Frazier の式(8)について)**:Frazier も最大化の場合の閉じた式(8)を示している [arxiv-1807.02811#c14](https://arxiv.org/pdf/1807.02811v1#page=7 "The expected improvement can be evaluated in closed form using integration by parts, as described in Jones et al. (1998) or Clark (1961).")。PDF に印刷された形では $\Phi$ の中が $\Delta_n(x)/\sigma_n(x)$($\Delta_n(x) = \mu_n(x) - f_n^*$)になっている。この記事で計算したところ、印刷された形は $\Delta_n(x) \le 0$ では上の導出と同じ値になるが、$\Delta_n(x) > 0$ では一致しない。$\Phi$ の中を $-|\Delta_n(x)|/\sigma_n(x)$ とすれば、どちらの場合も一致する。以下の説明では、上で導出した形を使う。

### EI の性質

- EI は、平均の良さ($\Delta_n(x)$)についても、不確かさ($\sigma_n(x)$)についても増加する。良さそうな点と、よくわからない点の釣り合いをとっている [arxiv-1807.02811#c15](https://arxiv.org/pdf/1807.02811v1#page=7 "EIn(x) is increasing in both ∆n(x) and σn(x).")。
- すでに評価した点では、事後の標準偏差が0になり、EI は最小値の0になる [arxiv-1807.02811#c16](https://arxiv.org/pdf/1807.02811v1#page=8 "The smallest expected improvement is 0, at points where we have previously evaluated.")。

**補足(例)**:事後平均がちょうどこれまでの最良値と同じ点($\gamma = 0$)では、$\Phi(0) = 0.5$ の項に $\gamma = 0$ が掛かって消え、EI は $\sigma\, \phi(0) = \sigma / \sqrt{2\pi} \approx 0.399\, \sigma$ になる。平均が同じなら、不確かさ $\sigma$ が大きい点ほど EI が大きい。

### ほかの獲得関数

Snoek らは、EI 以外の獲得関数も式で示している(最小化の場合)。

- **改善確率**(PI):改善する確率そのもの $a_{\mathrm{PI}}(x) = \Phi(\gamma(x))$ [arxiv-1206.2944#c11](https://arxiv.org/pdf/1206.2944v2#page=3 "One intuitive strategy is to maximize the probability of improving over the best current value (Kushner, 1964).")。改善の「大きさ」は見ない。
- **信頼下限**(GP-LCB、最大化では上限 UCB):$a_{\mathrm{LCB}}(x) = \mu(x) - \kappa\, \sigma(x)$。$\kappa$ は調整する定数で、活用と探索の釣り合いを決める [arxiv-1206.2944#c13](https://arxiv.org/pdf/1206.2944v2#page=3 "with a tunable κ to balance exploitation against exploration.")。

Snoek らは、EI が PI より振る舞いがよいと示されていることと、GP-UCB と違って自前の調整パラメータが要らないことを、EI を選んだ理由に挙げている [arxiv-1206.2944#c1](https://arxiv.org/pdf/1206.2944v2#page=3 "In this work we will focus on the expected improvement criterion, as it has been shown to be better-behaved than probability of improvement, but unlike the method of GP upper conﬁdence bounds (GP-UCB), it does not require its own tuning parameter.")。

## 3. ベイズ的オンライン変化点検知(BOCPD)

時系列データの性質(平均や分散)がある時点で急に変わることを**変化点**という。
Adams と MacKay の BOCPD は、データが1つ届くたびに「最後の変化点から何ステップ経ったか」の確率分布を更新する [arxiv-0710.3742#c3](https://arxiv.org/pdf/0710.3742v1#page=2 "We can thus generate a recursive message-passing algorithm for the joint distribution over the current run length and the data")。

### ラン長

時刻 $t$ での「最後の変化点からの経過ステップ数」を**ラン長** $r_t$ という。変化点が起きると $r_t = 0$ に戻り、起きなければ1つ増える。
同じ区間(ラン)の中では、データは同じ分布から出ると仮定する [arxiv-0710.3742#c1](https://arxiv.org/pdf/0710.3742v1#page=1 "We further assume that for each partition ρ, the data within it are i.i.d. from some probability distribution")。

### 予測:ラン長について平均する

次のデータの予測は、ラン長のそれぞれの可能性について予測を作り、その確率で重み付けして足す [arxiv-0710.3742#c10](https://arxiv.org/pdf/0710.3742v1#page=2 "We then integrate over the posterior distribution on the current run length to ﬁnd the marginal predictive distribution:")。

$$
P(x_{t+1} \mid x_{1:t}) = \sum_{r_t} P(x_{t+1} \mid r_t, x_t^{(r)})\, P(r_t \mid x_{1:t})
$$

$x_t^{(r)}$ は、ラン長 $r_t$ のランに属するデータ(最後の変化点以降のデータ)である。

### 再帰式

ラン長の事後分布は、同時確率を全体の和で割れば求まる。その同時確率は、1つ前の時刻の値から再帰的に計算できる [arxiv-0710.3742#c11](https://arxiv.org/pdf/0710.3742v1#page=2 "we write the joint distribution over run length and observed data recursively.")。

$$
\begin{aligned}
P(r_t \mid x_{1:t}) &= \frac{P(r_t, x_{1:t})}{P(x_{1:t})} \\
P(r_t, x_{1:t}) &= \sum_{r_{t-1}} \underbrace{P(r_t \mid r_{t-1})}_{\text{変化点の事前分布}}\ \underbrace{P(x_t \mid r_{t-1}, x_t^{(r)})}_{\text{新しいデータの予測確率}}\ P(r_{t-1}, x_{1:t-1})
\end{aligned}
$$

右辺の3つ目は1つ前の時刻で計算済みなので、新しく必要なのは「変化点の事前分布」と「新しいデータの予測確率」の2つだけである [arxiv-0710.3742#c3](https://arxiv.org/pdf/0710.3742v1#page=2 "We can thus generate a recursive message-passing algorithm for the joint distribution over the current run length and the data")。

### 変化点の事前分布とハザード関数

ラン長は「1つ増える」か「0に戻る」かのどちらかしかない。論文は、これがアルゴリズムの計算を効率的にしていると述べている [arxiv-0710.3742#c4](https://arxiv.org/pdf/0710.3742v1#page=2 "is a discrete exponential (geometric) distribution with timescale λ, the process is memoryless and the hazard function is constant")。

$$
P(r_t \mid r_{t-1}) =
\begin{cases}
H(r_{t-1} + 1) & r_t = 0 \\
1 - H(r_{t-1} + 1) & r_t = r_{t-1} + 1 \\
0 & \text{それ以外}
\end{cases}
$$

$H(\tau)$ を**ハザード関数**という。区間の長さ $g$ の分布 $P_{\text{gap}}$ から次のように決まる [arxiv-0710.3742#c12](https://arxiv.org/pdf/0710.3742v1#page=2 "The function H(τ) is the hazard function.")。

$$
H(\tau) = \frac{P_{\text{gap}}(g = \tau)}{\sum_{t=\tau}^{\infty} P_{\text{gap}}(g = t)}
$$

**補足(意味)**:分母は「区間の長さが $\tau$ 以上である確率」、分子は「ちょうど $\tau$ である確率」である。したがって $H(\tau)$ は「ここまで $\tau - 1$ ステップ続いたとき、次で終わる確率」という条件付き確率になる。

区間の長さが幾何分布(数学Bの「初めて成功するまでの回数」の分布)に従う場合、ハザードは定数 $H = 1/\lambda$ になる [arxiv-0710.3742#c4](https://arxiv.org/pdf/0710.3742v1#page=2 "is a discrete exponential (geometric) distribution with timescale λ, the process is memoryless and the hazard function is constant")。

### アルゴリズムの手順

論文の Algorithm 1 は、上の式を次の手順にまとめている [arxiv-0710.3742#c13](https://arxiv.org/pdf/0710.3742v1#page=3 "Algorithm 1: The online changepoint algorithm with")。

1. 新しいデータ $x_t$ について、各ラン長の仮説のもとでの予測確率 $\pi_t^{(r)}$ を計算する。
2. **成長の確率**:$P(r_t = r_{t-1} + 1, x_{1:t}) = P(r_{t-1}, x_{1:t-1})\, \pi_t^{(r)}\, (1 - H)$
3. **変化点の確率**:$P(r_t = 0, x_{1:t}) = \sum_{r_{t-1}} P(r_{t-1}, x_{1:t-1})\, \pi_t^{(r)}\, H$
4. 全部を足して $P(x_{1:t})$ を求め、それで割ってラン長の分布 $P(r_t \mid x_{1:t})$ を得る。

(Algorithm 1 では $H$ の引数が $r_{t-1}$、式(4)では $r_{t-1} + 1$ と書かれている。ハザードが定数の場合は違いが出ない。)

**補足(例)**:ハザードを定数 $H = 0.1$ とし、時刻1のあとラン長の分布が $P(r_1 = 0) = 0.1$、$P(r_1 = 1) = 0.9$ だったとする。
時刻2のデータ $x_2$ が、これまでのデータと比べて外れた値だったとしよう。予測確率は、

- $r_1 = 1$(1つ前のデータと同じラン)の仮説では $\pi = 0.01$(これまでのデータからは出にくい)
- $r_1 = 0$(直前で変化した)の仮説では $\pi = 0.05$(事前分布だけで予測するので、外れ値も出にくくはない)

とする。同時確率は(全体の定数倍を除いて)

| ラン長 $r_2$ | 計算 | 値 | 正規化後 |
|---|---|---|---|
| 2(成長) | $0.9 \times 0.01 \times 0.9$ | $0.0081$ | 約 $0.579$ |
| 1(成長) | $0.1 \times 0.05 \times 0.9$ | $0.0045$ | 約 $0.321$ |
| 0(変化点) | $(0.9 \times 0.01 + 0.1 \times 0.05) \times 0.1$ | $0.0014$ | $0.1$ |

となる。外れ値を見たことで、「直前に変化した」仮説($r_2 = 1$)の確率が、事前の $0.1$ から約 $0.321$ に増えている。

なお、ハザードが定数のとき、$r_t = 0$ の確率は正規化すると常に $H$ になる(手順3の和は、手順4で割る和の $H$ 倍だから)。そのため、この計算例では変化点の証拠は、$r_t = 0$ ではなく、次の時刻以降の「短いラン長」の確率が増えることに現れる。

### 計算量

各時刻で、ラン長の仮説の数だけ計算する。仮説の数は時刻とともに増えるので、1ステップの計算量はそれまでのデータ数に比例する。論文は、確率がしきい値より小さいラン長の仮説を捨てれば、1ステップあたりの平均の計算量を(期待ラン長の程度の)一定に抑えられるが、最悪の場合はデータ数に比例したままだと述べている [arxiv-0710.3742#c7](https://arxiv.org/pdf/0710.3742v1#page=4 "This yields a constant average complexity per iteration on the order of the expected run length E[r], although the worst-case complexity is still linear in the data.")。

## まとめ

| 式 | 何を表すか | 根拠 |
|---|---|---|
| $f(x_{1:k}) \sim \mathrm{Normal}(\mu_0, \Sigma_0)$ | ガウス過程の事前分布 | [arxiv-1807.02811#c10](https://arxiv.org/pdf/1807.02811v1#page=4 "The kernel is chosen so that points xi, xj that are closer in the input space have a large positive correlation, encoding the belief that they should have more similar function values than points that are far apart.") |
| $\mu_n(x)$、$\sigma_n^2(x)$ | 観測後の平均と分散 | [arxiv-1807.02811#c11](https://arxiv.org/pdf/1807.02811v1#page=5 "The posterior mean µn(x) is a weighted average between the prior µ0(x) and an estimate based on the data f(x1:n), with a weight that depends on the kernel.") [arxiv-1807.02811#c12](https://arxiv.org/pdf/1807.02811v1#page=5 "is equal to the prior covariance Σ0(x, x) less a term that corresponds to the variance removed by observing f(x1:n).") |
| $\mathrm{EI}_n(x) = E_n[[f(x) - f_n^*]^+]$ | 改善量の期待値 | [arxiv-1807.02811#c13](https://arxiv.org/pdf/1807.02811v1#page=7 "What we can do, however, is to take the expected value of this improvement and choose x to maximize it.") |
| $\sigma(\gamma \Phi(\gamma) + \phi(\gamma))$ | EI の閉じた式(最小化) | [arxiv-1206.2944#c12](https://arxiv.org/pdf/1206.2944v2#page=3 "This also has closed form under the Gaussian process:") |
| $\Phi(\gamma)$、$\mu - \kappa\sigma$ | 改善確率、信頼下限 | [arxiv-1206.2944#c11](https://arxiv.org/pdf/1206.2944v2#page=3 "One intuitive strategy is to maximize the probability of improving over the best current value (Kushner, 1964).") [arxiv-1206.2944#c13](https://arxiv.org/pdf/1206.2944v2#page=3 "with a tunable κ to balance exploitation against exploration.") |
| $P(r_t, x_{1:t}) = \sum_{r_{t-1}} \cdots$ | ラン長の再帰式 | [arxiv-0710.3742#c11](https://arxiv.org/pdf/0710.3742v1#page=2 "we write the joint distribution over run length and observed data recursively.") |
| $H(\tau)$ | 区間がそこで終わる条件付き確率 | [arxiv-0710.3742#c12](https://arxiv.org/pdf/0710.3742v1#page=2 "The function H(τ) is the hazard function.") |

## 参照カード

- [arxiv-1807.02811](../../papers/arxiv-1807.02811.yaml) Frazier, "A Tutorial on Bayesian Optimization"
- [arxiv-1206.2944](../../papers/arxiv-1206.2944.yaml) Snoek, Larochelle & Adams, "Practical Bayesian Optimization of Machine Learning Algorithms"
- [arxiv-0710.3742](../../papers/arxiv-0710.3742.yaml) Adams & MacKay, "Bayesian Online Changepoint Detection"
