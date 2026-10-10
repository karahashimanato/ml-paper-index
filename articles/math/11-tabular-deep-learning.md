---
title: 数式の解説 11 — 表データの深層学習:微分可能な木と entmax、TabNet のマスク、交差層、数値の埋め込み、近傍の重み
kind: math
tags: [tabular-mlp, tabular-attention, differentiable-trees]
depends_on: [arxiv-1909.06312, arxiv-1908.07442, arxiv-2008.13535, arxiv-1810.11921, arxiv-2203.05556, arxiv-2307.14338, arxiv-2106.15147, arxiv-2207.08815]
written_at: 2026-10-10
written_by: claude-opus-5-5 via Claude Code
---

# 数式の解説 11 — 表データの深層学習:微分可能な木と entmax、TabNet のマスク、交差層、数値の埋め込み、近傍の重み

<!-- generated:stale -->
> ⚠ この記事の執筆日(2026-10-10)以降に作成された関連カードが 8 件あります(未反映。執筆日と同じ日に作成されたカードを含む): `arxiv-2012.06678`, `arxiv-2106.01342`, `arxiv-2106.11189`, `arxiv-2110.01889`, `arxiv-2301.02819`, `arxiv-2305.18446`, `arxiv-2309.17130`, `arxiv-2407.00956`
<!-- /generated:stale -->

## この記事の読み方

[表データの深層学習モデル](../methods/tabular-deep-learning-models.md) の記事で扱ったモデルの式を解説する。

使う道具(Σ、指数関数、ベクトルと行列、三角関数)は [準備の記事](00-preliminaries.md)、ソフトマックスは [数式の解説 3](03-uncertainty-and-calibration.md)、注意は [数式の解説 10](10-distillation-and-gnn.md) の3節で説明している。

- 式は論文から取り、根拠のカード(論文の該当ページへのリンク)を付けている。
- 「**補足**」と書いた計算は、論文には書かれていない、この記事による説明である。

## 1. 準備:ソフトマックスと sparsemax・entmax

ソフトマックスは、どの成分にも正の確率を割り当てる。表データのモデルでは、**いくつかの成分をちょうど0にする**正規化がよく使われる。TabNet は sparsemax を [arxiv-1908.07442#c2](https://arxiv.org/pdf/1908.07442v5#page=3 "Sparsemax normalization (Martins and Astudillo 2016) encourages sparsity by mapping the Euclidean projection onto the probabilistic simplex, which is observed to be superior in performance and aligned with the goal of sparse feature selection for explainability.")、NODE は entmax を使う [arxiv-1909.06312#c1](https://arxiv.org/pdf/1909.06312v2#page=4 "Instead, we propose to use the α-entmax transformation (Peters et al., 2019) as it is able to learn sparse choices, depending only on a few features, via standard gradient descent.")。

**補足(sparsemax の計算)**:sparsemax は、ベクトル $z$ に最も近い確率ベクトル(成分が0以上で合計1)を返す。ある閾値 $\tau$ を決めて $p_i = \max(z_i - \tau,\ 0)$ とし、合計が1になるように $\tau$ を選べばよい。

$z = (1,\ 0.5,\ -1)$ の場合、上の2つの成分だけが正になると仮定すると、$(1 - \tau) + (0.5 - \tau) = 1$ より $\tau = 0.25$。3つ目は $-1 < 0.25$ なので確かに0になり、

$$
\mathrm{sparsemax}(z) = (0.75,\ 0.25,\ 0)
$$

同じ $z$ のソフトマックスは約 $(0.574,\ 0.348,\ 0.078)$ で、3つ目も0にはならない。entmax は、ソフトマックスと sparsemax の中間にあたる変換で、パラメータ $\alpha$ でその間を調整する。

## 2. NODE:微分可能な決定木

### 対称な決定木

NODE が使う**対称な決定木**(oblivious tree)は、深さごとに同じ特徴と閾値で分岐する。深さ $d$ の木は、$d$ 個の比較の結果(0か1)の組で $2^d$ 個の葉のどれかを選び、その葉の値を出力する [arxiv-1909.06312#c10](https://arxiv.org/pdf/1909.06312v2#page=3 "In this notation, the tree output is deﬁned as:")。

$$
h(x) = R\big[\, \mathbf{1}(f_1(x) - b_1),\ \ldots,\ \mathbf{1}(f_d(x) - b_d) \,\big]
$$

$\mathbf{1}$ は、引数が正なら1、そうでなければ0を返す階段関数(ヘヴィサイド関数)、$R$ は $2^d$ 個の葉の値の表である。

### 微分できるようにする

階段関数と「どの特徴で分岐するか」の選択は微分できない。NODE はこの2つを、entmax で連続的な形に置き換える [arxiv-1909.06312#c11](https://arxiv.org/pdf/1909.06312v2#page=4 "with weights computed as entmax over the learnable feature selection matrix")。

$$
\hat{f}_i(x) = \sum_{j=1}^{n} x_j \cdot \mathrm{entmax}_\alpha(F_{ij}), \qquad
c_i(x) = \sigma_\alpha\!\left( \frac{f_i(x) - b_i}{\tau_i} \right), \quad \sigma_\alpha(x) = \mathrm{entmax}_\alpha([x,\ 0])
$$

- 特徴の選択は、特徴の重み付き和になる。entmax は疎なので、少数の特徴だけに重みが付く。
- 比較は、2クラスの entmax で、0から1の間のなめらかな値 $c_i(x)$ になる。$b_i$ は閾値、$\tau_i$ はスケールで、どちらも学習する。

両方が0か1の値(one-hot)になったときは、通常の対称な決定木に一致する [arxiv-1909.06312#c1](https://arxiv.org/pdf/1909.06312v2#page=4 "Instead, we propose to use the α-entmax transformation (Peters et al., 2019) as it is able to learn sparse choices, depending only on a few features, via standard gradient descent.")。

**補足(例:深さ2の木)**:2つの比較の結果が $c_1 = 0.9$、$c_2 = 0.2$ だったとする。各葉に届く「重み」を、比較が1になる確率 $c_i$ と0になる確率 $1 - c_i$ の積として考えると

| 葉(比較1, 比較2) | 重み |
|---|---|
| (1, 1) | $0.9 \times 0.2 = 0.18$ |
| (1, 0) | $0.9 \times 0.8 = 0.72$ |
| (0, 1) | $0.1 \times 0.2 = 0.02$ |
| (0, 0) | $0.1 \times 0.8 = 0.08$ |

となり、合計は1。出力は、葉の値をこの重みで平均したものになる(論文の図1の説明では、出力は選択の重みで拡大縮小した葉の値の和である)。$c_i$ が0か1に近づくと、1つの葉だけが選ばれる、通常の木に近づく。

## 3. TabNet のマスクと事前スケール

TabNet は、各段階 $i$ で、特徴に掛けるマスク $M[i]$ を作る [arxiv-1908.07442#c10](https://arxiv.org/pdf/1908.07442v5#page=3 "is the prior scale term, denoting how much a particular feature")。

$$
M[i] = \mathrm{sparsemax}\big( P[i-1] \cdot h_i(a[i-1]) \big), \qquad
P[i] = \prod_{j=1}^{i} \big(\gamma - M[j]\big)
$$

- $a[i-1]$ は前の段階の処理結果、$h_i$ は学習する関数である。
- マスクは sparsemax なので、各行の合計は1で、多くの成分が0になる。
- $P[i]$(**事前スケール**)は、各特徴がこれまでにどれだけ使われたかを表す。$\gamma = 1$ なら、ある特徴は1つの段階でしか使えない。$\gamma$ を大きくすると、同じ特徴を何度も使いやすくなる [arxiv-1908.07442#c10](https://arxiv.org/pdf/1908.07442v5#page=3 "is the prior scale term, denoting how much a particular feature")。

**補足(例)**:$\gamma = 1$、3つの特徴で、最初の段階のマスクが $M[1] = (0.7,\ 0.3,\ 0)$ だったとする。$P[1] = (1 - 0.7,\ 1 - 0.3,\ 1 - 0) = (0.3,\ 0.7,\ 1)$ なので、次の段階では、たくさん使った特徴1の重みが小さく抑えられ、まだ使っていない特徴3が選ばれやすくなる。

## 4. 交差層(DCN V2)と特徴の交互作用

### 交差層

DCN V2 の交差層は次の式である [arxiv-2008.13535#c10](https://arxiv.org/pdf/2008.13535v2#page=3 "The core of DCN-V2 lies in the cross layers that create explicit feature crosses.")。

$$
x_{l+1} = x_0 \odot \big( W_l x_l + b_l \big) + x_l
$$

$x_0$ は元の特徴(の埋め込み)、$\odot$ は成分ごとの積、$W_l$ と $b_l$ は学習する重みとバイアスである。最後の $+ x_l$ は、入力をそのまま足す残差接続である。

**補足(なぜ「交差」なのか)**:2次元で $x_0 = (a,\ b)$、$x_1 = x_0$ として1層を計算すると、1つ目の成分は

$$
a \cdot (w_{11} a + w_{12} b + b_1) + a = w_{11} a^2 + w_{12}\, ab + (b_1 + 1)\, a
$$

になり、$a^2$ や $ab$ のような**特徴の積**(2次の交互作用)が現れる。層を1つ重ねるごとに $x_0$ がもう1回掛けられるので、扱える積の次数が1つずつ上がる。論文は、交差層が次数に上限のある交差を明示的に作ると述べている [arxiv-2008.13535#c2](https://arxiv.org/pdf/2008.13535v2#page=2 "The function class modeled by DCN-V2 is a strict superset of that modeled by DCN.")。

### 特徴の間の注意(AutoInt)

AutoInt は、数値の特徴 $x_m$ を学習するベクトル $v_m$ を使って $v_m x_m$ と埋め込み、カテゴリの特徴の埋め込みと同じ空間に置く [arxiv-1810.11921#c3](https://arxiv.org/pdf/1810.11921v2#page=4 "To allow the interaction between categorical and numerical features, we also represent the numerical features in the same low-dimensional feature space.")。そのうえで、特徴の埋め込みどうしに多頭注意をかける [arxiv-1810.11921#c4](https://arxiv.org/pdf/1810.11921v2#page=5 "Therefore a few interacting layers will suffice to model high-order feature interactions.")。注意の重みは、2つの特徴の組合せがどれだけ重要かを表す。

## 5. 数値の特徴の埋め込み

### 区分線形の符号化(PLE)

値の範囲を区間の端 $b_0 < b_1 < \cdots < b_T$ で $T$ 個の区間に分け、値 $x$ を $T$ 次元のベクトルに変える [arxiv-2203.05556#c10](https://arxiv.org/pdf/2203.05556v4#page=4 "where PLE stands for “peicewise linear
encoding”.")。

$$
e_t =
\begin{cases}
0 & (x < b_{t-1} \text{ かつ } t > 1) \\
1 & (x \ge b_t \text{ かつ } t < T) \\
\dfrac{x - b_{t-1}}{b_t - b_{t-1}} & (\text{それ以外})
\end{cases}
$$

**補足(例)**:区間の端が $0, 10, 20, 30$($T = 3$)で、$x = 15$ のとき、

- $e_1$:$x \ge b_1 = 10$ なので $1$
- $e_2$:それ以外なので $(15 - 10)/(20 - 10) = 0.5$
- $e_3$:$x < b_2 = 20$ なので $0$

で、$(1,\ 0.5,\ 0)$ になる。値が大きくなると、左の成分から順に1で埋まっていく「目盛り」のような表現である。
区間の端は、学習データの分位点か、1つの特徴だけで決定木を育てたときの分割から決める [arxiv-2203.05556#c2](https://arxiv.org/pdf/2203.05556v4#page=4 "PLE produces alternative initial representations for the numerical features and can be viewed as a preprocessing strategy.")。

### 周期的な埋め込み

値を、学習する周波数 $c$ の正弦と余弦で表す [arxiv-2203.05556#c3](https://arxiv.org/pdf/2203.05556v4#page=5 "We observe that σ is an important hyperparameter.")。

$$
f(x) = \big[ \sin(v),\ \cos(v) \big], \qquad v = 2\pi c\, x
$$

$c$ はベクトルで、初期値を正規分布 $\mathcal{N}(0, \sigma)$ から取る。論文によれば、$\sigma$ は重要なハイパーパラメータである [arxiv-2203.05556#c3](https://arxiv.org/pdf/2203.05556v4#page=5 "We observe that σ is an important hyperparameter.")。

**補足(読み方)**:周波数の違ういくつもの $\sin$・$\cos$ を並べると、値の小さな違いにも大きな違いにも反応する表現になる。[表データの深層学習モデル](../methods/tabular-deep-learning-models.md) の1節で触れた、ニューラルネットワークがなめらかな解に偏るという指摘 [arxiv-2207.08815#c4](https://arxiv.org/pdf/2207.08815v1#page=6 "For small lengthscales, smoothing the target function on the train set decreases markedly the accuracy of tree-based models, but barely impacts that of NNs.") への対処になりうると考えられる(この部分はこの記事の解釈である)。

## 6. 近傍の重み(TabR)

TabR は、予測したいサンプル $\tilde{x}$ と学習サンプル $\tilde{x}_i$ の**似ている度合い** $S$ を計算し、上位 $m$ 個の近傍の「値」$V$ を重み付きで集める。論文の改良の過程で、似ている度合いは内積から距離に変わった [arxiv-2307.14338#c10](https://arxiv.org/pdf/2307.14338v2#page=5 "Empirically, we observed that removing the notion of queries (i.e. removing WQ) and using the L2 distance instead of the dot product significantly improves performance on several datasets in Table 2:")。

$$
\text{改良前:} \ S(\tilde{x}, \tilde{x}_i) = W_Q(\tilde{x})^\top W_K(\tilde{x}_i) \cdot d^{-1/2}, \qquad
\text{改良後:} \ S(\tilde{x}, \tilde{x}_i) = -\big\Vert W_K(\tilde{x}) - W_K(\tilde{x}_i) \big\Vert^2 \cdot d^{-1/2}
$$

改良後の値は $V = W_Y(y_i) + W_V(\tilde{x}_i)$ で、近傍のラベル $y_i$ の埋め込みを含む [arxiv-2307.14338#c10](https://arxiv.org/pdf/2307.14338v2#page=5 "Empirically, we observed that removing the notion of queries (i.e. removing WQ) and using the L2 distance instead of the dot product significantly improves performance on several datasets in Table 2:")。著者らは、クエリをやめて L2 距離を使う変更が転機だったと述べている [arxiv-2307.14338#c3](https://arxiv.org/pdf/2307.14338v2#page=5 "Crucially, in subsection A.3, we show that removing any of the three ingredients (context labels, key-only representation, L2 distance) results in a performance drop back to the level of MLP.")。

**補足(例)**:2つの近傍との距離の2乗が $1$ と $4$ なら(スケール $d^{-1/2}$ は省略)、$S = (-1,\ -4)$ で、ソフトマックスの重みは $\left(\dfrac{e^{-1}}{e^{-1} + e^{-4}},\ \dfrac{e^{-4}}{e^{-1} + e^{-4}}\right) \approx (0.953,\ 0.047)$ になる。近い近傍のラベルがほとんどを決める。重みの付いた k 近傍法に近い動きである。

## 7. SCARF の「別の見え方」

SCARF は、各サンプルについて、特徴の一部をランダムに選び、その特徴の**周辺分布**(学習データでその特徴が取る値の一様分布)から取った値で置き換える [arxiv-2106.15147#c1](https://arxiv.org/pdf/2106.15147v2#page=4 "We sample some fraction of the features uniformly at random and replace each of those features by a random draw from that feature’s empirical marginal distribution,")。元のサンプルと置き換えたサンプルを「同じものの別の見え方」として、対照学習で表現を学ぶ。

**補足(例)**:(年齢, 年収, 職業) = (35, 500, 技術職) のサンプルで、年収が選ばれたら、学習データの別の誰かの年収(たとえば 320)に置き換えて (35, 320, 技術職) にする。置き換えた値も実際に現れる値なので、画像の切り抜きのような「ありえない入力」を作らずに済む。
論文は、この置き換えには調整するパラメータがなく、特徴のスケールにもよらないと述べている [arxiv-2106.15147#c9](https://arxiv.org/pdf/2106.15147v2#page=9 "Marginal sampling is neat in that in addition to not having hyperparameters, it is invariant to scaling and preserves the “units” of each feature.")。

## まとめ

| 式 | 何を表すか | 根拠 |
|---|---|---|
| $h(x) = R[\mathbf{1}(f_1(x) - b_1), \ldots]$ | 対称な決定木 | [arxiv-1909.06312#c10](https://arxiv.org/pdf/1909.06312v2#page=3 "In this notation, the tree output is deﬁned as:") |
| $\hat{f}_i = \sum_j x_j\, \mathrm{entmax}(F_{ij})$、$c_i = \sigma_\alpha((f_i - b_i)/\tau_i)$ | 微分可能にした分岐 | [arxiv-1909.06312#c11](https://arxiv.org/pdf/1909.06312v2#page=4 "with weights computed as entmax over the learnable feature selection matrix") |
| $M[i] = \mathrm{sparsemax}(P[i-1] \cdot h_i(a[i-1]))$、$P[i] = \prod (\gamma - M[j])$ | TabNet のマスクと事前スケール | [arxiv-1908.07442#c10](https://arxiv.org/pdf/1908.07442v5#page=3 "is the prior scale term, denoting how much a particular feature") |
| $x_{l+1} = x_0 \odot (W_l x_l + b_l) + x_l$ | 交差層 | [arxiv-2008.13535#c10](https://arxiv.org/pdf/2008.13535v2#page=3 "The core of DCN-V2 lies in the cross layers that create explicit feature crosses.") |
| $e_t$(0、1、区間内の位置)| 区分線形の符号化 | [arxiv-2203.05556#c10](https://arxiv.org/pdf/2203.05556v4#page=4 "where PLE stands for “peicewise linear
encoding”.") |
| $[\sin(2\pi c x), \cos(2\pi c x)]$ | 周期的な埋め込み | [arxiv-2203.05556#c3](https://arxiv.org/pdf/2203.05556v4#page=5 "We observe that σ is an important hyperparameter.") |
| $S = -\Vert W_K(\tilde{x}) - W_K(\tilde{x}_i) \Vert^2 d^{-1/2}$ | 近傍の似ている度合い | [arxiv-2307.14338#c10](https://arxiv.org/pdf/2307.14338v2#page=5 "Empirically, we observed that removing the notion of queries (i.e. removing WQ) and using the L2 distance instead of the dot product significantly improves performance on several datasets in Table 2:") |

## 参照カード

- [arxiv-1909.06312](../../papers/arxiv-1909.06312.yaml) Popov, Morozov & Babenko, "Neural Oblivious Decision Ensembles for Deep Learning on Tabular Data"
- [arxiv-1908.07442](../../papers/arxiv-1908.07442.yaml) Arik & Pfister, "TabNet: Attentive Interpretable Tabular Learning"
- [arxiv-2008.13535](../../papers/arxiv-2008.13535.yaml) Wang et al., "DCN V2"
- [arxiv-1810.11921](../../papers/arxiv-1810.11921.yaml) Song et al., "AutoInt"
- [arxiv-2203.05556](../../papers/arxiv-2203.05556.yaml) Gorishniy, Rubachev & Babenko, "On Embeddings for Numerical Features in Tabular Deep Learning"
- [arxiv-2307.14338](../../papers/arxiv-2307.14338.yaml) Gorishniy et al., "TabR: Tabular Deep Learning Meets Nearest Neighbors in 2023"
- [arxiv-2106.15147](../../papers/arxiv-2106.15147.yaml) Bahri et al., "SCARF: Self-Supervised Contrastive Learning using Random Feature Corruption"
