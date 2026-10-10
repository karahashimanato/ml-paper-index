---
title: 数式の解説 9 — 量子化:アフィン量子化と丸め、クリッピング、STE、GPTQ の目的、SmoothQuant
kind: math
tags: [quantization, post-training-quantization, quantization-aware-training]
depends_on: [arxiv-1712.05877, arxiv-2106.08295, arxiv-2208.07339, arxiv-2210.17323, arxiv-2211.10438]
written_at: 2026-10-10
written_by: claude-opus-5-5 via Claude Code
---

# 数式の解説 9 — 量子化:アフィン量子化と丸め、クリッピング、STE、GPTQ の目的、SmoothQuant

<!-- generated:stale -->
> ⚠ この記事の執筆後(2026-10-10)に、関連カードが 13 件追加されています(未反映): `arxiv-1510.00149`, `arxiv-1911.05248`, `arxiv-2010.03058`, `arxiv-2212.09720`, `arxiv-2301.00774`, `arxiv-2305.14314`, `arxiv-2306.00978`, `arxiv-2310.01382`, `arxiv-2402.18158`, `arxiv-2403.15447`, `arxiv-2404.14047`, `arxiv-2411.04330`, `arxiv-2609.13031`
<!-- /generated:stale -->

## この記事の読み方

[量子化による影響](../topics/quantization-effects.md) の記事で扱った、モデルの重みや活性(途中の計算結果)を少ないビット数の整数で表す**量子化**の式を解説する。

使う道具(関数、絶対値、行列の積、微分)は [準備の記事](00-preliminaries.md) で説明している。

- 式は論文から取り、根拠のカード(論文の該当ページへのリンク)を付けている。
- 「**補足**」と書いた計算は、論文には書かれていない、この記事による説明である。

## 1. 実数と整数の対応:アフィン量子化

Jacob らは、整数 $q$ と実数 $r$ を次の1次式で対応させている [arxiv-1712.05877#c8](https://arxiv.org/pdf/1712.05877v1#page=3 "Equation (1) is our quantization scheme and the constants S and Z are our quantization parameters.")。

$$
r = S\,(q - Z)
$$

- $S$(スケール)は正の実数で、整数が1つ違うと実数がどれだけ違うかを表す。
- $Z$(ゼロ点)は整数で、実数の $0$ に対応する整数である。これにより、$r = 0$ がちょうど表せる [arxiv-1712.05877#c9](https://arxiv.org/pdf/1712.05877v1#page=3 "This allows us to automatically meet the requirement that the real value r = 0 be exactly representable by a quantized value.")。

1次関数 $y = ax + b$ の形(アフィン写像)なので、アフィン量子化と呼ぶ。

## 2. 量子化と逆量子化

### 式

Nagel らのホワイトペーパーは、実数 $x$ を $b$ ビットの整数に変換し(量子化)、また実数に戻す(逆量子化)手順を次のように書いている [arxiv-2106.08295#c8](https://arxiv.org/pdf/2106.08295v1#page=4 "To approximate the real-valued input x we perfrom a de-quantization step:")。

$$
x_{\text{int}} = \mathrm{clamp}\!\left( \left\lfloor \frac{x}{s} \right\rceil + z;\ 0,\ 2^b - 1 \right), \qquad
\hat{x} = s\,(x_{\text{int}} - z)
$$

- $s$ はスケール、$z$ はゼロ点、$b$ はビット数。8ビットなら整数は $0$ から $2^8 - 1 = 255$ まで。
- $\lfloor \cdot \rceil$ は最も近い整数への丸め(四捨五入)。
- $\mathrm{clamp}(x; a, c)$ は、$x$ が $a$ より小さければ $a$、$c$ より大きければ $c$、その間なら $x$ そのものを返す。範囲の外の値を端に寄せる操作である。

$\hat{x}$ は $x$ の近似で、$x$ とぴったり同じにはならない。

### 2種類の誤差

表せる範囲は $[-sz,\ s(2^b - 1 - z)]$ で、その外の値は端に切り詰められる(**クリッピング誤差**)。範囲の中の値には、丸めによる誤差が $[-s/2,\ s/2]$ の範囲で生じる(**丸め誤差**)[arxiv-2106.08295#c9](https://arxiv.org/pdf/2106.08295v1#page=4 "If we want to reduce the clipping error we can expand the quantization range by increasing the scale factor.")。

スケール $s$ を大きくすると範囲が広がってクリッピング誤差は減るが、目盛りが粗くなって丸め誤差は増える [arxiv-2106.08295#c9](https://arxiv.org/pdf/2106.08295v1#page=4 "If we want to reduce the clipping error we can expand the quantization range by increasing the scale factor.")。この釣り合いをどう取るかが、量子化の設定の中心的な問題である。

**補足(例)**:8ビットで、範囲 $[-1, 3]$ を表したいとする。最小値と最大値から $s = \frac{3 - (-1)}{255} = \frac{4}{255} \approx 0.0157$、$z = \lfloor 1/s \rceil = \lfloor 63.75 \rceil = 64$ と決めると

| $x$ | $x/s + z$ | $x_{\text{int}}$ | $\hat{x} = s(x_{\text{int}} - z)$ | 誤差 |
|---|---|---|---|---|
| $0.5$ | $31.875 + 64$ | $96$ | $32 \times 0.0157 \approx 0.502$ | 丸め誤差(約 $0.002$)|
| $0$ | $0 + 64$ | $64$ | $0$ | なし |
| $5$ | $318.75 + 64$ | $255$(切り詰め)| $191 \times 0.0157 \approx 2.996$ | クリッピング誤差(約 $2$)|

丸め誤差は $s/2 \approx 0.0078$ 以下に収まるが、範囲の外の値には大きな誤差が出る。

### 対称量子化

ゼロ点を $0$ に固定したものを**対称量子化**という。$\hat{x} = s\, x_{\text{int}}$ となり、計算が簡単になる代わりに、表せる範囲の自由度が減る [arxiv-2106.08295#c10](https://arxiv.org/pdf/2106.08295v1#page=4 "The symmetric quantizer restricts the zero-point to 0.")。

Dettmers らが使う **absmax 量子化**は対称量子化の一種で、テンソル全体の絶対値の最大値で割って、$[-127, 127]$ に収める [arxiv-2208.07339#c8](https://arxiv.org/pdf/2208.07339v2#page=3 "Absmax quantization scales inputs into the 8-bit range [−127, 127] by multiplying with sxf16 which is 127 divided by the absolute maximum of the entire tensor.")。

$$
X_{i8} = \left\lfloor \frac{127}{\max_{ij} |X_{ij}|} \, X \right\rceil
$$

**補足(例:外れ値の影響)**:値が $(0.2,\ -1.5,\ 0.9)$ なら、最大の絶対値は $1.5$ で、$127/1.5 \approx 84.7$ を掛けて丸めると $(17,\ -127,\ 76)$ になる。
ここに外れ値 $60$ が1つ加わると、掛ける数は $127/60 \approx 2.12$ になり、$(0.2,\ -1.5,\ 0.9,\ 60)$ は $(0,\ -3,\ 2,\ 127)$ になる。小さな値はほとんど区別できなくなる。
Dettmers らは、大きな言語モデルでは、大きさの外れた特徴量が系統的に現れ、通常の8ビット量子化を難しくすると述べている [arxiv-2208.07339#c3](https://arxiv.org/pdf/2208.07339v2#page=2 "the need to explicitly represent the sparse but systematic large magnitude outlier features that ruin quantization precision once they emerge in all transformer layers starting at scales of 6.7B parameters")。

## 3. 学習しながら量子化する:STE

量子化を考慮した学習(QAT)では、順伝播で量子化を模擬する [arxiv-1712.05877#c3](https://arxiv.org/pdf/1712.05877v1#page=5 "We propose an approach that simulates quantization effects in the forward pass of training.")。しかし、丸めの関数 $\lfloor y \rceil$ は階段状なので、微分はほとんどの点で0、段差の点では定義できない。このままでは勾配を使った学習ができない [arxiv-2106.08295#c11](https://arxiv.org/pdf/2106.08295v1#page=19 "This poses an issue because the gradient of the round-to-nearest operation in equation (4) is either zero or undeﬁned everywhere, which makes gradient-based training impossible.")。

そこで **STE**(straight-through estimator)では、丸めの微分を1とみなす [arxiv-2106.08295#c11](https://arxiv.org/pdf/2106.08295v1#page=19 "This poses an issue because the gradient of the round-to-nearest operation in equation (4) is either zero or undeﬁned everywhere, which makes gradient-based training impossible.")。

$$
\frac{\partial \lfloor y \rceil}{\partial y} \approx 1
$$

**補足(読み方)**:順伝播では本当に丸めるが、逆伝播では「丸めなかったことにして」勾配をそのまま通す。階段関数を、傾き1の直線 $y$ で近似して微分していることになる。

## 4. 学習後の量子化:層ごとの再構成

### GPTQ の目的関数

学習済みのモデルを、再学習せずに量子化する方法を**学習後量子化**(PTQ)という。GPTQ は、層ごとに次の問題を解く [arxiv-2210.17323#c8](https://arxiv.org/pdf/2210.17323v2#page=3 "by performing quantization layer-by-layer, solving a corresponding reconstruction problem for each layer.")。

$$
\arg\min_{\widehat{W}} \ \big\Vert W X - \widehat{W} X \big\Vert_2^2
$$

- $W$ は元の重み、$\widehat{W}$ は量子化した重み、$X$ は少数のデータを流したときのその層への入力である。
- 重みそのものの誤差 $\Vert W - \widehat{W} \Vert$ ではなく、**層の出力の誤差**を小さくする。

**補足(読み方)**:重みを1つずつ単純に丸めると、それぞれの丸め誤差が出力で足し合わさる。出力の誤差を見ていれば、ある重みの丸め誤差を、別の重みを少し動かして打ち消すことができる。そのために、実際の入力 $X$(較正データ)が必要になる。
GPTQ は、較正データとして C4 から取った少数のテキスト断片を使っている [arxiv-2210.17323#c2](https://arxiv.org/pdf/2210.17323v2#page=6 "Our entire GPTQ calibration data consists of 128 random 2048 token segments from the C4 dataset (Raffel et al., 2020), i.e., excerpts from randomly crawled websites, which represents generic text data.")。

## 5. SmoothQuant:難しさを活性から重みに移す

### 等価な変形

層の計算 $Y = XW$ で、活性 $X$ の各チャネル(列)を $s_j$ で割り、重み $W$ の対応する行に $s_j$ を掛ける [arxiv-2211.10438#c8](https://arxiv.org/pdf/2211.10438v7#page=4 "Considering input X is usually produced from previous linear operations (e.g., linear layers, layer norms, etc.), we can easily fuse the smoothing factor into previous layers’ parameters offline, which doe not incur kernel call overhead from an extra scaling.")。

$$
Y = \big( X \operatorname{diag}(s)^{-1} \big) \cdot \big( \operatorname{diag}(s)\, W \big) = \hat{X} \hat{W}
$$

$\operatorname{diag}(s)$ は対角成分が $s_1, s_2, \ldots$ の対角行列である。$\operatorname{diag}(s)^{-1} \operatorname{diag}(s)$ は単位行列なので、量子化する前の計算結果は変わらない。
$s$ は前の層のパラメータにあらかじめ組み込めるので、実行時に余分な計算は増えない [arxiv-2211.10438#c8](https://arxiv.org/pdf/2211.10438v7#page=4 "Considering input X is usually produced from previous linear operations (e.g., linear layers, layer norms, etc.), we can easily fuse the smoothing factor into previous layers’ parameters offline, which doe not incur kernel call overhead from an extra scaling.")。

### 係数の決め方

- $s_j = \max |X_j|$ とすると、活性のどのチャネルも最大値がそろって量子化しやすくなるが、難しさがすべて重みに移る。逆に $s_j = 1/\max |W_j|$ とすると、すべて活性に移る。論文は、どちらも精度が悪いと述べている [arxiv-2211.10438#c9](https://arxiv.org/pdf/2211.10438v7#page=4 "This choice ensures that after the division, all the activation channels will have the same maximum value, which is easy to quantize.")。
- そこで、移す度合いを $\alpha$ で調整する [arxiv-2211.10438#c10](https://arxiv.org/pdf/2211.10438v7#page=4 "Here we introduce a hyper-parameter, migration strength α, to control how much difficulty we want to migrate from activation to weights, using the following equation:")。

$$
s_j = \frac{\max(|X_j|)^{\alpha}}{\max(|W_j|)^{1 - \alpha}}
$$

**補足(例)**:あるチャネルで活性の最大の絶対値が $100$、重みの最大の絶対値が $1$ だとする。$\alpha = 0.5$ なら $s_j = \sqrt{100}/\sqrt{1} = 10$ で、割った後の活性の最大は $10$、掛けた後の重みの最大も $10$ になる。外れ値の大きさが、活性と重みに半分ずつ(対数で見て)分けられている。

$\alpha$ は、論文では検証用データの一部での簡単なグリッド探索で選んでいる [arxiv-2211.10438#c5](https://arxiv.org/pdf/2211.10438v7#page=5 "We get a suitable α by running a quick grid search on a subset of the Pile (Gao et al., 2020) validation set.")。

## まとめ

| 式 | 何を表すか | 根拠 |
|---|---|---|
| $r = S(q - Z)$ | アフィン量子化 | [arxiv-1712.05877#c8](https://arxiv.org/pdf/1712.05877v1#page=3 "Equation (1) is our quantization scheme and the constants S and Z are our quantization parameters.") |
| $x_{\text{int}} = \mathrm{clamp}(\lfloor x/s \rceil + z; 0, 2^b - 1)$、$\hat{x} = s(x_{\text{int}} - z)$ | 量子化と逆量子化 | [arxiv-2106.08295#c8](https://arxiv.org/pdf/2106.08295v1#page=4 "To approximate the real-valued input x we perfrom a de-quantization step:") |
| 丸め誤差 $\in [-s/2, s/2]$ とクリッピング | 2種類の誤差の釣り合い | [arxiv-2106.08295#c9](https://arxiv.org/pdf/2106.08295v1#page=4 "If we want to reduce the clipping error we can expand the quantization range by increasing the scale factor.") |
| $\lfloor 127 X / \max \lvert X \rvert \rceil$ | absmax 量子化 | [arxiv-2208.07339#c8](https://arxiv.org/pdf/2208.07339v2#page=3 "Absmax quantization scales inputs into the 8-bit range [−127, 127] by multiplying with sxf16 which is 127 divided by the absolute maximum of the entire tensor.") |
| $\partial \lfloor y \rceil / \partial y \approx 1$ | STE | [arxiv-2106.08295#c11](https://arxiv.org/pdf/2106.08295v1#page=19 "This poses an issue because the gradient of the round-to-nearest operation in equation (4) is either zero or undeﬁned everywhere, which makes gradient-based training impossible.") |
| $\arg\min \Vert WX - \widehat{W}X \Vert_2^2$ | GPTQ の層ごとの目的 | [arxiv-2210.17323#c8](https://arxiv.org/pdf/2210.17323v2#page=3 "by performing quantization layer-by-layer, solving a corresponding reconstruction problem for each layer.") |
| $Y = (X\operatorname{diag}(s)^{-1})(\operatorname{diag}(s)W)$、$s_j = \max\lvert X_j \rvert^\alpha / \max\lvert W_j \rvert^{1-\alpha}$ | SmoothQuant | [arxiv-2211.10438#c8](https://arxiv.org/pdf/2211.10438v7#page=4 "Considering input X is usually produced from previous linear operations (e.g., linear layers, layer norms, etc.), we can easily fuse the smoothing factor into previous layers’ parameters offline, which doe not incur kernel call overhead from an extra scaling.") [arxiv-2211.10438#c10](https://arxiv.org/pdf/2211.10438v7#page=4 "Here we introduce a hyper-parameter, migration strength α, to control how much difficulty we want to migrate from activation to weights, using the following equation:") |

## 参照カード

- [arxiv-1712.05877](../../papers/arxiv-1712.05877.yaml) Jacob et al., "Quantization and Training of Neural Networks for Efficient Integer-Arithmetic-Only Inference"
- [arxiv-2106.08295](../../papers/arxiv-2106.08295.yaml) Nagel et al., "A White Paper on Neural Network Quantization"
- [arxiv-2208.07339](../../papers/arxiv-2208.07339.yaml) Dettmers et al., "LLM.int8(): 8-bit Matrix Multiplication for Transformers at Scale"
- [arxiv-2210.17323](../../papers/arxiv-2210.17323.yaml) Frantar et al., "GPTQ: Accurate Post-Training Quantization for Generative Pre-trained Transformers"
- [arxiv-2211.10438](../../papers/arxiv-2211.10438.yaml) Xiao et al., "SmoothQuant: Accurate and Efficient Post-Training Quantization for Large Language Models"
