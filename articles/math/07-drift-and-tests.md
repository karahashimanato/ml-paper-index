---
title: 数式の解説 7 — ドリフト検知と統計的検定:分布の変化の定義、KS 検定、Bonferroni 補正、MMD
kind: math
tags: [drift-detection, concept-drift-detection, dataset-shift-detection]
depends_on: [arxiv-2004.05785, arxiv-2310.15826, arxiv-1810.11953, arxiv-2602.06456]
written_at: 2026-10-10
written_by: claude-opus-5-5 via Claude Code
---

# 数式の解説 7 — ドリフト検知と統計的検定:分布の変化の定義、KS 検定、Bonferroni 補正、MMD

<!-- generated:stale -->
> ⚠ この記事の執筆後(2026-10-10)に、関連カードが 17 件追加されています(未反映): `arxiv-1610.02136`, `arxiv-1812.04606`, `arxiv-1906.02530`, `arxiv-2007.06299`, `arxiv-2107.03315`, `arxiv-2201.04234`, `arxiv-2311.06396`, `arxiv-2606.07789`, `arxiv-2608.08245`, `arxiv-2608.17824`, `arxiv-2609.04388`, `arxiv-2609.09432`, `arxiv-2609.25340`, `arxiv-2609.33940`, `arxiv-2609.39473`, `doi-10.1007_s41060-024-00620-y`, `doi-10.1007_s44163-026-02063-9`
<!-- /generated:stale -->

## この記事の読み方

[概念ドリフトとデータシフトの検出](../tasks/drift-detection.md) の記事で扱った、「データの分布が変わったか」を判定する式を解説する。

- まず「ドリフト」を確率の言葉で定義する。
- 次に、2つのデータの集まりが同じ分布から来たかを調べる**二標本検定**の式を見る。

使う道具(条件付き確率、独立、期待値)は [準備の記事](00-preliminaries.md)、カーネルは [数式の解説 5](05-linear-and-kernel.md) の3節で説明している。

- 式は論文から取り、根拠のカード(論文の該当ページへのリンク)を付けている。
- 「**補足**」と書いた計算は、論文には書かれていない、この記事による説明である。

## 1. ドリフトの定義

### 同時分布の変化

時刻 $t$ でのデータ $X$ とラベル $y$ の同時分布を $P_t(X, y)$ と書く。Lu らのサーベイは、ある時刻 $t$ で $P_t(X, y) \ne P_{t+1}(X, y)$ となることを**コンセプトドリフト**と定義している [arxiv-2004.05785#c3](https://arxiv.org/pdf/2004.05785v1#page=3 "concept drift at time t can be defined as the change of joint probability of X and y at time t.")。

同時分布は、$X$ の分布と、$X$ が与えられたときの $y$ の条件付き分布に分けられる。このため、ドリフトの原因は3通りに分けられる [arxiv-2004.05785#c15](https://arxiv.org/pdf/2004.05785v1#page=3 "concept drift can be triggered by three sources:")。

$$
P_t(X, y) = P_t(X) \times P_t(y \mid X)
$$

| 種類 | 変わるもの | 変わらないもの | 呼び名 |
|---|---|---|---|
| Source I | $P_t(X)$ | $P_t(y \mid X)$ | 仮想ドリフト(決定境界は動かない)|
| Source II | $P_t(y \mid X)$ | $P_t(X)$ | 実ドリフト(決定境界が動く)|
| Source III | 両方 | — | 両者の混合 |

$P_t(X)$ だけの変化は決定境界を動かさないので、仮想ドリフトと呼ばれる [arxiv-2004.05785#c4](https://arxiv.org/pdf/2004.05785v1#page=3 "drift does not affect the decision boundary, it has also been considered as virtual drift")。

**補足(例)**:迷惑メールの判定で、送られてくるメールの話題の割合が変わっても、「この文面なら迷惑メール」という関係が同じなら Source I である。同じ文面でも迷惑メールかどうかの基準が変われば Source II である。

### 「時刻とデータが独立でない」という定義

Hinder らは、サンプルに基づく定義には問題があると指摘している。同じデータ源から同じ期間に、異なる頻度でサンプルをとると、一方にはドリフトがあり、他方にはない、ということが起こりうる。そこで、時刻 $T$ も確率変数として扱う [arxiv-2310.15826#c11](https://arxiv.org/pdf/2310.15826v1#page=3 "In particular, it might happen that if we take two samples from the same data source over the same period of time using different sampling frequencies, one sample will have concept drift and the other will not.")。

この枠組みで、ドリフトがないことは、**時刻 $T$ とデータ $X$ が独立であること**と同値になる(論文の定理1)[arxiv-2310.15826#c12](https://arxiv.org/pdf/2310.15826v1#page=4 "One of the key findings however, which allows the development of new methods, is that drift can equivalently be formulated as data X and time T are dependent, i.e., not statistically independent:")。

$$
\text{ドリフトがない} \iff T \perp\!\!\!\perp X
$$

ドリフトがあるのは、ある時間の区間 $W$ とデータの集合 $A$ について次が成り立つときである。

$$
P[T \in W,\ X \in A] \ne P[T \in W] \, P[X \in A]
$$

**補足(読み方)**:独立とは「データを見ても、それがいつのデータかの手がかりにならない」ことである。逆に、データから時刻をある程度当てられるなら、時刻によって分布が違う、つまりドリフトがある。
Rabanser らが使っている「元のデータか新しいデータかを見分ける分類器」(ドメイン分類器)は、この考え方を実装したものと読める [arxiv-1810.11953#c7](https://arxiv.org/pdf/1810.11953v4#page=1 "we demonstrate that domain-discriminating approaches tend to be helpful for characterizing shifts qualitatively and determining if they are harmful.")。

## 2. 検定としてのドリフト検知

### 帰無仮説と2種類の誤り

ドリフト検知は統計的検定とみなせる。帰無仮説は「すべての時刻 $t, s$ で $D_t = D_s$(分布が同じ)」である [arxiv-2310.15826#c13](https://arxiv.org/pdf/2310.15826v1#page=7 "A type I error occurs if there is no drift but we detect one (false alarm), and a type II error occurs if there is drift but we do not detect it.")。

| | ドリフトなし | ドリフトあり |
|---|---|---|
| 検知した | **第1種の誤り**(誤報) | 正しい検知 |
| 検知しない | 正しい | **第2種の誤り**(見逃し) |

ごく小さなドリフトまで見逃さないことは不可能なので、Hinder らは第1種の誤り(誤報)を抑えることに注目している [arxiv-2310.15826#c13](https://arxiv.org/pdf/2310.15826v1#page=7 "A type I error occurs if there is no drift but we detect one (false alarm), and a type II error occurs if there is drift but we do not detect it.")。

**補足(p 値と有意水準)**:**p 値**は、帰無仮説が正しいとしたときに、観測したもの以上に極端な結果が出る確率である。p 値が**有意水準** $\alpha$ より小さいときに帰無仮説を棄却する(=ドリフトを検知する)と決めておけば、帰無仮説が正しいときに誤って棄却する確率(誤報の確率)は $\alpha$ 以下に抑えられる。

### 二標本検定とのつながり

Lu らは、データを取り出す段階を除けば、ドリフト検知は二標本検定の問題とみなせると述べている [arxiv-2004.05785#c5](https://arxiv.org/pdf/2004.05785v1#page=4 "the concept drift detection problem can be considered as a two-sample test problem which examines whether the population of two given sample sets are from the same distribution")。
「以前のデータ」と「新しいデータ」が同じ分布から来たかを検定すればよい。

## 3. KS 検定と Bonferroni 補正

### KS 統計量

1次元のデータについて、2つのサンプルの**経験累積分布関数**の差の最大値を統計量とする [arxiv-1810.11953#c17](https://arxiv.org/pdf/1810.11953v4#page=4 "Under the null hypothesis, Z follows the Kolmogorov distribution.")。

$$
Z = \sup_z \left| F_p(z) - F_q(z) \right|
$$

- $F_p(z)$ は、元のデータのうち $z$ 以下の値の割合である。$F_q(z)$ は新しいデータについて同じものである。
- $\sup$ は「最大値」とほぼ同じ意味(最大値がない場合も含めた上限)である。
- 帰無仮説のもとで、$Z$ はコルモゴロフ分布という既知の分布に従うので、p 値を計算できる [arxiv-1810.11953#c17](https://arxiv.org/pdf/1810.11953v4#page=4 "Under the null hypothesis, Z follows the Kolmogorov distribution.")。

**補足(例)**:元のデータが $\{1, 2, 3, 4\}$、新しいデータが $\{3, 4, 5, 6\}$ のとき

| $z$ の範囲 | $F_p(z)$ | $F_q(z)$ | 差 |
|---|---|---|---|
| $2 \le z < 3$ | $0.5$ | $0$ | $0.5$ |
| $3 \le z < 4$ | $0.75$ | $0.25$ | $0.5$ |
| $4 \le z < 5$ | $1$ | $0.5$ | $0.5$ |
| $5 \le z < 6$ | $1$ | $0.75$ | $0.25$ |

で、$Z = 0.5$ になる。全体がずれているほど $Z$ は大きくなる。

### 多次元のときの Bonferroni 補正

データが $K$ 次元なら、各次元で KS 検定を行い、$K$ 個の p 値を得る。Rabanser らは、検定どうしの依存関係を仮定できないので、保守的な **Bonferroni 補正**を使っている。$K$ 個の p 値の最小値が $\alpha / K$ より小さいときに帰無仮説を棄却する [arxiv-1810.11953#c18](https://arxiv.org/pdf/1810.11953v4#page=4 "As we cannot make strong assumptions about the (in)dependence among the tests, we rely on a conservative aggregation method, notably the Bonferroni correction [4], which rejects the null hypothesis if the minimum p-value among all tests is less than α/K")。

**補足(なぜ $\alpha / K$ か)**:各検定の誤報の確率が $\alpha / K$ 以下なら、「どれか1つでも誤報する」確率は、和の上限(確率の和の法則 $P(A \cup B) \le P(A) + P(B)$)から $K \times \alpha / K = \alpha$ 以下になる。これは検定どうしが独立かどうかに関係なく成り立つ。その代わり、検定どうしに強い相関があると必要以上に厳しくなる。これが「保守的」の意味である。
たとえば $\alpha = 0.05$、$K = 10$ なら、1つの検定あたりのしきい値は $0.005$ になる。

Rabanser らの実験では、このように1次元の検定をまとめる方法が、多変量のカーネル検定(MMD)と同程度の性能だった [arxiv-1810.11953#c3](https://arxiv.org/pdf/1810.11953v4#page=6 "despite the heavy correction, multiple univariate testing seem to offer comparable performance to multivariate testing")。

## 4. MMD:カーネルを使った多変量の検定

### 定義

**MMD**(Maximum Mean Discrepancy)は、2つの分布 $p$ と $q$ を、カーネルで決まる空間での「平均」の違いで比べる [arxiv-1810.11953#c15](https://arxiv.org/pdf/1810.11953v4#page=4 "MMD allows us to distinguish between two probability distributions p and q based on the mean embeddings µp and µq of the distributions in a reproducing kernel Hilbert space F, formally")。

$$
\mathrm{MMD}(\mathcal{F}, p, q) = \Vert \mu_p - \mu_q \Vert_{\mathcal{F}}^2
$$

$\mu_p$ は、分布 $p$ のデータを特徴量の空間に写したときの平均(平均埋め込み)である。

### サンプルからの推定

$p$ から $m$ 個のサンプル $x_i$、$q$ から $n$ 個のサンプル $x'_j$ があるとき、2乗 MMD の不偏推定量は次のようになる [arxiv-1810.11953#c15](https://arxiv.org/pdf/1810.11953v4#page=4 "MMD allows us to distinguish between two probability distributions p and q based on the mean embeddings µp and µq of the distributions in a reproducing kernel Hilbert space F, formally")。

$$
\widehat{\mathrm{MMD}}^2 = \frac{1}{m^2 - m} \sum_{i=1}^{m} \sum_{j \ne i} \kappa(x_i, x_j) + \frac{1}{n^2 - n} \sum_{i=1}^{n} \sum_{j \ne i} \kappa(x'_i, x'_j) - \frac{2}{mn} \sum_{i=1}^{m} \sum_{j=1}^{n} \kappa(x_i, x'_j)
$$

- 1つ目の項は「$p$ のサンプルどうしの似ている度合いの平均」、2つ目は「$q$ のサンプルどうし」、3つ目は「$p$ と $q$ の間」である。
- 同じ分布なら3つの平均はほぼ等しく、$1 + 1 - 2 = 0$ に近くなる。違う分布なら、仲間どうしが似ていて相手とは似ていないので、正の値になる。

Rabanser らは、カーネルに $\kappa(x, \tilde{x}) = \exp(-\Vert x - \tilde{x} \Vert^2 / \sigma)$ を使い、$\sigma$ を全サンプルの点の間の距離の中央値に設定している。p 値は、カーネル行列に対する**並べ替え検定**で求める [arxiv-1810.11953#c16](https://arxiv.org/pdf/1810.11953v4#page=4 "A p-value can then be obtained by carrying out a permutation test on the resulting kernel matrix.")。

**補足(カーネルの選び方)**:カーネルを $\kappa(x, x') = x x'$(1次元の積)にすると、$\Vert \mu_p - \mu_q \Vert^2$ は平均の差の2乗 $(E_p[x] - E_q[x])^2$ になる。この場合は平均しか比べられない。指数関数のカーネルを使うと、平均以外の分布の違いも捉えられる。

**補足(並べ替え検定)**:2つのサンプルを1つに混ぜ、ランダムに $m$ 個と $n$ 個に分け直して $\widehat{\mathrm{MMD}}^2$ を計算する、ということを何度も繰り返す。帰無仮説(同じ分布)が正しければ、元の分け方は「ランダムな分け方の1つ」と区別がつかないはずである。元の値が、分け直した値の中でどれだけ大きい側にあるかの割合が p 値になる。

### 注意

- Rabanser らは、カーネル二標本検定はサンプル数が多いと計算が重く、高次元では検出力が落ちると述べている [arxiv-1810.11953#c9](https://arxiv.org/pdf/1810.11953v4#page=2 "they scale badly with dataset size and their statistical power is known to decay badly with high ambient dimension")。
- 次元を減らさずにそのまま多変量検定をすると、性能が悪かった [arxiv-1810.11953#c6](https://arxiv.org/pdf/1810.11953v4#page=6 "the multivariate test performs poorly in the no reduction case")。

## 5. 誤り率に基づく検知と窓の問題

ラベルがすぐ手に入る場合は、分類器の**オンラインの誤り率**を追跡し、それが有意に上がったらドリフトとみなす方法がよく使われる。これが最も大きな分類である [arxiv-2004.05785#c7](https://arxiv.org/pdf/2004.05785v1#page=4 "error rate-based drift detection algorithms form the largest category of algorithms.")。DDM は、警告レベルとドリフトレベルの2段階を初めて定義した手法である [arxiv-2004.05785#c8](https://arxiv.org/pdf/2004.05785v1#page=4 "the first algorithm to define the warning level and drift")。

どの方法でも、データを**窓**(時間の区間)で区切って比べる。Gower-Winter らは、検知されるドリフトは窓の区切り方の産物であって、必ずしもデータを生成する過程の変化を表すとは限らないと指摘している(「窓のジレンマ」)[arxiv-2602.06456#c2](https://arxiv.org/pdf/2602.06456v1#page=1 "perceived drift is a product of windowing and not necessarily the underlying data generating process.")。
これは、1節の Hinder らの「サンプルのとり方でドリフトの有無が変わりうる」という指摘 [arxiv-2310.15826#c11](https://arxiv.org/pdf/2310.15826v1#page=3 "In particular, it might happen that if we take two samples from the same data source over the same period of time using different sampling frequencies, one sample will have concept drift and the other will not.") と同じ方向の問題である。

## まとめ

| 式 | 何を表すか | 根拠 |
|---|---|---|
| $P_t(X, y) \ne P_{t+1}(X, y)$ | コンセプトドリフト | [arxiv-2004.05785#c3](https://arxiv.org/pdf/2004.05785v1#page=3 "concept drift at time t can be defined as the change of joint probability of X and y at time t.") |
| $P_t(X, y) = P_t(X)\, P_t(y \mid X)$ | ドリフトの原因の3分類 | [arxiv-2004.05785#c15](https://arxiv.org/pdf/2004.05785v1#page=3 "concept drift can be triggered by three sources:") |
| ドリフトなし $\iff T \perp\!\!\!\perp X$ | 時刻とデータの独立 | [arxiv-2310.15826#c12](https://arxiv.org/pdf/2310.15826v1#page=4 "One of the key findings however, which allows the development of new methods, is that drift can equivalently be formulated as data X and time T are dependent, i.e., not statistically independent:") |
| $Z = \sup_z \lvert F_p(z) - F_q(z) \rvert$ | KS 統計量 | [arxiv-1810.11953#c17](https://arxiv.org/pdf/1810.11953v4#page=4 "Under the null hypothesis, Z follows the Kolmogorov distribution.") |
| $\min p < \alpha / K$ | Bonferroni 補正 | [arxiv-1810.11953#c18](https://arxiv.org/pdf/1810.11953v4#page=4 "As we cannot make strong assumptions about the (in)dependence among the tests, we rely on a conservative aggregation method, notably the Bonferroni correction [4], which rejects the null hypothesis if the minimum p-value among all tests is less than α/K") |
| $\Vert \mu_p - \mu_q \Vert^2$ とその不偏推定 | MMD | [arxiv-1810.11953#c15](https://arxiv.org/pdf/1810.11953v4#page=4 "MMD allows us to distinguish between two probability distributions p and q based on the mean embeddings µp and µq of the distributions in a reproducing kernel Hilbert space F, formally") |

## 参照カード

- [arxiv-2004.05785](../../papers/arxiv-2004.05785.yaml) Lu et al., "Learning under Concept Drift: A Review"
- [arxiv-2310.15826](../../papers/arxiv-2310.15826.yaml) Hinder, Vaquet & Hammer, "One or Two Things We know about Concept Drift -- A Survey on Monitoring Evolving Environments"
- [arxiv-1810.11953](../../papers/arxiv-1810.11953.yaml) Rabanser, Günnemann & Lipton, "Failing Loudly: An Empirical Study of Methods for Detecting Dataset Shift"
- [arxiv-2602.06456](../../papers/arxiv-2602.06456.yaml) Gower-Winter, Groen & Krempl, "The Window Dilemma: Why Concept Drift Detection is Ill-Posed"
