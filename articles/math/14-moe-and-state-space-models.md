---
title: 数式の解説 14 — 混合エキスパートと状態空間モデル:ゲートと top-k、負荷の補助損失と z-loss、離散化と畳み込み、選択、線形注意
kind: math
tags: [mixture-of-experts, state-space-models, efficient-attention]
depends_on: [arxiv-1701.06538, arxiv-2401.04088, arxiv-2101.03961, arxiv-2006.16668, arxiv-2202.08906, arxiv-2202.09368, arxiv-2111.00396, arxiv-2312.00752, arxiv-2405.21060, arxiv-2006.16236, arxiv-2009.14794, arxiv-2305.13048]
written_at: 2026-10-11
written_by: claude-opus-5-5 via Claude Code
---

# 数式の解説 14 — 混合エキスパートと状態空間モデル:ゲートと top-k、負荷の補助損失と z-loss、離散化と畳み込み、選択、線形注意

<!-- generated:stale -->
> 未反映のカードはありません。
<!-- /generated:stale -->

## この記事の読み方

[混合エキスパートと状態空間モデル](../methods/moe-and-state-space-models.md) の記事で扱った手法の式を解説する。

使う道具(Σ、指数関数と対数、行列とベクトル、微分方程式の考え方)は [準備の記事](00-preliminaries.md)、ソフトマックスは [数式の解説 3](03-uncertainty-and-calibration.md)、注意は [数式の解説 10](10-distillation-and-gnn.md) の3節で説明している。

- 式は論文から取り、根拠のカード(論文の該当ページへのリンク)を付けている。
- 「**補足**」と書いた計算は、論文には書かれていない、この記事による説明である。

## 1. 混合エキスパートのゲート

### 出力の形

MoE 層の出力は、エキスパート $E_i$ の出力を、ゲート $G(x)$ で重み付けして足したものである [arxiv-1701.06538#c1](https://arxiv.org/pdf/1701.06538v1#page=3 "We save computation based on the sparsity of the output of G(x).")。

$$
y = \sum_{i=1}^{n} G(x)_i \, E_i(x)
$$

### ノイズ付きの top-k

Shazeer らのゲートは、ロジット $x W_g$ に、学習する大きさ($\mathrm{Softplus}(x W_{\text{noise}})$)のガウスノイズを加え、上位 $k$ 個だけを残して(残りを $-\infty$ にして)ソフトマックスをとる [arxiv-1701.06538#c2](https://arxiv.org/pdf/1701.06538v1#page=4 "While this form of sparsity creates some theoretically scary discontinuities in the output of gating function, we have not yet observed this to be a problem in practice.")。

$$
G(x) = \mathrm{Softmax}\Big( \mathrm{KeepTopK}\big( H(x),\ k \big) \Big), \qquad
H(x)_i = (x W_g)_i + \text{ノイズ}_i \cdot \mathrm{Softplus}\big( (x W_{\text{noise}})_i \big)
$$

Mixtral も、ノイズなしで同じ形 $G(x) = \mathrm{Softmax}(\mathrm{TopK}(x W_g))$ を使う [arxiv-2401.04088#c2](https://arxiv.org/pdf/2401.04088v1#page=2 "There are multiple alternative ways of implementing G(x) [6, 15, 35], but a simple and performant one is implemented by taking the softmax over the Top-K logits of a linear layer [28].")。

**補足(例)**:4つのエキスパートのロジットが $(2,\ 1,\ 0.5,\ -1)$ で $k = 2$ なら、上位2つ $(2,\ 1)$ だけでソフトマックスをとり、$e^2 / (e^2 + e^1) \approx 0.731$、$e^1/(e^2 + e^1) \approx 0.269$ になる。残りの2つのゲートは0なので、そのエキスパートは計算しない。

$-\infty$ にした成分は $e^{-\infty} = 0$ になるので、ソフトマックスの後もちょうど0になる。論文は、この切り捨てがゲートの出力に不連続を生むことを「理論的には恐ろしい」と認めつつ、実際には問題になっていないと述べている [arxiv-1701.06538#c2](https://arxiv.org/pdf/1701.06538v1#page=4 "While this form of sparsity creates some theoretically scary discontinuities in the output of gating function, we have not yet observed this to be a problem in practice.")。

## 2. 負荷をそろえる補助損失

### 変動係数(Shazeer ら)

Shazeer らは、バッチ全体での各エキスパートのゲートの値の合計(重要度)を求め、その**変動係数**(標準偏差 ÷ 平均)の2乗に重みを掛けて損失に加えた [arxiv-1701.06538#c4](https://arxiv.org/pdf/1701.06538v1#page=5 "This imbalance is self-reinforcing, as the favored experts are trained more rapidly and thus are selected even more by the gating network.")。重要度がそろうと変動係数は0になる。ただし、重要度がそろっても処理する例の数がそろうとは限らないので、例の数(負荷)についても同様の損失を加えた [arxiv-1701.06538#c5](https://arxiv.org/pdf/1701.06538v1#page=13 "Instead, we deﬁne a smooth estimator Load(X) of the number of examples assigned to each expert for a batch X of inputs.")。

### 割合の内積(Switch Transformer)

Switch Transformer は、これを1つの損失にまとめた [arxiv-2101.03961#c8](https://arxiv.org/pdf/2101.03961v3#page=7 "Given N experts indexed by i = 1 to N and a batch B with T tokens, the auxiliary loss is computed as the scaled dot-product between vectors f and P,")。

$$
\text{loss} = \alpha \cdot N \cdot \sum_{i=1}^{N} f_i \cdot P_i, \qquad
f_i = \frac{1}{T} \sum_{x \in B} \mathbf{1}\{\arg\max p(x) = i\}, \qquad
P_i = \frac{1}{T} \sum_{x \in B} p_i(x)
$$

- $f_i$ は、エキスパート $i$ に実際に送られたトークンの割合。
- $P_i$ は、エキスパート $i$ に割り当てられたゲートの確率の平均。
- この損失は、送り先が一様なとき最小になる。$f$ は微分できないが $P$ は微分できるので、勾配は $P$ を通じて流れる [arxiv-2101.03961#c8](https://arxiv.org/pdf/2101.03961v3#page=7 "Given N experts indexed by i = 1 to N and a batch B with T tokens, the auxiliary loss is computed as the scaled dot-product between vectors f and P,")。

**補足(例)**:エキスパートが2つの場合、一様なら $f = P = (0.5,\ 0.5)$ で、損失は $\alpha \cdot 2 \cdot (0.25 + 0.25) = \alpha$。偏って $f = (0.9,\ 0.1)$、$P = (0.8,\ 0.2)$ なら $\alpha \cdot 2 \cdot (0.72 + 0.02) = 1.48\alpha$ で、損失が大きくなる。
$N$ を掛けるのは、一様なときの値をエキスパートの数によらず $\alpha$ にそろえるためである(一様なら $\sum_i f_i P_i = N \cdot (1/N)^2 = 1/N$)。

GShard の補助損失も、微分できない割合 $c_e / S$ を、ゲートの平均値 $m_e$ と組み合わせた同じ考え方である [arxiv-2006.16668#c3](https://arxiv.org/pdf/2006.16668v1#page=6 "But because ce is derived from top-2 operation and is not differentiable, we use the mean gates per expert me as a differentiable approximation and replace (ce/S)2 with me(ce/S), which can now be optimized with gradient descent.")。

### router z-loss

ST-MoE は、ゲートのロジット $x_{ij}$($i$ 番目のトークン、$j$ 番目のエキスパート)が大きくなりすぎないように罰する [arxiv-2202.08906#c1](https://arxiv.org/pdf/2202.08906v2#page=7 "This penalizes large logits into the gating network and Section 3.4 contains a more detailed explanation of why the z-loss before the router is useful.")。

$$
L_z(x) = \frac{1}{B} \sum_{i=1}^{B} \left( \log \sum_{j=1}^{N} e^{x_{ij}} \right)^2
$$

**補足(例)**:ロジットが $(10,\ 9)$ なら $\log(e^{10} + e^{9}) \approx 10.31$ で、2乗は約 $106.4$。ロジットが $(1,\ 0)$ なら $\log(e + 1) \approx 1.31$ で、2乗は約 $1.72$。2つの場合のソフトマックスの確率は同じ(どちらも約 $(0.731,\ 0.269)$)なのに、ロジットの大きい方が強く罰される。
ロジットが大きいと、指数関数の計算で丸め誤差が大きくなる。著者らは、それが不安定さの一因だと推測している [arxiv-2202.08906#c3](https://arxiv.org/pdf/2202.08906v2#page=9 "Finally, we conjecture that the higher stability we observed for decoder-only models (not shown here) was because they had fewer exponential functions.")。

### エキスパートがトークンを選ぶ

Zhou らの方式では、各エキスパートが上位 $k$ 個のトークンを選び、$k$ を次のように決める [arxiv-2202.09368#c1](https://arxiv.org/pdf/2202.09368v2#page=3 "Despite its simplicity, expert choice achieves perfect load balancing by design.")。

$$
k = \frac{n \cdot c}{e}
$$

$n$ はバッチのトークン数、$c$ は容量係数(1トークンあたり平均いくつのエキスパートを使うか)、$e$ はエキスパートの数である。

**補足(例)**:$n = 1024$、$c = 2$、$e = 64$ なら $k = 32$。すべてのエキスパートがちょうど32個のトークンを処理するので、負荷は設計上そろう。代わりに、あるトークンは多くのエキスパートに、別のトークンは1つにも選ばれない、ということが起こりうる。

## 3. 状態空間モデル:離散化と畳み込み

### 連続時間のモデルを離散にする

状態空間モデル $x'(t) = A x(t) + B u(t)$、$y(t) = C x(t)$ を、刻み幅 $\Delta$ で離散化すると、再帰の式になる。S4 は双一次変換を使う [arxiv-2111.00396#c1](https://arxiv.org/pdf/2111.00396v3#page=4 "The recurrent SSM (3) is not practical for training on modern hardware due to its sequentiality.")。

$$
\bar{A} = \left(I - \frac{\Delta}{2} A\right)^{-1} \left(I + \frac{\Delta}{2} A\right), \qquad
\bar{B} = \left(I - \frac{\Delta}{2} A\right)^{-1} \Delta B
$$

$$
x_k = \bar{A} x_{k-1} + \bar{B} u_k, \qquad y_k = C x_k
$$

**補足(例:1次元)**:$A = -1$、$B = 1$、$C = 1$、$\Delta = 0.1$ とすると、$\bar{A} = \dfrac{1 - 0.05}{1 + 0.05} \approx 0.9048$、$\bar{B} = \dfrac{0.1}{1.05} \approx 0.0952$。
状態は毎ステップ約 $0.9048$ 倍に減衰しながら、新しい入力を約 $0.0952$ の重みで取り込む。$\bar{A}$ は、連続時間の正確な減衰 $e^{-0.1} \approx 0.9048$ とほぼ一致している。

### 畳み込みとして計算する

$x_0 = 0$ から再帰を展開すると、$y_k = C\bar{B} u_k + C\bar{A}\bar{B} u_{k-1} + C\bar{A}^2\bar{B} u_{k-2} + \cdots$ となる。これは、次の**畳み込みの核** $\bar{K}$ と入力の畳み込みである [arxiv-2111.00396#c1](https://arxiv.org/pdf/2111.00396v3#page=4 "The recurrent SSM (3) is not practical for training on modern hardware due to its sequentiality.")。

$$
\bar{K} = \big( C\bar{B},\ C\bar{A}\bar{B},\ \ldots,\ C\bar{A}^{L-1}\bar{B} \big), \qquad y = \bar{K} * u
$$

**補足(例)**:上の1次元の例では $\bar{K} \approx (0.0952,\ 0.0862,\ 0.0780,\ \ldots)$ で、過去の入力ほど小さい重みが付く。
学習時は、核 $\bar{K}$ を一度計算すれば、高速フーリエ変換で系列全体を並列に処理できる。推論時は、再帰の式で1ステップずつ状態を更新すればよい。核を効率よく計算することが S4 の技術的な中心である [arxiv-2111.00396#c1](https://arxiv.org/pdf/2111.00396v3#page=4 "The recurrent SSM (3) is not practical for training on modern hardware due to its sequentiality.")。

### 選択:パラメータを入力に応じて変える(Mamba)

Mamba は、$\Delta$、$B$、$C$ を入力 $x$ の関数にする [arxiv-2312.00752#c8](https://arxiv.org/pdf/2312.00752v2#page=5 "In particular, we highlight that these parameters now have a length dimension 𝐿, meaning that the model has changed from time-invariant to time-varying.")。

$$
B = s_B(x) = \mathrm{Linear}_N(x), \quad C = s_C(x) = \mathrm{Linear}_N(x), \quad \Delta = \tau_\Delta\big(\cdots + s_\Delta(x)\big), \ \tau_\Delta = \mathrm{softplus}
$$

これで、パラメータが時刻ごとに変わる(時間不変でなくなる)ため、上の畳み込みの形は使えなくなる [arxiv-2312.00752#c8](https://arxiv.org/pdf/2312.00752v2#page=5 "In particular, we highlight that these parameters now have a length dimension 𝐿, meaning that the model has changed from time-invariant to time-varying.")。代わりに、ハードウェアを意識した再帰の並列計算を用いる [arxiv-2312.00752#c1](https://arxiv.org/pdf/2312.00752v2#page=1 "First, simply letting the SSM parameters be functions of the input addresses their weakness with discrete modalities, allowing the model to selectively propagate or forget information along the sequence length dimension depending on the current token.")。

**補足(刻み幅 $\Delta$ の役割)**:1次元で $A = -1$ のとき、連続時間の正確な解では1ステップの減衰は $e^{\Delta A} = e^{-\Delta}$ である。$\Delta = 0.01$ なら約 $0.99$ で、状態をほぼそのまま保つ(今の入力をほぼ無視する)。$\Delta = 5$ なら約 $0.0067$ で、状態をほぼ捨てて今の入力に置き換える。$\Delta$ を入力ごとに変えられると、「この入力は覚えておく」「この入力で前の文脈をリセットする」を選べる。

### Mamba-2:A をスカラーにする

Mamba-2 は、$A$ を「スカラー × 単位行列」に単純化し、計算の大部分を行列積で行えるようにした [arxiv-2405.21060#c1](https://arxiv.org/pdf/2405.21060v1#page=5 "Compared to the original selective SSM, these changes can be viewed as slightly decreasing the expressive power in return for significant training efficiency improvements.")。

## 4. 線形注意

### 結合法則で計算の順番を変える

ソフトマックスの注意を、特徴写像 $\phi$ を使った類似度に置き換えると、出力は次のように書ける [arxiv-2006.16236#c1](https://arxiv.org/pdf/2006.16236v3#page=1 "we express the self-attention as a linear dot-product of kernel feature maps and make use of the associativity property of matrix products to reduce the complexity")。

$$
V'_i = \frac{\phi(Q_i)^\top \sum_{j} \phi(K_j) V_j^\top}{\phi(Q_i)^\top \sum_{j} \phi(K_j)}
$$

$\sum_j \phi(K_j) V_j^\top$ は $i$ によらないので、一度計算すればすべての $i$ で使い回せる。これが $N^2$ を $N$ に下げる仕組みである [arxiv-2006.16236#c1](https://arxiv.org/pdf/2006.16236v3#page=1 "we express the self-attention as a linear dot-product of kernel feature maps and make use of the associativity property of matrix products to reduce the complexity")。論文の実験では $\phi(x) = \mathrm{elu}(x) + 1$ を使い、これはソフトマックスの近似ではない [arxiv-2006.16236#c3](https://arxiv.org/pdf/2006.16236v3#page=4 "to avoid setting the gradients to 0 when x is negative")。

**補足(計算量の例)**:系列長 $N = 4096$、次元 $d = 64$ とする。ソフトマックスの注意は $N \times N$ の行列を作るので、掛け算はおよそ $N^2 d \approx 1.07 \times 10^9$ 回。線形注意で $\phi(K)^\top V$ を先に計算すると、およそ $N d^2 \approx 1.68 \times 10^7$ 回で、$N/d = 64$ 倍少ない。

### RNN としての線形注意

因果的なマスク(未来を見ない)を付けると、和を前から順に足していけばよいので、2つの状態を持つ RNN として書ける [arxiv-2006.16236#c5](https://arxiv.org/pdf/2006.16236v3#page=5 "any transformer layer with causal masking can be written as a model that, given an input, modiﬁes an internal state and then predicts an output, namely a Recurrent Neural Network (RNN).")。

$$
s_i = s_{i-1} + \phi(x_i W_K)(x_i W_V)^\top, \qquad z_i = z_{i-1} + \phi(x_i W_K)
$$

状態の大きさは系列の長さによらないので、生成の各ステップの計算は一定である。一方、過去のすべての情報をこの固定の大きさの状態に押し込むことになる。

### Performer:ソフトマックスの正のランダム特徴

Performer は、ソフトマックスのカーネルを、次の期待値として書けることを使う [arxiv-2009.14794#c4](https://arxiv.org/pdf/2009.14794v4#page=4 "Consequently, softmax-kernel admits a positive random feature map unbiased approximation with")。

$$
\exp(x^\top y) = E_{w \sim \mathcal{N}(0, I)}\left[ \exp\!\left(w^\top x - \frac{\Vert x \Vert^2}{2}\right) \exp\!\left(w^\top y - \frac{\Vert y \Vert^2}{2}\right) \right]
$$

ランダムな $w$ をいくつか引いて平均すれば、ソフトマックスの注意を偏りなく、しかも正の値で近似でき、上の線形注意の形で計算できる [arxiv-2009.14794#c4](https://arxiv.org/pdf/2009.14794v4#page=4 "Consequently, softmax-kernel admits a positive random feature map unbiased approximation with")。

### RWKV の時間減衰

RWKV は、チャネルごとの減衰率 $w$ と、現在のトークンへのボーナス $u$ を持つ重み付き平均を使う [arxiv-2305.13048#c2](https://arxiv.org/pdf/2305.13048v2#page=4 "To circumvent any potential degradation of W, we introduce a vector U that separately attends to the current token.")。

$$
wkv_t = \frac{\sum_{i<t} e^{-(t-1-i) w + k_i} v_i + e^{u + k_t} v_t}{\sum_{i<t} e^{-(t-1-i) w + k_i} + e^{u + k_t}}
$$

**補足(読み方)**:過去のトークン $i$ の値 $v_i$ に、$e^{k_i}$(どれだけ重要か)と $e^{-(t-1-i)w}$(どれだけ前か)を掛けて平均している。古いトークンほど指数的に重みが小さくなる。分子と分母は、それぞれ前の時刻の値に $e^{-w}$ を掛けて新しい項を足すことで更新できるので、RNN として計算できる。

## まとめ

| 式 | 何を表すか | 根拠 |
|---|---|---|
| $y = \sum_i G(x)_i E_i(x)$ | MoE 層の出力 | [arxiv-1701.06538#c1](https://arxiv.org/pdf/1701.06538v1#page=3 "We save computation based on the sparsity of the output of G(x).") |
| $\mathrm{Softmax}(\mathrm{KeepTopK}(H(x), k))$ | ノイズ付きの top-k ゲート | [arxiv-1701.06538#c2](https://arxiv.org/pdf/1701.06538v1#page=4 "While this form of sparsity creates some theoretically scary discontinuities in the output of gating function, we have not yet observed this to be a problem in practice.") |
| $\alpha N \sum_i f_i P_i$ | 負荷をそろえる補助損失 | [arxiv-2101.03961#c8](https://arxiv.org/pdf/2101.03961v3#page=7 "Given N experts indexed by i = 1 to N and a batch B with T tokens, the auxiliary loss is computed as the scaled dot-product between vectors f and P,") |
| $\frac{1}{B}\sum_i (\log \sum_j e^{x_{ij}})^2$ | router z-loss | [arxiv-2202.08906#c1](https://arxiv.org/pdf/2202.08906v2#page=7 "This penalizes large logits into the gating network and Section 3.4 contains a more detailed explanation of why the z-loss before the router is useful.") |
| $k = nc/e$ | エキスパートがトークンを選ぶ数 | [arxiv-2202.09368#c1](https://arxiv.org/pdf/2202.09368v2#page=3 "Despite its simplicity, expert choice achieves perfect load balancing by design.") |
| $\bar{A} = (I - \frac{\Delta}{2}A)^{-1}(I + \frac{\Delta}{2}A)$ | 双一次変換による離散化 | [arxiv-2111.00396#c1](https://arxiv.org/pdf/2111.00396v3#page=4 "The recurrent SSM (3) is not practical for training on modern hardware due to its sequentiality.") |
| $\bar{K} = (C\bar{B}, C\bar{A}\bar{B}, \ldots)$ | 畳み込みの核 | [arxiv-2111.00396#c1](https://arxiv.org/pdf/2111.00396v3#page=4 "The recurrent SSM (3) is not practical for training on modern hardware due to its sequentiality.") |
| $B, C, \Delta$ を入力の関数に | 選択(Mamba) | [arxiv-2312.00752#c8](https://arxiv.org/pdf/2312.00752v2#page=5 "In particular, we highlight that these parameters now have a length dimension 𝐿, meaning that the model has changed from time-invariant to time-varying.") |
| $\phi(Q)(\phi(K)^\top V)$、$s_i = s_{i-1} + \phi(k_i)v_i^\top$ | 線形注意とその再帰 | [arxiv-2006.16236#c1](https://arxiv.org/pdf/2006.16236v3#page=1 "we express the self-attention as a linear dot-product of kernel feature maps and make use of the associativity property of matrix products to reduce the complexity") [arxiv-2006.16236#c5](https://arxiv.org/pdf/2006.16236v3#page=5 "any transformer layer with causal masking can be written as a model that, given an input, modiﬁes an internal state and then predicts an output, namely a Recurrent Neural Network (RNN).") |
| $E_w[\exp(w^\top x - \Vert x \Vert^2/2)\exp(w^\top y - \Vert y \Vert^2/2)]$ | 正のランダム特徴 | [arxiv-2009.14794#c4](https://arxiv.org/pdf/2009.14794v4#page=4 "Consequently, softmax-kernel admits a positive random feature map unbiased approximation with") |
| $wkv_t$ | RWKV の時間減衰 | [arxiv-2305.13048#c2](https://arxiv.org/pdf/2305.13048v2#page=4 "To circumvent any potential degradation of W, we introduce a vector U that separately attends to the current token.") |

## 参照カード

- [arxiv-1701.06538](../../papers/arxiv-1701.06538.yaml) Shazeer et al., "Outrageously Large Neural Networks: The Sparsely-Gated Mixture-of-Experts Layer"
- [arxiv-2401.04088](../../papers/arxiv-2401.04088.yaml) Jiang et al., "Mixtral of Experts"
- [arxiv-2101.03961](../../papers/arxiv-2101.03961.yaml) Fedus, Zoph & Shazeer, "Switch Transformers"
- [arxiv-2006.16668](../../papers/arxiv-2006.16668.yaml) Lepikhin et al., "GShard"
- [arxiv-2202.08906](../../papers/arxiv-2202.08906.yaml) Zoph et al., "ST-MoE: Designing Stable and Transferable Sparse Expert Models"
- [arxiv-2202.09368](../../papers/arxiv-2202.09368.yaml) Zhou et al., "Mixture-of-Experts with Expert Choice Routing"
- [arxiv-2111.00396](../../papers/arxiv-2111.00396.yaml) Gu, Goel & Ré, "Efficiently Modeling Long Sequences with Structured State Spaces"
- [arxiv-2312.00752](../../papers/arxiv-2312.00752.yaml) Gu & Dao, "Mamba: Linear-Time Sequence Modeling with Selective State Spaces"
- [arxiv-2405.21060](../../papers/arxiv-2405.21060.yaml) Dao & Gu, "Transformers are SSMs"
- [arxiv-2006.16236](../../papers/arxiv-2006.16236.yaml) Katharopoulos et al., "Transformers are RNNs"
- [arxiv-2009.14794](../../papers/arxiv-2009.14794.yaml) Choromanski et al., "Rethinking Attention with Performers"
- [arxiv-2305.13048](../../papers/arxiv-2305.13048.yaml) Peng et al., "RWKV: Reinventing RNNs for the Transformer Era"
