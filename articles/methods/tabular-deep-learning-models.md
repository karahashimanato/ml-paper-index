---
title: 表データの深層学習モデル — 木をまねる、特徴をトークンにする、数値を埋め込む、MLP を鍛える、近傍を引く
kind: method
tags: [tabular-mlp, tabular-attention, differentiable-trees]
depends_on: [arxiv-1908.07442, arxiv-1909.06312, arxiv-2309.17130, arxiv-2012.06678, arxiv-2106.01342, arxiv-2203.05556, arxiv-2307.14338, arxiv-2106.11189, arxiv-1810.11921, arxiv-2008.13535, arxiv-2305.18446, arxiv-2301.02819, arxiv-2106.15147, arxiv-2110.01889, arxiv-2407.00956, arxiv-2106.11959, arxiv-2207.08815, arxiv-2305.02997, arxiv-2407.04491, arxiv-2410.24210, arxiv-2106.03253]
written_at: 2026-10-10
written_by: claude-opus-5-5 via Claude Code
---

# 表データの深層学習モデル — 木をまねる、特徴をトークンにする、数値を埋め込む、MLP を鍛える、近傍を引く

<!-- generated:stale -->
> ⚠ この記事の執筆後(2026-10-10)に、関連カードが 40 件追加されています(未反映): `arxiv-2308.13068`, `arxiv-2506.16791`, `arxiv-2608.04348`, `arxiv-2608.09162`, `arxiv-2608.10522`, `arxiv-2608.17856`, `arxiv-2608.18026`, `arxiv-2608.18849`, `arxiv-2608.18919`, `arxiv-2608.23893`, `arxiv-2608.25774`, `arxiv-2608.27076`, `arxiv-2608.27489`, `arxiv-2608.28209`, `arxiv-2609.01262`, `arxiv-2609.03880`, `arxiv-2609.04540`, `arxiv-2609.06080`, `arxiv-2609.07441`, `arxiv-2609.12712`, `arxiv-2609.16091`, `arxiv-2609.16309`, `arxiv-2609.17488`, `arxiv-2609.22866`, `arxiv-2609.27679`, `arxiv-2609.31306`, `arxiv-2609.36039`, `arxiv-2609.36108`, `arxiv-2609.36337`, `arxiv-2609.37959`, `arxiv-2609.39124`, `arxiv-2610.00649`, `arxiv-2610.00806`, `doi-10.1007_s40123-026-01482-2`, `doi-10.1038_s41467-026-76154-7`, `doi-10.3389_fcvm.2026.1909097`, `doi-10.36079_lamintang.ijortas-0802.1081`, `doi-10.57185_yrw05r30`, `doi-10.65542_djei.v2i3.83`, `doi-10.70393_6a6374616d.343334`
<!-- /generated:stale -->

## この記事の読み方

表データ(行がサンプル、列が特徴量の表)のための深層学習モデルは、勾配ブースティング木(GBDT)に追いつくことを目標に、さまざまな設計が提案されてきた。
この記事は15本の新しいカードと既存の6本のカードから、設計の考え方を次の系統に分けて整理する。

1. なぜ表データは深層学習にとって難しいのか
2. 木をまねる(TabNet、NODE、GRANDE)
3. 特徴をトークンにして注意をかける(AutoInt、TabTransformer、FT-Transformer、SAINT、Trompt、ExcelFormer)
4. 数値の特徴を埋め込む
5. 特徴の交差を明示的に作る(DCN V2)
6. MLP を鍛える(正則化、既定値の工夫、暗黙のアンサンブル)
7. 近傍を引く(TabR)
8. 自己教師ありの事前学習(SCARF ほか)
9. 比較を読むときの注意

性能の数値は書かない。各論文のページの結果表を参照のこと(カードは結果表を記録せず、主張だけを記録している)。
GBDT と深層学習のどちらがよいかという比較そのものは [表データでの勾配ブースティング木と深層学習の比較](../tasks/tabular-gbdt-vs-deep-learning.md)、事前学習済みの基盤モデル(TabPFN など)は [表データ基盤モデル(TabPFN 系)](tabular-foundation-models.md) の記事で扱った。

## 1. なぜ表データは難しいのか

Borisov らのサーベイは、深層学習が表データで振るわない理由として、データの質の低さ(欠損、外れ値、小ささ、クラスの偏り)、特徴の間に画像や文章のような規則的な空間的依存がないこと、前処理への依存などを挙げている [arxiv-2110.01889#c1](https://arxiv.org/pdf/2110.01889v3#page=4 "In the following, we identify and discuss four possible reasons:")。

Grinsztajn らは、木のモデルとの差を調べる実験から、ニューラルネットワークに必要な3つの性質を導いた [arxiv-2207.08815#c2](https://arxiv.org/pdf/2207.08815v1#page=1 "be robust to uninformative features, 2. preserve the orientation of the data, and 3. be able to easily learn irregular functions.")。

- **意味のない特徴に強いこと**:MLP 系のモデルは意味のない特徴に弱く、それを除くと木との差が縮んだ [arxiv-2207.08815#c5](https://arxiv.org/pdf/2207.08815v1#page=7 "This shows that MLPs are less robust to uninformative features")。
- **データの向きを保つこと**:特徴をランダムに回転させても性能が変わらない(回転不変な)のは ResNet だけで、他のモデルは変わった。表データでは個々の列に意味があるので、回転不変であることは不利になりうる [arxiv-2207.08815#c6](https://arxiv.org/pdf/2207.08815v1#page=7 "only Resnets are rotationally invariant")。
- **不規則な関数を学べること**:目標をなめらかにすると木のモデルは大きく悪化したが、ニューラルネットワークはほとんど影響を受けなかった。著者らは、ニューラルネットワークがなめらかな解に偏っていることを示唆すると読んでいる [arxiv-2207.08815#c4](https://arxiv.org/pdf/2207.08815v1#page=6 "For small lengthscales, smoothing the target function on the train set decreases markedly the accuracy of tree-based models, but barely impacts that of NNs.")。

以下の設計の多くは、これらのどれかに対処しようとしている。たとえば ExcelFormer は、この3つの弱点に対応する部品をそれぞれ用意したと述べている [arxiv-2301.02819#c1](https://arxiv.org/pdf/2301.02819v8#page=1 "We delve into three key drawbacks of deep tabular models, encompassing: (P1) lack of rotational variance property, (P2) large data demand, and (P3) over-smooth solution.")。

## 2. 木をまねる

### TabNet:逐次的な注意で特徴を選ぶ

TabNet は、決定の各段階で、どの特徴を使うかを**注意**で選ぶ [arxiv-1908.07442#c1](https://arxiv.org/pdf/1908.07442v5#page=1 "TabNet uses sequential attention to choose which features to reason from at each decision step, enabling interpretability and more efﬁcient learning as the learning capacity is used for the most salient features.")。選択は、前の段階の結果から計算した乗算のマスクで、sparsemax で正規化するので多くの成分が0になる [arxiv-1908.07442#c2](https://arxiv.org/pdf/1908.07442v5#page=3 "Sparsemax normalization (Martins and Astudillo 2016) encourages sparsity by mapping the Euclidean projection onto the probabilistic simplex, which is observed to be superior in performance and aligned with the goal of sparse feature selection for explainability.")。
著者らは、マスクが特徴の重要度として解釈できると主張するが、それは各段階の関数が線形なら成り立つ近似的な意味でだ、と自ら述べている [arxiv-1908.07442#c4](https://arxiv.org/pdf/1908.07442v5#page=5 "Although each decision step employs non-linear processing, their outputs are combined later in a linear way.")。

### NODE:微分可能な決定木

NODE は、深さごとに同じ特徴と閾値で分岐する**対称な決定木**(oblivious tree)を、微分可能にした。どの特徴で分岐するかの選択と閾値との比較を、entmax という疎な関数で緩めている [arxiv-1909.06312#c1](https://arxiv.org/pdf/1909.06312v2#page=4 "Instead, we propose to use the α-entmax transformation (Peters et al., 2019) as it is able to learn sparse choices, depending only on a few features, via standard gradient descent.")。
この木の層を DenseNet のように積み重ね、すべての木の出力を平均する [arxiv-1909.06312#c2](https://arxiv.org/pdf/1909.06312v2#page=5 "Similar to DenseNet, our architecture is a sequence of k NODE layers (see Section 3.1), where each layer uses a concatenation of all previous layers as its input.")。学習では、各特徴を正規分布に変換する前処理が、安定した学習に重要だったと述べている [arxiv-1909.06312#c3](https://arxiv.org/pdf/1909.06312v2#page=5 "In experiments, we observed that this step was important for stable training and faster convergence.")。

### GRANDE:硬い分岐の木を勾配で学習する

GRANDE は、著者らの先行研究の GradTree を、重み付きの木のアンサンブルに広げた。NODE の柔らかい斜めの分岐に対し、硬い軸に沿った分岐を、ストレートスルー推定で勾配学習する [arxiv-2309.17130#c1](https://arxiv.org/pdf/2309.17130v3#page=2 "We extend GradTree (Marton et al., 2023) from individual trees to an end-to-end gradient-based tree ensemble, maintaining efficient computation (Section 3.1).")。
動機として、深層学習はなめらかな解に偏るが、表データの目標関数はなめらかでないことが多い、という先行研究の指摘を挙げている [arxiv-2309.17130#c2](https://arxiv.org/pdf/2309.17130v3#page=2 "As the target function in tabular datasets is usually not smooth, DL methods struggle to find these irregular functions.")。各葉に重みを持たせ、サンプルごとに木の重みを変える工夫も加えた [arxiv-2309.17130#c4](https://arxiv.org/pdf/2309.17130v3#page=4 "To address this, we propose an advanced weighting scheme that allows calculating instance-wise weights that can be learned within the gradient-based optimization.")。

### 木をまねるモデルの評価

- Ye らの大規模な比較では、木をまねるネットワーク(NODE、TabNet)は、木のアンサンブルより一般に劣っていた [arxiv-2407.00956#c7](https://arxiv.org/pdf/2407.00956v4#page=19 "Tree-mimic networks such as NODE and TabNet generally underperform relative to ensembles.")。
- Gorishniy らの比較でも、NODE は、より複雑なのに、より単純な ResNet に多くのデータセットで劣った [arxiv-2106.11959#c10](https://arxiv.org/pdf/2106.11959v5#page=7 "However, it is still inferior to ResNet on six datasets (Helena, Jannis, Higgs, ALOI, Epsilon, Covertype), while being a more complex solution.")。
- Shwartz-Ziv と Armon は、TabNet や NODE がそれぞれ自分の論文のデータセットでしかよくなかったと報告している [arxiv-2106.03253#c4](https://arxiv.org/pdf/2106.03253v2#page=6 "Each deep model was better only on the datasets that appeared in its own paper.")。

## 3. 特徴をトークンにして注意をかける

自然言語処理の Transformer のように、**各特徴を1つのトークン**(ベクトル)にして、特徴どうしに注意をかける系統である。

- **AutoInt**:クリック率の予測のために、カテゴリと数値の特徴を同じ空間に埋め込む(数値の特徴 $x_m$ は学習するベクトル $v_m$ を掛けて $v_m x_m$ にする)[arxiv-1810.11921#c3](https://arxiv.org/pdf/1810.11921v2#page=4 "To allow the interaction between categorical and numerical features, we also represent the numerical features in the same low-dimensional feature space.")。特徴の間に多頭注意をかけて、特徴の組合せ(交互作用)を学ぶ [arxiv-1810.11921#c4](https://arxiv.org/pdf/1810.11921v2#page=5 "Therefore a few interacting layers will suffice to model high-order feature interactions.")。
- **TabTransformer**:カテゴリの特徴だけを Transformer に通し、数値の特徴はそのまま後段の MLP に渡す [arxiv-2012.06678#c1](https://arxiv.org/pdf/2012.06678v1#page=3 "The contextual embeddings {h1, · · · , hm} are concatenated along with the continuous features xcont to form a vector of dimension (d × m + c).")。表の列には順序がないので、位置の符号化は使わない [arxiv-2012.06678#c2](https://arxiv.org/pdf/2012.06678v1#page=3 "Since, in tabular data, there is no ordering of the features, we do not use positional encodings.")。
- **FT-Transformer**:Gorishniy らの研究で提案されたモデルで、論文の比較の範囲では深層学習のモデルの中で多くのタスクで最もよかった [arxiv-2106.11959#c2](https://arxiv.org/pdf/2106.11959v5#page=2 "Second, FT-Transformer demonstrates the best performance on most tasks and becomes a new powerful solution for the field.")。ただし、ResNet より多くの計算資源が必要で、注意の計算量が特徴の数の2乗なので、特徴が非常に多いと使いにくい [arxiv-2106.11959#c9](https://arxiv.org/pdf/2106.11959v5#page=5 "FT-Transformer requires more resources (both hardware and time) for training than simple models such as ResNet")。
- **SAINT**:数値の特徴もそれぞれ全結合層で埋め込む(TabTransformer が数値をトークンにしないことで、カテゴリと数値の相関の情報を失うと指摘している)[arxiv-2106.01342#c2](https://arxiv.org/pdf/2106.01342v1#page=4 "we use a separate single fully-connected layer with a ReLU nonlinearity for each continuous feature")。特徴の間の注意に加えて、**行(サンプル)の間**の注意も使う [arxiv-2106.01342#c1](https://arxiv.org/pdf/2106.01342v1#page=2 "Intersample attention is akin to a nearest-neighbor classiﬁcation, where the distance metric is learned end-to-end rather than ﬁxed.")。
- **Trompt**:特徴の重要度はサンプルごとに違い、いくつかのパターンに分かれる、という仮説に基づく [arxiv-2305.18446#c2](https://arxiv.org/pdf/2305.18446v2#page=3 "We argue that the column importances of tabular data are not invariant for all samples and can be grouped into multiple modalities.")。入力によらない列の埋め込みとプロンプトの埋め込みから、サンプルごとの特徴の重要度を作る [arxiv-2305.18446#c3](https://arxiv.org/pdf/2305.18446v2#page=4 "Notice that the column embeddings are not connected to the input and the prompt embeddings are fused with the previous cell’s output.")。
- **ExcelFormer**:特徴量の情報量(相互情報量)に基づくマスクで、情報量の少ない特徴から多い特徴への注意を遮る [arxiv-2301.02819#c2](https://arxiv.org/pdf/2301.02819v8#page=4 "In this way, only more informative features are permitted to propagate information to the less informative ones, and the reverse is not allowed.")。

## 4. 数値の特徴を埋め込む

Gorishniy らは、数値の特徴をそのまま入力するのではなく、各特徴の値をベクトルに変換する**埋め込み**が重要だと示した。各特徴は独立に、同じ形の関数で、パラメータを共有せずに埋め込む [arxiv-2203.05556#c1](https://arxiv.org/pdf/2203.05556v4#page=3 "We never share parameters of embedding functions of different features.")。

- **区分線形の符号化**:値の範囲をいくつかの区間(ビン)に分け、どの区間に入るかとその中での位置で表す。区間は学習データの分位点か、決定木の分割から決める [arxiv-2203.05556#c2](https://arxiv.org/pdf/2203.05556v4#page=4 "PLE produces alternative initial representations for the numerical features and can be viewed as a preprocessing strategy.")。
- **周期的な埋め込み**:$\sin$ と $\cos$ を使い、周波数を学習する。周波数の初期値のばらつきが重要なハイパーパラメータだった [arxiv-2203.05556#c3](https://arxiv.org/pdf/2203.05556v4#page=5 "We observe that σ is an important hyperparameter.")。

論文は、適切な埋め込みを付けることが、ほとんどの場合で GBDT との差を埋めるのに必要なすべてだったと報告している [arxiv-2203.05556#c6](https://arxiv.org/pdf/2203.05556v4#page=8 "However, for the vast majority of the “backbone & dataset” pairs, proper embeddings are the only thing needed to close the gap with GBDT.")。また、埋め込みを付けた MLP は、Transformer 系のモデルと同程度になった [arxiv-2203.05556#c7](https://arxiv.org/pdf/2203.05556v4#page=8 "Importantly, after the MLP-like architectures are coupled with embeddings for numerical features, they perform on par with the Transformer-based models.")。
Grinsztajn らは、埋め込みが回転不変性を壊すことが、その効果の鍵かもしれないと示唆している [arxiv-2207.08815#c16](https://arxiv.org/pdf/2207.08815v1#page=8 "The fact that very different types of embeddings seem to improve performance suggests that the sheer presence of an embedding which breaks the invariance is a key part of these improvements.")。

## 5. 特徴の交差を明示的に作る:DCN V2

DCN V2 は、ウェブ規模のランキングのために設計された。**交差層**で特徴の掛け算(交差)を明示的に作り、通常の深いネットワークと組み合わせる [arxiv-2008.13535#c2](https://arxiv.org/pdf/2008.13535v2#page=2 "The function class modeled by DCN-V2 is a strict superset of that modeled by DCN.")。
実運用のモデルで学習した交差層の行列が低ランクに近いことを観察し、低ランクの分解と、その混合を導入した [arxiv-2008.13535#c3](https://arxiv.org/pdf/2008.13535v2#page=4 "In many settings, we indeed observe that the learned matrix is numerically low-rank in practice.")。

論文には示唆的な観察がある。よく調整した通常の ReLU のネットワークは、交互作用を学ぶ多くの専用モデルと互角だった [arxiv-2008.13535#c6](https://arxiv.org/pdf/2008.13535v2#page=8 "To our surprise, DNN performed neck to neck with most baselines and even outperformed certain models.")。著者らは、特定の用途では交差層が ReLU 層を置き換えうるかもしれないと述べつつ、検証にはずっと多くの分析が必要だとしている [arxiv-2008.13535#c7](https://arxiv.org/pdf/2008.13535v2#page=9 "Obviously we need significant more analysis and experiments to verify the hypothesis.")。
評価の一部は Google 社内のデータで行われている [arxiv-2008.13535#c8](https://arxiv.org/pdf/2008.13535v2#page=11 "When compared with production model, DCN-V2 yielded 0.6% AUCLoss (1 - AUC) improvement.")。

## 6. MLP を鍛える

構造を複雑にするのではなく、単純な MLP をよく学習させる系統である。

- **正則化の組合せ**:Kadra らは、13種類の正則化を使うかどうかと、その強さを、データセットごとにベイズ最適化で選んだ(正則化のカクテル)[arxiv-2106.11189#c1](https://arxiv.org/pdf/2106.11189v2#page=4 "In total, the optimal cocktail is searched in a space of 19 hyperparameters.")。論文は、こうして正則化した MLP が GBDT を統計的に有意に上回ったと報告している [arxiv-2106.11189#c7](https://arxiv.org/pdf/2106.11189v2#page=8 "The results show that our MLPs outperform all three GBDT variants (XGBoost, auto-sklearn, and CatBoost) with a statistically signiﬁcant margin.")。ただし、固定した構造と学習率は、評価に使う同じ40個のデータセットで、正則化なしのネットワークのために調整したものである [arxiv-2106.11189#c2](https://arxiv.org/pdf/2106.11189v2#page=6 "These ﬁxed hyperparameter values, as speciﬁed in Table 4 of Appendix B.1, have been tuned for maximizing the performance of an unregularized neural network on our dataset collection (see Table 9 in Appendix D).")。
- **既定値と前処理の工夫**:RealMLP は、特徴ごとの学習可能なスケーリング層などの構造の工夫に加え、外れ値に強いスケーリングなどの前処理を使う [arxiv-2407.04491#c22](https://arxiv.org/pdf/2407.04491v3#page=5 "To encourage (soft) feature selection, we introduce a scaling layer before the first linear layer") [arxiv-2407.04491#c18](https://arxiv.org/pdf/2407.04491v3#page=10 "our numerical preprocessing is easy to adopt and often beneficial for other NNs as well")。著者らは、構造以外の要素(学習、前処理、既定値)が構造と同じくらい重要だと述べている [arxiv-2407.04491#c24](https://arxiv.org/pdf/2407.04491v3#page=10 "our architectural improvements alone are beneficial when applied to MLP-D directly, although non-architectural aspects are at least as important.")。
- **暗黙のアンサンブル**:TabM は、重みを共有した多数の MLP を同時に学習する。個々の予測は弱いが、まとめると強い [arxiv-2410.24210#c3](https://arxiv.org/pdf/2410.24210v3#page=1 "We observe that the multiple predictions of TabM are weak individually, but powerful collectively.")。同時に学習することと重みの共有が、性能の2つの鍵だと分析している [arxiv-2410.24210#c11](https://arxiv.org/pdf/2410.24210v3#page=2 "the two key reasons for TabM's high performance are the collective training of the underlying implicit MLPs and the weight sharing.")。

Gorishniy らも、調整すれば MLP や ResNet のような単純なモデルが競争力を持つと述べ、ベースラインを調整することを勧めている [arxiv-2106.11959#c8](https://arxiv.org/pdf/2106.11959v5#page=7 "Tuning makes simple models such as MLP and ResNet competitive, so we recommend tuning baselines when possible.")。

## 7. 近傍を引く:TabR

TabR は、予測したいサンプルに似た学習サンプルを検索し、その特徴とラベルを使って予測を補う。本質的にはフィードフォワードのネットワークの途中に、k 近傍法に似た部品を入れたものである [arxiv-2307.14338#c1](https://arxiv.org/pdf/2307.14338v2#page=1 "In this work, we present TabR – essentially, a feed-forward network with a custom k-Nearest-Neighbors-like component in the middle.")。
著者らは、それまでの検索を使う表データのモデル(SAINT など)は、よく調整した MLP に対してせいぜい小さな利点しかなく、複雑で計算も重いと指摘している [arxiv-2307.14338#c2](https://arxiv.org/pdf/2307.14338v2#page=2 "While multiple retrieval-augmented models for tabular data problems exist, in our experiments, we show that they provide if only minor benefits over the properly tuned multilayer perceptron (MLP; the simplest parametric model), while being significantly more complex and costly.")。単純な自己注意の検索では MLP と同程度で、クエリを使わず L2 距離で似たものを探す変更が転機だったという [arxiv-2307.14338#c3](https://arxiv.org/pdf/2307.14338v2#page=5 "Crucially, in subsection A.3, we show that removing any of the three ingredients (context labels, key-only representation, L2 distance) results in a performance drop back to the level of MLP.")。
Ye らの比較でも、近傍に基づくモデル(ModernNCA)は CatBoost や LightGBM と統計的に同程度のことが多かった [arxiv-2407.00956#c7](https://arxiv.org/pdf/2407.00956v4#page=19 "Tree-mimic networks such as NODE and TabNet generally underperform relative to ensembles.")。
限界として、検索の部品は非常に大きなデータでは計算が重くなりうる [arxiv-2307.14338#c9](https://arxiv.org/pdf/2307.14338v2#page=18 "Lastly, while TabR is significantly more efficient than prior retrieval-based tabular DL models, the retrieval module R still causes overhead compared to purely parametric models, so TabR may not scale to truly large datasets as-is.")。

## 8. 自己教師ありの事前学習

ラベルのないデータで事前学習する試みも多い。

- **SCARF**:各サンプルの特徴の一部を、その特徴の周辺分布からランダムに取った値で置き換えて「別の見え方」を作り、対照学習で事前学習する [arxiv-2106.15147#c1](https://arxiv.org/pdf/2106.15147v2#page=4 "We sample some fraction of the features uniformly at random and replace each of those features by a random draw from that feature’s empirical marginal distribution,")。同じ置き換えを使う VIME とは、ノイズ除去ではなく対照学習の損失を使う点などが違う [arxiv-2106.15147#c2](https://arxiv.org/pdf/2106.15147v2#page=3 "The key differences with our work is that we pre-train using a contrastive loss, which we show to be more effective than the denoising auto-encoder loss that partly constitutes VIME.")。
- **TabNet、TabTransformer、SAINT**も、マスクした特徴の予測や対照学習による事前学習を提案している [arxiv-1908.07442#c8](https://arxiv.org/pdf/1908.07442v5#page=7 "Table 7 shows that unsupervised pre-training signiﬁcantly improves performance on the supervised classiﬁcation task, especially in the regime where the unlabeled dataset is much larger than the labeled dataset.") [arxiv-2012.06678#c3](https://arxiv.org/pdf/2012.06678v1#page=3 "We explore two different types of pre-training procedures, the masked language modeling (MLM) (Devlin et al. 2019) and the replaced token detection (RTD) (Clark et al. 2020).") [arxiv-2106.01342#c3](https://arxiv.org/pdf/2106.01342v1#page=3 "In this paper, to the best of our knowledge, we are the ﬁrst to adopt contrastive learning for tabular data.")。

共通する報告は、**事前学習の効果は、ラベルの少ない設定で主に現れる**ということである。TabTransformer と SAINT は、すべてのデータにラベルがあるときは事前学習の効果がほとんどなかったと述べている [arxiv-2012.06678#c4](https://arxiv.org/pdf/2012.06678v1#page=4 "We do not ﬁnd much beneﬁt in using it when the entire data is labeled.") [arxiv-2106.01342#c7](https://arxiv.org/pdf/2106.01342v1#page=8 "Interestingly, we note that when all the training data samples are labeled, pre-training does not contribute appreciably, hence the results with and without pre-training are fairly close.")。TabNet も、ラベルなしのデータがラベル付きよりずっと多いときに特に効いたと報告している [arxiv-1908.07442#c8](https://arxiv.org/pdf/1908.07442v5#page=7 "Table 7 shows that unsupervised pre-training signiﬁcantly improves performance on the supervised classiﬁcation task, especially in the regime where the unlabeled dataset is much larger than the labeled dataset.")。

## 9. 比較を読むときの注意

### 調整の予算がそろっているか

多くの論文で、提案手法と比較相手の調整の条件が違う。

- NODE:比較相手は TPE で50回調整し、NODE は小さなグリッドで調整した [arxiv-1909.06312#c5](https://arxiv.org/pdf/1909.06312v2#page=11 "For each method, we perform 50 steps of Tree-structured Parzen Estimator (TPE) optimization algorithm.")。著者ら自身は、先行研究が GBDT を適切に調整していないと批判している [arxiv-1909.06312#c8](https://arxiv.org/pdf/1909.06312v2#page=3 "The recent preprint (Ke et al., 2018) reports the marginal improvement over GBDT with default parameters, but in our experiments, the baseline performance is much higher.")。
- GRANDE:調整したハイパーパラメータの数が、GRANDE は XGBoost や CatBoost より多いことを著者が認めている [arxiv-2309.17130#c7](https://arxiv.org/pdf/2309.17130v3#page=22 "In contrast, for XGBoost and CatBoost we only optimized 4 and 3 hyperparameters, respectively.")。
- Trompt:比較相手の結果はベンチマークから流用し、Trompt の探索結果は他のモデルの探索の長さに合わせて水増しした [arxiv-2305.18446#c4](https://arxiv.org/pdf/2305.18446v2#page=13 "Due to limited computing resources, we have chosen a small search space (Table 30) consisting of 40 parameter combinations.") [arxiv-2305.18446#c5](https://arxiv.org/pdf/2305.18446v2#page=13 "To avoid unfairly truncating random search results of other models, and compromising the low search iterations of Trompt, we duplicated the grid search results of Trompt to exceed the lowest search iteration count among the models provided by Grinsztajn45.")。一部のデータセットでは Trompt を調整せず、比較相手の数値を元論文から取っている [arxiv-2305.18446#c9](https://arxiv.org/pdf/2305.18446v2#page=35 "It’s important to note that due to limited computing resources, Trompt did not undergo hyperparameter search.")。
- TabR:既定の設定は、評価に使うデータセットを含む調整結果の平均から作られ、著者は「100% 公平ではない」と認めている [arxiv-2307.14338#c8](https://arxiv.org/pdf/2307.14338v2#page=22 "Formally, this is not 100% fair to evaluate the obtained default TabR-S on the datasets which contributed to this default hyperparameters as in Table 4.")。
- SAINT:比較相手の結果は、可能な場合は元論文から引用している [arxiv-2106.01342#c5](https://arxiv.org/pdf/2106.01342v1#page=7 "Baseline results are quoted from original papers when possible (denoted with *) and reproduced otherwise.")。
- Shwartz-Ziv と Armon は、提案論文の結果の一因として、モデルがうまく働くデータセットを選んだこと(選択の偏り)と、ハイパーパラメータの調整がそろっていないことを挙げている [arxiv-2106.03253#c5](https://arxiv.org/pdf/2106.03253v2#page=6 "The first possibility is selection bias.") [arxiv-2106.03253#c6](https://arxiv.org/pdf/2106.03253v2#page=6 "The second possibility is differences in the optimization of hyperparameters.")。

### ベンチマークの偏り

- Gorishniy らは、自分たちのベンチマークで深層学習が多く勝ったのは、深層学習に有利な問題に少し偏っているためだと述べている [arxiv-2106.11959#c5](https://arxiv.org/pdf/2106.11959v5#page=8 "it only means that the constructed benchmark is slightly biased towards 'DL-friendly' problems.")。逆に、数値の埋め込みの論文では、ベンチマークが GBDT に有利な問題に偏っていると述べている [arxiv-2203.05556#c4](https://arxiv.org/pdf/2203.05556v4#page=5 "Importantly, we focus on the middle and large scale tasks, and our benchmark is biased towards GBDT-friendly problems, since, as of now, closing the gap with GBDT models on such tasks is one of the main challenges for tabular DL.")。
- Ye らの300個のデータセットでの比較では、木のアンサンブルは依然として強く信頼できるベースラインで [arxiv-2407.00956#c5](https://arxiv.org/pdf/2407.00956v4#page=19 "Tree-based ensembles (CatBoost, LightGBM, XGBoost) remain strong, reliable, and statistically robust baselines.")、上位の手法はしばしば統計的に区別できなかった [arxiv-2407.00956#c6](https://arxiv.org/pdf/2407.00956v4#page=19 "Despite these advances, the Wilcoxon–Holm tests show that foundation models, ensembles, and top DNNs (RealMLP, ModernNCA) often remain statistically tied, suggesting that universal superiority has not yet been achieved.")。木と深層学習の差は、特徴の不均一さの指標と最も強く相関した [arxiv-2407.00956#c8](https://arxiv.org/pdf/2407.00956v4#page=35 "These findings suggest that the degree of heterogeneity among dataset features is a more critical determinant driving the relative model superiority.")。数値とカテゴリが混ざったデータでは、生の特徴を使う MLP 系が最も振るわなかった [arxiv-2407.00956#c9](https://arxiv.org/pdf/2407.00956v4#page=36 "DNN-based methods such as MLP and RealMLP exhibit their worst performance on datasets with mixed feature types (Mixed Data).")。
- Borisov らの比較では、非常に大きな1つのデータセットを除き、GBDT が最もよかった [arxiv-2110.01889#c5](https://arxiv.org/pdf/2110.01889v3#page=13 "For all but the very large HIGGS data set, the best scores are still obtained by boosted decision tree ensembles.") [arxiv-2110.01889#c6](https://arxiv.org/pdf/2110.01889v3#page=13 "This suggests that for very large tabular data sets with predominantly continuous features, modern neural network architectures may have an advantage over classical approaches after all.")。
- McElfresh らは、多くのデータセットで GBDT と深層学習の差は無視できる程度で、軽く調整することのほうが、どちらを選ぶかより重要なことが多いと述べている [arxiv-2305.02997#c1](https://arxiv.org/pdf/2305.02997v4#page=1 "we find that the 'NN vs. GBDT' debate is overemphasized") [arxiv-2305.02997#c2](https://arxiv.org/pdf/2305.02997v4#page=1 "light hyperparameter tuning on a GBDT is more important than choosing between NNs and GBDTs")。

### 解釈可能性の主張の根拠

いくつかのモデルは「解釈できる」と主張するが、根拠は限られている。

- TabNet:合成データでのマスクの可視化と、2つのデータセットでの重要度の比較 [arxiv-1908.07442#c5](https://arxiv.org/pdf/1908.07442v5#page=7 "TabNet assigns an importance score ratio of 43% for it, while other methods like LIME (Ribeiro, Singh, and Guestrin 2016), Integrated Gradients (Sundararajan, Taly, and Yan 2017) and DeepLift (Shrikumar, Greenside, and Kundaje 2017) assign less than 30% (Ibrahim et al. 2019).")。
- GRANDE:1つのサンプルの事例研究 [arxiv-2309.17130#c9](https://arxiv.org/pdf/2309.17130v3#page=8 "In contrast, existing ensemble methods require a global interpretation of the model and do not provide simple, local explanations out-of-the-box.")。
- SAINT:MNIST などでの注意の可視化 [arxiv-2106.01342#c8](https://arxiv.org/pdf/2106.01342v1#page=8 "One advantage of using transformer-based models is that attention comes with some interpretability, in contrast, MLPs are hard to interpret.")。
- AutoInt:注意のヒートマップ [arxiv-1810.11921#c8](https://arxiv.org/pdf/1810.11921v2#page=9 "We can see that AutoInt is able to identify the meaningful combinatorial feature <Gender=Male, Age=[18-24), MovieGenre=Action&Triller> (i.e., red dotted rectangle).")。
- Borisov らは、注意に基づく特徴の帰属を検証し、KernelSHAP との順位の相関が意外に低かったと報告している [arxiv-2110.01889#c8](https://arxiv.org/pdf/2110.01889v3#page=14 "In these two simple benchmarks, the transformer models were not able to produce convincing feature attributions out-of-the-box.")。

### 利益相反

FT-Transformer、数値の埋め込み、TabR、TabM はいずれも Gorishniy と Babenko を含む同じ研究グループによるもので、後の論文が前の論文のモデルや評価手順を比較相手や基盤に使っている [arxiv-2203.05556#c5](https://arxiv.org/pdf/2203.05556v4#page=16 "For every dataset, we carefully tune each model’s hyperparameters.") [arxiv-2307.14338#c4](https://arxiv.org/pdf/2307.14338v2#page=3 "The most important points are that, for any given algorithm, on each dataset, following Gorishniy et al. (2022), (1) we perform hyperparameter tuning and early stopping using the validation set;")。Ye らの比較は著者ら自身のツールボックスと手法を含み、DCN V2 は第一著者が元の DCN の著者でもある(各カードの notes 参照)。

## 設計への示唆(本記事の整理)

- **まず強いベースラインを置く。** よく調整した GBDT と、よく調整した MLP(できれば数値の埋め込み付き)は、多くの論文で強い比較相手になっている [arxiv-2106.11959#c8](https://arxiv.org/pdf/2106.11959v5#page=7 "Tuning makes simple models such as MLP and ResNet competitive, so we recommend tuning baselines when possible.") [arxiv-2203.05556#c7](https://arxiv.org/pdf/2203.05556v4#page=8 "Importantly, after the MLP-like architectures are coupled with embeddings for numerical features, they perform on par with the Transformer-based models.") [arxiv-2106.11189#c7](https://arxiv.org/pdf/2106.11189v2#page=8 "The results show that our MLPs outperform all three GBDT variants (XGBoost, auto-sklearn, and CatBoost) with a statistically signiﬁcant margin.")。
- **構造より、埋め込み・前処理・正則化・アンサンブルを先に見直す。** これらが構造と同じくらい効くことが繰り返し報告されている [arxiv-2203.05556#c6](https://arxiv.org/pdf/2203.05556v4#page=8 "However, for the vast majority of the “backbone & dataset” pairs, proper embeddings are the only thing needed to close the gap with GBDT.") [arxiv-2407.04491#c24](https://arxiv.org/pdf/2407.04491v3#page=10 "our architectural improvements alone are beneficial when applied to MLP-D directly, although non-architectural aspects are at least as important.") [arxiv-2410.24210#c11](https://arxiv.org/pdf/2410.24210v3#page=2 "the two key reasons for TabM's high performance are the collective training of the underlying implicit MLPs and the weight sharing.")。
- **特徴が不均一なデータ(数値とカテゴリの混在)では木が強い可能性を考える** [arxiv-2407.00956#c8](https://arxiv.org/pdf/2407.00956v4#page=35 "These findings suggest that the degree of heterogeneity among dataset features is a more critical determinant driving the relative model superiority.") [arxiv-2407.00956#c9](https://arxiv.org/pdf/2407.00956v4#page=36 "DNN-based methods such as MLP and RealMLP exhibit their worst performance on datasets with mixed feature types (Mixed Data).")。
- **事前学習は、ラベルが少なくラベルなしのデータが多いときに試す** [arxiv-2012.06678#c4](https://arxiv.org/pdf/2012.06678v1#page=4 "We do not ﬁnd much beneﬁt in using it when the entire data is labeled.") [arxiv-2106.01342#c7](https://arxiv.org/pdf/2106.01342v1#page=8 "Interestingly, we note that when all the training data samples are labeled, pre-training does not contribute appreciably, hence the results with and without pre-training are fairly close.")。
- **論文の比較を読むときは、調整の予算と、比較相手の数値を流用していないかを確認する**(9節)。

## わかっていないこと

- 数値の埋め込みが最適化をどう助けているのかは、著者ら自身が未解明としている [arxiv-2203.05556#c9](https://arxiv.org/pdf/2203.05556v4#page=10 "For example, it is still to be explained how exactly the discussed embedding modules help optimization on the fundamental level.")。
- 木と深層学習の差が特徴の不均一さとどの程度因果的に結びつくかは、Ye らの相関の分析を超えて示されていない [arxiv-2407.00956#c8](https://arxiv.org/pdf/2407.00956v4#page=35 "These findings suggest that the degree of heterogeneity among dataset features is a more critical determinant driving the relative model superiority.")。
- ベンチマークの選び方によって結論が変わりうることは、多くの論文自身が認めている [arxiv-2106.11959#c5](https://arxiv.org/pdf/2106.11959v5#page=8 "it only means that the constructed benchmark is slightly biased towards 'DL-friendly' problems.") [arxiv-2203.05556#c4](https://arxiv.org/pdf/2203.05556v4#page=5 "Importantly, we focus on the middle and large scale tasks, and our benchmark is biased towards GBDT-friendly problems, since, as of now, closing the gap with GBDT models on such tasks is one of the main challenges for tabular DL.") [arxiv-2110.01889#c9](https://arxiv.org/pdf/2110.01889v3#page=16 "While we chose common data sets with varying characteristics for our experiments, a different choice of data sets or hyperparameter such as the encoding use (e.g., use one-hot encoding) may lead to a different outcome.")。

## 参照カード

- [arxiv-2110.01889](../../papers/arxiv-2110.01889.yaml) Borisov et al., "Deep Neural Networks and Tabular Data: A Survey"
- [arxiv-2207.08815](../../papers/arxiv-2207.08815.yaml) Grinsztajn et al., "Why do tree-based models still outperform deep learning on tabular data?"
- [arxiv-1908.07442](../../papers/arxiv-1908.07442.yaml) Arik & Pfister, "TabNet: Attentive Interpretable Tabular Learning"
- [arxiv-1909.06312](../../papers/arxiv-1909.06312.yaml) Popov, Morozov & Babenko, "Neural Oblivious Decision Ensembles for Deep Learning on Tabular Data"
- [arxiv-2309.17130](../../papers/arxiv-2309.17130.yaml) Marton et al., "GRANDE: Gradient-Based Decision Tree Ensembles for Tabular Data"
- [arxiv-1810.11921](../../papers/arxiv-1810.11921.yaml) Song et al., "AutoInt: Automatic Feature Interaction Learning via Self-Attentive Neural Networks"
- [arxiv-2012.06678](../../papers/arxiv-2012.06678.yaml) Huang et al., "TabTransformer: Tabular Data Modeling Using Contextual Embeddings"
- [arxiv-2106.11959](../../papers/arxiv-2106.11959.yaml) Gorishniy et al., "Revisiting Deep Learning Models for Tabular Data"
- [arxiv-2106.01342](../../papers/arxiv-2106.01342.yaml) Somepalli et al., "SAINT: Improved Neural Networks for Tabular Data via Row Attention and Contrastive Pre-Training"
- [arxiv-2305.18446](../../papers/arxiv-2305.18446.yaml) Chen et al., "Trompt: Towards a Better Deep Neural Network for Tabular Data"
- [arxiv-2301.02819](../../papers/arxiv-2301.02819.yaml) Chen et al., "ExcelFormer: A neural network surpassing GBDTs on tabular data"
- [arxiv-2203.05556](../../papers/arxiv-2203.05556.yaml) Gorishniy, Rubachev & Babenko, "On Embeddings for Numerical Features in Tabular Deep Learning"
- [arxiv-2008.13535](../../papers/arxiv-2008.13535.yaml) Wang et al., "DCN V2: Improved Deep & Cross Network and Practical Lessons for Web-scale Learning to Rank Systems"
- [arxiv-2106.11189](../../papers/arxiv-2106.11189.yaml) Kadra et al., "Well-tuned Simple Nets Excel on Tabular Datasets"
- [arxiv-2407.04491](../../papers/arxiv-2407.04491.yaml) Holzmüller et al., "Better by Default: Strong Pre-Tuned MLPs and Boosted Trees on Tabular Data"
- [arxiv-2410.24210](../../papers/arxiv-2410.24210.yaml) Gorishniy et al., "TabM: Advancing Tabular Deep Learning with Parameter-Efficient Ensembling"
- [arxiv-2307.14338](../../papers/arxiv-2307.14338.yaml) Gorishniy et al., "TabR: Tabular Deep Learning Meets Nearest Neighbors in 2023"
- [arxiv-2106.15147](../../papers/arxiv-2106.15147.yaml) Bahri et al., "SCARF: Self-Supervised Contrastive Learning using Random Feature Corruption"
- [arxiv-2407.00956](../../papers/arxiv-2407.00956.yaml) Ye et al., "A Closer Look at Deep Learning Methods on Tabular Datasets"
- [arxiv-2106.03253](../../papers/arxiv-2106.03253.yaml) Shwartz-Ziv & Armon, "Tabular Data: Deep Learning is Not All You Need"
- [arxiv-2305.02997](../../papers/arxiv-2305.02997.yaml) McElfresh et al., "When Do Neural Nets Outperform Boosted Trees on Tabular Data?"
