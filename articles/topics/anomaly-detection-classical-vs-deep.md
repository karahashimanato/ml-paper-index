---
title: 異常検知 — 古典的な手法と深層学習、設定の違いと評価の落とし穴
kind: topic
tags: [anomaly-detection, classical-outlier-detectors]
depends_on: [arxiv-2206.09426, arxiv-2305.00735, arxiv-2007.02500, arxiv-1901.01588, arxiv-1811.02141, arxiv-2206.06602, arxiv-2103.16440, arxiv-2005.02359, arxiv-1906.02694, arxiv-2006.00339, arxiv-1812.04606, arxiv-1805.10917, arxiv-2106.08265, arxiv-2011.08785, arxiv-2106.03844, arxiv-2009.11732, arxiv-2501.13864, arxiv-1904.02639, arxiv-1812.02765, arxiv-1810.09136, arxiv-2003.05991, arxiv-2308.13068, arxiv-2109.05257]
written_at: 2026-10-06
written_by: claude-opus-5-5 via Claude Code
---

# 異常検知 — 古典的な手法と深層学習、設定の違いと評価の落とし穴

<!-- generated:stale -->
> ⚠ この記事の執筆後(2026-10-06)に、関連カードが 9 件追加されています(未反映): `arxiv-2009.13807`, `arxiv-2506.18046`, `arxiv-2609.29194`, `arxiv-2609.36968`, `arxiv-2609.39215`, `arxiv-2609.39257`, `arxiv-2610.00978`, `arxiv-2610.01168`, `arxiv-2610.01223`
<!-- /generated:stale -->

## この記事の読み方

異常検知では、k 近傍法・LOF・Isolation Forest のような古典的な(浅い)手法と、深層学習の手法の両方が使われている。
この記事は、「深層学習の方が良いのか」という問いに、論文がどこまで答えているかを整理する。

結論を先に書くと、**答えは設定によって変わり、その設定の違いが論文ごとに揃っていない**。そこでこの記事は、次の順に整理する。

1. 異常検知の「設定」の違い
2. 大規模なベンチマークが古典と深層について何を示したか
3. 系統ごとの手法(孤立型、自己教師ありの変換型、1クラス・半教師あり、事前学習の特徴を使う画像の手法)
4. 評価の落とし穴

性能の数値は書かない。各論文のページの結果表を参照のこと(カードは結果表を記録せず、主張だけを記録している)。時系列の異常検知は [時系列異常検知の記事](../tasks/time-series-anomaly-detection.md) で、オートエンコーダによる異常検知は [オートエンコーダの記事](../methods/autoencoders.md) で扱っている。

## 1. 設定の違い — 「教師なし」が指すものは論文ごとに違う

同じ「教師なし」でも、論文によって指すものが違う。

| 設定 | 学習データ | 例 |
|---|---|---|
| 教師なし(汚染あり) | ラベルなし。異常が混ざっているかもしれない | ADBench の教師なしの設定 [arxiv-2206.09426#c2](https://arxiv.org/pdf/2206.09426v2#page=6 "We repeat each experiment 3 times and report the average.")、Bouman らの比較 [arxiv-2305.00735#c3](https://arxiv.org/pdf/2305.00735v1#page=10 "For each dataset, we calculate anomaly scores on all available data at once, without using any cross-validation or train-test splits.") |
| 1クラス・新規性検知(きれいな正常データ) | 正常データだけ | PatchCore [arxiv-2106.08265#c1](https://arxiv.org/pdf/2106.08265v2#page=1 "It arises in many industrial scenarios where it is easy to acquire imagery of normal examples but costly and complicated to specify the expected defect variations in full.")、PaDiM [arxiv-2011.08785#c1](https://arxiv.org/pdf/2011.08785v1#page=1 "Hence, anomaly detection models are often estimated in a one-class learning setting, i.e., when the training dataset contains only images from the normal class and anomalous examples are not available during the training.")、幾何変換 [arxiv-1805.10917#c1](https://arxiv.org/pdf/1805.10917v2#page=1 "In the present paper, we focus on the basic (and harder) version of anomaly detection, and consider only machine vision applications for which deep models (e.g., convolutional neural networks) are essential.") |
| 半教師あり | 大部分はラベルなし、少数のラベル付きの正常・異常 | Deep SAD [arxiv-1906.02694#c1](https://arxiv.org/pdf/1906.02694v2#page=2 "Unlike the standard unsupervised AD setting, in many real-world applications one may also have access to some veriﬁed (i.e., labeled) normal or anomalous samples in addition to the unlabeled data.")、ADBench の半教師ありの設定 [arxiv-2206.09426#c6](https://arxiv.org/pdf/2206.09426v2#page=7 "For most semi-supervised methods, merely 1% labeled anomalies are sufﬁcient to surpass the best unsupervised method (shown as the dashed line in Fig. 4b), while most supervised methods need 10% labeled anomalies to achieve so.") |
| 補助の外れ値を使う(Outlier Exposure) | 正常データ+テストの異常とは別の補助データ | Outlier Exposure [arxiv-1812.04606#c1](https://arxiv.org/pdf/1812.04606v3#page=2 "Thus, we consider the realistic setting where Dout is unknown.") |

用語も揃っていない。深層異常検知のレビューは、正常データだけで学習する方法を「半教師あり」と呼んでいる [arxiv-2007.02500#c2](https://arxiv.org/pdf/2007.02500v3#page=4 "To avoid unnecessary confusion, following [2, 28], these methods are referred to as semi-supervised methods hereafter.")。GOAD も同じ設定を半教師ありと呼んでいる [arxiv-2005.02359#c1](https://arxiv.org/pdf/2005.02359v1#page=1 "In this setting, we have a training set of normal examples (which contains no anomalies).")。
Ruff らは、教師なし・補助の外れ値を使う教師なし・補助の外れ値を使う教師ありの3つを区別することを提案している [arxiv-2006.00339#c1](https://arxiv.org/pdf/2006.00339v3#page=1 "Unsupervised OE: Adaptations of unsupervised methods that incorporate auxiliary data that is not nominal.")。

学習データに異常が混ざっているかどうかは重要である。正常を学習する方法の多くは、学習データがきれいだと暗に仮定している [arxiv-2007.02500#c7](https://arxiv.org/pdf/2007.02500v3#page=30 "This is because most methods in Sections 5 implicitly assume that the training data is clean and does not contain any noise/anomaly instances.")。汚染が大きいほど、正常の境界がゆがむ [arxiv-2009.11732#c7](https://arxiv.org/pdf/2009.11732v3#page=6 "The greater the contamination, the more the normal data decision boundary will be distorted by including the anomalous points.")。

## 2. 大規模なベンチマークは何を示したか

### 表形式のデータ(教師なし)

- **ADBench**(57 データセット): 教師なしの設定では、14 の手法のどれも統計的に他より優れてはいなかった [arxiv-2206.09426#c4](https://arxiv.org/pdf/2206.09426v2#page=7 "None of the unsupervised methods is statistically better than the others, as shown in the critical difference diagram of Fig. 4a")。DeepSVDD や DAGMM のような深層の手法は、浅い手法より悪いことがあった。著者らは、深層の教師なしの手法はハイパーパラメータが多く、ラベルなしでは学習も調整も難しいためだと考えている [arxiv-2206.09426#c5](https://arxiv.org/pdf/2206.09426v2#page=7 "We also note that some DL-based unsupervised methods like DeepSVDD and DAGMM are surprisingly worse than shallow methods.")。
- **Bouman らの比較**: k 近傍法の一種(k 番目の近傍までの距離)が、他の多くの手法を統計的に上回った。Isolation Forest とその拡張も安定していて、計算量の面で有利である [arxiv-2305.00735#c5](https://arxiv.org/pdf/2305.00735v1#page=13 "Since the computational complexity of Isolation Forest and variants thereof scales linearly with the number of samples n, this may give them a clear edge over methods such as kNN and derivatives for large datasets")。ニューラルネットワークの多くは良くなかった [arxiv-2305.00735#c6](https://arxiv.org/pdf/2305.00735v1#page=13 "From these overall results it is clear that many of the neural networks do not perform well.")。著者らは、この種のデータには3つの手法で足りるのでは、と慎重に答えている [arxiv-2305.00735#c8](https://arxiv.org/pdf/2305.00735v1#page=21 "a toolbox with k-thNN, kNN, and EIF seems suﬃcient to perform well on the type of multivariate datasets considered in our study")。
- **Ruff らのレビューの比較**: 結果はデータセットや異常の種類で大きく違い、表現力の高い非線形のモデルがすべてのクラスで良いわけではなく、浅いモデルが深いモデルを上回ることもあった [arxiv-2009.11732#c4](https://arxiv.org/pdf/2009.11732v3#page=20 "Also, the more powerful nonlinear models are not better on every class, and simple ‘shallow’ models occasionally outperform their deeper counterparts.")。
- **Deep SAD の論文自身の比較**: 古典的な表形式のベンチマークでは、浅いカーネル法の方がやや有利に見える、と著者らが書いている [arxiv-1906.02694#c9](https://arxiv.org/pdf/1906.02694v2#page=9 "Here we observe that the shallow kernel methods seem to have a slight edge on the relatively small, low-dimensional benchmarks.")。
- **GOAD の論文自身の比較**: 深いネットワークは大きなデータセットでは役立ったが、小さいデータセットでは必要なかった [arxiv-2005.02359#c7](https://arxiv.org/pdf/2005.02359v1#page=9 "For performance critical operations, our approach may be used in a linear setting.")。

一方、深層異常検知のレビューは、浅い手法は複雑なデータでは大きく劣ると論じている [arxiv-2007.02500#c1](https://arxiv.org/pdf/2007.02500v3#page=5 "Although there are shallow methods for handling those complex data, they are generally substantially weaker and less adaptive than the deep methods.")。点異常については深層の手法が伝統的な手法より大幅に良いとも書いている [arxiv-2007.02500#c8](https://arxiv.org/pdf/2007.02500v3#page=30 "Most deep anomaly detection methods focus on point anomalies, showing substantially better performance than traditional methods.")。ただし、これらは比較実験に基づく主張ではない。レビュー自身も、手法を性能で比較するメタ分析はしていない [arxiv-2007.02500#c5](https://arxiv.org/pdf/2007.02500v3#page=27 "Since these methods are evaluated on diverse datasets, it is difficult to have an universal meta-analysis of their empirical performance.")。

### 異常の種類で勝つ手法が変わる

- ADBench は、合成した異常の種類(局所、大域、依存関係、クラスタ)で比較した。手法の前提が異常の種類に合うかどうかで性能が決まった [arxiv-2206.09426#c7](https://arxiv.org/pdf/2206.09426v2#page=8 "Performance of unsupervised algorithms highly depends on the alignment of its assumptions and the underlying anomaly type.")。
- Bouman らも、データセットを「局所的」と「大域的」に分け、LOF のような局所的な手法は局所的なデータでだけ良いと報告している [arxiv-2305.00735#c7](https://arxiv.org/pdf/2305.00735v1#page=15 "This phenomenon is a ﬁne example of Simpson’s paradox (Simpson, 1951).")。ただし、この二分法は単純化しすぎかもしれない、と注記している [arxiv-2305.00735#c9](https://arxiv.org/pdf/2305.00735v1#page=20 "However, we are well aware that this characterization may turn out to be an")。

### ラベルが少しあると状況が変わる

ADBench では、ラベル付きの異常がごく少数でもあると、多くの半教師ありの手法が最良の教師なしの手法を上回った [arxiv-2206.09426#c6](https://arxiv.org/pdf/2206.09426v2#page=7 "For most semi-supervised methods, merely 1% labeled anomalies are sufﬁcient to surpass the best unsupervised method (shown as the dashed line in Fig. 4b), while most supervised methods need 10% labeled anomalies to achieve so.")。
ただし、異常の種類によっては、ラベルを使う手法が最良の教師なしの手法に及ばなかった [arxiv-2206.09426#c8](https://arxiv.org/pdf/2206.09426v2#page=8 "The “power” of prior knowledge on anomaly types may overweigh the usage of partial labels.")。

## 3. 系統ごとの手法

### 孤立型(Isolation Forest とその拡張)

- **Isolation Forest の偏り**: 軸に平行な分割しか使わないため、データの少ない領域に人工的な帯や「幽霊のクラスタ」ができる [arxiv-1811.02141#c1](https://arxiv.org/pdf/1811.02141v3#page=2 "As we will see in later sections, the diﬀerence in the anomaly score in the x and y directions are indeed an artifacts introduced by the algorithm.") [arxiv-1811.02141#c2](https://arxiv.org/pdf/1811.02141v3#page=3 "Not only does this increase the chances of false positives, it also wrongly indicates a non-existent structure in the data.") [arxiv-1811.02141#c3](https://arxiv.org/pdf/1811.02141v3#page=4 "However, because of the constraint that the branch cuts are only vertical and horizontal, regions that don’t necessarily contain many data points end up with many branch cuts through them.")。Extended Isolation Forest は、ランダムな傾きの超平面で分割してこれを解消する [arxiv-1811.02141#c5](https://arxiv.org/pdf/1811.02141v3#page=6 "This results in a uniform selection of points on the N-sphere.")。実データでの改善は、データによってわずかなこともある [arxiv-1811.02141#c8](https://arxiv.org/pdf/1811.02141v3#page=10 "Naturally, the axis-parallel limitation has more eﬀects on some datasets than other.")。
- **Deep Isolation Forest**: 複数の特徴量を組み合わせないと孤立させられない異常には、Isolation Forest は対応できない [arxiv-2206.06602#c1](https://arxiv.org/pdf/2206.06602v4#page=1 "because it treats all features separately and considers only one feature per isolation operation.")。そこで、学習しないランダムなニューラルネットワークで表現を作り、その上で孤立木を作る [arxiv-2206.06602#c3](https://arxiv.org/pdf/2206.06602v4#page=2 "These networks are only casually initialised and do not involve any optimisation or training process.")。最適化した表現ではなくランダムな表現を使う理由も論じている [arxiv-2206.06602#c4](https://arxiv.org/pdf/2206.06602v4#page=7 "(ii) The downstream data partition might be strongly controlled by the optimisation process.")。ただし、あるデータでは最近傍法の方が良かった [arxiv-2206.06602#c7](https://arxiv.org/pdf/2206.06602v4#page=9 "The features in Fraud are the results of PCA transformation due to the confidentiality issues, and thus the distance concept used in the nearest neighbour information can well reflect the proximity relationship.")。

### 自己教師ありの変換型

- **幾何変換**: 画像に回転などの変換をかけ、どの変換かを当てる分類器の出力で正常さを測る [arxiv-1805.10917#c2](https://arxiv.org/pdf/1805.10917v2#page=4 "under a naïve (typically incorrect) assumption that all of these conditional distributions are independent")。大きい画像で古典的な手法との差が最も大きかった [arxiv-1805.10917#c6](https://arxiv.org/pdf/1805.10917v2#page=7 "Our relative advantage is most prominent when focusing on the larger images.")。ただし、正常クラスの多様性が大きいと苦戦し [arxiv-1805.10917#c7](https://arxiv.org/pdf/1805.10917v2#page=7 "Inspecting the results on CIFAR-100 (where 20 super-classes deﬁned the partition), we observe that our method was challenged by the diversity inside the normal class.")、変換に対して不変なクラスどうしでは働かない [arxiv-1805.10917#c9](https://arxiv.org/pdf/1805.10917v2#page=8 "It can be expected that due to the invariance of ‘8’ to horizontal ﬂip, the classiﬁer will have difﬁculties learning distinguishing features.")。
- **画像以外への拡張**: 画像以外では良い変換を手で設計しにくい [arxiv-2103.16440#c1](https://arxiv.org/pdf/2103.16440v4#page=4 "Since it is not always easy to design transformations for new application domains, we study their suitability for learning data transformations.")。GOAD は、ランダムなアフィン変換が画像では画素の順序を壊して働かないことを指摘している [arxiv-2005.02359#c3](https://arxiv.org/pdf/2005.02359v1#page=5 "Random afﬁne matrices did not perform competitively as they are not pixel order preserving, this information is effectively used by CNNs and removing this information hurts performance.")。NeuTraL AD は変換そのものを学習するが、画像では効果を期待していない [arxiv-2103.16440#c3](https://arxiv.org/pdf/2103.16440v4#page=5 "We do not expect any beneﬁt from using NeuTraL AD there.")。正常クラスが多様になると、LOF(k 近傍法の一種)が NeuTraL AD を含むすべての手法を上回ったデータもある [arxiv-2103.16440#c7](https://arxiv.org/pdf/2103.16440v4#page=8 "The traditional method LOF performs better than deep learning methods on CT and SAD.")。

### 1クラス・半教師あり・補助の外れ値

- **Deep SVDD と Deep SAD**: Deep SVDD は、学習データを中心の近くに写すように学習する。すべてを中心に写す崩壊を防ぐため、バイアス項を使わないなどの構造上の制約が要る [arxiv-1906.02694#c3](https://arxiv.org/pdf/1906.02694v2#page=4 "For initialization, Ruff et al. (2018) ﬁrst pre-train an autoencoder and then initialize the weights W of the network φ with the converged weights of the encoder.") [arxiv-1906.02694#c4](https://arxiv.org/pdf/1906.02694v2#page=17 "Most importantly, network φ must have no bias terms and no bounded activation functions.")。Deep SAD は少数のラベル付きの例を加えるが、ラベルのないデータの大部分は正常だと仮定している [arxiv-1906.02694#c5](https://arxiv.org/pdf/1906.02694v2#page=5 "In doing this we also incorporate the assumption that most of the unlabeled data is normal.")。教師ありの分類器は、ラベルが少ないと新しい種類の異常に弱い [arxiv-1906.02694#c8](https://arxiv.org/pdf/1906.02694v2#page=7 "Figure 2 moreover conﬁrms that a supervised classiﬁcation approach is vulnerable to novel anomalies at testing time when only little labeled training data is available.")。
- **Outlier Exposure**: テストの異常とは別の補助データで「正常でないもの」を学ばせる [arxiv-1812.04606#c1](https://arxiv.org/pdf/1812.04606v3#page=2 "Thus, we consider the realistic setting where Dout is unknown.")。補助データは量より多様性が重要で [arxiv-1812.04606#c7](https://arxiv.org/pdf/1812.04606v3#page=7 "This suggests that dataset diversity is important, not just size.")、ノイズで作った人工的な外れ値は分類器に暗記されて役に立たなかった [arxiv-1812.04606#c6](https://arxiv.org/pdf/1812.04606v3#page=5 "Note that we made an attempt to distort images with noise and use these as outliers for OE, but the classiﬁer quickly memorized this statistical pattern and did not detect new OOD examples any better than before (Hafner et al., 2018).")。
- **前提の再検証**: Ruff らは、補助の外れ値を使えば、普通の分類器が当時の最先端の異常検知手法を上回ることを示した [arxiv-2006.00339#c2](https://arxiv.org/pdf/2006.00339v3#page=2 "We ﬁnd that, using the same experimental OE setup as Hendrycks et al. (2019b), a standard classiﬁer is able to outperform current state-of-the-art AD methods on the one vs. rest AD benchmarks on MNIST and CIFAR-10.")。必要な補助の外れ値はごく少数で足りた [arxiv-2006.00339#c3](https://arxiv.org/pdf/2006.00339v3#page=2 "With only 64 OE samples a classiﬁer outperforms unsupervised methods (with or without OE) on the ImageNet one vs. rest benchmark (Hendrycks et al., 2019b).")。そのうえで、多くの深層異常検知の論文で試金石とされてきた「1クラス対残り」のベンチマークを問い直している [arxiv-2006.00339#c4](https://arxiv.org/pdf/2006.00339v3#page=2 "This benchmark applied to the aforementioned datasets is used as a litmus test in virtually all deep AD papers published at top-tier venues")。ただし、補助の外れ値を使う教師ありの方法が一般の解だとは主張していない [arxiv-2006.00339#c9](https://arxiv.org/pdf/2006.00339v3#page=4 "that it may be time for the community to move to more challenging benchmarks (e.g., MVTec-AD (Bergmann et al., 2019)) to gauge the signiﬁcance of deep AD works.")。

### 事前学習の特徴を使う画像の手法

工業製品の外観検査(MVTec AD など)では、ImageNet で事前学習したネットワークの特徴を使う手法が主流である。

- **PaDiM**: 各パッチ位置の特徴が多変量ガウス分布に従うと仮定する [arxiv-2011.08785#c3](https://arxiv.org/pdf/2011.08785v1#page=3 "To sum up the information carried by this set we make the assumption that Xij is generated by a multivariate Gaussian distribution")。ネットワークの学習は要らない [arxiv-2011.08785#c9](https://arxiv.org/pdf/2011.08785v1#page=6 "Unlike SPADE [5] and Patch SVDD [4], the space complexity of our model is independent of the dataset training size and depends only on the image resolution.")。
- **PatchCore**: 正常画像のパッチ特徴をメモリに貯め、近傍の距離で異常を測る。深い層の特徴は自然画像の分類に偏るので、中間の層を使う [arxiv-2106.08265#c2](https://arxiv.org/pdf/2106.08265v2#page=3 "Secondly, very deep and abstract features in ImageNet pretrained networks are biased towards the task of natural image classiﬁcation, which has only little overlap with the cold-start industrial anomaly detection task and the evaluated data at hand.")。メモリの大きさを抑えるため、代表点を選んで間引く [arxiv-2106.08265#c3](https://arxiv.org/pdf/2106.08265v2#page=4 "In this work we use a coreset subsampling mechanism to reduce M, which we ﬁnd reduces inference time while retaining performance.")。
- **平均シフトの対照損失**: 先行研究を引いて、ImageNet の事前学習の表現に k 近傍法を使うだけで、ほぼすべての自己教師ありの手法を上回ると述べる [arxiv-2106.03844#c2](https://arxiv.org/pdf/2106.03844v2#page=1 "(Reiss et al. 2021) found that even a simple kNN anomaly detection classiﬁer based on ImageNet pre-trained representation already outperforms nearly all self-supervised methods.")。事前学習なしで学習すると大きく劣化する [arxiv-2106.03844#c6](https://arxiv.org/pdf/2106.03844v2#page=6 "Therefore when training a model from scratch without any strong initialization that comes from a pre-trained model, our objective does not improve over standard contrastive losses.")。

これらの手法は、**事前学習の特徴が対象に転移することを前提にしている**。PatchCore の著者らも、適用できる範囲は事前学習の特徴の転移しやすさで限られるとしている [arxiv-2106.08265#c9](https://arxiv.org/pdf/2106.08265v2#page=8 "While PatchCore shows high effectiveness for industrial anomaly detection without the need to specifically adapt to the problem domain at hand, applicability is generally limited by the transferability of the pretrained features leveraged.")。
PaDiM の利点は主にテクスチャのクラスで、物体のクラスでは別の手法が良い指標もあった [arxiv-2011.08785#c7](https://arxiv.org/pdf/2011.08785v1#page=5 "It is particularly efﬁcient on texture images because even if they are not aligned and centered like object images, PaDiM effectively captures their statistical similarity accross the normal train dataset.")。MVTec AD の物体は位置が揃っているので、位置をずらしたデータでも試している [arxiv-2011.08785#c8](https://arxiv.org/pdf/2011.08785v1#page=6 "Thus, we can conclude that our method seems to be more robust to non-aligned images than the other existing and tested works.")。

## 4. 評価の落とし穴

### 閾値・ハイパーパラメータを何で選んだか

異常検知の論文では、**テストデータやラベル付きの異常を、閾値やハイパーパラメータの選択に使っている**例が目立つ。

| 論文 | 何を、何で選んだか |
|---|---|
| Deep SAD | 浅い手法とハイブリッドの手法のハイパーパラメータを、テストデータの一部での AUC を最大にするように選んだ。著者らは「意図的に与えた不公平な利点」と明記 [arxiv-1906.02694#c7](https://arxiv.org/pdf/1906.02694v2#page=6 "In our experiments we deliberately grant the shallow and hybrid methods an unfair advantage by selecting their hyperparameters to maximize AUC on a subset (10%) of the test set to minimize hyperparameter selection issues.") |
| 幾何変換 | 比較対象の OC-SVM のパラメータを、後から AUROC が最大になるように選んだ(不公平な利点と明記) [arxiv-1805.10917#c5](https://arxiv.org/pdf/1805.10917v2#page=5 "Note that the hyperparameter optimization procedure has been provided with a two-class classiﬁcation problem.") |
| NeuTraL AD | テストデータの一部を検証データとして構成の選択に使った(脚注) [arxiv-2103.16440#c4](https://arxiv.org/pdf/2103.16440v4#page=6 "We use 10% of the test set as the validation set to allow parameterization selection.") |
| GOAD | F1 の閾値を、テストデータの真の異常の数に合わせて決めた(先行研究に従った) [arxiv-2005.02359#c5](https://arxiv.org/pdf/2005.02359v1#page=7 "Following the protocol in Zong et al. (2018), the decision threshold value is chosen to result in the correct number of anomalies e.g. if the test set contains Na anomalies, the threshold is selected so that the highest Na scoring examples are classiﬁed as anomalies.") |
| PatchCore | 誤分類の数を、テストのスコアで F1 が最適になる閾値で数えた [arxiv-2106.08265#c8](https://arxiv.org/pdf/2106.08265v2#page=12 "We compute the working point (threshold above which scores are considered anomalous) using the F1-optimal point.")。近傍の大きさなどは MVTec AD での比較で決めている [arxiv-2106.08265#c6](https://arxiv.org/pdf/2106.08265v2#page=7 "Results in the top half of Figure 4 show a clear optimum between locality and global context for patch-based anomaly predictions, thus motivating the neighbourhood size p = 3.") |
| 平均シフトの対照損失 | 崩壊を避ける早期終了の時点を、評価データの曲線から読み取っている [arxiv-2106.03844#c7](https://arxiv.org/pdf/2106.03844v2#page=9 "We ﬁnd that early stopping after 25 iterations typically gets very close to the optimal accuracy.") |
| Ruff らの比較 | ハイパーパラメータを、テストデータから取り出した少数の正常と異常で選んだ例がある [arxiv-2009.11732#c6](https://arxiv.org/pdf/2009.11732v3#page=22 "Following the standard model training / validation procedure, we train a set of models on the training data, select their hyperparameters on hold out data (e.g., a few inliers and anomalies extracted from the test set), and then evaluate their performance on the remainder of the test set.") |

これに対し、ADBench は全手法を元論文の既定値で動かした。小さな検証データで調整できる可能性は認めたうえで、行っていない [arxiv-2206.09426#c3](https://arxiv.org/pdf/2206.09426v2#page=28 "It is also acknowledged that it is possible to use a small hold-out data for hyperparameter tuning for semi- and fully-supervised methods [164], while we do not consider this setting in this work.")。Bouman らは、ハイパーパラメータを最適化せず、妥当な設定の平均で評価した [arxiv-2305.00735#c1](https://arxiv.org/pdf/2305.00735v1#page=6 "We refrain from optimizing hyperparameters, e.g., using cross-validation, to reﬂect the real-world situation in which no labels are available for training the models.")。
Nalisnick らの論文は別の研究を引いて、VAE や GAN が k 近傍法を上回ったのは、既知の外れ値をハイパーパラメータの選択に使えた場合だけだったと紹介している [arxiv-1810.09136#c8](https://arxiv.org/pdf/1810.09136v3#page=9 "Škvára et al. (2018) experimentally compare VAEs and GANs against k-nearest neighbors (kNNs), showing that VAEs and GANs outperform kNNs only when known outliers can be used for hyperparameter selection.")。

### ベンチマークの作り方

- **分類データからの変換**: 多くの研究は、分類データを変換した異常検知のデータで評価している。これは実世界の性能を反映しないかもしれない [arxiv-2007.02500#c6](https://arxiv.org/pdf/2007.02500v3#page=27 "This way may fail to reflect the performance of the methods in real-world anomaly detection applications.")。「k クラスを除く」型のベンチマークは、本当の異常の良い代用ではないかもしれない [arxiv-2009.11732#c8](https://arxiv.org/pdf/2009.11732v3#page=19 "One caveat of AUC is that it can produce overly optimistic scores in case of highly imbalanced test sets [200], [451].")。
- **他論文の数値の転記**: GOAD と NeuTraL AD は、表形式のベンチマークで比較手法の数値を先行研究から転記している [arxiv-2005.02359#c4](https://arxiv.org/pdf/2005.02359v1#page=7 "OC-SVM, E2E-AE and DAGMM results are directly taken from those reported by Zong et al. (2018).") [arxiv-2103.16440#c8](https://arxiv.org/pdf/2103.16440v4#page=8 "We follow the conﬁguration of (Zong et al., 2018) to train all models on half of the normal data, and test on the rest of the normal data as well as the anomalies.")。
- **既定値か調整か**: 古典的な手法を scikit-learn の既定値で動かし、提案手法は調整している比較がある [arxiv-2103.16440#c5](https://arxiv.org/pdf/2103.16440v4#page=16 "OC-SVM, IF, and LOF are taken from scikit-learn library with default parameters.")。

### 指標の選び方

- AUC は閾値に依らないが、不均衡なテストデータでは楽観的になりやすいので、AUPRC も併せて報告するのが望ましい [arxiv-2009.11732#c8](https://arxiv.org/pdf/2009.11732v3#page=19 "One caveat of AUC is that it can produce overly optimistic scores in case of highly imbalanced test sets [200], [451].")。
- 画像の位置特定では、画素の AUROC は大きな異常を優遇するので、領域ごとの重なりの指標(PRO)も使う [arxiv-2011.08785#c5](https://arxiv.org/pdf/2011.08785v1#page=3 "Since the AUROC is biased in favor of large anomalies we also employ the per-region-overlap score (PRO-score) [2].")。

### 学習していないモデル・単純な手法との比較

時系列の異常検知では、単純な PCA が多くの深層手法を上回った [arxiv-2308.13068#c3](https://arxiv.org/pdf/2308.13068v2#page=1 "we propose a simple, yet challenging, baseline based on Principal Components Analysis (PCA) that surprisingly outperforms many recent Deep Learning (DL) based approaches on popular benchmark datasets.")。学習していないモデルが既存手法と同程度になった例もある [arxiv-2109.05257#c2](https://arxiv.org/pdf/2109.05257v2#page=1 "an untrained model obtains comparable detection performance to the existing methods even when PA is forbidden.")。
表形式でも、k 近傍法のような単純な手法が強い [arxiv-2305.00735#c5](https://arxiv.org/pdf/2305.00735v1#page=13 "Since the computational complexity of Isolation Forest and variants thereof scales linearly with the number of samples n, this may give them a clear edge over methods such as kNN and derivatives for large datasets")。深層の手法を提案する論文が、こうした単純な基準と比べているかを確認したい。

## 5. 深層の手法の失敗のしかた

オートエンコーダの記事で詳しく扱ったように、再構成誤差を使う手法には、異常までうまく再構成してしまう失敗がある [arxiv-1904.02639#c1](https://arxiv.org/pdf/1904.02639v2#page=1 "However, this assumption may not always hold, and sometimes the AE can “generalize” so well that it can also reconstruct the abnormal inputs well.") [arxiv-1812.02765#c2](https://arxiv.org/pdf/1812.02765v1#page=2 "Experimentally, we have found that autoencoders will sometimes reconstruct OOD samples with less error than many inlier samples.")。線形の場合には、訓練データから遠い点を誤差ゼロで再構成できることが示されている [arxiv-2501.13864#c2](https://arxiv.org/pdf/2501.13864v1#page=4 "We can prove this even in the semi-supervised setting, where we guarantee that the model was not exposed to anomalous data at training time.")。
オートエンコーダの異常検知の前提は、正常データの部分空間を学ぶことである [arxiv-2003.05991#c4](https://arxiv.org/pdf/2003.05991v2#page=11 "The use of autoencoders for this tasks, follows the assumption that a trained autoencoder would learn the latent subspace of normal samples.")。サーベイも、制約がなければ恒等写像で解けてしまうと指摘する [arxiv-2009.11732#c2](https://arxiv.org/pdf/2009.11732v3#page=14 "For models that have learned some truthful manifold structure or prototypical representation, a high reconstruction error would then detect off-manifold or non-prototypical instances.")。

## 選び方への示唆(本記事の整理)

論文の主張そのものではなく、本記事のまとめである。

1. **まず設定を確かめる**: 学習データに異常が混ざるか、きれいな正常データがあるか、少数のラベルがあるか。これで有力な手法が変わる [arxiv-2206.09426#c6](https://arxiv.org/pdf/2206.09426v2#page=7 "For most semi-supervised methods, merely 1% labeled anomalies are sufﬁcient to surpass the best unsupervised method (shown as the dashed line in Fig. 4b), while most supervised methods need 10% labeled anomalies to achieve so.") [arxiv-2007.02500#c7](https://arxiv.org/pdf/2007.02500v3#page=30 "This is because most methods in Sections 5 implicitly assume that the training data is clean and does not contain any noise/anomaly instances.")。
2. **表形式なら、まず k 近傍法と Isolation Forest を試す**: 大規模な比較で強く安定していて、計算も安い [arxiv-2305.00735#c5](https://arxiv.org/pdf/2305.00735v1#page=13 "Since the computational complexity of Isolation Forest and variants thereof scales linearly with the number of samples n, this may give them a clear edge over methods such as kNN and derivatives for large datasets") [arxiv-2305.00735#c8](https://arxiv.org/pdf/2305.00735v1#page=21 "a toolbox with k-thNN, kNN, and EIF seems suﬃcient to perform well on the type of multivariate datasets considered in our study")。
3. **画像で事前学習の特徴が使えるなら、それを使う**: ただし、対象が自然画像から遠いと転移しない可能性がある [arxiv-2106.08265#c9](https://arxiv.org/pdf/2106.08265v2#page=8 "While PatchCore shows high effectiveness for industrial anomaly detection without the need to specifically adapt to the problem domain at hand, applicability is generally limited by the transferability of the pretrained features leveraged.") [arxiv-2106.03844#c6](https://arxiv.org/pdf/2106.03844v2#page=6 "Therefore when training a model from scratch without any strong initialization that comes from a pre-trained model, our objective does not improve over standard contrastive losses.")。
4. **異常の種類を想定する**: 局所的か大域的かで勝つ手法が変わる [arxiv-2206.09426#c7](https://arxiv.org/pdf/2206.09426v2#page=8 "Performance of unsupervised algorithms highly depends on the alignment of its assumptions and the underlying anomaly type.") [arxiv-2305.00735#c7](https://arxiv.org/pdf/2305.00735v1#page=15 "This phenomenon is a ﬁne example of Simpson’s paradox (Simpson, 1951).")。
5. **論文の比較を読むときは、閾値とハイパーパラメータの出どころを見る**: テストデータやラベル付きの異常で選んでいないか [arxiv-1906.02694#c7](https://arxiv.org/pdf/1906.02694v2#page=6 "In our experiments we deliberately grant the shallow and hybrid methods an unfair advantage by selecting their hyperparameters to maximize AUC on a subset (10%) of the test set to minimize hyperparameter selection issues.") [arxiv-2103.16440#c4](https://arxiv.org/pdf/2103.16440v4#page=6 "We use 10% of the test set as the validation set to allow parameterization selection.")。
6. **少数でもラベルが得られるなら、半教師ありを検討する**: ラベル付きの異常がごく少数でも効くことがある [arxiv-2206.09426#c6](https://arxiv.org/pdf/2206.09426v2#page=7 "For most semi-supervised methods, merely 1% labeled anomalies are sufﬁcient to surpass the best unsupervised method (shown as the dashed line in Fig. 4b), while most supervised methods need 10% labeled anomalies to achieve so.")。

## わかっていないこと

- **深層が古典に勝つ条件**: 大規模な比較では深層の教師なしの手法は優位を示していない [arxiv-2206.09426#c4](https://arxiv.org/pdf/2206.09426v2#page=7 "None of the unsupervised methods is statistically better than the others, as shown in the critical difference diagram of Fig. 4a") [arxiv-2305.00735#c6](https://arxiv.org/pdf/2305.00735v1#page=13 "From these overall results it is clear that many of the neural networks do not perform well.")。データの種類や大きさによる条件は、この範囲では体系的に示されていない。
- **実際の異常での評価**: 分類データから作ったベンチマークへの依存が続いている [arxiv-2007.02500#c6](https://arxiv.org/pdf/2007.02500v3#page=27 "This way may fail to reflect the performance of the methods in real-world anomaly detection applications.") [arxiv-2006.00339#c9](https://arxiv.org/pdf/2006.00339v3#page=4 "that it may be time for the community to move to more challenging benchmarks (e.g., MVTec-AD (Bergmann et al., 2019)) to gauge the signiﬁcance of deep AD works.")。
- **調整の公平な比較**: 深層の手法は調整が難しいとされる [arxiv-2206.09426#c5](https://arxiv.org/pdf/2206.09426v2#page=7 "We also note that some DL-based unsupervised methods like DeepSVDD and DAGMM are surprisingly worse than shallow methods.") が、同じ調整予算で比べた研究はこの範囲にない。

## 現時点での整理

- **「教師なし」の意味は論文ごとに違い、設定を揃えないと比較できない** [arxiv-2007.02500#c2](https://arxiv.org/pdf/2007.02500v3#page=4 "To avoid unnecessary confusion, following [2, 28], these methods are referred to as semi-supervised methods hereafter.") [arxiv-2006.00339#c1](https://arxiv.org/pdf/2006.00339v3#page=1 "Unsupervised OE: Adaptations of unsupervised methods that incorporate auxiliary data that is not nominal.")。
- **表形式の大規模な比較では、深層の教師なしの手法は古典的な手法に対して優位を示していない** [arxiv-2206.09426#c4](https://arxiv.org/pdf/2206.09426v2#page=7 "None of the unsupervised methods is statistically better than the others, as shown in the critical difference diagram of Fig. 4a") [arxiv-2305.00735#c5](https://arxiv.org/pdf/2305.00735v1#page=13 "Since the computational complexity of Isolation Forest and variants thereof scales linearly with the number of samples n, this may give them a clear edge over methods such as kNN and derivatives for large datasets") [arxiv-2009.11732#c4](https://arxiv.org/pdf/2009.11732v3#page=20 "Also, the more powerful nonlinear models are not better on every class, and simple ‘shallow’ models occasionally outperform their deeper counterparts.")。
- **少数のラベルや補助の外れ値があると、状況は大きく変わる** [arxiv-2206.09426#c6](https://arxiv.org/pdf/2206.09426v2#page=7 "For most semi-supervised methods, merely 1% labeled anomalies are sufﬁcient to surpass the best unsupervised method (shown as the dashed line in Fig. 4b), while most supervised methods need 10% labeled anomalies to achieve so.") [arxiv-2006.00339#c2](https://arxiv.org/pdf/2006.00339v3#page=2 "We ﬁnd that, using the same experimental OE setup as Hendrycks et al. (2019b), a standard classiﬁer is able to outperform current state-of-the-art AD methods on the one vs. rest AD benchmarks on MNIST and CIFAR-10.")。
- **画像では、事前学習の特徴と単純な距離の組み合わせが強いが、事前学習の転移を前提にしている** [arxiv-2106.03844#c2](https://arxiv.org/pdf/2106.03844v2#page=1 "(Reiss et al. 2021) found that even a simple kNN anomaly detection classiﬁer based on ImageNet pre-trained representation already outperforms nearly all self-supervised methods.") [arxiv-2106.08265#c9](https://arxiv.org/pdf/2106.08265v2#page=8 "While PatchCore shows high effectiveness for industrial anomaly detection without the need to specifically adapt to the problem domain at hand, applicability is generally limited by the transferability of the pretrained features leveraged.")。
- **閾値やハイパーパラメータを、テストデータやラベル付きの異常で選ぶ評価が多い** [arxiv-1906.02694#c7](https://arxiv.org/pdf/1906.02694v2#page=6 "In our experiments we deliberately grant the shallow and hybrid methods an unfair advantage by selecting their hyperparameters to maximize AUC on a subset (10%) of the test set to minimize hyperparameter selection issues.") [arxiv-1805.10917#c5](https://arxiv.org/pdf/1805.10917v2#page=5 "Note that the hyperparameter optimization procedure has been provided with a two-class classiﬁcation problem.") [arxiv-2005.02359#c5](https://arxiv.org/pdf/2005.02359v1#page=7 "Following the protocol in Zong et al. (2018), the decision threshold value is chosen to result in the correct number of anomalies e.g. if the test set contains Na anomalies, the threshold is selected so that the highest Na scoring examples are classiﬁed as anomalies.")。

**この整理に含まれていないもの**: Isolation Forest・LOF・One-Class SVM の原典(arXiv にない)、グラフの異常検知、ログやテキストの異常検知、動画の異常検知、大規模言語モデルを使う異常検知。

## 参照カード

- [arxiv-2206.09426](../../papers/arxiv-2206.09426.yaml) Han et al., "ADBench: Anomaly Detection Benchmark"
- [arxiv-2305.00735](../../papers/arxiv-2305.00735.yaml) Bouman, Bukhsh & Heskes, "Unsupervised anomaly detection algorithms on real-world data: how many do we need?"
- [arxiv-2007.02500](../../papers/arxiv-2007.02500.yaml) Pang et al., "Deep Learning for Anomaly Detection: A Review"
- [arxiv-1901.01588](../../papers/arxiv-1901.01588.yaml) Zhao, Nasrullah & Li, "PyOD: A Python Toolbox for Scalable Outlier Detection"
- [arxiv-1811.02141](../../papers/arxiv-1811.02141.yaml) Hariri, Carrasco Kind & Brunner, "Extended Isolation Forest"
- [arxiv-2206.06602](../../papers/arxiv-2206.06602.yaml) Xu et al., "Deep Isolation Forest for Anomaly Detection"
- [arxiv-2103.16440](../../papers/arxiv-2103.16440.yaml) Qiu et al., "Neural Transformation Learning for Deep Anomaly Detection Beyond Images"
- [arxiv-2005.02359](../../papers/arxiv-2005.02359.yaml) Bergman & Hoshen, "Classification-Based Anomaly Detection for General Data"
- [arxiv-1906.02694](../../papers/arxiv-1906.02694.yaml) Ruff et al., "Deep Semi-Supervised Anomaly Detection"
- [arxiv-2006.00339](../../papers/arxiv-2006.00339.yaml) Ruff et al., "Rethinking Assumptions in Deep Anomaly Detection"
- [arxiv-1812.04606](../../papers/arxiv-1812.04606.yaml) Hendrycks, Mazeika & Dietterich, "Deep Anomaly Detection with Outlier Exposure"
- [arxiv-1805.10917](../../papers/arxiv-1805.10917.yaml) Golan & El-Yaniv, "Deep Anomaly Detection Using Geometric Transformations"
- [arxiv-2106.08265](../../papers/arxiv-2106.08265.yaml) Roth et al., "Towards Total Recall in Industrial Anomaly Detection"
- [arxiv-2011.08785](../../papers/arxiv-2011.08785.yaml) Defard et al., "PaDiM: a Patch Distribution Modeling Framework for Anomaly Detection and Localization"
- [arxiv-2106.03844](../../papers/arxiv-2106.03844.yaml) Reiss & Hoshen, "Mean-Shifted Contrastive Loss for Anomaly Detection"
- [arxiv-2009.11732](../../papers/arxiv-2009.11732.yaml) Ruff et al., "A Unifying Review of Deep and Shallow Anomaly Detection"
- [arxiv-2501.13864](../../papers/arxiv-2501.13864.yaml) Bouman & Heskes, "Autoencoders for Anomaly Detection are Unreliable"
- [arxiv-1904.02639](../../papers/arxiv-1904.02639.yaml) Gong et al., "Memorizing Normality to Detect Anomaly: Memory-augmented Deep Autoencoder for Unsupervised Anomaly Detection"
- [arxiv-1812.02765](../../papers/arxiv-1812.02765.yaml) Denouden et al., "Improving Reconstruction Autoencoder Out-of-distribution Detection with Mahalanobis Distance"
- [arxiv-1810.09136](../../papers/arxiv-1810.09136.yaml) Nalisnick et al., "Do Deep Generative Models Know What They Don't Know?"
- [arxiv-2003.05991](../../papers/arxiv-2003.05991.yaml) Bank, Koenigstein & Giryes, "Autoencoders"
- [arxiv-2308.13068](../../papers/arxiv-2308.13068.yaml) Sehili & Zhang, "Multivariate Time Series Anomaly Detection: Fancy Algorithms and Flawed Evaluation Methodology"
- [arxiv-2109.05257](../../papers/arxiv-2109.05257.yaml) Kim et al., "Towards a Rigorous Evaluation of Time-series Anomaly Detection"
