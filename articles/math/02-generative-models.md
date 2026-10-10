---
title: 数式の解説 2 — 生成モデルと表現学習:VAE の ELBO、拡散モデルのノイズ、InfoNCE
kind: math
tags: [variational-autoencoders, diffusion-models, joint-embedding]
depends_on: [arxiv-1312.6114, arxiv-2006.11239, arxiv-1807.03748, arxiv-2002.05709]
written_at: 2026-10-10
written_by: claude-opus-5-5 via Claude Code
---

# 数式の解説 2 — 生成モデルと表現学習:VAE の ELBO、拡散モデルのノイズ、InfoNCE

<!-- generated:stale -->
> ⚠ この記事の執筆日(2026-10-10)以降に作成された関連カードが 1 件あります(未反映。執筆日と同じ日に作成されたカードを含む): `arxiv-1705.08821`
<!-- /generated:stale -->

## この記事の読み方

[オートエンコーダ](../methods/autoencoders.md)、[拡散モデル](../methods/diffusion-models.md)、[対照学習・自己教師あり表現学習](../methods/self-supervised-representation-learning.md) の記事で扱った手法の、中心にある式を解説する。
使う道具(Σ、期待値、条件付き確率、対数、正規分布)は [準備の記事](00-preliminaries.md) で説明している。

- 式は論文から取り、根拠のカード(論文の該当ページへのリンク)を付けている。
- 「**補足**」と書いた計算は、論文には書かれていない、この記事による説明である。

## 1. 準備:2つの分布の「ずれ」を測る KL ダイバージェンス

**補足**:この節は、以降の式を読むための説明で、特定の論文の主張ではない。

2つの確率分布 $q$ と $p$ がどれだけ違うかを測る量に、KL ダイバージェンスがある。

$$
D_{\mathrm{KL}}(q \,\|\, p) = E_{z \sim q}\left[ \log \frac{q(z)}{p(z)} \right]
$$

$E_{z \sim q}[\cdots]$ は「$z$ を分布 $q$ から引いたときの期待値」である。

- $q$ と $p$ が同じなら、どこでも $\log 1 = 0$ なので KL はゼロになる。
- それ以外のときは正になる(負にはならない)。
- $q \,\|\, p$ と $p \,\|\, q$ では値が違う。距離のように対称ではない。

**例**:平均 $\mu$、分散 $\sigma^2$ の正規分布 $q = \mathcal{N}(\mu, \sigma^2)$ と、標準正規分布 $p = \mathcal{N}(0, 1)$ の KL は

$$
D_{\mathrm{KL}}\big(\mathcal{N}(\mu, \sigma^2) \,\|\, \mathcal{N}(0, 1)\big) = \frac{1}{2}\left( \mu^2 + \sigma^2 - 1 - \log \sigma^2 \right)
$$

となる。$\mu = 0$、$\sigma = 1$(つまり $q = p$)を入れると $\frac{1}{2}(0 + 1 - 1 - 0) = 0$ で、確かにゼロになる。

## 2. VAE — 「直接計算できない量」の下界を最大にする

### 何が難しいのか

VAE は、データ $x$ の背後に見えない変数(潜在変数)$z$ があり、$z$ から $x$ が生成される、というモデルである。データの確率 $p_\theta(x)$ を大きくしたいが、それには $z$ のあらゆる値について足し合わせ(積分)が必要で、直接計算できない。

### 下界への分解

Kingma と Welling は、各データについて、対数尤度を次のように分解した [arxiv-1312.6114#c10](https://arxiv.org/pdf/1312.6114v11#page=3 "The ﬁrst RHS term is the KL divergence of the approximate from the true posterior.")。

$$
\log p_\theta(x) = D_{\mathrm{KL}}\big(q_\phi(z \mid x) \,\|\, p_\theta(z \mid x)\big) + \mathcal{L}(\theta, \phi; x)
$$

$q_\phi(z \mid x)$ は、データ $x$ から $z$ の分布を推定するネットワーク(エンコーダ)の出力である。右辺の第1項は KL なので負にならない。したがって、

$$
\log p_\theta(x) \ge \mathcal{L}(\theta, \phi; x)
$$

となり、$\mathcal{L}$ は対数尤度の**下界**(ELBO)になる。直接計算できない $\log p_\theta(x)$ の代わりに、この下界を大きくする。

### 下界の2つの項 — 正則化と再構成

下界は、次のようにも書ける [arxiv-1312.6114#c2](https://arxiv.org/pdf/1312.6114v11#page=4 "The ﬁrst term is (the KL divergence of the approximate posterior from the prior) acts as a regularizer, while the second term is a an expected negative reconstruction error.")。

$$
\mathcal{L}(\theta, \phi; x) = -D_{\mathrm{KL}}\big(q_\phi(z \mid x) \,\|\, p_\theta(z)\big) + E_{q_\phi(z \mid x)}\big[ \log p_\theta(x \mid z) \big]
$$

- 第1項(KL):エンコーダの出す分布を、事前分布 $p_\theta(z)$ に近づける**正則化**。
- 第2項:$z$ からデータ $x$ を復元したときの確率。オートエンコーダの言葉では「再構成の誤差」の符号を変えたもの。

**読み方**:「入力をうまく復元せよ」(第2項)と「潜在変数の分布を決まった形に保て」(第1項)の綱引きになっている。[オートエンコーダの記事](../methods/autoencoders.md) で扱った事後崩壊は、第1項を小さくするために潜在変数が何の情報も持たなくなる現象だった。

### 再パラメータ化 — 乱数を「外に出す」

第2項の期待値は、$z$ を $q_\phi$ から引いて平均をとるサンプリングで近似する。しかし、そのままでは、引いた $z$ をエンコーダのパラメータ $\phi$ で微分できない。

そこで、正規分布の場合は次のように書き直す [arxiv-1312.6114#c11](https://arxiv.org/pdf/1312.6114v11#page=5 "Take, for example, the univariate Gaussian case: let z ∼p(z/x) = N(µ, σ2).") [arxiv-1312.6114#c1](https://arxiv.org/pdf/1312.6114v11#page=1 "First, we show that a reparameterization of the variational lower bound yields a lower bound estimator that can be straightforwardly optimized using standard stochastic gradient methods.")。

$$
z = \mu + \sigma \, \epsilon, \qquad \epsilon \sim \mathcal{N}(0, 1)
$$

**読み方**:$z$ を直接ランダムに引く代わりに、パラメータに依存しない乱数 $\epsilon$ を引き、それを $\mu$ と $\sigma$ で変換する。こうすると、$z$ は $\mu$ と $\sigma$ の普通の関数になり、微分できる。乱数を「外に出した」と見ることができる。

**補足(確かめ)**:$\epsilon$ の平均は0、分散は1なので、$z = \mu + \sigma\epsilon$ の平均は $\mu$、分散は $\sigma^2$ になる(数学Bの「$aX + b$ の期待値と分散」)。つまり $z$ は確かに $\mathcal{N}(\mu, \sigma^2)$ に従う。

### KL の項は式で計算できる

事前分布を標準正規分布、エンコーダの出力を各次元が独立な正規分布(平均 $\mu_j$、標準偏差 $\sigma_j$)にすると、KL の項はサンプリングなしで計算できる。下界は次の形になる [arxiv-1312.6114#c12](https://arxiv.org/pdf/1312.6114v11#page=5 "where the KL divergence can be computed and differentiated without estimation")。

$$
\mathcal{L} \approx \frac{1}{2} \sum_{j=1}^{J} \left( 1 + \log \sigma_j^2 - \mu_j^2 - \sigma_j^2 \right) + \frac{1}{L} \sum_{l=1}^{L} \log p_\theta(x \mid z^{(l)}), \qquad z^{(l)} = \mu + \sigma \odot \epsilon^{(l)}
$$

$J$ は潜在変数の次元、$L$ はサンプルの数、$\odot$ は成分ごとの積である。

**補足(確かめ)**:第1節の例の KL $\frac{1}{2}(\mu^2 + \sigma^2 - 1 - \log \sigma^2)$ の符号を変え、次元ごとに足したものが第1項になっている。

## 3. 拡散モデル — ノイズを足す過程と、ノイズを当てる学習

### ノイズを少しずつ足す

DDPM では、データ $x_0$ に少しずつノイズを足して $x_1, x_2, \ldots, x_T$ を作る。1段の足し方は

$$
q(x_t \mid x_{t-1}) = \mathcal{N}\big(x_t;\, \sqrt{1 - \beta_t}\, x_{t-1},\, \beta_t I\big)
$$

である。$\beta_t$ は各段で足すノイズの量で、学習しない定数に固定する [arxiv-2006.11239#c2](https://arxiv.org/pdf/2006.11239v2#page=3 "Thus, in our implementation, the approximate posterior q has no learnable parameters, so LT is a constant during training and can be ignored.")。

### 何段目でも一度に計算できる

$\alpha_t = 1 - \beta_t$、$\bar{\alpha}_t = \prod_{s=1}^{t} \alpha_s$ とおくと、$t$ 段目の分布は、途中を飛ばして閉じた形で書ける [arxiv-2006.11239#c2](https://arxiv.org/pdf/2006.11239v2#page=3 "Thus, in our implementation, the approximate posterior q has no learnable parameters, so LT is a constant during training and can be ignored.")。

$$
q(x_t \mid x_0) = \mathcal{N}\big(x_t;\, \sqrt{\bar{\alpha}_t}\, x_0,\, (1 - \bar{\alpha}_t) I\big)
$$

再パラメータ化(第2節)と同じ書き方をすると、

$$
x_t = \sqrt{\bar{\alpha}_t}\, x_0 + \sqrt{1 - \bar{\alpha}_t}\, \epsilon, \qquad \epsilon \sim \mathcal{N}(0, I)
$$

である。

**読み方**:$x_t$ は「元のデータを $\sqrt{\bar{\alpha}_t}$ 倍に縮めたもの」と「ノイズを $\sqrt{1 - \bar{\alpha}_t}$ 倍したもの」の和である。$t$ が大きくなると $\bar{\alpha}_t$ は0に近づき、$x_t$ はほぼノイズだけになる。

**補足(なぜ平方根なのか)**:$x_0$ の分散が1で $\epsilon$ と独立なら、$x_t$ の分散は $\bar{\alpha}_t \cdot 1 + (1 - \bar{\alpha}_t) \cdot 1 = 1$ になる(数学Bの「独立な確率変数の和の分散」と「$aX$ の分散は $a^2$ 倍」)。平方根を付けておくと、ノイズを足しても全体の大きさ(分散)が保たれる。

**補足(数値の例)**:説明のために $\beta_t$ を一定の $0.02$ とすると、$\bar{\alpha}_t = 0.98^t$ である。$t = 100$ なら $0.98^{100} \approx 0.13$ で、元のデータの成分は $\sqrt{0.13} \approx 0.36$ 倍まで縮み、ノイズの成分は $\sqrt{0.87} \approx 0.93$ 倍になる。(DDPM の実際の $\beta_t$ は一定ではなく、段ごとに増やしている [arxiv-2006.11239#c7](https://arxiv.org/pdf/2006.11239v2#page=5 "We set T = 1000 for all experiments so that the number of neural network evaluations needed during sampling matches previous work [53, 55].")。)

### 学習:足したノイズを当てる

逆向き(ノイズからデータへ)の過程を学習するために、DDPM は、$x_t$ から**足したノイズ $\epsilon$ を予測する**ネットワーク $\epsilon_\theta(x_t, t)$ を使う [arxiv-2006.11239#c3](https://arxiv.org/pdf/2006.11239v2#page=4 "We have shown that the ϵ-prediction parameterization both resembles Langevin dynamics and simpliﬁes the diffusion model’s variational bound to an objective that resembles denoising score matching.")。学習は、次の量を小さくするように進める(論文のアルゴリズム1)。

$$
\big\| \epsilon - \epsilon_\theta\big( \sqrt{\bar{\alpha}_t}\, x_0 + \sqrt{1 - \bar{\alpha}_t}\, \epsilon,\; t \big) \big\|^2
$$

手順は次のとおりである。

1. データ $x_0$ を1つ選ぶ
2. 段 $t$ をランダムに選ぶ
3. ノイズ $\epsilon$ を引き、上の式で $x_t$ を作る
4. ネットワークが当てたノイズと本当のノイズの差の2乗を小さくする

この「各項の重みを落とした」簡略化した損失は、ノイズの小さい段を軽く扱うことになり、サンプルの質が最も良かった [arxiv-2006.11239#c4](https://arxiv.org/pdf/2006.11239v2#page=5 "Since our simpliﬁed objective (14) discards the weighting in Eq. (12), it is a weighted variational bound that emphasizes different aspects of reconstruction compared to the standard variational bound [18, 22].")。

**読み方**:「ノイズまみれの画像を見て、どんなノイズが足されたかを当てる」練習である。当てたノイズを引けば、少しだけきれいな画像に戻せる。これを $T$ 段繰り返すと、純粋なノイズから画像が生成される。

## 4. InfoNCE — 「正解の組」を当てる分類として学ぶ

### CPC の損失

CPC は、文脈 $c_t$ と、それに対応する正しいサンプル1つ(正例)と、無関係な $N - 1$ 個のサンプル(負例)を並べ、正例を当てる分類の損失を使う [arxiv-1807.03748#c2](https://arxiv.org/pdf/1807.03748v2#page=3 "Both the encoder and autoregressive model are trained to jointly optimize a loss based on NCE, which we will call InfoNCE.")。

$$
\mathcal{L}_N = -E\left[ \log \frac{f_k(x_{t+k}, c_t)}{\sum_{x_j \in X} f_k(x_j, c_t)} \right]
$$

$f_k$ は「$x$ と $c$ がどれだけ合っているか」を表す正の値の得点である。

**読み方**:分数は「全候補の得点の合計のうち、正例の得点が占める割合」で、モデルが「これが正例だ」とつける確率にあたる。その対数の符号を変えたものを小さくするのは、正例を高い確率で選べるようにすることである。

### 相互情報量の下界

この損失は、相互情報量(2つの変数がどれだけ情報を共有しているか)の下界を与える [arxiv-1807.03748#c4](https://arxiv.org/pdf/1807.03748v2#page=4 "Also observe that minimizing the InfoNCE loss LN maximizes a lower bound on mutual information.")。

$$
I(x_{t+k}, c_t) \ge \log N - \mathcal{L}_N
$$

**補足(確かめ)**:モデルが正例と負例を区別できず、すべての候補に同じ得点をつけると、分数は $\frac{1}{N}$ になり、$\mathcal{L}_N = -\log \frac{1}{N} = \log N$ である。このとき右辺は $\log N - \log N = 0$ で、下界は何も言わない。逆に、正例を完全に当てられると $\mathcal{L}_N \to 0$ で、右辺は $\log N$ に近づく。**負例の数 $N$ が下界の上限を決める**ことがわかる。論文も、この下界は $N$ が大きいほど厳しくなると述べている [arxiv-1807.03748#c4](https://arxiv.org/pdf/1807.03748v2#page=4 "Also observe that minimizing the InfoNCE loss LN maximizes a lower bound on mutual information.")。

ただし、成功が相互情報量の最大化で説明できるかには批判がある。[対照学習・自己教師あり表現学習の記事](../methods/self-supervised-representation-learning.md) を参照。

### SimCLR の損失(NT-Xent)

SimCLR は、同じ画像から作った2つの見え方を正例の組とし、同じミニバッチの他の画像を負例にする [arxiv-2002.05709#c1](https://arxiv.org/pdf/2002.05709v3#page=2 "We do not sample negative examples explicitly.")。2つのベクトル $\boldsymbol{u}, \boldsymbol{v}$ の類似度には、コサイン類似度を使う。

$$
\mathrm{sim}(\boldsymbol{u}, \boldsymbol{v}) = \frac{\boldsymbol{u} \cdot \boldsymbol{v}}{\|\boldsymbol{u}\| \|\boldsymbol{v}\|}
$$

これは、2つのベクトルのなす角を $\theta$ としたときの $\cos\theta$ である(数学Cの内積の定義 $\boldsymbol{u} \cdot \boldsymbol{v} = \|\boldsymbol{u}\|\|\boldsymbol{v}\|\cos\theta$ から)。正例の組 $(i, j)$ の損失は

$$
\ell_{i,j} = -\log \frac{\exp(\mathrm{sim}(\boldsymbol{z}_i, \boldsymbol{z}_j)/\tau)}{\sum_{k=1}^{2N} \mathbb{1}[k \ne i]\, \exp(\mathrm{sim}(\boldsymbol{z}_i, \boldsymbol{z}_k)/\tau)}
$$

である。$\mathbb{1}[k \ne i]$ は「$k \ne i$ なら1、そうでなければ0」、$\tau$ は温度と呼ばれる正の定数である。

**読み方**:CPC の $f_k$ を $\exp(\text{類似度}/\tau)$ にした形である。$\tau$ を小さくすると、類似度の小さな差が $\exp$ で大きく広がり、正例と負例の区別がより厳しく評価される(この解釈は本記事の補足)。

## まとめ

| 式 | 何を表すか | 根拠 |
|---|---|---|
| $\log p_\theta(x) = D_{\mathrm{KL}}(\cdots) + \mathcal{L}$ | 対数尤度は ELBO 以上 | [arxiv-1312.6114#c10](https://arxiv.org/pdf/1312.6114v11#page=3 "The ﬁrst RHS term is the KL divergence of the approximate from the true posterior.") |
| $\mathcal{L} = -D_{\mathrm{KL}}(q \,\Vert\, p(z)) + E[\log p(x \mid z)]$ | 正則化と再構成 | [arxiv-1312.6114#c2](https://arxiv.org/pdf/1312.6114v11#page=4 "The ﬁrst term is (the KL divergence of the approximate posterior from the prior) acts as a regularizer, while the second term is a an expected negative reconstruction error.") |
| $z = \mu + \sigma\epsilon$ | 再パラメータ化 | [arxiv-1312.6114#c11](https://arxiv.org/pdf/1312.6114v11#page=5 "Take, for example, the univariate Gaussian case: let z ∼p(z/x) = N(µ, σ2).") |
| $\frac{1}{2}\sum_j (1 + \log\sigma_j^2 - \mu_j^2 - \sigma_j^2)$ | 正規分布どうしの KL を式で計算 | [arxiv-1312.6114#c12](https://arxiv.org/pdf/1312.6114v11#page=5 "where the KL divergence can be computed and differentiated without estimation") |
| $x_t = \sqrt{\bar{\alpha}_t}\, x_0 + \sqrt{1 - \bar{\alpha}_t}\, \epsilon$ | 何段目のノイズも一度に足せる | [arxiv-2006.11239#c2](https://arxiv.org/pdf/2006.11239v2#page=3 "Thus, in our implementation, the approximate posterior q has no learnable parameters, so LT is a constant during training and can be ignored.") |
| $\Vert\epsilon - \epsilon_\theta(x_t, t)\Vert^2$ | 足したノイズを当てる学習 | [arxiv-2006.11239#c3](https://arxiv.org/pdf/2006.11239v2#page=4 "We have shown that the ϵ-prediction parameterization both resembles Langevin dynamics and simpliﬁes the diffusion model’s variational bound to an objective that resembles denoising score matching.") |
| $\mathcal{L}_N$、$I \ge \log N - \mathcal{L}_N$ | 正例を当てる分類と相互情報量の下界 | [arxiv-1807.03748#c2](https://arxiv.org/pdf/1807.03748v2#page=3 "Both the encoder and autoregressive model are trained to jointly optimize a loss based on NCE, which we will call InfoNCE.") [arxiv-1807.03748#c4](https://arxiv.org/pdf/1807.03748v2#page=4 "Also observe that minimizing the InfoNCE loss LN maximizes a lower bound on mutual information.") |
| $\ell_{i,j}$(NT-Xent) | コサイン類似度と温度を使った対照損失 | [arxiv-2002.05709#c1](https://arxiv.org/pdf/2002.05709v3#page=2 "We do not sample negative examples explicitly.") |

## 参照カード

- [arxiv-1312.6114](../../papers/arxiv-1312.6114.yaml) Kingma & Welling, "Auto-Encoding Variational Bayes"
- [arxiv-2006.11239](../../papers/arxiv-2006.11239.yaml) Ho, Jain & Abbeel, "Denoising Diffusion Probabilistic Models"
- [arxiv-1807.03748](../../papers/arxiv-1807.03748.yaml) van den Oord, Li & Vinyals, "Representation Learning with Contrastive Predictive Coding"
- [arxiv-2002.05709](../../papers/arxiv-2002.05709.yaml) Chen et al., "A Simple Framework for Contrastive Learning of Visual Representations"
