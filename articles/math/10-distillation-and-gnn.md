---
title: 数式の解説 10 — 知識蒸留と GNN:温度と T² の補正、ヒント損失、GCN の導出、注意、GIN と WL、同質性
kind: math
tags: [knowledge-distillation, graph-neural-networks]
depends_on: [arxiv-1503.02531, arxiv-1412.6550, arxiv-1910.01348, arxiv-1609.02907, arxiv-1902.07153, arxiv-1801.07606, arxiv-1704.01212, arxiv-1710.10903, arxiv-1810.00826, arxiv-2006.11468]
written_at: 2026-10-10
written_by: claude-opus-5-5 via Claude Code
---

# 数式の解説 10 — 知識蒸留と GNN:温度と T² の補正、ヒント損失、GCN の導出、注意、GIN と WL、同質性

<!-- generated:stale -->
> ⚠ この記事の執筆日(2026-10-10)以降に作成された関連カードが 13 件あります(未反映。執筆日と同じ日に作成されたカードを含む): `arxiv-1706.02216`, `arxiv-1805.04770`, `arxiv-1811.05868`, `arxiv-1905.10947`, `arxiv-1910.01108`, `arxiv-1912.09893`, `arxiv-2003.00982`, `arxiv-2005.00687`, `arxiv-2005.07683`, `arxiv-2006.05205`, `arxiv-2106.05945`, `arxiv-2206.08164`, `arxiv-2302.11640`
<!-- /generated:stale -->

## この記事の読み方

[知識蒸留と枝刈り](../methods/knowledge-distillation-and-pruning.md) と [グラフニューラルネットワーク](../methods/graph-neural-networks.md) の記事で扱った手法の式を解説する。

使う道具(Σ、指数関数、行列とベクトル、偏微分)は [準備の記事](00-preliminaries.md)、ソフトマックスと温度は [数式の解説 3](03-uncertainty-and-calibration.md) で説明している。

- 式は論文から取り、根拠のカード(論文の該当ページへのリンク)を付けている。
- 「**補足**」と書いた計算は、論文には書かれていない、この記事による説明である。

## 1. 知識蒸留の式

### 温度付きソフトマックス

先生のロジット $v_i$、生徒のロジット $z_i$ を、温度 $T$ 付きのソフトマックスで確率に直す [arxiv-1503.02531#c2](https://arxiv.org/pdf/1503.02531v1#page=3 "The same high temperature is used when training the distilled model, but after it has been trained it uses a temperature of 1.")。

$$
q_i = \frac{\exp(z_i / T)}{\sum_j \exp(z_j / T)}
$$

先生の確率 $p_i$ も同じ温度で作り、これを生徒の目標(柔らかい目標)にする。

**補足(例:温度で何が見えるようになるか)**:先生のロジットが $(3, 1, 0)$ のとき、

- $T = 1$:$e^3 \approx 20.09$、$e^1 \approx 2.718$、$e^0 = 1$ で、確率は約 $(0.844,\ 0.114,\ 0.042)$。
- $T = 4$:ロジットを4で割ると $(0.75,\ 0.25,\ 0)$。$e^{0.75} \approx 2.117$、$e^{0.25} \approx 1.284$、$e^0 = 1$ で、確率は約 $(0.481,\ 0.292,\ 0.227)$。

$T = 1$ ではほぼ正解クラスの確率だけが目立つが、$T = 4$ では「2番目のクラスのほうが3番目より似ている」という情報が、目に見える大きさで残る。Hinton らは、このような柔らかい目標は1件あたりの情報が多いと述べている [arxiv-1503.02531#c1](https://arxiv.org/pdf/1503.02531v1#page=2 "When the soft targets have high entropy, they provide much more information per training case than hard targets and much less variance in the gradient between training cases,")。

### 勾配と T² の補正

柔らかい目標との交差エントロピー $C$ を生徒のロジット $z_i$ で微分すると、次のようになる [arxiv-1503.02531#c10](https://arxiv.org/pdf/1503.02531v1#page=3 "If the temperature is high compared with the magnitude of the logits, we can approximate:")。

$$
\frac{\partial C}{\partial z_i} = \frac{1}{T} (q_i - p_i)
$$

温度がロジットに比べて十分高いとき、$e^{x} \approx 1 + x$ で近似し、ロジットを事例ごとに平均0にそろえると [arxiv-1503.02531#c10](https://arxiv.org/pdf/1503.02531v1#page=3 "If the temperature is high compared with the magnitude of the logits, we can approximate:")

$$
\frac{\partial C}{\partial z_i} \approx \frac{1}{N T^2} (z_i - v_i)
$$

になる($N$ はクラスの数)。これは $\frac{1}{2}(z_i - v_i)^2$ の勾配に比例するので、高温の極限では、蒸留は先生と生徒のロジットの2乗誤差を小さくすることと同じになる [arxiv-1503.02531#c4](https://arxiv.org/pdf/1503.02531v1#page=3 "At lower temperatures, distillation pays much less attention to matching logits that are much more negative than the average.")。

**補足(近似の計算)**:$T$ が大きいと $e^{z_j / T} \approx 1 + z_j / T$ なので、$q_i \approx \dfrac{1 + z_i/T}{N + \sum_j z_j / T}$。ロジットの平均が0なら $\sum_j z_j = 0$ で、$q_i \approx \dfrac{1}{N} + \dfrac{z_i}{NT}$。$p_i$ も同様なので、$q_i - p_i \approx \dfrac{z_i - v_i}{NT}$。これに $\dfrac{1}{T}$ を掛けると上の式になる。

この式から、柔らかい目標による勾配の大きさは $1/T^2$ に比例することがわかる。正解ラベルの損失と組み合わせるときは、柔らかい目標の項に $T^2$ を掛けて、温度を変えても両者の釣り合いが大きく変わらないようにする [arxiv-1503.02531#c3](https://arxiv.org/pdf/1503.02531v1#page=3 "This ensures that the relative contributions of the hard and soft targets remain roughly unchanged if the temperature used for distillation is changed while experimenting with meta-parameters.")。
後の論文では、この形を次のように書いている [arxiv-1910.01348#c2](https://arxiv.org/pdf/1910.01348v1#page=2 "Trained neural networks produce peaky probability distributions, which may be less informative.")。

$$
L = \alpha L_{\text{cls}} + (1 - \alpha) L_{\text{KD}}, \qquad L_{\text{KD}} = -\tau^2 \sum_k \tilde{p}^{\,t}_k \log \tilde{p}^{\,s}_k
$$

$\tau$ が温度、$\tilde{p}^{\,t}$ と $\tilde{p}^{\,s}$ は温度で柔らかくした先生と生徒の確率である。

### ヒント損失(FitNets)

FitNets は、先生の中間層の出力 $u_h$ を、生徒の中間層の出力 $v_g$ に回帰器 $r$ をかぶせたものでまねさせる [arxiv-1412.6550#c3](https://arxiv.org/pdf/1412.6550v4#page=3 "To mitigate this limitation, we use a convolutional regressor instead.")。

$$
\mathcal{L}_{HT} = \frac{1}{2} \big\Vert u_h(x; W_{\text{Hint}}) - r\big(v_g(x; W_{\text{Guided}});\ W_r\big) \big\Vert^2
$$

生徒の中間層は先生より細いことが多いので、回帰器 $r$ で大きさをそろえる。全結合の回帰器は大きくなりすぎるので、畳み込みの回帰器を使う [arxiv-1412.6550#c3](https://arxiv.org/pdf/1412.6550v4#page=3 "To mitigate this limitation, we use a convolutional regressor instead.")。

## 2. GCN の式

### 層の規則

GCN の1層は次の式で表される [arxiv-1609.02907#c1](https://arxiv.org/pdf/1609.02907v4#page=2 "We consider a multi-layer Graph Convolutional Network (GCN) with the following layer-wise propagation rule:")。

$$
H^{(l+1)} = \sigma\!\left( \tilde{D}^{-1/2} \tilde{A} \tilde{D}^{-1/2} H^{(l)} W^{(l)} \right), \qquad \tilde{A} = A + I,\quad \tilde{D}_{ii} = \sum_j \tilde{A}_{ij}
$$

- $A$ は隣接行列(ノード $i$ と $j$ がつながっていれば $A_{ij} = 1$)。
- $H^{(l)}$ は第 $l$ 層の各ノードの特徴を並べた行列で、$H^{(0)} = X$(入力の特徴)。
- $W^{(l)}$ は学習する重み、$\sigma$ は非線形関数。

**補足(例:3つのノードが一列につながったグラフ)**:ノード1–2–3 で、自分へのループを加えると次数は $(2, 3, 2)$ になる。$\tilde{D}^{-1/2}\tilde{A}\tilde{D}^{-1/2}$ の $(i, j)$ 成分は、$i$ と $j$ がつながっていれば $1/\sqrt{\tilde{d}_i \tilde{d}_j}$ である。

$$
\tilde{D}^{-1/2}\tilde{A}\tilde{D}^{-1/2} =
\begin{pmatrix}
1/2 & 1/\sqrt{6} & 0 \\
1/\sqrt{6} & 1/3 & 1/\sqrt{6} \\
0 & 1/\sqrt{6} & 1/2
\end{pmatrix}
$$

特徴が $x = (1, 0, 0)$(ノード1だけが1)なら、これを掛けると約 $(0.5,\ 0.408,\ 0)$ になる。ノード1の値が隣のノード2にしみ出している。もう一度掛けるとノード3にも届く。これが「隣から情報を集める」操作の正体である。

### 導出の流れ

この形は、次の順で導かれた。

1. **スペクトルでの畳み込み**:正規化ラプラシアン $L = I - D^{-1/2} A D^{-1/2}$ の固有ベクトル $U$ を使い、$g_\theta \star x = U g_\theta U^\top x$ とする。固有分解が必要で計算が重い [arxiv-1609.02907#c2](https://arxiv.org/pdf/1609.02907v4#page=2 "Note that this expression is now K-localized since it is a Kth-order polynomial in the Laplacian, i.e. it depends only on nodes that are at maximum K steps away from the central node (Kth-order neighborhood).")。
2. **チェビシェフ多項式で近似**:フィルタをラプラシアンの $K$ 次の多項式で近似すると、$K$ 歩以内のノードだけに依存する局所的な操作になり、固有分解も不要になる [arxiv-1609.02907#c2](https://arxiv.org/pdf/1609.02907v4#page=2 "Note that this expression is now K-localized since it is a Kth-order polynomial in the Laplacian, i.e. it depends only on nodes that are at maximum K steps away from the central node (Kth-order neighborhood).")。
3. **1次で打ち切る**:$K = 1$、最大固有値を $2$ で近似し、2つのパラメータを1つにまとめると、$\theta (I + D^{-1/2} A D^{-1/2}) x$ になる [arxiv-1609.02907#c3](https://arxiv.org/pdf/1609.02907v4#page=3 "In this linear formulation of a GCN we further approximate λmax ≈2, as we can expect that neural network parameters will adapt to this change in scale during training.")。
4. **再正規化**:$I + D^{-1/2} A D^{-1/2}$ の固有値は $[0, 2]$ にあり、繰り返し掛けると数値が不安定になる。そこで、先に自分へのループを加えてから正規化した $\tilde{D}^{-1/2} \tilde{A} \tilde{D}^{-1/2}$ に置き換える [arxiv-1609.02907#c4](https://arxiv.org/pdf/1609.02907v4#page=3 "Repeated application of this operator can therefore lead to numerical instabilities and exploding/vanishing gradients when used in a deep neural network model.")。

**補足(なぜ固有値の範囲が問題か)**:行列を $m$ 回掛けると、固有値も $m$ 乗される。固有値が $2$ に近いと $2^m$ のように爆発し、$0$ に近いと消える。深いネットワークで勾配が爆発・消失する原因になる。

### SGC:非線形を除くと

GCN の層の間の非線形を取り除くと、$K$ 層分の操作は1つにまとまる [arxiv-1902.07153#c1](https://arxiv.org/pdf/1902.07153v2#page=3 "We hypothesize that the nonlinearity between GCN layers is not critical - but that the majority of the beneﬁt arises from the local averaging.")。

$$
\hat{Y}_{\text{SGC}} = \mathrm{softmax}\big( S^K X \Theta \big), \qquad S = \tilde{D}^{-1/2} \tilde{A} \tilde{D}^{-1/2}
$$

$S^K X$ は学習するパラメータを含まないので、前もって計算しておける。残りはロジスティック回帰である。
スペクトルで見ると、自分へのループなしでは各周波数成分が $(2 - \lambda_i)^K$ 倍され、高い次数で爆発するが、再正規化した行列では $(1 - \tilde{\lambda}_i)^K$ 倍になる。自分へのループを加えると最大固有値が小さくなることが、論文の定理1で示されている [arxiv-1902.07153#c3](https://arxiv.org/pdf/1902.07153v2#page=4 "Theorem 1 shows that the largest eigenvalue of the normalized graph Laplacian becomes smaller after adding self-loops γ > 0 (see supplementary materials for the proof).")。

### 過平滑化:平均化を繰り返すと

Li らは、GCN の操作をラプラシアン平滑化として書いた [arxiv-1801.07606#c2](https://arxiv.org/pdf/1801.07606v1#page=4 "We thus call the graph convolution a special form of Laplacian smoothing – symmetric Laplacian smoothing.")。

$$
y_i = (1 - \gamma) x_i + \gamma \sum_j \frac{\tilde{a}_{ij}}{\tilde{d}_i} x_j
$$

$\gamma = 1$ とし、正規化を対称にしたものが GCN の操作になる。この平滑化を何度も繰り返すと、二部グラフの成分がないなどの仮定のもとで、各連結成分の中で値が一定のベクトル(を次数で調整したもの)に収束する(論文の定理1)[arxiv-1801.07606#c5](https://arxiv.org/pdf/1801.07606v1#page=5 "Based on the above theorem, over-smoothing will make the features indistinguishable and hurt the classiﬁcation accuracy.")。

**補足(例)**:上の3ノードの例で、$\tilde{D}^{-1/2}\tilde{A}\tilde{D}^{-1/2}$ を何度も掛けると、ほとんどの初期値で、3つのノードの値の比は $\sqrt{2} : \sqrt{3} : \sqrt{2}$(次数の平方根の比)に近づいていく(この行列の最大固有値1の固有ベクトルの方向に縮むため)。つまり、ノードごとの違いが消える。層を深くしすぎるとノードの区別がつかなくなる、という過平滑化はこの性質による。

## 3. メッセージパッシングと注意

### MPNN の3つの関数

Gilmer らの枠組みでは、各ステップ $t$ で次の計算をする [arxiv-1704.01212#c10](https://arxiv.org/pdf/1704.01212v2#page=3 "The readout phase computes a feature vector for the whole graph using some readout function R according to")。

$$
m_v^{t+1} = \sum_{w \in N(v)} M_t\big(h_v^t,\ h_w^t,\ e_{vw}\big), \qquad
h_v^{t+1} = U_t\big(h_v^t,\ m_v^{t+1}\big), \qquad
\hat{y} = R\big(\{ h_v^T \mid v \in G \}\big)
$$

$N(v)$ は $v$ の隣のノード、$e_{vw}$ はエッジの特徴、$M_t$ はメッセージ関数、$U_t$ は更新関数、$R$ は読み出し関数である。$R$ はノードの並べ方によらない必要がある [arxiv-1704.01212#c1](https://arxiv.org/pdf/1704.01212v2#page=3 "R operates on the set of node states and must be invariant to permutations of the node states in order for the MPNN to be invariant to graph isomorphism.")。
GCN は、メッセージを $c_{vw} h_w$($c_{vw}$ は次数による正規化)、更新を $\mathrm{ReLU}(W m_v)$ とした場合にあたる [arxiv-1704.01212#c2](https://arxiv.org/pdf/1704.01212v2#page=2 "There are at least eight notable examples of models from the literature that we can describe using our Message Passing Neural Networks (MPNN) framework.")。

### GAT の注意

GAT は、隣のノード $j$ ごとに重み $\alpha_{ij}$ を計算し、重み付きで足す [arxiv-1710.10903#c1](https://arxiv.org/pdf/1710.10903v3#page=3 "We inject the graph structure into the mechanism by performing masked attention—we only compute eij for nodes j ∈Ni, where Ni is some neighborhood of node i in the graph.") [arxiv-1710.10903#c10](https://arxiv.org/pdf/1710.10903v3#page=3 "the normalized attention coefﬁcients are used to compute a linear combination of the features corresponding to them")。

$$
\alpha_{ij} = \frac{\exp\!\big(\mathrm{LeakyReLU}(a^\top [W h_i \,\Vert\, W h_j])\big)}{\sum_{k \in N_i} \exp\!\big(\mathrm{LeakyReLU}(a^\top [W h_i \,\Vert\, W h_k])\big)}, \qquad
h'_i = \sigma\!\left( \sum_{j \in N_i} \alpha_{ij} W h_j \right)
$$

- $[\cdot \,\Vert\, \cdot]$ は2つのベクトルを縦につなげる操作、$a$ は学習するベクトルである。
- 分母の和は $i$ の隣($i$ 自身を含む)だけでとるので、グラフの構造が重みに反映される。
- 複数の注意を並べ、中間層ではつなげ、最終層では平均する [arxiv-1710.10903#c2](https://arxiv.org/pdf/1710.10903v3#page=4 "To stabilize the learning process of self-attention, we have found extending our mechanism to employ multi-head attention to be beneﬁcial, similarly to Vaswani et al. (2017).")。

**補足(例)**:ある点の隣が2つで、$\mathrm{LeakyReLU}(\cdots)$ の値が $1$ と $0$ だったとする。$\alpha = \left(\dfrac{e}{e + 1},\ \dfrac{1}{e + 1}\right) \approx (0.731,\ 0.269)$ となり、1つ目の隣の特徴が強く反映される。GCN では、この重みが次数だけで決まっていた。

## 4. GIN と WL 検定

### 単射な集約

Xu らによれば、更新が次の形で、集約 $f$ と更新 $\phi$ がどちらも単射なら、GNN は WL 検定と同じ力を持つ [arxiv-1810.00826#c2](https://arxiv.org/pdf/1810.00826v3#page=4 "if the neighbor aggregation and graph-level readout functions are injective, then the resulting GNN is as powerful as the WL test.")。

$$
h_v^{(k)} = \phi\Big( h_v^{(k-1)},\ f\big(\{ h_u^{(k-1)} : u \in N(v) \}\big) \Big)
$$

これを満たすように作ったのが GIN の更新である [arxiv-1810.00826#c4](https://arxiv.org/pdf/1810.00826v3#page=5 "Our next lemma states that sum aggregators can represent injective, in fact, universal functions over multisets.")。

$$
h_v^{(k)} = \mathrm{MLP}^{(k)}\!\left( \big(1 + \epsilon^{(k)}\big)\, h_v^{(k-1)} + \sum_{u \in N(v)} h_u^{(k-1)} \right)
$$

### なぜ和で、平均や最大値ではないのか

隣の特徴の集まりは、同じ値が何度も現れうる**多重集合**である。論文によれば、和は多重集合を見分けられるが、平均は見分けられない [arxiv-1810.00826#c4](https://arxiv.org/pdf/1810.00826v3#page=5 "Our next lemma states that sum aggregators can represent injective, in fact, universal functions over multisets.")。

**補足(例)**:隣の特徴が $\{a\}$ のノードと $\{a, a\}$ のノードを考える。

| 集約 | $\{a\}$ | $\{a, a\}$ | 見分けられるか |
|---|---|---|---|
| 和 | $a$ | $2a$ | 見分けられる |
| 平均 | $a$ | $a$ | 見分けられない |
| 最大値 | $a$ | $a$ | 見分けられない |

平均は割合しか、最大値はどの値があるかしか見ていない。同じ特徴を持つ隣が1つか2つかという「数」の違いは、和でしか区別できない。

自分自身の特徴に掛ける $(1 + \epsilon)$ は、自分の特徴と隣の和を区別するためのものである。論文の系6は、無理数を含む無数の $\epsilon$ についてこの形が単射になることを示している [arxiv-1810.00826#c4](https://arxiv.org/pdf/1810.00826v3#page=5 "Our next lemma states that sum aggregators can represent injective, in fact, universal functions over multisets.")。

## 5. エッジ同質性

Zhu らは、グラフの同質性を、同じクラスどうしをつなぐエッジの割合で定義した [arxiv-2006.11468#c1](https://arxiv.org/pdf/2006.11468v2#page=2 "is the fraction of edges in a graph which connect nodes that have the same class label (i.e., intra-class edges).")。

$$
h = \frac{\big|\{ (u, v) \in E : y_u = y_v \}\big|}{|E|}
$$

$h$ が1に近いほど同質的(つながったノードは同じクラス)、0に近いほど異質的である。

**補足(例)**:4本のエッジのうち、両端のクラスが同じものが1本なら $h = 0.25$ で、異質的なグラフである。このとき、2節の GCN のように隣の特徴を平均すると、違うクラスの特徴が混ざりやすい。H2GCN のように自分と隣の表現を分けて扱う設計は、この問題への対処である([GNN の記事](../methods/graph-neural-networks.md) の4節)。

## まとめ

| 式 | 何を表すか | 根拠 |
|---|---|---|
| $q_i = \exp(z_i/T) / \sum_j \exp(z_j/T)$ | 温度付きソフトマックス | [arxiv-1503.02531#c2](https://arxiv.org/pdf/1503.02531v1#page=3 "The same high temperature is used when training the distilled model, but after it has been trained it uses a temperature of 1.") |
| $\partial C/\partial z_i = (q_i - p_i)/T \approx (z_i - v_i)/(NT^2)$ | 蒸留の勾配と高温の極限 | [arxiv-1503.02531#c10](https://arxiv.org/pdf/1503.02531v1#page=3 "If the temperature is high compared with the magnitude of the logits, we can approximate:") |
| $\alpha L_{\text{cls}} + (1-\alpha)L_{\text{KD}}$、$L_{\text{KD}}$ に $\tau^2$ | 正解ラベルとの組合せと T² の補正 | [arxiv-1503.02531#c3](https://arxiv.org/pdf/1503.02531v1#page=3 "This ensures that the relative contributions of the hard and soft targets remain roughly unchanged if the temperature used for distillation is changed while experimenting with meta-parameters.") [arxiv-1910.01348#c2](https://arxiv.org/pdf/1910.01348v1#page=2 "Trained neural networks produce peaky probability distributions, which may be less informative.") |
| $\frac{1}{2}\Vert u_h - r(v_g) \Vert^2$ | ヒント損失 | [arxiv-1412.6550#c3](https://arxiv.org/pdf/1412.6550v4#page=3 "To mitigate this limitation, we use a convolutional regressor instead.") |
| $\sigma(\tilde{D}^{-1/2}\tilde{A}\tilde{D}^{-1/2} H W)$ | GCN の層 | [arxiv-1609.02907#c1](https://arxiv.org/pdf/1609.02907v4#page=2 "We consider a multi-layer Graph Convolutional Network (GCN) with the following layer-wise propagation rule:") |
| $\mathrm{softmax}(S^K X \Theta)$ | SGC | [arxiv-1902.07153#c1](https://arxiv.org/pdf/1902.07153v2#page=3 "We hypothesize that the nonlinearity between GCN layers is not critical - but that the majority of the beneﬁt arises from the local averaging.") |
| $m_v = \sum M_t(\cdot)$、$h_v = U_t(\cdot)$、$\hat{y} = R(\cdot)$ | メッセージパッシング | [arxiv-1704.01212#c10](https://arxiv.org/pdf/1704.01212v2#page=3 "The readout phase computes a feature vector for the whole graph using some readout function R according to") |
| $\alpha_{ij}$、$h'_i = \sigma(\sum_j \alpha_{ij} W h_j)$ | GAT の注意 | [arxiv-1710.10903#c10](https://arxiv.org/pdf/1710.10903v3#page=3 "the normalized attention coefﬁcients are used to compute a linear combination of the features corresponding to them") |
| $\mathrm{MLP}((1+\epsilon)h_v + \sum_u h_u)$ | GIN | [arxiv-1810.00826#c4](https://arxiv.org/pdf/1810.00826v3#page=5 "Our next lemma states that sum aggregators can represent injective, in fact, universal functions over multisets.") |
| 同じクラスをつなぐエッジの割合 | エッジ同質性 | [arxiv-2006.11468#c1](https://arxiv.org/pdf/2006.11468v2#page=2 "is the fraction of edges in a graph which connect nodes that have the same class label (i.e., intra-class edges).") |

## 参照カード

- [arxiv-1503.02531](../../papers/arxiv-1503.02531.yaml) Hinton, Vinyals & Dean, "Distilling the Knowledge in a Neural Network"
- [arxiv-1910.01348](../../papers/arxiv-1910.01348.yaml) Cho & Hariharan, "On the Efficacy of Knowledge Distillation"
- [arxiv-1412.6550](../../papers/arxiv-1412.6550.yaml) Romero et al., "FitNets: Hints for Thin Deep Nets"
- [arxiv-1609.02907](../../papers/arxiv-1609.02907.yaml) Kipf & Welling, "Semi-Supervised Classification with Graph Convolutional Networks"
- [arxiv-1902.07153](../../papers/arxiv-1902.07153.yaml) Wu et al., "Simplifying Graph Convolutional Networks"
- [arxiv-1801.07606](../../papers/arxiv-1801.07606.yaml) Li, Han & Wu, "Deeper Insights into Graph Convolutional Networks for Semi-Supervised Learning"
- [arxiv-1704.01212](../../papers/arxiv-1704.01212.yaml) Gilmer et al., "Neural Message Passing for Quantum Chemistry"
- [arxiv-1710.10903](../../papers/arxiv-1710.10903.yaml) Veličković et al., "Graph Attention Networks"
- [arxiv-1810.00826](../../papers/arxiv-1810.00826.yaml) Xu et al., "How Powerful are Graph Neural Networks?"
- [arxiv-2006.11468](../../papers/arxiv-2006.11468.yaml) Zhu et al., "Beyond Homophily in Graph Neural Networks"
