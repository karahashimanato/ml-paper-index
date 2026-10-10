---
title: 混合エキスパートと状態空間モデル — Transformer の計算をどこで減らし、何を失うのか
kind: method
tags: [mixture-of-experts, state-space-models, efficient-attention]
depends_on: [arxiv-1701.06538, arxiv-2006.16668, arxiv-2202.08906, arxiv-2202.09368, arxiv-2112.06905, arxiv-2401.04088, arxiv-2101.03961, arxiv-2110.12894, arxiv-2008.07669, arxiv-2111.00396, arxiv-2212.14052, arxiv-2312.00752, arxiv-2405.21060, arxiv-2402.01032, arxiv-2406.07887, arxiv-2006.16236, arxiv-2009.14794, arxiv-2305.13048, arxiv-2011.04006, arxiv-2205.14135, arxiv-2009.06732]
written_at: 2026-10-11
written_by: claude-opus-5-5 via Claude Code
---

# 混合エキスパートと状態空間モデル — Transformer の計算をどこで減らし、何を失うのか

<!-- generated:stale -->
> 未反映のカードはありません。
<!-- /generated:stale -->

## この記事の読み方

標準的な(密な)Transformer には、大きく2つの重い部分がある。

- **フィードフォワード層**:パラメータの大部分を占め、すべてのトークンですべてのパラメータを使う。
- **注意**:系列の長さ $N$ に対して計算とメモリが $N^2$ で増える。

この記事は、それぞれを軽くする2つの系統を整理する。

1. **混合エキスパート(MoE)**:トークンごとに一部のパラメータ(エキスパート)だけを使い、パラメータを増やしても計算を増やさない。
2. **状態空間モデル(SSM)と線形注意**:注意を、系列の長さに比例する計算で済む再帰的な形に置き換える。

さらに、両者の弱点(学習の不安定さ、コピーや検索の苦手さ)と、効率の比べ方の注意を整理する。16本の新しいカードと既存の5本のカードに基づく。
性能の数値は書かない。各論文のページの結果表を参照のこと(カードは結果表を記録せず、主張だけを記録している)。

## 1. 混合エキスパート

### 基本の形

Shazeer らの MoE 層は、$n$ 個のエキスパート $E_1, \ldots, E_n$ と、ゲート $G$ からなる [arxiv-1701.06538#c1](https://arxiv.org/pdf/1701.06538v1#page=3 "We save computation based on the sparsity of the output of G(x).")。

$$
y = \sum_{i=1}^{n} G(x)_i \, E_i(x)
$$

$G(x)$ はほとんどの成分が0の疎なベクトルで、$G(x)_i = 0$ のエキスパートは計算しなくてよい [arxiv-1701.06538#c1](https://arxiv.org/pdf/1701.06538v1#page=3 "We save computation based on the sparsity of the output of G(x).")。ゲートはロジットにノイズを加えてから上位 $k$ 個だけを残す(ノイズ付きの top-k)[arxiv-1701.06538#c2](https://arxiv.org/pdf/1701.06538v1#page=4 "While this form of sparsity creates some theoretically scary discontinuities in the output of gating function, we have not yet observed this to be a problem in practice.")。
Mixtral も同じ形で、各層に8つのエキスパートを持ち、トークンごとに2つを選ぶ [arxiv-2401.04088#c1](https://arxiv.org/pdf/2401.04088v1#page=1 "As a result, each token has access to 47B parameters, but only uses 13B active parameters during inference.") [arxiv-2401.04088#c2](https://arxiv.org/pdf/2401.04088v1#page=2 "There are multiple alternative ways of implementing G(x) [6, 15, 35], but a simple and performant one is implemented by taking the softmax over the Top-K logits of a linear layer [28].")。

### 総パラメータと活性パラメータ

エキスパートの数を増やしても、選ぶ数 $k$ が同じなら1トークンあたりの計算はほぼ変わらない。そのため、MoE では**総パラメータ数**と、1トークンで実際に使う**活性パラメータ数**を区別する [arxiv-2401.04088#c3](https://arxiv.org/pdf/2401.04088v1#page=3 "This motivates a distinction between the model’s total parameter count (commonly referenced as the sparse parameter count), which grows with n, and the number of parameters used for processing an individual token (called the active parameter count), which grows with K up to n.")。Switch Transformer の論文も、パラメータは多いが計算は一定の「疎に活性化される」モデルとして MoE を位置づけている [arxiv-2101.03961#c1](https://arxiv.org/pdf/2101.03961v3#page=1 "The result is a sparsely-activated model—with an outrageous number of parameters—but a constant computational cost.")。

### 負荷の偏り

MoE の典型的な失敗は、ゲートがいつも同じ少数のエキスパートに大きな重みを与えるようになり、その偏りが自己強化されることである [arxiv-1701.06538#c4](https://arxiv.org/pdf/1701.06538v1#page=5 "This imbalance is self-reinforcing, as the favored experts are trained more rapidly and thus are selected even more by the gating network.")。対策として、各エキスパートの重要度や負荷をそろえる**補助損失**を加える [arxiv-1701.06538#c4](https://arxiv.org/pdf/1701.06538v1#page=5 "This imbalance is self-reinforcing, as the favored experts are trained more rapidly and thus are selected even more by the gating network.") [arxiv-1701.06538#c5](https://arxiv.org/pdf/1701.06538v1#page=13 "Instead, we deﬁne a smooth estimator Load(X) of the number of examples assigned to each expert for a batch X of inputs.")。偏りをそろえる損失をまったく使わないと、品質は大きく悪化した [arxiv-1701.06538#c6](https://arxiv.org/pdf/1701.06538v1#page=14 "All the combinations containing at least one the two losses led to very similar model quality, where having no loss was much worse.")。

GShard は、エキスパートが処理するトークン数に**容量**の上限を設け、上限を超えたトークンは処理せずに残差接続だけで次の層に渡す [arxiv-2006.16668#c2](https://arxiv.org/pdf/2006.16668v1#page=6 "Such tokens have their representation xs passed on to the next layer via residual connections.")。補助損失も、微分できない top-2 の選択の代わりに、微分できる近似を使って定義している [arxiv-2006.16668#c3](https://arxiv.org/pdf/2006.16668v1#page=6 "But because ce is derived from top-2 operation and is not differentiable, we use the mean gates per expert me as a differentiable approximation and replace (ce/S)2 with me(ce/S), which can now be optimized with gradient descent.")。
Zhou らは、トークンがエキスパートを選ぶ方式では、補助損失があっても特に学習の初期に負荷がそろわず、一部のエキスパートが容量を大きく超えることを観察した [arxiv-2202.09368#c2](https://arxiv.org/pdf/2202.09368v2#page=3 "Indeed, we empirically observe that the over-capacity ratio can reach 20%–40% for some experts in token choice routing, indicating that a signiﬁcant portion of the tokens routed to these experts will be dropped.")。そこで逆に、**エキスパートがトークンを選ぶ**方式を提案し、負荷を設計上完全にそろえた [arxiv-2202.09368#c1](https://arxiv.org/pdf/2202.09368v2#page=3 "Despite its simplicity, expert choice achieves perfect load balancing by design.")。ただしこの方式は、未来のトークンも使って選ぶため、自己回帰的な生成にはそのまま使えない [arxiv-2202.09368#c7](https://arxiv.org/pdf/2202.09368v2#page=9 "The expert choice method might not immediately apply to auto-regressive text generation as our current implementation takes in the past and future tokens to perform the top-k selection.")。

### 学習の不安定さと微調整

- GShard は、安定性のために重みと活性を float32 で学習し、bfloat16 での1兆パラメータの学習は数値の不安定さのため断念した [arxiv-2006.16668#c5](https://arxiv.org/pdf/2006.16668v1#page=16 "Although trainable by careful and manual diagnostics, with deep 1 trillion model we encountered several trainability issues with numerical stability, hence did not include the results for the sake of reproducibility.")。
- ST-MoE は、ゲートのロジットが大きくなりすぎないように罰する **router z-loss** を提案した [arxiv-2202.08906#c1](https://arxiv.org/pdf/2202.08906v2#page=7 "This penalizes large logits into the gating network and Section 3.4 contains a more detailed explanation of why the z-loss before the router is useful.")。安定化の手法の多くは品質を下げたが、z-loss は品質を下げずに安定させた [arxiv-2202.08906#c2](https://arxiv.org/pdf/2202.08906v2#page=8 "Table 4 shows that both update clipping and the router z-loss stabilize the model in all 3 runs, but the update clipping signiﬁcantly hurts the model quality.")。著者らは、ゲートの指数関数が bfloat16 の丸め誤差を増幅することが不安定さの一因だと推測している [arxiv-2202.08906#c3](https://arxiv.org/pdf/2202.08906v2#page=9 "Finally, we conjecture that the higher stability we observed for decoder-only models (not shown here) was because they had fewer exponential functions.")。
- GLaM は、勾配に NaN や Inf が出たバッチの更新を飛ばし、健全なチェックポイントから再開する方法で対処した [arxiv-2112.06905#c8](https://arxiv.org/pdf/2112.06905v2#page=5 "We restart from an early healthy checkpoint when encountering rare large ﬂuctuations or even NaN/Inf during training.")。
- 微調整では、疎なモデルは小さいデータセットで過学習しやすい [arxiv-2202.08906#c4](https://arxiv.org/pdf/2202.08906v2#page=10 "However, on the smaller task, CB, the sparse model lags its dense counterpart on held-out data.")。疎なモデルは、密なモデルとは逆に、小さいバッチと大きい学習率が合う傾向があり、密なモデル向けの設定を使い回すと利点が隠れうる [arxiv-2202.08906#c5](https://arxiv.org/pdf/2202.08906v2#page=11 "Sparse models beneﬁt from smaller batch sizes and a higher learning rate.")。

### 費用の数え方

- Mixtral の論文は、効率の比較は活性パラメータ数(推論の計算に比例)に注目したもので、メモリやハードウェアの利用率は考慮していないと明記している。推論時のメモリは総パラメータ数に比例する [arxiv-2401.04088#c6](https://arxiv.org/pdf/2401.04088v1#page=4 "Note that this analysis focuses on the active parameter count (see Section 2.1), which is directly proportional to the inference compute cost, but does not consider the memory costs and hardware utilization.")。
- GLaM の著者らは、学習の消費エネルギーが減ったのは MoE の構造だけでなく、ハードウェアとソフトウェアの最適化も合わせた結果だとしている [arxiv-2112.06905#c7](https://arxiv.org/pdf/2112.06905v2#page=7 "The reduced energy consumption of GLaM is due to the MoE architecture and computation efﬁciency optimizations from TPU-v4 hardware and GSPMD software.")。また、総パラメータが多いぶん多くの機器が必要で、利用が少ないときの提供コストが高くなる [arxiv-2112.06905#c9](https://arxiv.org/pdf/2112.06905v2#page=9 "This limits the resource accessibility and increases the serving cost especially when the serving trafﬁc is low.")。Zhou らも、使わない機器を確保しておく電力は節約できないと述べている [arxiv-2202.09368#c8](https://arxiv.org/pdf/2202.09368v2#page=9 "Therefore, dynamic (used) power is saved while static (reserved) power is not.")。
- Switch Transformer の論文は、1ステップあたりのサンプル効率が高くても、通信やゲートの計算が増えるので、実時間で速いとは限らないと注意している [arxiv-2101.03961#c4](https://arxiv.org/pdf/2101.03961v3#page=13 "Therefore, the increased sample eﬃciency observed on a step-basis doesn’t necessarily translate to a better model quality as measured by wall-clock.")。
- GShard の著者らは、パラメータ数だけでは大規模なモデルの実際の能力を測れないと述べている [arxiv-2006.16668#c8](https://arxiv.org/pdf/2006.16668v1#page=25 "Lastly, our experimental results empirically support that, mere parameter counting does not always correlate with the effective capacity of the models at scale [85, 86].")。The Efficiency Misnomer も、疎なモデルをパラメータ数をそろえて比べることは意味がないと論じている [arxiv-2110.12894#c6](https://arxiv.org/pdf/2110.12894v2#page=8 "Hence, parameter matched comparisons do not make sense for sparse models and parameter-matching sparse models can be seen as an unfair method of unnecessarily downplaying the strengths of sparse models.")。

### エキスパートは何に特化しているか

Mixtral のゲートの分析では、話題(論文、医学の要旨、哲学など)による明らかな分担は見られなかった [arxiv-2401.04088#c8](https://arxiv.org/pdf/2401.04088v1#page=7 "Surprisingly, we do not observe obvious patterns in the assignment of experts based on the topic.")。代わりに、連続するトークンが同じエキスパートに送られやすい(位置の局所性)ことがわかった [arxiv-2401.04088#c9](https://arxiv.org/pdf/2401.04088v1#page=8 "For example, cases with high locality are more likely to cause over-subscription of certain experts when doing Expert Parallelism.")。

## 2. 状態空間モデル

### 連続時間の状態空間と HiPPO

**補足**:状態空間モデルの一般的な形は、入力 $u(t)$ を、状態 $x(t)$ を通じて出力 $y(t)$ に写す次の式である(特定の論文の主張ではなく、以下の論文に共通する出発点)。

$$
x'(t) = A x(t) + B u(t), \qquad y(t) = C x(t) + D u(t)
$$

HiPPO は、これまでの入力の履歴を多項式で近似し続けると、その係数がちょうどこの形の微分方程式に従うことを示した [arxiv-2008.07669#c1](https://arxiv.org/pdf/2008.07669v2#page=4 "Thus our results show how to tractably obtain c(t) online by solving an ODE, or more concretely by running a discrete recurrence.")。過去全体に一様な重みを置く版(LegS)は、時間のスケールを変えても係数が変わらない性質を持つ [arxiv-2008.07669#c4](https://arxiv.org/pdf/2008.07669v2#page=6 "Formally, the HiPPO-LegS operator is timescale-equivariant: dilating the input f does not change the approximation coeﬃcients.")。

### S4:長い系列を効率よく

S4 は、この連続時間のモデルを刻み幅 $\Delta$ で離散化し、再帰(RNN)としても、畳み込みとしても計算できるようにした [arxiv-2111.00396#c1](https://arxiv.org/pdf/2111.00396v3#page=4 "The recurrent SSM (3) is not practical for training on modern hardware due to its sequentiality.")。学習時は畳み込みで並列に、推論時は再帰で1ステップずつ計算できる。
HiPPO の行列をそのまま対角化すると数値的に不安定になるので [arxiv-2111.00396#c2](https://arxiv.org/pdf/2111.00396v3#page=5 "Unfortunately, the naive application of diagonalization does not work due to numerical issues.")、「正規行列 + 低ランク行列」の分解を使って計算を速くした [arxiv-2111.00396#c3](https://arxiv.org/pdf/2111.00396v3#page=5 "We make the observation that although the HiPPO matrix is not normal, it can be decomposed as the sum of a normal and low-rank matrix.")。著者らのアブレーションでは、効果の主な源は HiPPO による初期化だった [arxiv-2111.00396#c8](https://arxiv.org/pdf/2111.00396v3#page=11 "Fig. 4a shows that random NPLR matrices still do not perform well, which validates that S4’s eﬀectiveness primarily comes from the HiPPO initialization, not the NPLR parameterization.")。
ただし、実装は理論上速いアルゴリズムではなく素朴なアルゴリズムを使っており [arxiv-2111.00396#c4](https://arxiv.org/pdf/2111.00396v3#page=16 "Our current implementation of S4 actually uses the naive O(NL) algorithm which is easily parallelized on GPUs")、言語モデルでは Transformer との差が残ると述べている [arxiv-2111.00396#c9](https://arxiv.org/pdf/2111.00396v3#page=16 "For example, Table 8 still found a gap compared to Transformers for language modeling.")。

### H3:言語モデルに足りなかったもの

Fu らは、合成タスク(帰納ヘッド、連想の想起)で、それまでの SSM が失敗することを示し、言語の一般的な処理に必要な表現力が足りないかもしれないと述べた [arxiv-2212.14052#c1](https://arxiv.org/pdf/2212.14052v3#page=4 "We argue that these failures suggest two missing capabilities: (i) to remember tokens that appear after a particular event (e.g., the special token in the induction head task), and (ii) to compare tokens across the sequence (e.g., comparing keys to decide which value to recall).")。H3 は、線形注意の構造の一部を SSM で置き換えた層である [arxiv-2212.14052#c2](https://arxiv.org/pdf/2212.14052v3#page=5 "H3 is loosely inspired by linear attention (Section 2): we project the input u to get three signals Q, K, V.")。注意の層を2つだけ残した混成モデルは、Transformer より良いパープレキシティを示した [arxiv-2212.14052#c4](https://arxiv.org/pdf/2212.14052v3#page=6 "A simple hybrid H3-attention language model surprisingly outperforms Transformers on OpenWebText by 1.0 point.")。

### Mamba と Mamba-2

Mamba は、SSM のパラメータを**入力に応じて変える**(選択的)ことで、情報を選んで残したり忘れたりできるようにした [arxiv-2312.00752#c1](https://arxiv.org/pdf/2312.00752v2#page=1 "First, simply letting the SSM parameters be functions of the input addresses their weakness with discrete modalities, allowing the model to selectively propagate or forget information along the sequence length dimension depending on the current token.")。推論時に注意のキャッシュが要らないので、大きなバッチで高いスループットが出る [arxiv-2312.00752#c4](https://arxiv.org/pdf/2312.00752v2#page=15 "Mamba achieves 4-5× higher inference throughput than a Transformer of similar size, since without the KV cache it can use much higher batch sizes.")。著者らは、評価が小さいモデルに限られ、大規模でも有利かはわからないと認めている [arxiv-2312.00752#c7](https://arxiv.org/pdf/2312.00752v2#page=17 "It remains to assess whether Mamba still compares favorably at these larger sizes.")。

Mamba-2 は、状態の行列 $A$ を「スカラー × 単位行列」に単純化し、行列積を多く使えるようにした [arxiv-2405.21060#c1](https://arxiv.org/pdf/2405.21060v1#page=5 "Compared to the original selective SSM, these changes can be viewed as slightly decreasing the expressive power in return for significant training efficiency improvements.")。理論の面では、SSM が半分離行列と同値であり、線形注意の一般化と SSM が対応すること(状態空間の双対性)を示した [arxiv-2405.21060#c2](https://arxiv.org/pdf/2405.21060v1#page=2 "We also prove that any kernel attention method possessing a fast recurrent form must be an SSM.")。

## 3. 線形注意と RNN 型の構造

### 線形注意

Katharopoulos らは、注意をカーネルの特徴写像 $\phi$ の内積として書き、行列積の結合法則を使うことで、計算量を $N^2$ から $N$ に下げた [arxiv-2006.16236#c1](https://arxiv.org/pdf/2006.16236v3#page=1 "we express the self-attention as a linear dot-product of kernel feature maps and make use of the associativity property of matrix products to reduce the complexity")。

$$
\text{softmax 注意:} \ \mathrm{softmax}(QK^\top) V \quad \longrightarrow \quad \text{線形注意:} \ \phi(Q) \big( \phi(K)^\top V \big)
$$

右の形では、$\phi(K)^\top V$ を先に計算すれば、$N \times N$ の行列を作らずに済む。因果的なマスクを付けると、この操作は「注意の記憶」と「正規化の記憶」の2つの状態を持つ RNN として書ける [arxiv-2006.16236#c5](https://arxiv.org/pdf/2006.16236v3#page=5 "any transformer layer with causal masking can be written as a model that, given an input, modiﬁes an internal state and then predicts an output, namely a Recurrent Neural Network (RNN).")。
ただし、音声認識の実験では、ソフトマックスの注意が線形注意を含むどのベースラインよりも誤り率が低かった(代わりにずっと遅い)[arxiv-2006.16236#c8](https://arxiv.org/pdf/2006.16236v3#page=8 "Note that the softmax transformer, achieves lower phone error rate in comparison to all baselines, but is signiﬁcantly slower.")。

### Performer

Performer は、ソフトマックスのカーネルを**正の**ランダム特徴で近似する [arxiv-2009.14794#c4](https://arxiv.org/pdf/2009.14794v4#page=4 "Consequently, softmax-kernel admits a positive random feature map unbiased approximation with")。三角関数のランダム特徴では、カーネルの値が0に近いところで推定が不安定になり、負の値も出るためである [arxiv-2009.14794#c3](https://arxiv.org/pdf/2009.14794v4#page=4 "Applying random feature maps with potentially negative dimension-values (sin / cos) leads to unstable behaviours")。ただし、近似の小さな誤差が層を重ねるごとに伝わるので、学習済みのソフトマックスのモデルの重みを移すには微調整が必要だった [arxiv-2009.14794#c8](https://arxiv.org/pdf/2009.14794v4#page=7 "In other words, the model’s Lipschitz constant can easily scale up small attention approximation error, which means that very tight approximations may sometimes be needed.")。

### RWKV

RWKV は、チャネルごとの時間減衰を使って、注意に似た計算を RNN として行う [arxiv-2305.13048#c1](https://arxiv.org/pdf/2305.13048v2#page=3 "and the per-channel weights decay backwards in time.") [arxiv-2305.13048#c2](https://arxiv.org/pdf/2305.13048v2#page=4 "To circumvent any potential degradation of W, we introduce a vector U that separately attends to the current token.")。著者らは、線形注意は情報を1つのベクトルに押し込むので、長い文脈の細部を思い出す課題では性能が限られうると述べている [arxiv-2305.13048#c9](https://arxiv.org/pdf/2305.13048v2#page=8 "First, the linear attention of RWKV leads to significant efficiency gains but still, it may also limit the model’s performance on tasks that require recalling minutiae information over very long contexts.")。

### 近似しない高速化:FlashAttention

これらとは逆に、FlashAttention は、注意を近似せず、GPU のメモリの読み書きを減らして速くする [arxiv-2205.14135#c1](https://arxiv.org/pdf/2205.14135v2#page=1 "We propose FlashAttention, an IO-aware exact attention algorithm that uses tiling to reduce the number of memory reads/writes between GPU high bandwidth memory (HBM) and GPU on-chip SRAM.")。著者らは、多くの近似の注意は計算量を減らしても、メモリの読み書きを考えないため実時間で速くならないと批判している [arxiv-2205.14135#c2](https://arxiv.org/pdf/2205.14135v2#page=1 "One main reason is that they focus on FLOP reduction (which may not correlate with wall-clock speed) and tend to ignore overheads from memory access (IO).")。

## 4. 共通の弱点:コピーと検索

状態空間モデルや線形注意は、固定の大きさの状態に過去を要約する。このため、入力をそのまま覚えて取り出す課題が苦手になりうる。

- Jelassi らは、状態の記憶が入力の長さより小さいモデルは、長い文字列のコピーを正しく行えないことを理論で示した [arxiv-2402.01032#c3](https://arxiv.org/pdf/2402.01032v2#page=4 "This is intuitive: to be able to copy the entire input sequence, the model needs to store it in its state space, which requires the memory to grow linearly with the sequence length.")。ただし、これは表現力の理論で、学習で獲得できるかは別の問題である [arxiv-2402.01032#c4](https://arxiv.org/pdf/2402.01032v2#page=1 "Our theory studies representation expressivity, but not whether these representations will be learned.")。実験では、Transformer はコピーの課題を、状態空間モデルよりずっと少ないデータで学習できた [arxiv-2402.01032#c6](https://arxiv.org/pdf/2402.01032v2#page=5 "We observe that the transformers need 100x less samples than the best GSSMs to learn the copy task.")。一方、検索するキーが先に与えられる課題では、状態空間モデルもうまくいった [arxiv-2402.01032#c7](https://arxiv.org/pdf/2402.01032v2#page=6 "Indeed, GSSMs achieve perfect length-generalization on this variant.")。
- Waleffe らは、同じデータと設定で学習した 8B の Mamba 系と Transformer を比べた [arxiv-2406.07887#c1](https://arxiv.org/pdf/2406.07887v1#page=2 "In particular, our primary goal is to provide a rigorous apples-to-apples comparison between Mamba, Mamba-2, Mamba-2-Hybrid (containing Mamba-2, attention, and MLP layers), and Transformers for 8B-parameter models trained on up to 3.5T tokens, with the same hyperparameters.")。電話帳の検索の課題で、Mamba 系はある程度より長い文脈で誤り始めた [arxiv-2406.07887#c5](https://arxiv.org/pdf/2406.07887v1#page=8 "In contrast, both Mamba and Mamba-2 models begin to respond incorrectly for input sequence lengths beyond approximately 500 tokens.")。知識を問う MMLU では、問題の書き方によって差が大きく変わった [arxiv-2406.07887#c4](https://arxiv.org/pdf/2406.07887v1#page=6 "While the pure SSM models struggle with the standard and choice-text-in-targets formulations, they actually exceed the accuracy of the Transformer in the cloze setting.")。
- Mamba-2 の論文も、有限の状態のため検索の課題が難しいことを、引用した研究に基づいて述べている [arxiv-2405.21060#c7](https://arxiv.org/pdf/2405.21060v1#page=30 "(We are not sure which aspect of the architecture is the predominant factor, which remains a question to explore in future work.)")。

この弱点への答えとして、少数の注意層を混ぜる**混成モデル**が提案されている。Mamba-2 の実験では約1割を注意層にするのがよく [arxiv-2405.21060#c8](https://arxiv.org/pdf/2405.21060v1#page=30 "We hypothesize that the SSM layers function well as a general sequence-to-sequence mapping, and attention layers act as a retrieval mechanism to quickly refer to previous tokens in the sequence instead of forcing the model to compress all the context to its memory (SSM states).")、Waleffe らの混成モデルは56層のうち4層が注意である [arxiv-2406.07887#c6](https://arxiv.org/pdf/2406.07887v1#page=10 "Out of 56 total layers, the hybrid model has 4 (7.1%) self-attention layers, 24 (42.9%) Mamba-2 layers, and 28 (50%) MLP layers.")。ただし、混成モデルも長い文脈の複数文書の質問応答では Transformer に及ばなかった [arxiv-2406.07887#c9](https://arxiv.org/pdf/2406.07887v1#page=12 "We hypothesize that the hybrid model reaches lower accuracy than the Transformer on these tasks because the SSM layer states are sometimes confused by documents irrelevant to the question")。

## 5. 効率の比べ方

### ベンチマーク:Long Range Arena

Long Range Arena は、効率的な Transformer を比べる共通の場がないという問題意識から作られた [arxiv-2011.04006#c1](https://arxiv.org/pdf/2011.04006v1#page=1 "Firstly, there is no unifying consensus on what makes an acceptable test bed for benchmarking efﬁcient Transformers.")。

- 完全に公平な評価はほぼ不可能だと認め、すべてのモデルに同じハイパーパラメータを使っている。積極的に調整すれば順位は変わりうる [arxiv-2011.04006#c4](https://arxiv.org/pdf/2011.04006v1#page=6 "The best performance and relative order of the models may change if we aggressively tune hyperparameters for all models.")。
- 最も長い課題(Path-X)では、すべてのモデルが失敗した [arxiv-2011.04006#c6](https://arxiv.org/pdf/2011.04006v1#page=7 "All models failed to solve the Path-X task, achieving at best 50%.")。S4 は後にこの課題を解いたと報告している [arxiv-2111.00396#c6](https://arxiv.org/pdf/2111.00396v3#page=9 "S4 substantially advances the SoTA, outperforming all baselines on all tasks and averaging 80.48% compared to less than 60% for every baseline.")。ただし S4 の論文自身、表の数値を後続研究の結果に差し替えたと注記している [arxiv-2111.00396#c7](https://arxiv.org/pdf/2111.00396v3#page=30 "Since the ﬁrst version of this paper, several experiments have been updated.")。
- 速度とメモリの測定は1つの課題だけで行い、結果はハードウェアと実装に大きく依存すると強調している [arxiv-2011.04006#c7](https://arxiv.org/pdf/2011.04006v1#page=7 "We emphasize that this is again largely conditioned on hardware and implementation details (more details can be found in the appendix).")。
- 効率的な Transformer のサーベイは、LRA はエンコーダ専用で、自己回帰の課題を含まないと注意している [arxiv-2009.06732#c6](https://arxiv.org/pdf/2009.06732v3#page=26 "It is good to note that LRA was designed for evalu-ating Transformers in encoder-only mode and do not consider generative (or autoregressive tasks) that require causal masking.")。

### 測り方の注意

- The Efficiency Misnomer は、パラメータ数、FLOPs、スループットといった費用の指標が互いに矛盾しうるので、すべてを報告すべきだと述べている [arxiv-2110.12894#c1](https://arxiv.org/pdf/2110.12894v2#page=1 "We demonstrate how incomplete reporting of cost indicators can lead to partial conclusions and a blurred or incomplete picture of the practical considerations of different models.") [arxiv-2110.12894#c7](https://arxiv.org/pdf/2110.12894v2#page=9 "Since each indicator stands for something different and comes with its own pros and cons, we suggest always reporting and plotting curves using all available cost indicators, and refraining from highlighting results using just a single one.")。FLOPs は多くの場合理論値で、並列化できるかどうかなどを無視している [arxiv-2110.12894#c2](https://arxiv.org/pdf/2110.12894v2#page=3 "Note that theoretical FLOPs ignores practical factors, like which parts of the model can be parallelized.")。
- 効率的な Transformer のサーベイの改訂版は、効率的な注意が必ずしも Transformer を速くするわけではなく、多くはかえって遅くなると振り返っている [arxiv-2009.06732#c7](https://arxiv.org/pdf/2009.06732v3#page=30 "Moreover, many linear attention models do not observe any speed or memory gain at all if the sequence length is short.")。
- 速度の数値が何を測ったものかを確認する。Mamba のスキャンの比較は、畳み込みの核や射影の計算を含まない [arxiv-2312.00752#c6](https://arxiv.org/pdf/2312.00752v2#page=35 "Note that these do not include the cost of other operations outside of this core operation, such as computing the convolutional kernel in global-convolution models, or computing the QKV projections in attention.")。Waleffe らの推論の速さは測定ではなく予測である [arxiv-2406.07887#c8](https://arxiv.org/pdf/2406.07887v1#page=11 "In Figure 5, we plot the predicted time to generate one token for the 8B Transformer model over the time for the 8B Mamba-2-Hybrid model using a batch size of 32.")。Performer の速度は逆伝播で測っている [arxiv-2009.14794#c7](https://arxiv.org/pdf/2009.14794v4#page=7 "We observed (Fig. 3) that in terms of L, the Performer reaches nearly linear time and sub-quadratic memory consumption")。

### 利益相反

HiPPO、S4、H3、Mamba、Mamba-2 は重なる著者による一連の研究で、後の論文が前の論文の手法を比較相手や土台にしている。MoE の GShard、Switch、GLaM、ST-MoE、Expert Choice も、Google の重なる著者による。Mixtral は Mistral AI が自社のモデルを評価している(各カードの notes 参照)。

## 設計への示唆(本記事の整理)

- **MoE は「活性パラメータ」と「総パラメータ」の両方で費用を見る。** 計算は活性パラメータで決まるが、メモリと提供コストは総パラメータで決まる [arxiv-2401.04088#c6](https://arxiv.org/pdf/2401.04088v1#page=4 "Note that this analysis focuses on the active parameter count (see Section 2.1), which is directly proportional to the inference compute cost, but does not consider the memory costs and hardware utilization.") [arxiv-2112.06905#c9](https://arxiv.org/pdf/2112.06905v2#page=9 "This limits the resource accessibility and increases the serving cost especially when the serving trafﬁc is low.")。
- **MoE は負荷の偏りと学習の不安定さへの対策を前提にする。** 補助損失や router z-loss を使う [arxiv-1701.06538#c6](https://arxiv.org/pdf/1701.06538v1#page=14 "All the combinations containing at least one the two losses led to very similar model quality, where having no loss was much worse.") [arxiv-2202.08906#c2](https://arxiv.org/pdf/2202.08906v2#page=8 "Table 4 shows that both update clipping and the router z-loss stabilize the model in all 3 runs, but the update clipping signiﬁcantly hurts the model quality.")。微調整の設定は密なモデルから使い回さない [arxiv-2202.08906#c5](https://arxiv.org/pdf/2202.08906v2#page=11 "Sparse models beneﬁt from smaller batch sizes and a higher learning rate.")。
- **状態空間モデルや線形注意は、コピーや検索が必要な課題で確かめる** [arxiv-2402.01032#c6](https://arxiv.org/pdf/2402.01032v2#page=5 "We observe that the transformers need 100x less samples than the best GSSMs to learn the copy task.") [arxiv-2406.07887#c5](https://arxiv.org/pdf/2406.07887v1#page=8 "In contrast, both Mamba and Mamba-2 models begin to respond incorrectly for input sequence lengths beyond approximately 500 tokens.")。必要なら少数の注意層を混ぜる [arxiv-2405.21060#c8](https://arxiv.org/pdf/2405.21060v1#page=30 "We hypothesize that the SSM layers function well as a general sequence-to-sequence mapping, and attention layers act as a retrieval mechanism to quickly refer to previous tokens in the sequence instead of forcing the model to compress all the context to its memory (SSM states).")。
- **速さの主張は、何を・どのハードウェアで・どこまで含めて測ったかを確認する** [arxiv-2011.04006#c7](https://arxiv.org/pdf/2011.04006v1#page=7 "We emphasize that this is again largely conditioned on hardware and implementation details (more details can be found in the appendix).") [arxiv-2110.12894#c7](https://arxiv.org/pdf/2110.12894v2#page=9 "Since each indicator stands for something different and comes with its own pros and cons, we suggest always reporting and plotting curves using all available cost indicators, and refraining from highlighting results using just a single one.")。

## わかっていないこと

- Mamba などの状態空間モデルが、大規模になっても Transformer と比べて有利かは、元の論文では確かめられていなかった [arxiv-2312.00752#c7](https://arxiv.org/pdf/2312.00752v2#page=17 "It remains to assess whether Mamba still compares favorably at these larger sizes.")。
- 状態空間モデルの理論的な弱点(コピー)は表現力についてのもので、学習で実際にどこまで克服できるかは別の問題として残る [arxiv-2402.01032#c4](https://arxiv.org/pdf/2402.01032v2#page=1 "Our theory studies representation expressivity, but not whether these representations will be learned.")。
- 疎なモデルの微調整がなぜ難しいのか、事前学習の品質と下流の性能の関係はよくわかっていない [arxiv-2101.03961#c7](https://arxiv.org/pdf/2101.03961v3#page=26 "This suggests a poorly understood dependence between ﬁne-tuning quality, FLOPS per token and number of parameters.") [arxiv-2202.09368#c5](https://arxiv.org/pdf/2202.09368v2#page=7 "This result indicates that a good training perplexity does not always translate to better performance of downstream tasks.")。

## 参照カード

- [arxiv-1701.06538](../../papers/arxiv-1701.06538.yaml) Shazeer et al., "Outrageously Large Neural Networks: The Sparsely-Gated Mixture-of-Experts Layer"
- [arxiv-2006.16668](../../papers/arxiv-2006.16668.yaml) Lepikhin et al., "GShard"
- [arxiv-2101.03961](../../papers/arxiv-2101.03961.yaml) Fedus, Zoph & Shazeer, "Switch Transformers"
- [arxiv-2202.08906](../../papers/arxiv-2202.08906.yaml) Zoph et al., "ST-MoE: Designing Stable and Transferable Sparse Expert Models"
- [arxiv-2202.09368](../../papers/arxiv-2202.09368.yaml) Zhou et al., "Mixture-of-Experts with Expert Choice Routing"
- [arxiv-2112.06905](../../papers/arxiv-2112.06905.yaml) Du et al., "GLaM: Efficient Scaling of Language Models with Mixture-of-Experts"
- [arxiv-2401.04088](../../papers/arxiv-2401.04088.yaml) Jiang et al., "Mixtral of Experts"
- [arxiv-2008.07669](../../papers/arxiv-2008.07669.yaml) Gu et al., "HiPPO: Recurrent Memory with Optimal Polynomial Projections"
- [arxiv-2111.00396](../../papers/arxiv-2111.00396.yaml) Gu, Goel & Ré, "Efficiently Modeling Long Sequences with Structured State Spaces"
- [arxiv-2212.14052](../../papers/arxiv-2212.14052.yaml) Fu et al., "Hungry Hungry Hippos: Towards Language Modeling with State Space Models"
- [arxiv-2312.00752](../../papers/arxiv-2312.00752.yaml) Gu & Dao, "Mamba: Linear-Time Sequence Modeling with Selective State Spaces"
- [arxiv-2405.21060](../../papers/arxiv-2405.21060.yaml) Dao & Gu, "Transformers are SSMs"
- [arxiv-2006.16236](../../papers/arxiv-2006.16236.yaml) Katharopoulos et al., "Transformers are RNNs"
- [arxiv-2009.14794](../../papers/arxiv-2009.14794.yaml) Choromanski et al., "Rethinking Attention with Performers"
- [arxiv-2305.13048](../../papers/arxiv-2305.13048.yaml) Peng et al., "RWKV: Reinventing RNNs for the Transformer Era"
- [arxiv-2205.14135](../../papers/arxiv-2205.14135.yaml) Dao et al., "FlashAttention"
- [arxiv-2402.01032](../../papers/arxiv-2402.01032.yaml) Jelassi et al., "Repeat After Me: Transformers are Better than State Space Models at Copying"
- [arxiv-2406.07887](../../papers/arxiv-2406.07887.yaml) Waleffe et al., "An Empirical Study of Mamba-based Language Models"
- [arxiv-2011.04006](../../papers/arxiv-2011.04006.yaml) Tay et al., "Long Range Arena: A Benchmark for Efficient Transformers"
- [arxiv-2009.06732](../../papers/arxiv-2009.06732.yaml) Tay et al., "Efficient Transformers: A Survey"
- [arxiv-2110.12894](../../papers/arxiv-2110.12894.yaml) Dehghani et al., "The Efficiency Misnomer"
