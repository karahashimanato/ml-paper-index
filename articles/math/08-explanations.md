---
title: 数式の解説 8 — 説明手法:シャープレイ値と SHAP、LIME、積分勾配、観測的と介入的の違い
kind: math
tags: [feature-attribution, model-explanation]
depends_on: [arxiv-1705.07874, arxiv-1602.04938, arxiv-1703.01365, arxiv-2006.16234, arxiv-2002.11097]
written_at: 2026-10-10
written_by: claude-opus-5-5 via Claude Code
---

# 数式の解説 8 — 説明手法:シャープレイ値と SHAP、LIME、積分勾配、観測的と介入的の違い

<!-- generated:stale -->
> ⚠ この記事の執筆後(2026-10-10)に、関連カードが 21 件追加されています(未反映): `arxiv-1511.05741`, `arxiv-1806.10758`, `arxiv-1810.03292`, `arxiv-1811.10154`, `arxiv-1902.10186`, `arxiv-1903.05179`, `arxiv-1905.04610`, `arxiv-1908.04626`, `arxiv-1909.09223`, `arxiv-1911.02508`, `arxiv-2001.04295`, `arxiv-2003.03629`, `arxiv-2004.13912`, `arxiv-2007.06299`, `arxiv-2202.01602`, `arxiv-2608.05265`, `arxiv-2609.24278`, `doi-10.1186_s44147-026-01203-3`, `doi-10.3389_fpsyg.2026.1875261`, `doi-10.3389_fpubh.2026.1911565`, `doi-10.36079_lamintang.ijortas-0802.1081`
<!-- /generated:stale -->

## この記事の読み方

[モデルの解釈可能性](../topics/model-interpretability.md) の記事で扱った、「この予測にどの特徴量がどれだけ効いたか」を数で表す方法(**特徴量の帰属**)の式を解説する。

使う道具(Σ、偏微分、定積分、条件付き期待値)は [準備の記事](00-preliminaries.md) で説明している。

- 式は論文から取り、根拠のカード(論文の該当ページへのリンク)を付けている。
- 「**補足**」と書いた計算は、論文には書かれていない、この記事による説明である。

## 1. 共通の形:加法的な特徴量の帰属

Lundberg と Lee は、多くの説明手法が次の形をしていることを指摘した [arxiv-1705.07874#c8](https://arxiv.org/pdf/1705.07874v2#page=2 "Methods with explanation models matching Deﬁnition 1 attribute an effect φi to each feature, and summing the effects of all feature attributions approximates the output f(x) of the original model.")。

$$
g(z') = \phi_0 + \sum_{i=1}^{M} \phi_i z'_i, \qquad z' \in \{0, 1\}^M
$$

- $z'_i$ は「特徴量 $i$ がある(1)か、ない(0)か」を表す単純化した入力である。
- $\phi_i$ が特徴量 $i$ の**帰属**(効き具合)で、$\phi_0$ は基準の値である。
- 帰属をすべて足すと、元のモデルの出力 $f(x)$ を近似する [arxiv-1705.07874#c8](https://arxiv.org/pdf/1705.07874v2#page=2 "Methods with explanation models matching Deﬁnition 1 attribute an effect φi to each feature, and summing the effects of all feature attributions approximates the output f(x) of the original model.")。

## 2. シャープレイ値

### 協力ゲームの考え方

シャープレイ値は、協力ゲーム理論で「チームで得た報酬を、メンバーの貢献に応じて分ける」ための値である。
特徴量をメンバー、特徴量の集合 $S$ がわかっているときのモデルの出力 $v(S)$ を報酬とみなす。

特徴量を1つずつ加えていく**順番**を考え、特徴量 $i$ が加わったときの報酬の増え方を、すべての順番について平均する [arxiv-2006.16234#c9](https://arxiv.org/pdf/2006.16234v1#page=1 "where R is one possible permutation of the order in which the players join the coalition, SR is the set of players joining the coalition before player i")。

$$
\phi_i = \frac{1}{M!} \sum_{R} \big[ v(S_R \cup \{i\}) - v(S_R) \big]
$$

$R$ は $M$ 個の特徴量の並べ方($M!$ 通り)、$S_R$ はその並べ方で $i$ より前に加わった特徴量の集合である。

### 部分集合で書いた形

同じ値を、部分集合についての和で書くこともできる [arxiv-1705.07874#c9](https://arxiv.org/pdf/1705.07874v2#page=3 "They are a weighted average of all possible differences:")。

$$
\phi_i = \sum_{S \subseteq F \setminus \{i\}} \frac{|S|!\,(|F| - |S| - 1)!}{|F|!} \big[ v(S \cup \{i\}) - v(S) \big]
$$

**補足(重みの意味)**:$i$ より前に $S$ の特徴量がちょうど並ぶ並べ方は、$S$ の中の並べ方が $|S|!$ 通り、$i$ より後の残りの並べ方が $(|F| - |S| - 1)!$ 通りある。それを全体の $|F|!$ で割ったのが重みである。つまり、1つ前の「順番の平均」の式を、部分集合ごとにまとめ直したものである。

**補足(例:特徴量が2つのとき)**:$v(\varnothing) = 10$(何もわからないときの予測の平均)、$v(\{1\}) = 14$、$v(\{2\}) = 12$、$v(\{1, 2\}) = 20$(実際の予測)とする。並べ方は「1→2」と「2→1」の2通りで、

$$
\phi_1 = \frac{1}{2}\big[ (14 - 10) + (20 - 12) \big] = 6, \qquad
\phi_2 = \frac{1}{2}\big[ (12 - 10) + (20 - 14) \big] = 4
$$

になる。$\phi_1 + \phi_2 = 10$ は、予測 $20$ と基準 $10$ の差にちょうど一致する。

### 3つの性質と一意性

Lundberg と Lee は、帰属に次の3つの性質を求めた。

- **局所的な正確さ**:説明したい入力で、説明のモデルが元のモデルに一致する。$f(x) = \phi_0 + \sum_i \phi_i x'_i$ [arxiv-1705.07874#c10](https://arxiv.org/pdf/1705.07874v2#page=4 "The explanation model g(x′) matches the original model f(x) when x = hx(x′).")。上の例で、足すと差に一致したのがこれである。
- **欠損**:入力にない特徴量の帰属は0。
- **一貫性**:モデルが変わって、ある特徴量の寄与が(他の特徴量によらず)増えるか同じなら、その帰属は減らない。

この3つを満たす加法的な帰属は、シャープレイ値ただ1つである(論文の定理1)[arxiv-1705.07874#c11](https://arxiv.org/pdf/1705.07874v2#page=4 "Theorem 1 follows from combined cooperative game theory results, where the values φi are known as Shapley values [6].")。論文は、シャープレイ値に基づかない方法は、局所的な正確さか一貫性のどちらかを破ることになると述べている [arxiv-1705.07874#c2](https://arxiv.org/pdf/1705.07874v2#page=4 "This result implies that methods not based on Shapley values violate local accuracy and/or consistency (methods in Section 2 already respect missingness).")。

### SHAP:報酬に条件付き期待値を使う

$v(S)$ をどう決めるかが問題である。モデルは「特徴量がない」入力を扱えないことが多い。
SHAP は、$S$ の特徴量だけがわかっているときの**モデルの出力の条件付き期待値**を使う [arxiv-1705.07874#c12](https://arxiv.org/pdf/1705.07874v2#page=4 "These are the Shapley values of a conditional expectation function of the original model; thus, they are the solution to Equation")。

$$
v(S) = E[f(z) \mid z_S]
$$

基準の値は、何もわからないときの期待値 $E[f(z)]$ になる。SHAP は、この基準の値から実際の出力 $f(x)$ までの差を、特徴量に分配している [arxiv-1705.07874#c12](https://arxiv.org/pdf/1705.07874v2#page=4 "These are the Shapley values of a conditional expectation function of the original model; thus, they are the solution to Equation")。
実用上の推定では、特徴量の独立やモデルの線形性を仮定して、この期待値の計算を簡単にすることがある [arxiv-1705.07874#c3](https://arxiv.org/pdf/1705.07874v2#page=5 "When using these methods, feature independence and model linearity are two optional assumptions simplifying the computation of the expected values")。

## 3. 観測的と介入的:報酬の決め方の違い

Chen らは、$v(S)$ の決め方を2つに分けている [arxiv-2006.16234#c8](https://arxiv.org/pdf/2006.16234v1#page=1 "There are two ways the model’s output (f : x ∈R/N/×1 →R1) for a particular sample is used to deﬁne v(S):")。

$$
\text{観測的:} \ v(S) = E[f(X) \mid X_S = x_S], \qquad
\text{介入的:} \ v(S) = E[f(X) \mid do(X_S = x_S)]
$$

- **観測的**:データの分布のもとで、$X_S = x_S$ という条件を付けた期待値。他の特徴量は、$x_S$ と相関した値をとる。
- **介入的**:$S$ の特徴量を $x_S$ に「設定」し、他の特徴量との依存関係を断ち切った期待値。他の特徴量は、元の分布のまま動く。

**補足(例:モデルが使っていない特徴量)**:モデルが $f(x) = x_1$ で、$x_2$ は $x_1$ とまったく同じ値をとる(完全に相関している)とする。

- 観測的:$v(\{2\}) = E[X_1 \mid X_2 = x_2] = x_2 = x_1$。$x_2$ だけがわかっても予測がわかるので、$x_2$ にも帰属が付く。
- 介入的:$x_2$ を設定しても $X_1$ は元の分布のまま動くので、$v(\{2\}) = E[X_1]$。$x_2$ の帰属は0になる。

Chen らは実データでも、線形モデルが使っていない特徴量に、観測的シャープレイ値では相関を通じて重要度が付く例を示している [arxiv-2006.16234#c3](https://arxiv.org/pdf/2006.16234v1#page=3 "This implies that even though BMI is not included in the model, the correlation between BMI and other features makes BMI important under observational Shapley values.")。
一方、Kumar らは、介入的な方法はモデルをデータの分布の外の点で評価することになる、と問題を指摘している [arxiv-2002.11097#c4](https://arxiv.org/pdf/2002.11097v2#page=5 "Methods which use an interventional value function fundamentally rely on evaluating a model on out-of-distribution samples (Figure 1).")。Chen らは、どちらの値にも適切な使いどころがあり、どちらを選ぶかは用途によると主張している [arxiv-2006.16234#c1](https://arxiv.org/pdf/2006.16234v1#page=2 "in this paper, we argue that rather than representing some critical flaw in using the Shapley value for feature attribution, each approach is meaningful when applied in the proper context")。論文の題名「モデルに忠実か、データに忠実か」は、この選択を指している。

## 4. LIME:局所的な単純モデル

LIME は、説明したい点 $x$ の近くで、元のモデル $f$ を単純なモデル $g$(たとえば少数の係数だけを持つ線形モデル)で近似する [arxiv-1602.04938#c8](https://arxiv.org/pdf/1602.04938v3#page=3 "The explanation produced by LIME is obtained by the following:")。

$$
\xi(x) = \arg\min_{g \in G} \ \mathcal{L}(f, g, \pi_x) + \Omega(g)
$$

- $\pi_x(z)$ は、点 $z$ が $x$ にどれだけ近いかを表す重みで、「$x$ の近く」を決める。
- $\mathcal{L}(f, g, \pi_x)$ は、その近くで $g$ が $f$ からどれだけずれているか。
- $\Omega(g)$ は $g$ の複雑さ(線形モデルなら0でない係数の数など)。

[数式の解説 5](05-linear-and-kernel.md) の Lasso と同じく、「当てはまりのよさ」と「単純さ」の釣り合いを取る形である。
$\mathcal{L}$ は、$x$ の周りでランダムに作った点で $f$ を評価し、$\pi_x$ で重みを付けて近似する [arxiv-1602.04938#c9](https://arxiv.org/pdf/1602.04938v3#page=3 "Thus, in order to learn the local behavior of f as the interpretable inputs vary, we approximate L(f, g, πx) by drawing samples, weighted by πx.")。

**補足**:LIME の線形の説明 $g$ も、1節の加法的な形をしている。ただし $\pi_x$ や $\Omega$ の選び方は自由なので、得られる係数がシャープレイ値の3つの性質を満たすとは限らない。
LIME の論文自身は、局所的にも強く非線形なモデルでは、忠実な線形の説明が存在しないことがあると述べている [arxiv-1602.04938#c2](https://arxiv.org/pdf/1602.04938v3#page=4 "Second, our choice of G (sparse linear models) means that if the underlying model is highly non-linear even in the locality of the prediction, there may not be a faithful explanation.")。

## 5. 積分勾配

### 定義

ニューラルネットワーク $F$ について、基準の入力 $x'$(画像なら真っ黒な画像など)から実際の入力 $x$ まで、直線に沿って勾配を積分する [arxiv-1703.01365#c8](https://arxiv.org/pdf/1703.01365v2#page=3 "Speciﬁcally, integrated gradients are deﬁned as the path intergral of the gradients along the straightline path from the baseline x′ to the input x.")。

$$
\mathrm{IG}_i(x) = (x_i - x'_i) \times \int_{0}^{1} \frac{\partial F\big(x' + \alpha (x - x')\big)}{\partial x_i} \, d\alpha
$$

$\alpha$ を $0$ から $1$ まで動かすと、$x' + \alpha(x - x')$ は基準 $x'$ から入力 $x$ まで直線上を動く。

### 完全性

帰属をすべて足すと、入力と基準での出力の差にちょうど一致する [arxiv-1703.01365#c9](https://arxiv.org/pdf/1703.01365v2#page=3 "This is formalized by the proposition below, which instanti-
ates the fundamental theorem of calculus for path integrals.")。

$$
\sum_{i=1}^{n} \mathrm{IG}_i(x) = F(x) - F(x')
$$

**補足(なぜ成り立つか)**:$h(\alpha) = F(x' + \alpha(x - x'))$ とおくと、合成関数の微分(連鎖律)から $h'(\alpha) = \sum_i \frac{\partial F}{\partial x_i}(x_i - x'_i)$ になる。これを $0$ から $1$ まで積分すると、左辺は積分勾配の和、右辺は微積分の基本定理から $h(1) - h(0) = F(x) - F(x')$ になる。論文も、これを経路積分についての微積分の基本定理の一例と述べている [arxiv-1703.01365#c9](https://arxiv.org/pdf/1703.01365v2#page=3 "This is formalized by the proposition below, which instanti-
ates the fundamental theorem of calculus for path integrals.")。

**補足(例)**:$F(x) = x_1 x_2$、基準 $x' = (0, 0)$、入力 $x = (2, 3)$ とする。経路上の点は $(2\alpha, 3\alpha)$ で、$\partial F/\partial x_1 = x_2 = 3\alpha$、$\partial F/\partial x_2 = x_1 = 2\alpha$。

$$
\mathrm{IG}_1 = 2 \int_0^1 3\alpha \, d\alpha = 2 \times \frac{3}{2} = 3, \qquad
\mathrm{IG}_2 = 3 \int_0^1 2\alpha \, d\alpha = 3 \times 1 = 3
$$

和は $6 = F(2, 3) - F(0, 0)$ で、完全性が成り立っている。

帰属は基準の選び方で変わる。論文は、出力がほぼ0で「何もない」ことを表す基準を選ぶよう勧めている [arxiv-1703.01365#c3](https://arxiv.org/pdf/1703.01365v2#page=5 "So we would additionally like the baseline to convey a complete absence of signal, so that the features that are apparent from the attributions are properties only of the input, and not of the baseline.")。

## 6. 共通点と違い

**補足**:ここまでの手法を並べると、次のように整理できる。

| 手法 | 「特徴量がない」状態の表し方 | 足すと何に一致するか |
|---|---|---|
| SHAP | 条件付き期待値(観測的または介入的)| $f(x) - E[f]$ |
| 積分勾配 | 基準の入力 $x'$ | $F(x) - F(x')$ |
| LIME | ランダムに作った近くの点 | 一致は保証されない |

どの手法も「何と比べた差を分けているか」が違う。同じ予測でも、手法によって帰属が違いうるのはこのためである。

## まとめ

| 式 | 何を表すか | 根拠 |
|---|---|---|
| $g(z') = \phi_0 + \sum_i \phi_i z'_i$ | 加法的な特徴量の帰属 | [arxiv-1705.07874#c8](https://arxiv.org/pdf/1705.07874v2#page=2 "Methods with explanation models matching Deﬁnition 1 attribute an effect φi to each feature, and summing the effects of all feature attributions approximates the output f(x) of the original model.") |
| $\phi_i = \sum_S \frac{\lvert S \rvert!(\lvert F \rvert - \lvert S \rvert - 1)!}{\lvert F \rvert!}[v(S \cup \{i\}) - v(S)]$ | シャープレイ値 | [arxiv-1705.07874#c9](https://arxiv.org/pdf/1705.07874v2#page=3 "They are a weighted average of all possible differences:") [arxiv-2006.16234#c9](https://arxiv.org/pdf/2006.16234v1#page=1 "where R is one possible permutation of the order in which the players join the coalition, SR is the set of players joining the coalition before player i") |
| $v(S) = E[f(z) \mid z_S]$ | SHAP の報酬 | [arxiv-1705.07874#c12](https://arxiv.org/pdf/1705.07874v2#page=4 "These are the Shapley values of a conditional expectation function of the original model; thus, they are the solution to Equation") |
| $E[f \mid X_S = x_S]$ と $E[f \mid do(X_S = x_S)]$ | 観測的と介入的 | [arxiv-2006.16234#c8](https://arxiv.org/pdf/2006.16234v1#page=1 "There are two ways the model’s output (f : x ∈R/N/×1 →R1) for a particular sample is used to deﬁne v(S):") |
| $\arg\min_g \mathcal{L}(f, g, \pi_x) + \Omega(g)$ | LIME | [arxiv-1602.04938#c8](https://arxiv.org/pdf/1602.04938v3#page=3 "The explanation produced by LIME is obtained by the following:") |
| $(x_i - x'_i)\int_0^1 \partial_i F \, d\alpha$ | 積分勾配 | [arxiv-1703.01365#c8](https://arxiv.org/pdf/1703.01365v2#page=3 "Speciﬁcally, integrated gradients are deﬁned as the path intergral of the gradients along the straightline path from the baseline x′ to the input x.") |
| $\sum_i \mathrm{IG}_i = F(x) - F(x')$ | 完全性 | [arxiv-1703.01365#c9](https://arxiv.org/pdf/1703.01365v2#page=3 "This is formalized by the proposition below, which instanti-
ates the fundamental theorem of calculus for path integrals.") |

## 参照カード

- [arxiv-1705.07874](../../papers/arxiv-1705.07874.yaml) Lundberg & Lee, "A Unified Approach to Interpreting Model Predictions"
- [arxiv-2006.16234](../../papers/arxiv-2006.16234.yaml) Chen, Janizek, Lundberg & Lee, "True to the Model or True to the Data?"
- [arxiv-2002.11097](../../papers/arxiv-2002.11097.yaml) Kumar et al., "Problems with Shapley-value-based explanations as feature importance measures"
- [arxiv-1602.04938](../../papers/arxiv-1602.04938.yaml) Ribeiro, Singh & Guestrin, ""Why Should I Trust You?": Explaining the Predictions of Any Classifier"
- [arxiv-1703.01365](../../papers/arxiv-1703.01365.yaml) Sundararajan, Taly & Yan, "Axiomatic Attribution for Deep Networks"
