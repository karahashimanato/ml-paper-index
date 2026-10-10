---
title: 数式の解説 3 — 不確実性と較正:ソフトマックス、温度スケーリング、ECE、分割共形予測
kind: math
tags: [post-hoc-calibration, conformal-prediction]
depends_on: [arxiv-1706.04599, arxiv-2107.07511]
written_at: 2026-10-10
written_by: claude-opus-5-5 via Claude Code
---

# 数式の解説 3 — 不確実性と較正:ソフトマックス、温度スケーリング、ECE、分割共形予測

<!-- generated:stale -->
> 未反映のカードはありません。
<!-- /generated:stale -->

## この記事の読み方

[不確実性の推定と較正](../topics/uncertainty-and-calibration.md) の記事で扱った手法のうち、2つの式を解説する。

- 分類モデルの「確信度」を後から直す**温度スケーリング**と、そのずれを測る **ECE**
- 「正解を含む候補の集合」を、確率の保証付きで作る**分割共形予測**

使う道具(Σ、指数関数、期待値、条件付き確率)は [準備の記事](00-preliminaries.md) で説明している。

- 式は論文から取り、根拠のカード(論文の該当ページへのリンク)を付けている。
- 「**補足**」と書いた計算は、論文には書かれていない、この記事による説明である。

## 1. ソフトマックスと確信度

$K$ 個のクラスに分類するニューラルネットワークは、最後に $K$ 個の実数を出力する。これを**ロジット**といい、データ $i$ のロジットを $z_i = (z_i^{(1)}, \ldots, z_i^{(K)})$ と書く。
ロジットは負にもなり、合計も1にならないので、そのままでは確率として読めない。そこで**ソフトマックス関数**で確率に直す [arxiv-1706.04599#c13](https://arxiv.org/pdf/1706.04599v2#page=5 "The network outputs a class prediction ˆyi and conﬁdence score ˆpi for each input xi.")。

$$
\sigma_{SM}(z_i)^{(k)} = \frac{\exp(z_i^{(k)})}{\sum_{j=1}^{K} \exp(z_i^{(j)})}
$$

- 分子の $\exp$ で、どの値も正になる。
- 分母で全クラスの和を割るので、$K$ 個の値の合計は1になる。
- $\exp$ は単調に増えるので、ロジットが大きいクラスほど確率も大きい。

予測するクラスは確率が最大のクラス $\hat{y}_i$ で、その確率の値 $\hat{p}_i = \max_k \sigma_{SM}(z_i)^{(k)}$ を**確信度**と呼ぶ [arxiv-1706.04599#c13](https://arxiv.org/pdf/1706.04599v2#page=5 "The network outputs a class prediction ˆyi and conﬁdence score ˆpi for each input xi.")。

**補足(例)**:3クラスでロジットが $(2, 1, 0)$ のとき、$e^2 \approx 7.389$、$e^1 \approx 2.718$、$e^0 = 1$ で、合計は約 $11.107$。確率は約 $(0.665, 0.245, 0.090)$ になり、予測はクラス1、確信度は約 $0.665$ である。

## 2. 「較正されている」とは

確信度が $0.8$ の予測を集めたら、そのうち8割が当たっている。どの確信度でもこれが成り立つモデルを、**較正されている**(calibrated)という。
Guo らは、近年のニューラルネットワークは較正されていない、つまり確信度と実際の正解率がずれていると報告した [arxiv-1706.04599#c1](https://arxiv.org/pdf/1706.04599v2#page=1 "We discover that modern neural networks, unlike those from a decade ago, are poorly calibrated.")。

### ビンに分けて正解率と確信度を比べる

データは有限個しかないので、「確信度がちょうど $0.8$ の予測」はほとんど無い。そこで、確信度の範囲 $(0, 1]$ を幅 $1/M$ の $M$ 個の区間(**ビン**)に分け、ビンごとに比べる [arxiv-1706.04599#c8](https://arxiv.org/pdf/1706.04599v2#page=2 "To estimate the expected accuracy from ﬁnite samples, we group predictions into M interval bins (each of size 1/M) and calculate the accuracy of each bin.")。
確信度が $m$ 番目の区間に入るデータの番号の集合を $B_m$ とし、$|B_m|$ をその個数とする。

$$
\mathrm{acc}(B_m) = \frac{1}{|B_m|} \sum_{i \in B_m} \mathbf{1}(\hat{y}_i = y_i), \qquad
\mathrm{conf}(B_m) = \frac{1}{|B_m|} \sum_{i \in B_m} \hat{p}_i
$$

- $\mathbf{1}(\hat{y}_i = y_i)$ は、予測が当たっていれば1、外れていれば0になる記号(指示関数)。したがって $\mathrm{acc}(B_m)$ は、そのビンの**正解率**である。
- $\mathrm{conf}(B_m)$ は、そのビンの**確信度の平均**である。
- 完全に較正されたモデルでは、すべての $m$ で $\mathrm{acc}(B_m) = \mathrm{conf}(B_m)$ になる [arxiv-1706.04599#c8](https://arxiv.org/pdf/1706.04599v2#page=2 "To estimate the expected accuracy from ﬁnite samples, we group predictions into M interval bins (each of size 1/M) and calculate the accuracy of each bin.")。

### ECE:ずれの重み付き平均

ビンごとのずれ $|\mathrm{acc}(B_m) - \mathrm{conf}(B_m)|$ を、そのビンに入ったデータの割合 $|B_m|/n$ で重み付けして足したものが **ECE**(Expected Calibration Error)である [arxiv-1706.04599#c9](https://arxiv.org/pdf/1706.04599v2#page=3 "The difference between acc and conf for a given bin represents the calibration gap (red bars in reliability diagrams – e.g. Figure 1).")。$n$ は全データ数。

$$
\mathrm{ECE} = \sum_{m=1}^{M} \frac{|B_m|}{n} \left| \mathrm{acc}(B_m) - \mathrm{conf}(B_m) \right|
$$

Guo らは、ECE を較正の主な評価指標として使っている [arxiv-1706.04599#c6](https://arxiv.org/pdf/1706.04599v2#page=3 "We use ECE as the primary empirical metric to measure calibration.")。

**補足(例)**:10個のデータを、$M = 2$ のビン $(0, 0.5]$ と $(0.5, 1]$ に分けたとする。

| ビン | 個数 | 確信度の平均 | 正解率 | 重み × ずれ |
|---|---|---|---|---|
| $(0, 0.5]$ | 4 | $0.4$ | $2/4 = 0.5$ | $\frac{4}{10} \times 0.1 = 0.04$ |
| $(0.5, 1]$ | 6 | $0.9$ | $4/6 \approx 0.667$ | $\frac{6}{10} \times 0.233 \approx 0.14$ |

ECE は約 $0.04 + 0.14 = 0.18$ になる。2つ目のビンでは、確信度の平均が正解率より高い。これを「過信している」という。

**補足**:ECE はビンの分け方で決まる量なので、ビンの数 $M$ を変えると値も変わりうる。論文どうしで ECE を比べるときは、ビンの数がそろっているかに注意が要る。

## 3. 温度スケーリング

### 式

温度スケーリングは、ロジットを1つの正の数 $T$ で割ってからソフトマックスに通す [arxiv-1706.04599#c10](https://arxiv.org/pdf/1706.04599v2#page=6 "Temperature scaling, the simplest extension of Platt scaling, uses a single scalar parameter T > 0 for all classes.")。$T$ はすべてのクラスで共通である。

$$
\hat{q}_i = \max_k \, \sigma_{SM}(z_i / T)^{(k)}
$$

$\hat{q}_i$ が直した後の確信度である。$T$ を**温度**という。

### $T$ を変えると何が起きるか

論文は次のように述べている [arxiv-1706.04599#c11](https://arxiv.org/pdf/1706.04599v2#page=6 "T is called the temperature, and it “softens” the softmax (i.e. raises the output entropy) with T > 1.")。

- $T > 1$ では、ソフトマックスの出力が「なだらか」になる(確率が均等に近づく)。
- $T \to \infty$ では、確率は $1/K$(全クラス同じ確率)に近づく。
- $T = 1$ では、元の確率に戻る。
- $T \to 0$ では、最大のクラスの確率が1になる。

**補足(理由)**:$z/T$ は、ロジットどうしの差を $1/T$ 倍にする。$T$ が大きいほど差が縮み、すべてのロジットが0に近づくので、確率は均等に近づく。$T$ が小さいほど差が広がり、最大のクラスが圧倒する。

**補足(例)**:1節の例 $(2, 1, 0)$ を $T = 2$ で割ると $(1, 0.5, 0)$ になる。$e^1 \approx 2.718$、$e^{0.5} \approx 1.649$、$e^0 = 1$ で、合計は約 $5.367$。確率は約 $(0.507, 0.307, 0.186)$ で、確信度は約 $0.665$ から約 $0.507$ に下がる。

### 予測は変わらない

$T > 0$ で割っても、ロジットの大小の順は変わらない。$\exp$ も単調に増えるので、確率が最大のクラスは同じままである。
したがって、温度スケーリングは予測するクラスを変えず、正解率にも影響しない [arxiv-1706.04599#c3](https://arxiv.org/pdf/1706.04599v2#page=6 "In other words, temperature scaling does not affect the model’s accuracy.")。変わるのは確信度の値だけである。

### $T$ の決め方

$T$ は、検証データでの NLL(負の対数尤度)を最小にするように決める [arxiv-1706.04599#c12](https://arxiv.org/pdf/1706.04599v2#page=6 "T is optimized with respect to NLL on the validation set.")。

**補足**:NLL は、各データで正解クラスに割り当てた確率 $q_i$ の対数にマイナスを付けて足したもの $-\sum_i \log q_i$ である。正解に高い確率を付けるほど小さくなる。過信して外れると、正解クラスの確率がとても小さくなり、$-\log$ が大きくなる。そのため、NLL を小さくする $T$ を選ぶと、過信が和らぐ方向に $T$ が決まる。
動かすのは $T$ という1つの数だけなので、1変数関数の最小化([準備の記事](00-preliminaries.md) の3節)と同じ問題になる。

### 前提

温度スケーリングを含む後処理の較正は、訓練・検証・テストのデータが同じ分布から来ることを前提にしている [arxiv-1706.04599#c4](https://arxiv.org/pdf/1706.04599v2#page=4 "We assume that the training, validation, and test sets are drawn from the same distribution.")。

## 4. 分割共形予測

温度スケーリングは「確率の値」を直す方法だった。分割共形予測は、問いの立て方が違う。
1つのクラスを答える代わりに、**候補のクラスの集合** $C(X_{\text{test}})$ を答え、「その集合が正解を含む確率」を保証する。

### 保証される性質

ユーザーが誤り率 $\alpha$(たとえば $0.1$)を決める。較正用のデータが $n$ 個あるとき、分割共形予測で作った集合は次を満たす [arxiv-2107.07511#c1](https://arxiv.org/pdf/2107.07511v6#page=4 "In words, the probability that the prediction set contains the correct label is almost exactly 1 −α; we call this property marginal coverage, since the probability is marginal (averaged) over the randomness in the calibration and test points.")。

$$
1 - \alpha \le P\big(Y_{\text{test}} \in C(X_{\text{test}})\big) \le 1 - \alpha + \frac{1}{n + 1}
$$

正解が集合に含まれる確率は、ほぼちょうど $1 - \alpha$ になる。この確率は、較正データとテストデータの選ばれ方について平均したものなので、論文はこれを**周辺被覆**(marginal coverage)と呼んでいる [arxiv-2107.07511#c1](https://arxiv.org/pdf/2107.07511v6#page=4 "In words, the probability that the prediction set contains the correct label is almost exactly 1 −α; we call this property marginal coverage, since the probability is marginal (averaged) over the randomness in the calibration and test points.")。

### 手順

1. **スコアを計算する**。較正データ $(X_1, Y_1), \ldots, (X_n, Y_n)$ のそれぞれで、正解クラスのソフトマックス出力を $1$ から引く [arxiv-2107.07511#c10](https://arxiv.org/pdf/2107.07511v6#page=4 "The score is high when the softmax output of the true class is low, i.e., when the model is badly wrong.")。

    $$
    s_i = 1 - \hat{f}(X_i)_{Y_i}
    $$

    モデルが正解に低い確率しか付けていない(大きく外れている)ほど、スコアは大きい。

2. **分位点を求める**。スコア $s_1, \ldots, s_n$ の、$\lceil (n+1)(1-\alpha) \rceil / n$ 分位点を $\hat{q}$ とする [arxiv-2107.07511#c11](https://arxiv.org/pdf/2107.07511v6#page=4 "Next comes the critical step: deﬁne ˆq to be the ⌈(n+1)(1−α)⌉/n empirical quantile of s1, ..., sn, where ⌈·⌉is the ceiling function (ˆq is essentially the 1 −α quantile, but with a small correction).")。$\lceil \cdot \rceil$ は切り上げ(天井関数)である。論文は、$\hat{q}$ を「ほぼ $1 - \alpha$ 分位点だが、少し補正したもの」と説明している。

3. **集合を作る**。テストデータについて、ソフトマックス出力が $1 - \hat{q}$ 以上のクラスをすべて集める [arxiv-2107.07511#c12](https://arxiv.org/pdf/2107.07511v6#page=4 "Remarkably, this algorithm gives prediction sets that are guaranteed to satisfy (1), no matter what (possibly incorrect) model is used or what the (unknown) distribution of the data is.")。

    $$
    C(X_{\text{test}}) = \{\, y : \hat{f}(X_{\text{test}})_y \ge 1 - \hat{q} \,\}
    $$

論文によれば、この手順で作った集合は、モデルがどんなものでも(間違っていても)、データの分布が何であっても、上の保証を満たす [arxiv-2107.07511#c12](https://arxiv.org/pdf/2107.07511v6#page=4 "Remarkably, this algorithm gives prediction sets that are guaranteed to satisfy (1), no matter what (possibly incorrect) model is used or what the (unknown) distribution of the data is.")。

**補足(例)**:$n = 19$、$\alpha = 0.1$ とする。$(n+1)(1-\alpha) = 20 \times 0.9 = 18$ なので、$\hat{q}$ は19個のスコアを小さい順に並べた18番目の値になる。
仮に $\hat{q} = 0.7$ なら、テストデータでソフトマックス出力が $0.3$ 以上のクラスを集合に入れる。モデルが自信を持っているデータでは集合が小さく、迷っているデータでは大きくなる。

### なぜ $n$ ではなく $n + 1$ なのか

**補足**:ここは論文の証明を写したものではなく、この記事による直感的な説明である。スコアに同じ値(同点)が無いものとする。

- テストデータのスコア $s_{\text{test}}$ と較正データの $n$ 個のスコアは、同じ分布から独立に出ている。すると、$n + 1$ 個を小さい順に並べたとき、$s_{\text{test}}$ が何番目に来るかは $1$ 番目から $n + 1$ 番目まで等しく確からしい。
- $\hat{q}$ は較正スコアの $k = \lceil (n+1)(1-\alpha) \rceil$ 番目の値である。$s_{\text{test}} \le \hat{q}$ となるのは、$s_{\text{test}}$ が $n + 1$ 個の中で $k$ 番目以内に来るときなので、その確率は $\dfrac{k}{n+1}$ である。
- $s_{\text{test}} \le \hat{q}$ は、正解クラスのソフトマックス出力が $1 - \hat{q}$ 以上であること、つまり正解が集合に入ることと同じである。
- $k \ge (n+1)(1-\alpha)$ なので、確率は $1 - \alpha$ 以上になる。また $k < (n+1)(1-\alpha) + 1$ なので、確率は $1 - \alpha + \dfrac{1}{n+1}$ より小さい。

これで保証の式の下限と上限が出てくる。「$n+1$」は、テストデータ自身を数に入れていることから来ている。

### 保証の前提と、保証されないこと

- 保証の定理は、較正データとテストデータが独立同分布であることを仮定する。論文の付録は、より弱い**交換可能性**の仮定でも成り立つと述べている [arxiv-2107.07511#c2](https://arxiv.org/pdf/2107.07511v6#page=50 "As a technical remark, the theorem also holds if the observations to satisfy the weaker condition of exchangeability; see [1].")。
- テストデータの分布が較正データと違う場合、この保証は成り立たない [arxiv-2107.07511#c9](https://arxiv.org/pdf/2107.07511v6#page=20 "All previous conformal methods rely on Theorem 1, which assumes that the incoming test points come from the same distribution as the calibration points.")。
- 保証は「平均すると」の話である。特定の入力 $X_{\text{test}}$ に条件を付けた被覆は、これより強い性質で、最も一般的な場合には達成できない(Vovk を引用して述べている)[arxiv-2107.07511#c4](https://arxiv.org/pdf/2107.07511v6#page=13 "This is a stronger property than the marginal coverage property in (1) that conformal prediction is guaranteed to achieve—indeed, in the most general case, conditional coverage is impossible to achieve [14].")。
- 保証はどんなスコアでも成り立つが、集合が役に立つかどうかはスコアの選び方で決まる [arxiv-2107.07511#c3](https://arxiv.org/pdf/2107.07511v6#page=6 "although the guarantee always holds, the usefulness of the prediction sets is primarily determined by the score function.")。

## まとめ

| 式 | 何を表すか | 根拠 |
|---|---|---|
| $\sigma_{SM}(z)^{(k)} = \exp(z^{(k)}) / \sum_j \exp(z^{(j)})$ | ロジットを確率に直す | [arxiv-1706.04599#c13](https://arxiv.org/pdf/1706.04599v2#page=5 "The network outputs a class prediction ˆyi and conﬁdence score ˆpi for each input xi.") |
| $\mathrm{acc}(B_m)$、$\mathrm{conf}(B_m)$ | ビンごとの正解率と確信度の平均 | [arxiv-1706.04599#c8](https://arxiv.org/pdf/1706.04599v2#page=2 "To estimate the expected accuracy from ﬁnite samples, we group predictions into M interval bins (each of size 1/M) and calculate the accuracy of each bin.") |
| $\mathrm{ECE} = \sum_m \frac{\lvert B_m \rvert}{n} \lvert \mathrm{acc} - \mathrm{conf} \rvert$ | 確信度と正解率のずれの重み付き平均 | [arxiv-1706.04599#c9](https://arxiv.org/pdf/1706.04599v2#page=3 "The difference between acc and conf for a given bin represents the calibration gap (red bars in reliability diagrams – e.g. Figure 1).") |
| $\hat{q}_i = \max_k \sigma_{SM}(z_i / T)^{(k)}$ | 温度スケーリング | [arxiv-1706.04599#c10](https://arxiv.org/pdf/1706.04599v2#page=6 "Temperature scaling, the simplest extension of Platt scaling, uses a single scalar parameter T > 0 for all classes.") [arxiv-1706.04599#c11](https://arxiv.org/pdf/1706.04599v2#page=6 "T is called the temperature, and it “softens” the softmax (i.e. raises the output entropy) with T > 1.") |
| $s_i = 1 - \hat{f}(X_i)_{Y_i}$ | 共形予測のスコア | [arxiv-2107.07511#c10](https://arxiv.org/pdf/2107.07511v6#page=4 "The score is high when the softmax output of the true class is low, i.e., when the model is badly wrong.") |
| $\lceil (n+1)(1-\alpha) \rceil / n$ 分位点 | 補正付きの分位点 $\hat{q}$ | [arxiv-2107.07511#c11](https://arxiv.org/pdf/2107.07511v6#page=4 "Next comes the critical step: deﬁne ˆq to be the ⌈(n+1)(1−α)⌉/n empirical quantile of s1, ..., sn, where ⌈·⌉is the ceiling function (ˆq is essentially the 1 −α quantile, but with a small correction).") |
| $1 - \alpha \le P(Y \in C(X)) \le 1 - \alpha + \frac{1}{n+1}$ | 周辺被覆の保証 | [arxiv-2107.07511#c1](https://arxiv.org/pdf/2107.07511v6#page=4 "In words, the probability that the prediction set contains the correct label is almost exactly 1 −α; we call this property marginal coverage, since the probability is marginal (averaged) over the randomness in the calibration and test points.") |

## 参照カード

- [arxiv-1706.04599](../../papers/arxiv-1706.04599.yaml) Guo et al., "On Calibration of Modern Neural Networks"
- [arxiv-2107.07511](../../papers/arxiv-2107.07511.yaml) Angelopoulos & Bates, "A Gentle Introduction to Conformal Prediction and Distribution-Free Uncertainty Quantification"
