---
title: 数式の解説 13 — AutoML とアーキテクチャ探索:CASH、TPE、REINFORCE と基準値、DARTS の緩和と近似、順位の一致、アンサンブル選択
kind: math
tags: [automl-systems, neural-architecture-search]
depends_on: [arxiv-1208.3719, arxiv-1611.01578, arxiv-1401.0118, arxiv-1802.01548, arxiv-1806.09055, arxiv-1902.08142, arxiv-2006.13799]
written_at: 2026-10-10
written_by: claude-opus-5-5 via Claude Code
---

# 数式の解説 13 — AutoML とアーキテクチャ探索:CASH、TPE、REINFORCE と基準値、DARTS の緩和と近似、順位の一致、アンサンブル選択

<!-- generated:stale -->
> ⚠ この記事の執筆日(2026-10-10)以降に作成された関連カードが 10 件あります(未反映。執筆日と同じ日に作成されたカードを含む): `arxiv-1603.06212`, `arxiv-1802.03268`, `arxiv-1808.05377`, `arxiv-1902.09635`, `arxiv-1907.00909`, `arxiv-1908.00709`, `arxiv-1909.09656`, `arxiv-1911.04706`, `arxiv-2003.06505`, `arxiv-2207.12560`
<!-- /generated:stale -->

## この記事の読み方

[AutoML システムとアーキテクチャ探索](../methods/automl-systems.md) の記事で扱った手法の式を解説する。

使う道具(Σ、argmin、確率、対数の微分、勾配降下法)は [準備の記事](00-preliminaries.md)、ソフトマックスは [数式の解説 3](03-uncertainty-and-calibration.md)、スコア関数による勾配は [数式の解説 6](06-approximate-inference.md) の1節で説明している。

- 式は論文から取り、根拠のカード(論文の該当ページへのリンク)を付けている。
- 「**補足**」と書いた計算は、論文には書かれていない、この記事による説明である。

## 1. ハイパーパラメータ最適化と CASH

### 交差検証の平均を最小にする

Auto-WEKA は、ハイパーパラメータ最適化を次のように書いている [arxiv-1208.3719#c10](https://arxiv.org/pdf/1208.3719v2#page=2 "Given such a structured space Λ, the (hierarchical) hyperparameter optimization problem can be written as:")。

$$
\lambda^* \in \arg\min_{\lambda \in \Lambda} \ \frac{1}{k} \sum_{i=1}^{k} \mathcal{L}\big( A_\lambda,\ D^{(i)}_{\text{train}},\ D^{(i)}_{\text{valid}} \big)
$$

- $A_\lambda$ はハイパーパラメータ $\lambda$ を設定した学習アルゴリズム、$\Lambda$ はハイパーパラメータの空間である。
- $D^{(i)}_{\text{train}}$ と $D^{(i)}_{\text{valid}}$ は、$k$ 分割交差検証の $i$ 番目の学習用と検証用のデータで、$\mathcal{L}$ は検証用データでの損失である。
- つまり、「交差検証の平均の損失が最小になる設定を選ぶ」という式である。

$\Lambda$ には、ある値が選ばれたときだけ意味を持つ**条件付き**のハイパーパラメータが含まれ、木のような構造をしている [arxiv-1208.3719#c10](https://arxiv.org/pdf/1208.3719v2#page=2 "Given such a structured space Λ, the (hierarchical) hyperparameter optimization problem can be written as:")。

### CASH:アルゴリズムの選択も1つのハイパーパラメータにする

アルゴリズムの集合 $\{A^{(1)}, \ldots, A^{(k)}\}$ のどれを使うかも、最上位の1つのハイパーパラメータとみなす。各アルゴリズムのハイパーパラメータは、そのアルゴリズムが選ばれたときだけ意味を持つ条件付きのものになる。こうすると、アルゴリズムの選択とハイパーパラメータの最適化(CASH)が、上の式と同じ形の1つの問題になる [arxiv-1208.3719#c1](https://arxiv.org/pdf/1208.3719v2#page=2 "We note that this problem can be reformulated as a single combined hierarchical hyperparameter optimization problem")。

**補足(例)**:「ランダムフォレストか SVM か」を最上位の選択にすると、ランダムフォレストの木の数は「ランダムフォレストが選ばれたとき」だけ、SVM のカーネルの幅は「SVM が選ばれたとき」だけ意味を持つ。

## 2. TPE:良い設定と悪い設定の密度の比

TPE は、これまでに試した設定を、損失がある閾値より小さい「良い」設定と、それ以外の「悪い」設定に分け、それぞれの密度 $\ell(\lambda)$ と $g(\lambda)$ を推定する。閾値は損失の $\gamma$ 分位点で、Auto-WEKA の既定値は $\gamma = 0.15$ である [arxiv-1208.3719#c3](https://arxiv.org/pdf/1208.3719v2#page=3 "Note that this means that TPE assumes independence for hyperparameters that do not appear together along any path from the tree’s root to one of its leaves.")。
このとき、期待改善量は次の量に比例する [arxiv-1208.3719#c11](https://arxiv.org/pdf/1208.3719v2#page=3 "TPE maximizes this expression by generating many candi-
date hyperparameter conﬁgurations at random and picking")。

$$
E[I(\lambda)] \ \propto \ \left( \gamma + \frac{g(\lambda)}{\ell(\lambda)} (1 - \gamma) \right)^{-1}
$$

右辺は $g(\lambda) / \ell(\lambda)$ が小さいほど大きい。そこで TPE は、多数の候補をランダムに作り、$g / \ell$ が最小のものを次に試す [arxiv-1208.3719#c11](https://arxiv.org/pdf/1208.3719v2#page=3 "TPE maximizes this expression by generating many candi-
date hyperparameter conﬁgurations at random and picking")。

**補足(例)**:$\gamma = 0.15$ で、候補 A は $\ell = 0.6$、$g = 0.2$($g/\ell \approx 0.333$)、候補 B は $\ell = 0.2$、$g = 0.6$($g/\ell = 3$)とする。

$$
\text{A}:\ \frac{1}{0.15 + 0.333 \times 0.85} \approx 2.31, \qquad \text{B}:\ \frac{1}{0.15 + 3 \times 0.85} \approx 0.37
$$

「良い設定の近くにあり、悪い設定から離れている」A が選ばれる。

期待改善量そのものは [数式の解説 4](04-bayes.md) の2節で説明した。TPE は、ガウス過程の代わりに2つの密度の比でそれを計算している。

## 3. REINFORCE:微分できない報酬の勾配

### 方策勾配

Zoph と Le の制御器は、ネットワークの構造を、行動 $a_1, \ldots, a_T$ の列として確率的に生成する。報酬 $R$(生成した構造を学習した検証の正確さ)は微分できないので、REINFORCE で勾配を推定する [arxiv-1611.01578#c2](https://arxiv.org/pdf/1611.01578v2#page=4 "In this work, our baseline b is an exponential moving average of the previous architecture accuracies.")。

$$
\nabla_{\theta_c} J \approx \frac{1}{m} \sum_{k=1}^{m} \sum_{t=1}^{T} \nabla_{\theta_c} \log P\big(a_t \mid a_{(t-1):1};\ \theta_c\big)\, \big(R_k - b\big)
$$

$m$ は1回の更新で試す構造の数、$R_k$ は $k$ 番目の構造の報酬、$\theta_c$ は制御器のパラメータである [arxiv-1611.01578#c9](https://arxiv.org/pdf/1611.01578v2#page=4 "As long as the baseline function b does not depend on the on the current action, then this is still an unbiased gradient estimate.")。

**補足(なぜこの形か)**:[数式の解説 6](06-approximate-inference.md) のブラックボックス変分推論と同じく、$\nabla p = p\, \nabla \log p$ という関係から、「報酬の期待値の勾配」を「報酬 × 対数確率の勾配」の期待値に書き換えている。報酬を微分する必要がない。

### 基準値 $b$

$b$ は**基準値**(ベースライン)で、論文ではこれまでの構造の正確さの指数移動平均を使う [arxiv-1611.01578#c2](https://arxiv.org/pdf/1611.01578v2#page=4 "In this work, our baseline b is an exponential moving average of the previous architecture accuracies.")。基準値が現在の行動に依存しなければ、引いても推定は偏らず、ばらつきだけが小さくなる [arxiv-1611.01578#c9](https://arxiv.org/pdf/1611.01578v2#page=4 "As long as the baseline function b does not depend on the on the current action, then this is still an unbiased gradient estimate.")。

**補足(なぜ偏らないか)**:$E[\nabla \log P(a)] = \sum_a P(a)\, \frac{\nabla P(a)}{P(a)} = \nabla \sum_a P(a) = \nabla 1 = 0$ なので、$b \cdot \nabla \log P(a)$ の期待値は0になる。スコア関数の期待値が0になるこの性質は、ブラックボックス変分推論の制御変量でも使われている [arxiv-1401.0118#c5](https://arxiv.org/pdf/1401.0118v1#page=4 "This equation implies that good control variates have high covariance with the function whose expectation is being computed.")。

**補足(例)**:2つの行動 A、B をソフトマックスで選び、パラメータ $\theta$ を増やすと A の確率が上がるとする。今は $P(A) = P(B) = 0.5$ で、$\nabla_\theta \log P(A) = 1 - P(A) = 0.5$、$\nabla_\theta \log P(B) = -P(A) = -0.5$。報酬が $R_A = 0.9$、$R_B = 0.7$、基準値 $b = 0.8$ なら、

$$
\text{A}:\ 0.5 \times (0.9 - 0.8) = 0.05, \qquad \text{B}:\ (-0.5) \times (0.7 - 0.8) = 0.05
$$

で、どちらの試行も $\theta$ を増やす(A を選びやすくする)方向に働く。基準値より良い行動は強め、悪い行動は弱める。基準値がなければ、両方とも報酬が正なので、両方の確率を上げようとする力がぶつかり合い、推定のばらつきが大きくなる。

## 4. 年齢による進化

Real らの年齢による進化は、次の手順を繰り返す(論文の説明を手順に書き直したもの)[arxiv-1802.01548#c1](https://arxiv.org/pdf/1802.01548v7#page=3 "in this paper we prefer a novel approach: killing the oldest model in the population")。

1. 母集団からランダムに $S$ 個を選び、その中で最も良いものを親にする。
2. 親を少し変えた(突然変異させた)子を作り、学習・評価して母集団に加える。
3. 母集団から**最も古いもの**(最も早く学習したもの)を取り除く。

**補足(なぜ「最も悪いもの」ではないのか)**:最も悪いものを取り除くと、一度たまたま良い評価を得たモデルがずっと残る。最も古いものを取り除くと、良い構造でも子孫として何度も学習し直されて良い評価を得続けなければ生き残れない。著者らは、この仕組みが学習のノイズに対する一種の正則化として働く、と推測している [arxiv-1802.01548#c9](https://arxiv.org/pdf/1802.01548v7#page=7 "We can speculate that aging may help navigate the training noise in evolutionary experiments, as follows.")。

## 5. DARTS:離散的な選択を連続にする

### ソフトマックスによる緩和

DARTS は、各辺 $(i, j)$ で候補の演算の集合 $\mathcal{O}$ から1つを選ぶ代わりに、すべての演算をソフトマックスで重み付けして足す [arxiv-1806.09055#c10](https://arxiv.org/pdf/1806.09055v2#page=3 "To make the search space continuous, we relax the categorical choice of a particular operation to a softmax over all possible operations:")。

$$
\bar{o}^{(i,j)}(x) = \sum_{o \in \mathcal{O}} \frac{\exp\big(\alpha^{(i,j)}_o\big)}{\sum_{o' \in \mathcal{O}} \exp\big(\alpha^{(i,j)}_{o'}\big)}\, o(x)
$$

探索の最後に、各辺で重みが最大の演算だけを残して、離散的な構造に戻す [arxiv-1806.09055#c1](https://arxiv.org/pdf/1806.09055v2#page=3 "To make the search space continuous, we relax the categorical choice of a particular operation to a softmax over all possible operations:")。

**補足(例)**:候補が「3×3 畳み込み、最大プーリング、スキップ接続」の3つで、$\alpha = (1,\ 0,\ -1)$ なら、重みは約 $(0.665,\ 0.245,\ 0.090)$ で、出力はこの重みでの3つの出力の和になる。最後は畳み込みが残る。
ただし、探索中は重みの付いた和で学習しているのに、最後に1つだけを残すので、両者の性能にずれが生じうる。論文もこの食い違いを限界に挙げている [arxiv-1806.09055#c9](https://arxiv.org/pdf/1806.09055v2#page=9 "For example, the current method may suffer from discrepancies between the continuous architecture encoding and the derived discrete architecture.")。

### 二段階の最適化

構造のパラメータ $\alpha$ は検証の損失を、ネットワークの重み $w$ は学習の損失を最小にする [arxiv-1806.09055#c10](https://arxiv.org/pdf/1806.09055v2#page=3 "To make the search space continuous, we relax the categorical choice of a particular operation to a softmax over all possible operations:")。

$$
\min_\alpha \ \mathcal{L}_{\text{val}}\big(w^*(\alpha),\ \alpha\big) \qquad \text{subject to} \quad w^*(\alpha) = \arg\min_w \mathcal{L}_{\text{train}}(w, \alpha)
$$

内側の最適化を毎回最後まで解くのは高価なので、$w^*(\alpha)$ を**1ステップの学習**で近似する [arxiv-1806.09055#c11](https://arxiv.org/pdf/1806.09055v2#page=4 "denotes the weights for a one-step forward model.")。

$$
\nabla_\alpha \mathcal{L}_{\text{val}}\big(w^*(\alpha), \alpha\big) \ \approx \ \nabla_\alpha \mathcal{L}_{\text{val}}\big(w - \xi \nabla_w \mathcal{L}_{\text{train}}(w, \alpha),\ \alpha\big)
$$

$\xi$ は内側の学習率である。$\xi = 0$ にすると、今の重みを最適とみなす「1次の近似」になり、速いが性能は悪かった [arxiv-1806.09055#c4](https://arxiv.org/pdf/1806.09055v2#page=4 "This leads to some speed-up but empirically worse performance, according to our experimental results in Table 1 and Table 2.")。著者らは、この近似の収束の保証は知られていないと述べている [arxiv-1806.09055#c3](https://arxiv.org/pdf/1806.09055v2#page=4 "While we are not currently aware of the convergence guarantees for our optimization algorithm, in practice it is able to reach a ﬁxed point with a suitable choice of")。

**補足(連鎖律)**:$w' = w - \xi \nabla_w \mathcal{L}_{\text{train}}(w, \alpha)$ も $\alpha$ に依存するので、$\alpha$ で微分すると、$w'$ を通じた項 $-\xi\, \nabla^2_{\alpha, w} \mathcal{L}_{\text{train}}\, \nabla_{w'} \mathcal{L}_{\text{val}}$ が加わる。この2階微分の項は差分で近似する [arxiv-1806.09055#c11](https://arxiv.org/pdf/1806.09055v2#page=4 "denotes the weights for a one-step forward model.")。

## 6. 順位の一致:ケンドールの τ

重み共有で評価した構造の順位が、ゼロから学習したときの順位とどれだけ一致するかを、Yu らはケンドールの順位相関係数 τ で測った [arxiv-1902.08142#c7](https://arxiv.org/pdf/1902.08142v3#page=2 "the architecture rankings obtained with and without weight sharing are entirely uncorrelated in RNN space")。

**補足(定義)**:$n$ 個のものの2通りの順位について、すべてのペア($n(n-1)/2$ 組)を調べ、順序が一致するペアの数を「一致」、逆になるペアの数を「不一致」とする。

$$
\tau = \frac{(\text{一致}) - (\text{不一致})}{n(n-1)/2}
$$

順位が完全に同じなら $\tau = 1$、完全に逆なら $\tau = -1$、無関係なら0に近い。

**補足(例)**:4つの構造の、ゼロから学習したときの順位が (1, 2, 3, 4)、重み共有での順位が (2, 1, 3, 4) なら、6つのペアのうち構造1と2のペアだけが逆なので、$\tau = (5 - 1)/6 \approx 0.67$。
τ が0に近いと、重み共有で選んだ「最良」の構造が、本当に良い構造である保証はほとんどない。

## 7. アンサンブルの貪欲な選択

Auto-PyTorch Tabular は、探索中に保存した上位のモデルから、Caruana 流の**アンサンブル選択**で組合せを作る [arxiv-2006.13799#c3](https://arxiv.org/pdf/2006.13799v3#page=4 "An advantage of our post-hoc ensembling is that we can also include other models besides DNNs easily.")。

**補足(手順)**:

1. 空のアンサンブルから始める。
2. 候補のモデルのうち、アンサンブルに加えたとき(同じモデルを何度加えてもよい)、検証データでの予測の平均の性能が最も良くなるものを1つ加える。
3. 決めた回数だけ2を繰り返す。

同じモデルを何度も加えられるので、結果は「モデルごとの重み(加えた回数の割合)を持つ平均」になる。

**補足(例)**:候補 A、B、C の検証の正確さがそれぞれ 0.80、0.78、0.70 でも、A と B が違う例を間違えるなら、A と B の平均が A 単独より良いことがある。貪欲な選択は、そうした補い合う組合せを見つける。
ただし、同じ検証データで何度も選ぶので、アンサンブルも検証データに過学習しうる。Auto-PyTorch の論文もこれを限界に挙げている [arxiv-2006.13799#c9](https://arxiv.org/pdf/2006.13799v3#page=10 "First of all, while the ensem-bles improve performance overall, it is also known that they can lead to overﬁtting.")。

## まとめ

| 式 | 何を表すか | 根拠 |
|---|---|---|
| $\lambda^* \in \arg\min \frac{1}{k}\sum_i \mathcal{L}(A_\lambda, D^{(i)}_{\text{train}}, D^{(i)}_{\text{valid}})$ | 交差検証によるハイパーパラメータ最適化 | [arxiv-1208.3719#c10](https://arxiv.org/pdf/1208.3719v2#page=2 "Given such a structured space Λ, the (hierarchical) hyperparameter optimization problem can be written as:") |
| $(\gamma + \frac{g}{\ell}(1-\gamma))^{-1}$ | TPE の期待改善量 | [arxiv-1208.3719#c11](https://arxiv.org/pdf/1208.3719v2#page=3 "TPE maximizes this expression by generating many candi-
date hyperparameter conﬁgurations at random and picking") |
| $\frac{1}{m}\sum_k \sum_t \nabla \log P(a_t \mid \cdot)(R_k - b)$ | REINFORCE と基準値 | [arxiv-1611.01578#c9](https://arxiv.org/pdf/1611.01578v2#page=4 "As long as the baseline function b does not depend on the on the current action, then this is still an unbiased gradient estimate.") |
| 最も古いものを取り除く | 年齢による進化 | [arxiv-1802.01548#c1](https://arxiv.org/pdf/1802.01548v7#page=3 "in this paper we prefer a novel approach: killing the oldest model in the population") |
| $\bar{o}(x) = \sum_o \mathrm{softmax}(\alpha)_o\, o(x)$ | DARTS の連続的な緩和 | [arxiv-1806.09055#c10](https://arxiv.org/pdf/1806.09055v2#page=3 "To make the search space continuous, we relax the categorical choice of a particular operation to a softmax over all possible operations:") |
| $\nabla_\alpha \mathcal{L}_{\text{val}}(w - \xi \nabla_w \mathcal{L}_{\text{train}}, \alpha)$ | 1ステップの近似 | [arxiv-1806.09055#c11](https://arxiv.org/pdf/1806.09055v2#page=4 "denotes the weights for a one-step forward model.") |
| ケンドールの τ | 2つの順位の一致度 | [arxiv-1902.08142#c7](https://arxiv.org/pdf/1902.08142v3#page=2 "the architecture rankings obtained with and without weight sharing are entirely uncorrelated in RNN space") |

## 参照カード

- [arxiv-1208.3719](../../papers/arxiv-1208.3719.yaml) Thornton et al., "Auto-WEKA: Combined Selection and Hyperparameter Optimization of Classification Algorithms"
- [arxiv-1611.01578](../../papers/arxiv-1611.01578.yaml) Zoph & Le, "Neural Architecture Search with Reinforcement Learning"
- [arxiv-1401.0118](../../papers/arxiv-1401.0118.yaml) Ranganath, Gerrish & Blei, "Black Box Variational Inference"
- [arxiv-1802.01548](../../papers/arxiv-1802.01548.yaml) Real et al., "Regularized Evolution for Image Classifier Architecture Search"
- [arxiv-1806.09055](../../papers/arxiv-1806.09055.yaml) Liu, Simonyan & Yang, "DARTS: Differentiable Architecture Search"
- [arxiv-1902.08142](../../papers/arxiv-1902.08142.yaml) Yu et al., "Evaluating the Search Phase of Neural Architecture Search"
- [arxiv-2006.13799](../../papers/arxiv-2006.13799.yaml) Zimmer, Lindauer & Hutter, "Auto-PyTorch Tabular"
