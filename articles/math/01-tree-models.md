---
title: 数式の解説 1 — 木モデル:勾配ブースティングの更新、XGBoost の目的関数、不純度と変数重要度
kind: math
tags: [gradient-boosted-trees, random-forests]
depends_on: [arxiv-0804.2752, arxiv-1603.02754, arxiv-2001.04295]
written_at: 2026-10-10
written_by: claude-opus-5-5 via Claude Code
---

# 数式の解説 1 — 木モデル:勾配ブースティングの更新、XGBoost の目的関数、不純度と変数重要度

<!-- generated:stale -->
> ⚠ この記事の執筆後(2026-10-10)に、関連カードが 72 件追加されています(未反映): `arxiv-1005.0208`, `arxiv-1405.2881`, `arxiv-1504.07676`, `arxiv-1505.01866`, `arxiv-1510.04342`, `arxiv-1511.05741`, `arxiv-1604.04173`, `arxiv-1610.01271`, `arxiv-1706.09516`, `arxiv-1802.05640`, `arxiv-1802.09596`, `arxiv-1804.03515`, `arxiv-1810.11363`, `arxiv-1903.05179`, `arxiv-1904.06019`, `arxiv-1905.03222`, `arxiv-1905.04610`, `arxiv-1910.03225`, `arxiv-1910.13204`, `arxiv-1911.00190`, `arxiv-1911.01914`, `arxiv-2003.03629`, `arxiv-2006.10562`, `arxiv-2106.03253`, `arxiv-2106.11959`, `arxiv-2107.05847`, `arxiv-2109.06716`, `arxiv-2207.01848`, `arxiv-2207.08815`, `arxiv-2305.02997`, `arxiv-2402.01502`, `arxiv-2407.04491`, `arxiv-2410.24210`, `arxiv-2506.16791`, `arxiv-2602.06456`, `arxiv-2608.05265`, `arxiv-2608.07349`, `arxiv-2608.16429`, `arxiv-2608.16659`, `arxiv-2608.17856`, `arxiv-2608.18849`, `arxiv-2608.18919`, `arxiv-2608.20024`, `arxiv-2608.22069`, `arxiv-2608.22594`, `arxiv-2608.23893`, `arxiv-2608.24056`, `arxiv-2608.27076`, `arxiv-2608.30392`, `arxiv-2609.03003`, `arxiv-2609.06080`, `arxiv-2609.07441`, `arxiv-2609.13785`, `arxiv-2609.16258`, `arxiv-2609.16309`, `arxiv-2609.29690`, `arxiv-2609.36039`, `arxiv-2609.39613`, `arxiv-2610.00649`, `arxiv-2610.00806`, `doi-10.1007_s40123-026-01482-2`, `doi-10.1038_s41467-026-76154-7`, `doi-10.1038_s41586-024-08328-6`, `doi-10.1109_tsg.2026.3676842`, `doi-10.1186_s44147-026-01203-3`, `doi-10.3389_fpsyg.2026.1875261`, `doi-10.3389_fpubh.2026.1911565`, `doi-10.3389_frai.2026.1876396`, `doi-10.36079_lamintang.ijortas-0802.1081`, `doi-10.47852_bonviewaia620210522`, `doi-10.57185_yrw05r30`, `doi-10.70393_6a6374616d.343334`
<!-- /generated:stale -->

## この記事の読み方

[勾配ブースティング木の記事](../methods/gradient-boosted-trees.md) と [ランダムフォレストと決定木の記事](../methods/random-forests-and-decision-trees.md) で扱った手法の、中心にある式を解説する。
使う道具(Σ 記号、微分、勾配降下、2次の近似)は [準備の記事](00-preliminaries.md) で説明している。

- 式は論文から取り、根拠のカード(論文の該当ページへのリンク)を付けている。
- 「**補足**」と書いた計算は、論文には書かれていない、この記事による説明である。

## 1. 勾配ブースティング — 「誤差を少しずつ直す」を式にする

### 一般形

Bühlmann と Hothorn のレビューは、Friedman による一般的なアルゴリズムを次のように紹介している [arxiv-0804.2752#c2](https://arxiv.org/pdf/0804.2752v1#page=4 "The stopping iteration, which is the main tuning parameter, can be determined via cross-validation or some information criterion; see Section 5.4.")。予測したい量を関数 $f$ で表し、データ $(X_i, Y_i)$($i = 1, \ldots, n$)に対する損失 $\rho(Y_i, f(X_i))$ を小さくしたい。

1. 最初の予測 $\hat{f}^{[0]}$ を決める(たとえば定数)。
2. 各データで、損失の**負の勾配**を計算する。

    $$
    U_i = -\frac{\partial}{\partial f} \rho(Y_i, f) \Big|_{f = \hat{f}^{[m-1]}(X_i)}
    $$

3. $(X_i, U_i)$ に基底の学習器(ここでは決定木)を当てはめ、$U_i$ を予測する関数 $\hat{g}^{[m]}$ を得る。
4. 小さい係数 $\nu$ を掛けて足す。

    $$
    \hat{f}^{[m]} = \hat{f}^{[m-1]} + \nu \cdot \hat{g}^{[m]}
    $$

5. これを決めた回数 $m_{\text{stop}}$ まで繰り返す。

**読み方**:[準備の記事](00-preliminaries.md) の勾配降下法 $\boldsymbol{x} \leftarrow \boldsymbol{x} - \eta \nabla f$ と見比べてほしい。ここで動かしているのは、数ではなく**予測そのもの**である。「各データで、損失が減る向き($U_i$)」を木で近似し、その方向に少しだけ予測を動かす。だからこの方法は「関数空間での勾配降下」と呼ばれる。

- $\nu$ は勾配降下の学習率にあたる。小さければ(たとえば 0.1)細かい値はあまり重要でない、とされる [arxiv-0804.2752#c3](https://arxiv.org/pdf/0804.2752v1#page=4 "The choice of the step-length factor ν in step 4 is of minor importance, as long as it is “small,” such as ν = 0.1.")。
- 繰り返しの回数 $m_{\text{stop}}$ が主なチューニングパラメータである [arxiv-0804.2752#c2](https://arxiv.org/pdf/0804.2752v1#page=4 "The stopping iteration, which is the main tuning parameter, can be determined via cross-validation or some information criterion; see Section 5.4.")。

### 二乗誤差なら「残差に木を当てはめる」

損失を二乗誤差 $\rho(y, f) = \frac{1}{2}(y - f)^2$ にすると、負の勾配は残差そのものになる [arxiv-0804.2752#c9](https://arxiv.org/pdf/0804.2752v1#page=8 "Note that the negative gradient vector becomes the residual vector.")。

**補足(確かめ)**:$\dfrac{\partial}{\partial f} \dfrac{1}{2}(y - f)^2 = -(y - f)$ なので、負の勾配は $U_i = Y_i - \hat{f}^{[m-1]}(X_i)$、つまり「正解と今の予測の差(残差)」である。$\frac{1}{2}$ は、微分したときに係数がきれいになるように付けている。

**補足(数値の例)**:正解が $Y = (10, 20)$、今の予測が $(14, 14)$ なら、残差は $(-4, 6)$。木がこの残差をそのまま当てられたとして $\nu = 0.1$ なら、予測は $(14 - 0.4, 14 + 0.6) = (13.6, 14.6)$ と、正解に少し近づく。これを繰り返す。

## 2. XGBoost — 正則化した目的関数と、葉の重みの公式

### 目的関数

XGBoost は、$K$ 本の木の予測の和でデータ $i$ を予測する($\hat{y}_i = \sum_{k=1}^{K} f_k(\boldsymbol{x}_i)$)。そして、次の目的関数を最小にする [arxiv-1603.02754#c2](https://arxiv.org/pdf/1603.02754v3#page=2 "When the regularization parameter is set to zero, the objective falls back to the traditional gradient tree boosting.")。

$$
\mathcal{L} = \sum_{i} l(\hat{y}_i, y_i) + \sum_{k} \Omega(f_k), \qquad \Omega(f) = \gamma T + \frac{1}{2} \lambda \|\boldsymbol{w}\|^2
$$

- $l$ は損失(予測と正解のずれ)。
- $\Omega$ は木の複雑さへの罰則。$T$ は葉の数、$\boldsymbol{w}$ は葉の値(重み)を並べたベクトル。
- $\gamma$ は「葉を1枚増やすコスト」、$\lambda$ は「葉の値を大きくしすぎないための罰則」の強さ。

罰則をゼロにすると、従来の勾配ブースティングに戻る [arxiv-1603.02754#c2](https://arxiv.org/pdf/1603.02754v3#page=2 "When the regularization parameter is set to zero, the objective falls back to the traditional gradient tree boosting.")。

### 2次の近似

$t$ 本目の木 $f_t$ を足すとき、損失を2次式で近似する [arxiv-1603.02754#c3](https://arxiv.org/pdf/1603.02754v3#page=2 "Second-order approximation can be used to quickly optimize the objective in the general setting [12].")。

$$
\mathcal{L}^{(t)} \approx \sum_{i=1}^{n} \left[ l(y_i, \hat{y}_i^{(t-1)}) + g_i f_t(\boldsymbol{x}_i) + \frac{1}{2} h_i f_t^2(\boldsymbol{x}_i) \right] + \Omega(f_t)
$$

ここで $g_i$ と $h_i$ は、損失を今の予測 $\hat{y}_i^{(t-1)}$ で1回・2回微分した値である。

**読み方**:[準備の記事](00-preliminaries.md) の2次の近似 $f(x + t) \approx f(x) + f'(x)t + \frac{1}{2}f''(x)t^2$ で、「$x$」を今の予測、「$t$」を新しい木が足す量 $f_t(\boldsymbol{x}_i)$ と読み替えたものである。1回微分 $g_i$ だけを使う第1節の方法に、2回微分 $h_i$(曲がり具合)の情報を加えている。

### 葉ごとに分けて、最適な重みを求める

木の構造(どのデータがどの葉に入るか)を決めると、葉 $j$ に入るデータの集合 $I_j$ ごとに式を整理できる。各葉の $g_i$ と $h_i$ の和を $G_j = \sum_{i \in I_j} g_i$、$H_j = \sum_{i \in I_j} h_i$ と書くと、定数を除いて

$$
\sum_{j=1}^{T} \left[ G_j w_j + \frac{1}{2} (H_j + \lambda) w_j^2 \right] + \gamma T
$$

となる。各葉について $w_j$ の2次式なので、最小にする重みと、そのときの値が求まる [arxiv-1603.02754#c9](https://arxiv.org/pdf/1603.02754v3#page=3 "Eq (6) can be used as a scoring function to measure the quality of a tree structure q.")。

$$
w_j^{*} = -\frac{G_j}{H_j + \lambda}, \qquad \tilde{\mathcal{L}}^{(t)}(q) = -\frac{1}{2} \sum_{j=1}^{T} \frac{G_j^2}{H_j + \lambda} + \gamma T
$$

**補足(確かめ)**:[準備の記事](00-preliminaries.md) で見たとおり、2次式 $a t + \frac{1}{2} b t^2$ は $t = -a/b$ で最小値 $-a^2/(2b)$ をとる。$a = G_j$、$b = H_j + \lambda$ とおけば、上の2つの式がそのまま出る。

右の式は、木の構造の良さを測る得点として使える。論文は、これを決定木の不純度のような得点だと述べている [arxiv-1603.02754#c9](https://arxiv.org/pdf/1603.02754v3#page=3 "Eq (6) can be used as a scoring function to measure the quality of a tree structure q.")。

**補足(二乗誤差の場合)**:損失が $l = \frac{1}{2}(y - \hat{y})^2$ なら、$g_i = \hat{y}_i - y_i$(残差の符号を変えたもの)、$h_i = 1$ である。すると、葉に入るデータの数を $n_j$ として

$$
w_j^{*} = \frac{\sum_{i \in I_j} (y_i - \hat{y}_i)}{n_j + \lambda}
$$

となる。$\lambda = 0$ なら「葉の中の残差の平均」で、第1節の「残差に木を当てはめる」と一致する。$\lambda > 0$ だと分母が大きくなり、葉の値がゼロの方へ縮む。これが $\lambda$ の正則化の効果である。

### 分割の利得

葉を左右に分けるかどうかは、分ける前後の得点の差で決める。左右の子に入るデータの $g, h$ の和を $G_L, H_L$、$G_R, H_R$、分ける前を $G, H$ とすると、分割による損失の減少は [arxiv-1603.02754#c10](https://arxiv.org/pdf/1603.02754v3#page=3 "This formula is usually used in practice for evaluating the split candidates.")

$$
\text{Gain} = \frac{1}{2} \left[ \frac{G_L^2}{H_L + \lambda} + \frac{G_R^2}{H_R + \lambda} - \frac{G^2}{H + \lambda} \right] - \gamma
$$

である。

**読み方**:かっこの中は「分けた後の得点の改善」、最後の $-\gamma$ は「葉が1枚増える罰則」である。改善が $\gamma$ を上回らなければ、分けない方がよい。$\gamma$ は木を小さく保つ働きをする。

**補足(数値の例)**:二乗誤差で $\lambda = 0$、ある葉に残差 $(+2, +2, -2, -2)$ のデータが入っているとする($g$ はその符号を変えたもの、$h = 1$)。分ける前は $G = 0$ なので第3項は $0$。プラスの2つとマイナスの2つにうまく分けられれば $G_L = -4$、$G_R = +4$、$H_L = H_R = 2$ で、かっこの中は $\frac{16}{2} + \frac{16}{2} - 0 = 16$、利得は $8 - \gamma$ となる。全体では平均がゼロで予測を動かせない葉でも、分ければ大きく改善できることがわかる。

### 縮小

XGBoost も、足す木の重みに係数を掛けて小さくする(縮小)。これは第1節の $\nu$ と同じ働きで、論文は列のサブサンプリングと並べて過学習を防ぐ工夫として挙げている [arxiv-1603.02754#c4](https://arxiv.org/pdf/1603.02754v3#page=3 "According to user feedback, using column sub-sampling prevents over-ﬁtting even more so than the traditional row sub-sampling (which is also supported).")。

## 3. 不純度と変数重要度(MDI)

### 回帰木の分割の基準

回帰木(CART)は、各ノードで「どの変数のどこで分けるか」を、不純度の減少が最大になるように選ぶ。回帰では、**不純度はそのノードに入るデータの出力の分散**である [arxiv-2001.04295#c9](https://arxiv.org/pdf/2001.04295v3#page=5 "where the impurity is simply deﬁned as the variance of the output in regression")。

あるノード(領域 $A$)を左右 $A_L$、$A_R$ に分けるとき、分割の良さは「分ける前の分散」から「分けた後の分散を、データの割合で重み付けした平均」を引いたものになる。Scornet は、この量を母集団の版で次のように書いている(記号は論文に合わせた)。

$$
L^{\star}_A(j, z) = V[Y \mid X \in A] - P[X^{(j)} < z \mid X \in A]\, V[Y \mid X^{(j)} < z, X \in A] - P[X^{(j)} \ge z \mid X \in A]\, V[Y \mid X^{(j)} \ge z, X \in A]
$$

$j$ は分ける変数、$z$ は分ける位置である。

**読み方**:分けた後の左右それぞれで $Y$ のばらつきが小さければ、つまり分割によって $Y$ がよく揃えば、この値は大きくなる。

**補足(数値の例)**:$Y = (1, 1, 5, 5)$ のノードを $(1,1)$ と $(5,5)$ に分けると、分ける前の分散は $4$(平均 $3$ からの差の2乗の平均)、分けた後は左右とも分散 $0$ なので、減少は $4 - 0 = 4$ になる。$(1,5)$ と $(1,5)$ に分けると、左右とも分散 $4$ で、減少は $0$ になる。

XGBoost の分割の利得(第2節)も、論文自身が不純度のような得点だと述べている [arxiv-1603.02754#c9](https://arxiv.org/pdf/1603.02754v3#page=3 "Eq (6) can be used as a scoring function to measure the quality of a tree structure q.")。二乗誤差の場合、どちらも「分けると残差(または $Y$)のばらつきがどれだけ減るか」を測っている、と見ることができる(この見方は本記事の補足)。

### MDI — 不純度の減少で変数の重要度を測る

ランダムフォレストの変数重要度の1つである MDI は、**その変数で分けたすべてのノードについて、不純度の減少を足し合わせたもの**である [arxiv-2001.04295#c10](https://arxiv.org/pdf/2001.04295v3#page=6 "In other words, the MDI of X(j) computes the weighted decrease in impurity related to splits along the variable X(j).")。1本の木 $T$ での変数 $X^{(j)}$ の MDI は

$$
\widehat{\mathrm{MDI}}_T(X^{(j)}) = \sum_{\substack{A \in T \\ j_{n,A} = j}} p_{n,A}\, L_{n,A}(j_{n,A}, z_{n,A})
$$

である。$p_{n,A}$ はノード $A$ に入るデータの割合、$L_{n,A}$ はそのノードの分割による不純度の減少。森全体の MDI は、木ごとの MDI の平均である [arxiv-2001.04295#c5](https://arxiv.org/pdf/2001.04295v3#page=12 "Theorem 3 is the ﬁrst result highlighting that empirical MDI computed with CART procedure converge to reasonable values that can be used for variable selection, in the framework of Model 3.")。

**読み方**:根に近い大きなノード($p_{n,A}$ が大きい)で、ばらつきを大きく減らした変数ほど、重要度が高くなる。

**注意**:この定義は計算しやすいが、偏りがあることが知られている。たとえば、木を最後まで伸ばすと、ノイズまで重要度に入ってしまう [arxiv-2001.04295#c4](https://arxiv.org/pdf/2001.04295v3#page=9 "The noise, when having a larger variance than the regression function, can induce a very important bias in the MDI by overestimating the importance of some variables.")。カテゴリの多い変数を好む偏りも報告されている(先行研究を引いた記述) [arxiv-2001.04295#c1](https://arxiv.org/pdf/2001.04295v3#page=2 "MDI is known to favor variables with many categories [see, e.g., Strobl et al., 2007, Nicodemus, 2011].")。詳しくは [ランダムフォレストと決定木の記事](../methods/random-forests-and-decision-trees.md) を参照。

## まとめ

| 式 | 何を表すか | 根拠 |
|---|---|---|
| $\hat{f}^{[m]} = \hat{f}^{[m-1]} + \nu \hat{g}^{[m]}$ | 負の勾配を木で近似し、少しずつ足す | [arxiv-0804.2752#c2](https://arxiv.org/pdf/0804.2752v1#page=4 "The stopping iteration, which is the main tuning parameter, can be determined via cross-validation or some information criterion; see Section 5.4.") |
| 二乗誤差で $U_i = Y_i - \hat{f}(X_i)$ | 負の勾配は残差 | [arxiv-0804.2752#c9](https://arxiv.org/pdf/0804.2752v1#page=8 "Note that the negative gradient vector becomes the residual vector.") |
| $w_j^{*} = -G_j / (H_j + \lambda)$ | 葉の最適な重み($\lambda$ で縮む) | [arxiv-1603.02754#c9](https://arxiv.org/pdf/1603.02754v3#page=3 "Eq (6) can be used as a scoring function to measure the quality of a tree structure q.") |
| $\text{Gain} = \frac{1}{2}[\cdots] - \gamma$ | 分割の利得と、葉を増やす罰則 | [arxiv-1603.02754#c10](https://arxiv.org/pdf/1603.02754v3#page=3 "This formula is usually used in practice for evaluating the split candidates.") |
| 分散の減少 $L^{\star}_A(j, z)$ | 回帰木の分割の基準 | [arxiv-2001.04295#c9](https://arxiv.org/pdf/2001.04295v3#page=5 "where the impurity is simply deﬁned as the variance of the output in regression") |
| $\widehat{\mathrm{MDI}}_T$ | 不純度の減少の重み付き和 | [arxiv-2001.04295#c10](https://arxiv.org/pdf/2001.04295v3#page=6 "In other words, the MDI of X(j) computes the weighted decrease in impurity related to splits along the variable X(j).") |

## 参照カード

- [arxiv-0804.2752](../../papers/arxiv-0804.2752.yaml) Bühlmann & Hothorn, "Boosting Algorithms: Regularization, Prediction and Model Fitting"
- [arxiv-1603.02754](../../papers/arxiv-1603.02754.yaml) Chen & Guestrin, "XGBoost: A Scalable Tree Boosting System"
- [arxiv-2001.04295](../../papers/arxiv-2001.04295.yaml) Scornet, "Trees, forests, and impurity-based variable importance"
