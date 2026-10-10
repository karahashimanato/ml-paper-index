---
title: 数式の解説 0 — 準備:記号、ベクトル、偏微分、確率
kind: math
tags: []
depends_on: []
written_at: 2026-10-10
written_by: claude-opus-5-5 via Claude Code
---

# 数式の解説 0 — 準備:記号、ベクトル、偏微分、確率

<!-- generated:stale -->
> 未反映のカードはありません。
<!-- /generated:stale -->

## このシリーズについて

このシリーズは、これまでの記事で扱ったアルゴリズムの式を、**高校数学Ⅲまでを学んだ人が読める**ように解説する。

- 式は論文から取り、各記事で根拠のカード(論文の該当ページへのリンク)を付ける。
- 式の意味の説明や、簡単な例での計算は、論文の主張ではなく**この記事による解説**である。
- 高校の範囲を少し超える道具(Σ 記号、行列、偏微分、条件付き確率など)は、この「準備」の記事でまとめて説明する。

| 記事 | 扱う式 | 対応する手法の記事 |
|---|---|---|
| [1. 木モデル](01-tree-models.md) | 勾配ブースティングの更新、XGBoost の目的関数と分割の利得、不純度と変数重要度 | [勾配ブースティング木](../methods/gradient-boosted-trees.md)、[ランダムフォレストと決定木](../methods/random-forests-and-decision-trees.md) |
| [2. 生成モデルと表現学習](02-generative-models.md) | VAE の ELBO と再パラメータ化、拡散モデルのノイズの式、InfoNCE と NT-Xent | [オートエンコーダ](../methods/autoencoders.md)、[拡散モデル](../methods/diffusion-models.md)、[対照学習・自己教師あり表現学習](../methods/self-supervised-representation-learning.md) |
| [3. 不確実性と較正](03-uncertainty-and-calibration.md) | ソフトマックス、温度スケーリング、ECE、分割共形予測の分位点と保証 | [不確実性の推定と較正](../topics/uncertainty-and-calibration.md) |
| [4. ベイズ系](04-bayes.md) | ガウス過程の事後分布、期待改善量(EI)と獲得関数、BOCPD のラン長の再帰式とハザード関数 | [ベイズ最適化とハイパーパラメータ最適化](../methods/bayesian-optimization.md)、[ベイズ変化点検知](../topics/bayesian-change-point-detection.md) |
| [5. 線形モデルとカーネル](05-linear-and-kernel.md) | 最小二乗、Lasso と最良部分集合選択、カーネルリッジ回帰、SVM の双対問題、ノイズありのガウス過程と GP-UCB | [ベイズ最適化とハイパーパラメータ最適化](../methods/bayesian-optimization.md) |
| [6. 近似推論](06-approximate-inference.md) | ELBO と CAVI、スコア関数の勾配、メトロポリス・ヘイスティングス法、HMC とリープフロッグ法、R-hat、重要度比、SBC | [近似ベイズ推論とその診断](../methods/approximate-inference-and-diagnostics.md) |
| [7. ドリフト検知と統計的検定](07-drift-and-tests.md) | ドリフトの定義、時刻とデータの独立、KS 統計量、Bonferroni 補正、MMD | [概念ドリフトとデータシフトの検出](../tasks/drift-detection.md) |
| [8. 説明手法](08-explanations.md) | シャープレイ値と SHAP、観測的と介入的の価値関数、LIME の目的関数、積分勾配と完全性 | [モデルの解釈可能性](../topics/model-interpretability.md) |
| [9. 量子化](09-quantization.md) | アフィン量子化、量子化と逆量子化、丸め誤差とクリッピング、absmax、STE、GPTQ の目的、SmoothQuant | [量子化による影響](../topics/quantization-effects.md) |
| [10. 知識蒸留と GNN](10-distillation-and-gnn.md) | 温度付きソフトマックスと蒸留の勾配、T² の補正、ヒント損失、GCN の層とその導出、SGC、過平滑化、メッセージパッシング、GAT の注意、GIN と WL 検定、エッジ同質性 | [知識蒸留と枝刈り](../methods/knowledge-distillation-and-pruning.md)、[グラフニューラルネットワーク](../methods/graph-neural-networks.md) |
| [11. 表データの深層学習](11-tabular-deep-learning.md) | sparsemax と entmax、NODE の微分可能な決定木、TabNet のマスクと事前スケール、DCN V2 の交差層、区分線形の符号化と周期的な埋め込み、TabR の近傍の重み、SCARF の置き換え | [表データの深層学習モデル](../methods/tabular-deep-learning-models.md) |
| [12. 因果効果の推定](12-causal-effect-estimation.md) | 潜在的結果と CATE、傾向スコアと逆確率重み付け、T/S/X/RA-learner、DR-learner と二重頑健性、Robinson の分解と R-loss、DML の部分線形モデル | [因果効果の推定](../topics/causal-effect-estimation.md) |

この記事には論文の主張は含まれない。高校数学で学ぶ内容の確認と、そこから一歩進んだ道具の説明である。

## 1. 記号の読み方

### 和の記号 Σ

$\sum$(シグマ)は「足し合わせ」を表す。数学Bの数列で学ぶ記号である。

$$
\sum_{i=1}^{n} a_i = a_1 + a_2 + \cdots + a_n
$$

機械学習では、$i$ がデータの番号を表すことが多い。たとえば $n$ 個のデータそれぞれの誤差 $e_i$ の合計は $\sum_{i=1}^{n} e_i$ と書く。
足す範囲を集合で書くこともある。$\sum_{i \in I} g_i$ は「集合 $I$ に属する番号 $i$ についてだけ $g_i$ を足す」という意味である。

### 積の記号 Π

$\prod$(パイ)は「掛け合わせ」を表す。

$$
\prod_{i=1}^{n} a_i = a_1 \times a_2 \times \cdots \times a_n
$$

### 最小値を与える点:argmin と argmax

$\min_x f(x)$ は「$f(x)$ の最小値」、$\arg\min_x f(x)$ は「$f(x)$ を最小にする $x$」を表す。値そのものではなく、それを実現する点を返すのが argmin である。

例:$f(x) = (x-3)^2 + 1$ なら、$\min_x f(x) = 1$、$\arg\min_x f(x) = 3$。

### 集合の記号

- $x \in A$:$x$ は集合 $A$ の要素である
- $A \cup B$:$A$ と $B$ の和集合
- $\{ i \mid \text{条件} \}$:条件を満たす $i$ の集合

## 2. ベクトルと行列の最低限

### ベクトル

数学Cでは、平面や空間のベクトルを $(a_1, a_2)$ や $(a_1, a_2, a_3)$ のように成分で表した。機械学習では、これを**任意の個数の数を並べたもの**に広げる。$d$ 個の数を並べたものを $d$ 次元のベクトルという。

$$
\boldsymbol{x} = (x_1, x_2, \ldots, x_d)
$$

たとえば、ある人の「年齢、身長、体重」を並べた $(35, 170, 60)$ は3次元のベクトルである。表データの1行が1つのベクトルにあたる。

- **内積**:$\boldsymbol{x} \cdot \boldsymbol{y} = \sum_{j=1}^{d} x_j y_j$。数学Cの内積を $d$ 次元に広げたもの。
- **長さ(ノルム)**:$\|\boldsymbol{x}\| = \sqrt{\boldsymbol{x} \cdot \boldsymbol{x}} = \sqrt{\sum_{j} x_j^2}$。$\|\boldsymbol{x}\|^2$ はその2乗で、成分の2乗の和になる。

### 行列

行列は、数を長方形に並べたものである(現在の高校の範囲には含まれない)。この記事のシリーズでは、次の2点だけ知っていれば読める。

- **行列とベクトルの積**:行列 $A$ の各行とベクトル $\boldsymbol{x}$ の内積を並べたもの。1次関数 $y = ax$ を多次元に広げた「線形な変換」を表す。
- **単位行列 $I$**:対角成分が1、それ以外が0の行列。$I\boldsymbol{x} = \boldsymbol{x}$ となり、数の「1」にあたる。

## 3. 関数の最小化と微分

### 数学Ⅲの微分の復習

関数 $f(x)$ の微分係数 $f'(x)$ は、$x$ を少し動かしたときの $f$ の変化の割合である。

- $f'(x) > 0$ なら、$x$ を増やすと $f$ が増える
- $f'(x) < 0$ なら、$x$ を増やすと $f$ が減る
- 最小値をとる点では(なめらかな関数なら)$f'(x) = 0$

### 偏微分と勾配

変数が複数ある関数 $f(x_1, x_2)$ では、**1つの変数だけを動かし、他を定数とみなして**微分する。これを偏微分といい、$\dfrac{\partial f}{\partial x_1}$ と書く。

例:$f(x_1, x_2) = x_1^2 + 3x_1 x_2$ なら

$$
\frac{\partial f}{\partial x_1} = 2x_1 + 3x_2, \qquad \frac{\partial f}{\partial x_2} = 3x_1
$$

偏微分を並べたベクトルを**勾配**といい、$\nabla f$ と書く。

$$
\nabla f = \left( \frac{\partial f}{\partial x_1}, \frac{\partial f}{\partial x_2}, \ldots, \frac{\partial f}{\partial x_d} \right)
$$

勾配は「$f$ が最も急に増える向き」を指す。したがって、**勾配と逆向きに少し動けば $f$ は減る**。

### 勾配降下法

関数を小さくしたいとき、次の更新を繰り返す方法を勾配降下法という。

$$
\boldsymbol{x} \leftarrow \boldsymbol{x} - \eta \, \nabla f(\boldsymbol{x})
$$

$\eta$(イータ)は「1回にどれだけ動くか」を決める小さな正の数で、**学習率**と呼ばれる。$\leftarrow$ は「右辺の値で左辺を置き換える」という意味である。

例:$f(x) = (x-3)^2$、$\eta = 0.25$、$x = 1$ から始めると、$f'(x) = 2(x-3)$ なので
$x \leftarrow 1 - 0.25 \times 2 \times (1-3) = 2$、次は $x \leftarrow 2 - 0.25 \times 2 \times (2-3) = 2.5$ と、最小値をとる $x = 3$ に近づいていく。

### 2次の近似(テイラー展開の最初の項)

$x$ の近くで $f(x + t)$ を、$t$ の2次式で近似できる。

$$
f(x + t) \approx f(x) + f'(x)\, t + \frac{1}{2} f''(x)\, t^2
$$

この近似は数学Ⅲの範囲で確かめられる。右辺を $t$ で微分すると $f'(x) + f''(x) t$ で、$t = 0$ のとき左辺と右辺の値・1回微分・2回微分がすべて一致するように作られている。

2次式 $a t + \frac{1}{2} b t^2$($b > 0$)は、$t = -\dfrac{a}{b}$ で最小値 $-\dfrac{a^2}{2b}$ をとる(平方完成で確かめられる)。木モデルの記事で、XGBoost の葉の重みの式がこの形で出てくる。

## 4. 確率の道具

### 期待値と分散(数学Bの復習)

確率変数 $X$ の期待値 $E[X]$ は「平均的な値」、分散 $V[X] = E[(X - E[X])^2]$ は「平均からのばらつき」である。データの平均 $\bar{y} = \frac{1}{n}\sum_i y_i$ は、期待値の推定にあたる。

### 条件付き確率とベイズの定理

「$B$ が起きたときに $A$ が起きる確率」を条件付き確率といい、$P(A \mid B)$ と書く。

$$
P(A \mid B) = \frac{P(A \cap B)}{P(B)}
$$

これを使うと、**ベイズの定理**が得られる。

$$
P(A \mid B) = \frac{P(B \mid A)\, P(A)}{P(B)}
$$

機械学習では、$A$ を「モデルのパラメータ $\theta$」、$B$ を「観測したデータ $D$」とすることが多い。

$$
\underbrace{p(\theta \mid D)}_{\text{事後分布}} = \frac{\overbrace{p(D \mid \theta)}^{\text{尤度}} \; \overbrace{p(\theta)}^{\text{事前分布}}}{p(D)}
$$

データを見る前の考え(事前分布)を、データの出やすさ(尤度)で更新すると、データを見た後の考え(事後分布)が得られる、という式である。

### 独立と対数

データが互いに**独立**に生成されると仮定すると、全データの確率は個々の確率の積になる。

$$
p(y_1, \ldots, y_n) = \prod_{i=1}^{n} p(y_i)
$$

積は扱いにくいので、対数をとって和に直すことが多い($\log ab = \log a + \log b$)。

$$
\log \prod_{i=1}^{n} p(y_i) = \sum_{i=1}^{n} \log p(y_i)
$$

対数は単調に増える関数なので、確率を最大にする点と、対数をとった値を最大にする点は同じである。

### 正規分布

平均 $\mu$、分散 $\sigma^2$ の正規分布(数学Bで扱う)の密度は

$$
p(x) = \frac{1}{\sqrt{2\pi \sigma^2}} \exp\!\left( -\frac{(x - \mu)^2}{2\sigma^2} \right)
$$

である。$\exp(a)$ は $e^a$ のこと。$\mathcal{N}(\mu, \sigma^2)$ と書くことが多い。

## このシリーズの読み方の注意

- 論文ごとに記号の使い方が少しずつ違う。各記事では、その論文の記号に合わせたうえで、意味を言葉で説明する。
- 式の導出のうち、論文に書かれている部分は根拠のカードで示す。書かれていない途中の計算は、この記事による補足であることを明示する。
