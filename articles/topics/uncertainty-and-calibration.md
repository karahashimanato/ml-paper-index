---
title: 不確実性の推定と較正 — ベイズ近似、較正の測り方、conformal prediction の保証の範囲
kind: topic
tags: [uncertainty-estimation, conformal-prediction, post-hoc-calibration, bayesian-deep-learning]
depends_on: [arxiv-1506.02142, arxiv-1612.01474, arxiv-1703.04977, arxiv-2002.02405, arxiv-2107.03342, arxiv-1706.04599, arxiv-1904.01685, arxiv-1909.10155, arxiv-2106.07998, arxiv-1910.12656, arxiv-1807.00263, arxiv-1906.02530, arxiv-2107.07511, arxiv-1604.04173, arxiv-1905.03222, arxiv-2009.14193, arxiv-1904.06019, arxiv-2202.13415, arxiv-2106.00170, arxiv-1910.03225, arxiv-2006.10562, arxiv-1610.01271, arxiv-1510.04342, doi-10.1109_tsg.2026.3676842]
written_at: 2026-10-06
written_by: claude-opus-5-5 via Claude Code
---

# 不確実性の推定と較正 — ベイズ近似、較正の測り方、conformal prediction の保証の範囲

<!-- generated:stale -->
> ⚠ この記事の執筆日(2026-10-06)以降に作成された関連カードが 3 件あります(未反映。執筆日と同じ日に作成されたカードを含む): `arxiv-1402.4102`, `arxiv-1711.05597`, `arxiv-1910.04102`
<!-- /generated:stale -->

## この記事の読み方

予測モデルに「どれくらい自信があるか」を出させる方法には、大きく3つの系統がある。

1. **モデルの中で不確実性を推定する**: ベイズ近似(MC dropout)、アンサンブル
2. **出力の確率を事後に較正する**: 温度スケーリングなど。較正がどれだけできているかを測る方法も含む
3. **予測集合・予測区間に保証を付ける**: conformal prediction

この記事は、それぞれが**何を保証し、何を仮定し、どんな代償を払うか**を整理する。とくに、分布が変わったときに何が壊れるかに注意する。
[フォールバックの記事](model-fallback-and-selection.md) で扱った「確信度を切り替えの引き金に使えるか」という問いの、その先にあたる内容である。

性能の数値は書かない。各論文のページの結果表を参照のこと(カードは結果表を記録せず、主張だけを記録している)。

## 1. 2種類の不確実性

Kendall と Gal は、不確実性を2つに分けた [arxiv-1703.04977#c1](https://arxiv.org/pdf/1703.04977v2#page=1 "This could be for example sensor noise or motion noise, resulting in uncertainty which cannot be reduced even if more data were to be collected.")。

- **データの不確実性(aleatoric)**: 観測のノイズによるもので、データを増やしても減らない。
- **モデルの不確実性(epistemic)**: モデルのパラメータについての不確かさで、データを増やせば減る。

それぞれの推定の仕方も分かれる。モデルの不確実性は MC dropout で、データの不確実性は出力の分散を予測させて推定する [arxiv-1703.04977#c2](https://arxiv.org/pdf/1703.04977v2#page=4 "This approach does not capture epistemic model uncertainty, as epistemic uncertainty is a property of the model and not of the data.")。
データの不確実性だけを予測するモデルは、モデルの不確実性を捉えない。勾配ブースティングで予測分布を出す方法も、ノイズの不確実性しか捉えない、という指摘がある [arxiv-2006.10562#c1](https://arxiv.org/pdf/2006.10562v4#page=2 "However, such models only capture data uncertainty (Gal, 2016; Malinin, 2019), also known as aleatoric uncertainty, which arises due to inherent class overlap or noise in the data.")。
実験では、データが増えるとモデルの不確実性は減り、学習データと違うデータでは増えた。データの不確実性はほぼ一定だった [arxiv-1703.04977#c8](https://arxiv.org/pdf/1703.04977v2#page=9 "Testing the models with a different test set (bottom two lines) shows that epistemic uncertainty increases considerably on those test points which lie far from the training sets.")。
一方だけを推定すると、もう一方の分まで補おうとするらしい、とも述べている [arxiv-1703.04977#c6](https://arxiv.org/pdf/1703.04977v2#page=8 "This suggests that when only one uncertainty is explicitly modeled, it attempts to compensate for the lack of the alternative uncertainty when possible.")。

サーベイは、方法を「1回の順伝播で出す決定的な方法」「ベイズ的な方法」「アンサンブル」「テスト時のデータ拡張」の4つに分類している [arxiv-2107.03342#c2](https://arxiv.org/pdf/2107.03342v3#page=7 "In general, the methods for estimating the uncertainty can be split in four different types based on the number (single or multiple) and the nature (deterministic or stochastic) of the used DNNs.")。

## 2. ベイズ近似とアンサンブル

### MC dropout

dropout を各層の前に入れたネットワークは、深いガウス過程の近似推論と等価である、という結果がある [arxiv-1506.02142#c2](https://arxiv.org/pdf/1506.02142v6#page=2 "We show that a neural network with arbitrary depth and non-linearities, with dropout applied before every weight layer, is mathematically equivalent to an approximation to the probabilistic deep Gaussian process")。予測のときも dropout を有効にして何度も順伝播し、その平均と分散を予測分布の近似とする [arxiv-1506.02142#c3](https://arxiv.org/pdf/1506.02142v6#page=4 "In practice this is equivalent to performing T stochastic forward passes through the network and averaging the results.")。

- 既存の dropout 付きのネットワークにそのまま使え、順伝播は並列に回せる [arxiv-1506.02142#c5](https://arxiv.org/pdf/1506.02142v6#page=4 "Furthermore, the forward passes can be done concurrently, resulting in constant running time identical to that of standard dropout.")。ただし、ネットワーク全体を何度も通す必要があるモデルでは、実際には大きく遅くなる [arxiv-1703.04977#c9](https://arxiv.org/pdf/1703.04977v2#page=9 "This is difﬁcult to parallelize due to GPU memory constraints, and often results in a 50× slow-down for 50 Monte Carlo samples.")。
- 予測分布は多峰的と考えられ、平均と分散はその一端しか表さない [arxiv-1506.02142#c4](https://arxiv.org/pdf/1506.02142v6#page=4 "and the above approximations only give a glimpse into its properties")。
- 不確実性の振る舞いは活性化関数などのモデルの選択に依存する [arxiv-1506.02142#c6](https://arxiv.org/pdf/1506.02142v6#page=5 "Note that the uncertainty is increasing far from the data for the ReLU model, whereas for the TanH model it stays bounded.")。
- 初期の版では標準誤差の報告に誤りがあり、後の版で訂正されている [arxiv-1506.02142#c9](https://arxiv.org/pdf/1506.02142v6#page=7 "Note that in an earlier version of this paper our reported dropout standard error was erroneously scaled-up by a factor of 4.5")。

### 深層アンサンブル

独立に学習した複数のネットワークを平均する [arxiv-1612.01474#c4](https://arxiv.org/pdf/1612.01474v3#page=3 "We suggest a simple recipe: (1) use a proper scoring rule as the training criterion, (2) use adversarial training [18] to smooth the predictive distributions, and (3) train an ensemble.")。

- 著者らは、ベイズモデル平均とアンサンブルは別物だと強調する [arxiv-1612.01474#c2](https://arxiv.org/pdf/1612.01474v3#page=2 "It is important to note that even exact BMA is not guaranteed be robust to mis-speciﬁcation with respect to domain shift.")。dropout も、率をデータに合わせて調整しないなら、パラメータを共有したアンサンブルと見る方が自然かもしれない、と論じる [arxiv-1612.01474#c1](https://arxiv.org/pdf/1612.01474v3#page=2 "The ensemble interpretation seems more plausible particularly in the scenario where the dropout rates are not tuned based on the training data")。
- 代償として、パラメータが M 倍になる [arxiv-1612.01474#c5](https://arxiv.org/pdf/1612.01474v3#page=9 "The ensemble has M times more parameters than a single network; for memory-constrained applications, the ensemble can be distilled into a simpler model [10, 26].")。
- 学習していないクラスの画像に対して、MC dropout は過信した予測を出し、アンサンブルの方が不確実性が上がりやすかった [arxiv-1612.01474#c7](https://arxiv.org/pdf/1612.01474v3#page=7 "In particular, MC-dropout seems to give high conﬁdence predictions for some of the test examples, as evidenced by the mode around 0 even for unseen classes.")。
- 二乗誤差で学習したネットワークの予測のばらつきだけでは、不確実性を過小評価した [arxiv-1612.01474#c9](https://arxiv.org/pdf/1612.01474v3#page=13 "For instance, the 80% prediction interval contains only 20% of the test observations, which means the empirical variance signiﬁcantly underestimates the true predictive uncertainty.")。

### ベイズ事後分布は本当に良いのか

Wenzel らは、深いネットワークで正確なベイズ事後分布を近似すると、SGD で学習した点推定より悪くなり、事後分布を「冷やす」(温度を1より下げる)と良くなることを示した(cold posterior) [arxiv-2002.02405#c1](https://arxiv.org/pdf/2002.02405v2#page=2 "Cold Posteriors: among all temperized posteriors the best posterior predictive performance on holdout data is achieved at temperature T < 1.")。温度を下げることは、データを何倍にも水増しするのと同じで、ベイズの原理から外れる [arxiv-2002.02405#c2](https://arxiv.org/pdf/2002.02405v2#page=3 "This is equivalent to a Bayes posterior obtained from a dataset consisting of 1/T replications of the original data, giving too strong evidence to individual models.")。

原因の候補として、推論の不正確さ、データ拡張などで尤度が「汚れている」こと、事前分布の悪さを調べた。しかし、どれも単独では説明しきれなかった [arxiv-2002.02405#c4](https://arxiv.org/pdf/2002.02405v2#page=6 "For the cases tested we conclude that SG-MCMC is almost as accurate as HMC and the lack of accept-reject correction cannot explain cold posteriors.") [arxiv-2002.02405#c5](https://arxiv.org/pdf/2002.02405v2#page=7 "demonstrates that cold posteriors remain when a clean likelihood is used in a suitably modiﬁed ResNet model") [arxiv-2002.02405#c6](https://arxiv.org/pdf/2002.02405v2#page=7 "The cold posterior effect cannot be resolved by using the right scaling of the Normal prior.")。
結論として、アンサンブルの計算量を考えると、もっと実用的な方法があるかもしれない、と述べている [arxiv-2002.02405#c8](https://arxiv.org/pdf/2002.02405v2#page=9 "However, taking into account the added computation from evaluating ensembles, there may be more practical methods, (Lakshminarayanan et al., 2017; Wen et al., 2019; Ashukha et al., 2020).")。

サーベイは別の研究を引いて、アンサンブルがベイズ的な方法を上回ったという結果を紹介している [arxiv-2107.03342#c5](https://arxiv.org/pdf/2107.03342v3#page=21 "Interestingly, they found for their tests ensembles to outperform the considered Bayesian approaches.")。一方、アンサンブルのメモリと計算量はメンバー数に比例して増える [arxiv-2107.03342#c4](https://arxiv.org/pdf/2107.03342v3#page=20 "The independence of the single ensemble members leads to a linear increase in the required memory and computation power with each additional member.")。

### 木のモデルの場合

勾配ブースティングでは、分布のパラメータを同時にブースティングして予測分布を出す方法(NGBoost) [arxiv-1910.03225#c2](https://arxiv.org/pdf/1910.03225v4#page=3 "Thus the choice of parameterization can drastically impact the training dynamics, even though the minima are unchanged.") と、知識の不確実性のためにアンサンブルを使う方法 [arxiv-2006.10562#c2](https://arxiv.org/pdf/2006.10562v4#page=4 "Unfortunately, there are no guarantees on how well the distribution q(θ) estimates the true posterior p(θ/D).") がある。詳しくは [勾配ブースティング木の記事](../methods/gradient-boosted-trees.md) を参照。
ランダムフォレストを因果効果の推定に使う研究では、漸近的な正規性に基づく信頼区間が示されている [arxiv-1510.04342#c3](https://arxiv.org/pdf/1510.04342v4#page=7 "This condition eﬀectively guarantees that, for large enough n, there will be enough treatment and control units near any test point x for local methods to work.")。ただし、その信頼区間は過小平滑化に依存し、そうでない場合のバイアスを捉えない [arxiv-1610.01271#c7](https://arxiv.org/pdf/1610.01271v4#page=27 "In particular, as discussed above, our conﬁdence interval construction relies on undersmoothing to get valid asymptotic coverage (without undersmoothing, the conﬁdence intervals account for sampling variability of the forest, but do not capture bias).")。

## 3. 較正 — 出力の確率は信用できるか

### 「現代のネットワークは較正が悪い」は本当か

Guo らは、現代のニューラルネットワークは10年前のものと違い較正が悪い、と報告した [arxiv-1706.04599#c1](https://arxiv.org/pdf/1706.04599v2#page=1 "We discover that modern neural networks, unlike those from a decade ago, are poorly calibrated.")。その対策として、1つの温度パラメータで出力の確率をならす温度スケーリングを提案した。温度は検証データで決める [arxiv-1706.04599#c3](https://arxiv.org/pdf/1706.04599v2#page=6 "In other words, temperature scaling does not affect the model’s accuracy.")。

Minderer らはこれを再検証した。最近のモデル族(MLP-Mixer、ViT、BiT)は精度が高く、較正も良いことを示し、「精度の高い現代のモデルほど較正が悪い」という傾向は続いていないかもしれない、と述べた [arxiv-2106.07998#c1](https://arxiv.org/pdf/2106.07998v2#page=5 "This suggests that there may be no continuing trend for highly accurate modern neural networks to be poorly calibrated")。
温度スケーリングで比べると、モデル族の違いがはっきり見えるようになった [arxiv-2106.07998#c4](https://arxiv.org/pdf/2106.07998v2#page=5 "Notably, temperature scaling reconciles our results for BiT (a ResNet architecture) with the results reported by Guo et al. for ResNets trained on IMAGENET.")。モデルの大きさや事前学習の量では族の違いを説明しきれず、構造の違いが効いているのではと推測している [arxiv-2106.07998#c5](https://arxiv.org/pdf/2106.07998v2#page=6 "Given that the best-calibrated families (MLP-Mixer and ViT) are non-convolutional, we speculate that model architecture, and in particular its spatial inductive bias, play an important role.")。

### ECE の測り方は結論を左右する

較正の指標として広く使われる ECE(期待較正誤差)は、確信度をいくつかの区間(ビン)に分けて、各ビンの確信度と正解率の差を平均する。この測り方には、次のような問題が指摘されている。

- **定義があいまい**: ビンの切り方や多クラスの扱いが定まっていない [arxiv-1904.01685#c2](https://arxiv.org/pdf/1904.01685v2#page=2 "ECE as framed in Naeini et al. (2015) leaves ambiguity in both its binning implementation and how to compute calibration for multiple classes.")。
- **ビンの数**: ビンの数はバイアスと分散のトレードオフである [arxiv-1904.01685#c3](https://arxiv.org/pdf/1904.01685v2#page=4 "Selecting the number of bins has a bias-variance tradeoff as it determines how many data points fall into each bin and therefore the quality of the estimate of calibration from that bin’s range.")。ビンの数で結論が入れ替わりうる [arxiv-2106.07998#c7](https://arxiv.org/pdf/2106.07998v2#page=9 "It is therefore possible to arrive at opposite conclusions about the relationship between accuracy and calibration, depending on the chosen bin size (Figure 9), especially when comparing models with widely varying accuracies.")。
- **ビン内での打ち消し**: 過信と自信不足が同じビンの中で打ち消し合う [arxiv-1904.01685#c4](https://arxiv.org/pdf/1904.01685v2#page=4 "Metrics that depend on static binning schemes like ECE suffer from issues where you can get near 0 calibration error due to overconﬁdent and underconﬁdent predictions overlapping in the same bin.")。
- **最大確率しか見ない**: ECE は各点の最大確率しか見ないので、全クラスを見る指標が提案されている [arxiv-1904.01685#c5](https://arxiv.org/pdf/1904.01685v2#page=5 "Unlike ECE, assuming inﬁnite data and inﬁnite bins, SCE is guaranteed to be zero if only if the model is calibrated.")。
- **過小評価**: ビンに分ける推定は、真の較正誤差を大きく過小評価しうる [arxiv-1909.10155#c3](https://arxiv.org/pdf/1909.10155v2#page=4 "A simple example shows that using binning to estimate the calibration error can severely underestimate the true calibration error.")。温度スケーリングのような連続な出力の方法は、報告されているほど較正できておらず、どれだけ外れているかを確かめるのも難しい [arxiv-1909.10155#c1](https://arxiv.org/pdf/1909.10155v2#page=4 "In this section, we show that methods like Platt scaling and temperature scaling are (i) less calibrated than reported and (ii) it is difﬁcult to tell how miscalibrated they are.")。
- **指標の選び方で順位が変わる**: 同じ較正手法の比較でも、指標の変種によって順位が大きく変わった [arxiv-1904.01685#c7](https://arxiv.org/pdf/1904.01685v2#page=7 "This demonstrates that varying the properties of the calibration error metric can lead to different conclusions about which model has the best calibration.")。
- **常に同じ確率を出す予測でも較正は良くなる**: クラスの全体の割合を出し続けるだけでもほぼ完全に較正されるので、誤り率や適切なスコアリングルールも併せて見る必要がある [arxiv-1910.12656#c3](https://arxiv.org/pdf/1910.12656v1#page=4 "Namely, it is easy to obtain almost perfectly calibrated probabilities by predicting the overall class distribution, regardless of the given instance.")。深層アンサンブルの論文は、較正を NLL や Brier スコアといった適切なスコアリングルールで測っている [arxiv-1612.01474#c3](https://arxiv.org/pdf/1612.01474v3#page=1 "The quality of calibration can be measured by proper scoring rules [17] such as log predictive probabilities and the Brier score [9].")。

### 温度スケーリングの限界と、その先

- **クラスごとの較正**: 温度スケーリングはパラメータが1つなので、最大確率では較正できても、クラスごとの確率は較正できないことがある [arxiv-1910.12656#c2](https://arxiv.org/pdf/1910.12656v1#page=3 "Having only a single tuneable parameter, temperature scaling cannot learn to act differently on different classes.")。Dirichlet 較正はこれを扱えるが、最良の手法はモデルとデータによって大きく変わる [arxiv-1910.12656#c9](https://arxiv.org/pdf/1910.12656v1#page=8 "According to the average rank across all deep net experiments, Dir-ODIR is best, but without statistical signiﬁcance.")。
- **パラメータの多い較正器**: クラスが多いと、パラメータの多い較正器は学習しにくい [arxiv-1706.04599#c7](https://arxiv.org/pdf/1706.04599v2#page=8 "Any calibration model with tens of thousands (or more) parameters will overﬁt to a small validation set, even when applying regularization.")。正則化すれば十分だという反論もある [arxiv-1910.12656#c6](https://arxiv.org/pdf/1910.12656v1#page=6 "We agree that some overﬁtting happens, but in our experiments a simple L2 regularisation sufﬁces on non-neural models")。
- **回帰の予測区間**: 回帰でも、ベイズの信用区間が名目どおりの頻度で当たらないことがある。予測の分位点を事後に較正する方法が提案されている [arxiv-1807.00263#c1](https://arxiv.org/pdf/1807.00263v1#page=1 "This problem arises because of model bias: a predictor may not be sufﬁciently expressive to assign the right probability to every credible interval, just as it may not be able to always assign the right label to a datapoint.") [arxiv-1807.00263#c2](https://arxiv.org/pdf/1807.00263v1#page=3 "In other words, the empirical and the predicted CDFs should match as the dataset size goes to inﬁnity.")。ただし、較正だけでは足りず、区間の鋭さも要る [arxiv-1807.00263#c3](https://arxiv.org/pdf/1807.00263v1#page=4 "In order to be useful, forecasts must also be sharp.")。

### 較正に使うデータ

事後の較正は、学習に使っていない、同じ分布の較正用データを必要とする [arxiv-1706.04599#c4](https://arxiv.org/pdf/1706.04599v2#page=4 "We assume that the training, validation, and test sets are drawn from the same distribution.") [arxiv-2107.03342#c6](https://arxiv.org/pdf/2107.03342v3#page=24 "They only work under the assumption that the distribution of the left-out validation set is equivalent to the distribution, on which inference is done.")。較正しても、モデルの不確実性は減らない [arxiv-2107.03342#c7](https://arxiv.org/pdf/2107.03342v3#page=24 "It is important to note that these methods do not reduce the model uncertainty, but propagate the model uncertainty onto the representation of the data uncertainty.")。

**読むときの注意**: 較正器をどのデータで当てはめたかは論文によって違う。

- 回帰の較正の論文は、別の較正用データを勧めながら、実験では学習データでそのまま較正している [arxiv-1807.00263#c5](https://arxiv.org/pdf/1807.00263v1#page=5 "As in classiﬁer recalibration, it is advisable to ﬁt R on a separate calibration set in order to reduce overﬁtting.") [arxiv-1807.00263#c6](https://arxiv.org/pdf/1807.00263v1#page=6 "We didn’t observe signiﬁcant overﬁtting and did not use a distinct calibration set.")。
- 再検証の論文は、ImageNet の検証データの一部で温度を当てはめ、残りで評価している [arxiv-2106.07998#c2](https://arxiv.org/pdf/2106.07998v2#page=4 "For the post-hoc recalibration of models, we reserve 20% of the IMAGENET validation set (randomly sampled) for ﬁtting the temperature scaling parameter.")。
- 検証付きの較正の論文は、検証データを3つに分けて、較正・ビンの選択・誤差の測定に使い分けている [arxiv-1909.10155#c4](https://arxiv.org/pdf/1909.10155v2#page=5 "We split the validation set into 3 sets of sizes (20000, 5000, 25000).")。

### 分布が変わると較正は崩れる

Ovadia らは、i.i.d. の検証データで較正しても、分布の変化が大きくなるにつれて較正誤差が大きく増えることを示した [arxiv-1906.02530#c4](https://arxiv.org/pdf/1906.02530v2#page=7 "Interestingly, while temperature scaling achieves low ECE for low values of shift, the ECE increases signiﬁcantly as the shift increases, which indicates that calibration on the i.i.d. validation dataset does not guarantee calibration under distributional shift.")。調べたすべての方法で、精度とともに不確実性の質も、分布の変化に伴って劣化した [arxiv-1906.02530#c6](https://arxiv.org/pdf/1906.02530v2#page=9 "Along with accuracy, the quality of uncertainty consistently degrades with increasing dataset shift regardless of method.")。
分布の変化の下では、大きなモデルの方が較正を保ちやすかった、という報告もある [arxiv-2106.07998#c6](https://arxiv.org/pdf/2106.07998v2#page=6 "In other words, the calibration of larger models is more robust to distribution shift (Figure 5).")。ただし、その変化は人工的な破損(ImageNet-C)である。
ラベルのない分布外のデータで較正を保つ方法は未解決の問題として挙げられている [arxiv-1909.10155#c9](https://arxiv.org/pdf/1909.10155v2#page=10 "However, can we maintain calibration when we do not have labeled examples from the target dataset?")。

## 4. conformal prediction — 保証付きの予測集合

### 何が保証されるか

split conformal prediction は、学習済みモデルと、学習に使っていない較正用データから、予測集合(回帰なら予測区間)を作る。正解がその集合に入る確率が、指定した水準以上になることを有限標本で保証する [arxiv-2107.07511#c1](https://arxiv.org/pdf/2107.07511v6#page=4 "In words, the probability that the prediction set contains the correct label is almost exactly 1 −α; we call this property marginal coverage, since the probability is marginal (averaged) over the randomness in the calibration and test points.")。

- **前提は交換可能性(i.i.d.)**: 較正用データとテストデータが同じ分布から来ている必要がある [arxiv-2107.07511#c2](https://arxiv.org/pdf/2107.07511v6#page=50 "As a technical remark, the theorem also holds if the observations to satisfy the weaker condition of exchangeability; see [1].") [arxiv-1905.03222#c1](https://arxiv.org/pdf/1905.03222v1#page=2 "Unlike the original interval, the conformalized prediction interval is guaranteed to satisfy the coverage requirement (1) regardless of the choice or accuracy of the quantile regression estimator.")。
- **保証は周辺の被覆**: 保証は平均についてのもので、個々の入力についてではない [arxiv-2009.14193#c1](https://arxiv.org/pdf/2009.14193v5#page=2 "Note that the guarantee in Eq. (1) is marginal over X and Y —it holds on average, not for a particular image X.") [arxiv-1604.04173#c4](https://arxiv.org/pdf/1604.04173v2#page=9 "Conditional coverage does hold asymptotically under certain conditions; see Theorem 3.5 in Section 3.")。入力ごとの条件付きの被覆は、分布を仮定しなければ一般に不可能である(先行研究を引いた記述) [arxiv-2107.07511#c4](https://arxiv.org/pdf/2107.07511v6#page=13 "This is a stronger property than the marginal coverage property in (1) that conformal prediction is guaranteed to achieve—indeed, in the most general case, conditional coverage is impossible to achieve [14].") [arxiv-2009.14193#c9](https://arxiv.org/pdf/2009.14193v5#page=10 "Therefore, conditional coverage isn’t the right goal for prediction sets with realistic sample sizes.")。
- **保証はどのスコアでも成り立つが、有用さはスコアで決まる**: 易しい入力で小さく、難しい入力で大きい集合を作れるかは、スコア関数次第である [arxiv-2107.07511#c3](https://arxiv.org/pdf/2107.07511v6#page=6 "although the guarantee always holds, the usefulness of the prediction sets is primarily determined by the score function.")。

### 代償と工夫

- **データの分割**: split conformal は1回のモデルの学習で済むが、データを学習用と較正用に分けるので統計的な効率が落ちる [arxiv-2107.07511#c8](https://arxiv.org/pdf/2107.07511v6#page=28 "Split conformal prediction requires only one model ﬁtting step, but sacriﬁces statistical eﬃciency.") [arxiv-1604.04173#c5](https://arxiv.org/pdf/1604.04173v2#page=10 "The split conformal method separates the ﬁtting and ranking steps using sample splitting, and its computational cost is simply that of the ﬁtting step.")。
- **区間の幅が一定**: 単純な split conformal の区間は入力によらず幅が一定で、ばらつきが入力で変わるときに不都合である [arxiv-1604.04173#c8](https://arxiv.org/pdf/1604.04173v2#page=30 "In fact, for split conformal, the width is exactly constant over x.") [arxiv-1905.03222#c3](https://arxiv.org/pdf/1905.03222v1#page=4 "A closer look at the prediction interval (8) reveals a major limitation of this procedure")。分位点回帰と組み合わせる方法(CQR)は、入力に応じた幅の区間を作り、同じ保証を保つ [arxiv-1905.03222#c4](https://arxiv.org/pdf/1905.03222v1#page=6 "The result even holds, and we will prove it, conditionally on the proper training set.")。
- **分類の予測集合**: CNN の確率は正しくないので、確率を足していくだけの素朴な方法では保証が得られない [arxiv-2009.14193#c2](https://arxiv.org/pdf/2009.14193v5#page=2 "There are two problems with naive: ﬁrst, the probabilities output by CNNs are known to be incorrect (Nixon et al., 2019), so the sets from naive do not achieve")。被覆・集合の小ささ・入力への適応性は互いに競合する [arxiv-2009.14193#c4](https://arxiv.org/pdf/2009.14193v5#page=4 "Coverage and size are obviously competing objectives, but size and adaptiveness are also often in tension.")。

### 評価を読むときの注意

- **集合が小さいほど良いとは限らない**: 平均の集合の大きさが最小の方法が最良とは限らず、適応性も見る必要がある [arxiv-2107.07511#c5](https://arxiv.org/pdf/2107.07511v6#page=12 "It is extremely important to keep in mind that the conformal prediction procedure with the smallest average set size is not necessarily the best.")。
- **較正用データの大きさで被覆がばらつく**: 保証はどんな大きさでも成り立つが、特定の較正用データでの被覆はばらつく [arxiv-2107.07511#c6](https://arxiv.org/pdf/2107.07511v6#page=14 "Roughly speaking, our conclusion will that be choosing a calibration set of size n = 1000 is suﬃcient for most purposes.")。
- **被覆の確かめ方**: ランダムな分割を何度も繰り返して、被覆の分布を確かめることが勧められている [arxiv-2107.07511#c7](https://arxiv.org/pdf/2107.07511v6#page=15 "So, we compute the coverage values by randomly splitting the n + nval data points R times into calibration and validation datasets, then running conformal.")。

## 5. 分布が変わったときの conformal prediction

| 状況 | 方法 | 保証がどう変わるか | 代償・限界 |
|---|---|---|---|
| 共変量シフト(入力の分布だけが変わる) | 尤度比で重み付けした conformal [arxiv-1904.06019#c1](https://arxiv.org/pdf/1904.06019v3#page=3 "Notice that the conditional distribution of Y /X is assumed to be the same for both the training and test data.") | 尤度比がわかれば周辺の被覆を保つ [arxiv-1904.06019#c2](https://arxiv.org/pdf/1904.06019v3#page=4 "Assume that ePX is absolutely continuous with respect to PX") | 実効的な標本数が減る [arxiv-1904.06019#c6](https://arxiv.org/pdf/1904.06019v3#page=6 "This is because, by using a quantile of the weighted empirical distribution of nonconformity scores, we are relying on a reduced “effective sample size”.")。尤度比を推定する場合の検証は、低次元の例に限られる [arxiv-1904.06019#c8](https://arxiv.org/pdf/1904.06019v3#page=14 "When the likelihood ratio d ePX/dPX is not known, it can be estimated given access to unlabeled data (test covariate points), which we showed empirically, on a low-dimensional example, can still yield correct coverage.") |
| 交換可能性がない一般の場合 | 固定の重みで古いデータを軽く扱う [arxiv-2202.13415#c1](https://arxiv.org/pdf/2202.13415v5#page=1 "Its validity relies on the assumptions of exchangeability of the data, and symmetry of the given model ﬁtting algorithm as a function of the data.") | 被覆の不足が、分布の違い(全変動距離)の重み付き和で抑えられる [arxiv-2202.13415#c2](https://arxiv.org/pdf/2202.13415v5#page=4 "In particular, if we use these methods, we are implicitly assuming that this weighted sum of total variation terms is small.") | その和が大きければ保証は意味をなさない [arxiv-2202.13415#c5](https://arxiv.org/pdf/2202.13415v5#page=18 "On the other hand, if the test point comes from a new distribution that bears no resemblance to the training data, neither our bound nor any other method would be able to guarantee valid coverage without further assumptions.")。重みが小さいと実効的な標本数が減り、区間が広がる [arxiv-2202.13415#c4](https://arxiv.org/pdf/2202.13415v5#page=18 "How to choose weights optimally (and, even how to quantify optimality) is an interesting and important question that we leave for future work.") |
| 時系列で分布が任意に変わる | 目標の水準をオンラインで調整する適応型 conformal(ACI) [arxiv-2106.00170#c2](https://arxiv.org/pdf/2106.00170v3#page=3 "To perform this calibration we will use a simple online update.") | 長期の平均の被覆が保証される [arxiv-2106.00170#c3](https://arxiv.org/pdf/2106.00170v3#page=6 "Proposition 4.1 puts no constraints on the data generating distribution.") | 各時点での被覆は保証しない [arxiv-2106.00170#c4](https://arxiv.org/pdf/2106.00170v3#page=8 "On the other hand, it provides no information about the marginal coverage frequency at a single time step.")。毎時点で正解が得られる必要がある [arxiv-2106.00170#c9](https://arxiv.org/pdf/2106.00170v3#page=10 "The methods we develop are speciﬁc to cases where Yt is revealed at each time point.") |

- 分類の予測集合の論文は、別の分布(ImageNet-V2)でも、較正用データがその新しい分布から来ていれば被覆を保つと述べている [arxiv-2009.14193#c7](https://arxiv.org/pdf/2009.14193v5#page=8 "The result shows that our method can still provide coverage even for models trained on different distributions, as long as the conformal calibration set comes from the new distribution.")。裏を返せば、新しい分布の較正用データが要る。
- 入門の論文も、標準の保証はテストデータが較正用データと同じ分布から来ることを前提にしていると明記している [arxiv-2107.07511#c9](https://arxiv.org/pdf/2107.07511v6#page=20 "All previous conformal methods rely on Theorem 1, which assumes that the incoming test points come from the same distribution as the calibration points.")。

既存カードでは、太陽光発電の推定に conformal prediction の変種を使う応用研究もある [doi-10.1109_tsg.2026.3676842#c1](https://edepot.wur.nl/713863#page=2 "To address the arbitrary bin count in CP with MB, the paper proposes a novel CP variant, namely: Adaptive Mondrian Binning (AMB).")。

## 運用への示唆(本記事の整理)

論文の主張そのものではなく、本記事のまとめである。

1. **ノイズの不確実性と、モデルの不確実性(知らない入力)を区別する**: 分散を予測するだけでは、学習データから遠い入力を見分けられない [arxiv-1703.04977#c2](https://arxiv.org/pdf/1703.04977v2#page=4 "This approach does not capture epistemic model uncertainty, as epistemic uncertainty is a property of the model and not of the data.") [arxiv-2006.10562#c1](https://arxiv.org/pdf/2006.10562v4#page=2 "However, such models only capture data uncertainty (Gal, 2016; Malinin, 2019), also known as aleatoric uncertainty, which arises due to inherent class overlap or noise in the data.")。
2. **較正は「同じ分布」でしか効かないと考える**: 分布が変わると較正は崩れる [arxiv-1906.02530#c4](https://arxiv.org/pdf/1906.02530v2#page=7 "Interestingly, while temperature scaling achieves low ECE for low values of shift, the ECE increases signiﬁcantly as the shift increases, which indicates that calibration on the i.i.d. validation dataset does not guarantee calibration under distributional shift.")。本番のデータで定期的に較正し直すことを前提にする。
3. **ECE だけで判断しない**: ビンの数や種類で結論が変わる [arxiv-1904.01685#c7](https://arxiv.org/pdf/1904.01685v2#page=7 "This demonstrates that varying the properties of the calibration error metric can lead to different conclusions about which model has the best calibration.")。適切なスコアリングルールも併せて見る [arxiv-1910.12656#c3](https://arxiv.org/pdf/1910.12656v1#page=4 "Namely, it is easy to obtain almost perfectly calibrated probabilities by predicting the overall class distribution, regardless of the given instance.")。
4. **conformal prediction の保証は「平均」で「同じ分布」**: 個々の入力の保証ではない [arxiv-2107.07511#c4](https://arxiv.org/pdf/2107.07511v6#page=13 "This is a stronger property than the marginal coverage property in (1) that conformal prediction is guaranteed to achieve—indeed, in the most general case, conditional coverage is impossible to achieve [14].")。分布の変化には、重み付けや適応型の方法が要り、それぞれ保証が弱まる [arxiv-2202.13415#c2](https://arxiv.org/pdf/2202.13415v5#page=4 "In particular, if we use these methods, we are implicitly assuming that this weighted sum of total variation terms is small.") [arxiv-2106.00170#c4](https://arxiv.org/pdf/2106.00170v3#page=8 "On the other hand, it provides no information about the marginal coverage frequency at a single time step.")。
5. **較正用データは学習にも較正器の選択にも使わない**: データの使い分けを明記する [arxiv-1909.10155#c4](https://arxiv.org/pdf/1909.10155v2#page=5 "We split the validation set into 3 sets of sizes (20000, 5000, 25000).") [arxiv-1807.00263#c6](https://arxiv.org/pdf/1807.00263v1#page=6 "We didn’t observe signiﬁcant overﬁtting and did not use a distinct calibration set.")。

## わかっていないこと

- **ラベルなしでの較正の維持**: 分布が変わった先でラベルなしに較正を保つ方法は未解決である [arxiv-1909.10155#c9](https://arxiv.org/pdf/1909.10155v2#page=10 "However, can we maintain calibration when we do not have labeled examples from the target dataset?")。
- **cold posterior の原因**: 候補は検討されたが、どれも単独では説明しきれていない [arxiv-2002.02405#c6](https://arxiv.org/pdf/2002.02405v2#page=7 "The cold posterior effect cannot be resolved by using the right scaling of the Normal prior.")。
- **モデル族で較正が違う理由**: 構造の違いが効いているという推測にとどまる [arxiv-2106.07998#c5](https://arxiv.org/pdf/2106.07998v2#page=6 "Given that the best-calibrated families (MLP-Mixer and ViT) are non-convolutional, we speculate that model architecture, and in particular its spatial inductive bias, play an important role.")。
- **実世界での検証**: 不確実性の方法は標準的なデータセットで開発されていて、実世界の問題での検証や標準化された評価手順が欠けている [arxiv-2107.03342#c9](https://arxiv.org/pdf/2107.03342v3#page=32 "However, a clear standardized protocol of tests that should be performed on uncertainty quantiﬁcation methods is still not available.")。

## 現時点での整理

- **不確実性には、データのノイズによるものと、モデルの知識不足によるものがあり、方法によって捉えられる種類が違う** [arxiv-1703.04977#c1](https://arxiv.org/pdf/1703.04977v2#page=1 "This could be for example sensor noise or motion noise, resulting in uncertainty which cannot be reduced even if more data were to be collected.") [arxiv-1703.04977#c2](https://arxiv.org/pdf/1703.04977v2#page=4 "This approach does not capture epistemic model uncertainty, as epistemic uncertainty is a property of the model and not of the data.")。
- **アンサンブルは単純で強いが計算量がかかり、正確なベイズ事後分布は必ずしも良くない** [arxiv-1612.01474#c5](https://arxiv.org/pdf/1612.01474v3#page=9 "The ensemble has M times more parameters than a single network; for memory-constrained applications, the ensemble can be distilled into a simpler model [10, 26].") [arxiv-2002.02405#c1](https://arxiv.org/pdf/2002.02405v2#page=2 "Cold Posteriors: among all temperized posteriors the best posterior predictive performance on holdout data is achieved at temperature T < 1.")。
- **較正の良し悪しは測り方で結論が変わり、分布が変わると崩れる** [arxiv-1904.01685#c7](https://arxiv.org/pdf/1904.01685v2#page=7 "This demonstrates that varying the properties of the calibration error metric can lead to different conclusions about which model has the best calibration.") [arxiv-1909.10155#c3](https://arxiv.org/pdf/1909.10155v2#page=4 "A simple example shows that using binning to estimate the calibration error can severely underestimate the true calibration error.") [arxiv-1906.02530#c4](https://arxiv.org/pdf/1906.02530v2#page=7 "Interestingly, while temperature scaling achieves low ECE for low values of shift, the ECE increases signiﬁcantly as the shift increases, which indicates that calibration on the i.i.d. validation dataset does not guarantee calibration under distributional shift.")。
- **conformal prediction は有限標本の保証を与えるが、それは交換可能性の下での周辺の被覆である** [arxiv-2107.07511#c2](https://arxiv.org/pdf/2107.07511v6#page=50 "As a technical remark, the theorem also holds if the observations to satisfy the weaker condition of exchangeability; see [1].") [arxiv-2107.07511#c4](https://arxiv.org/pdf/2107.07511v6#page=13 "This is a stronger property than the marginal coverage property in (1) that conformal prediction is guaranteed to achieve—indeed, in the most general case, conditional coverage is impossible to achieve [14].")。
- **分布が変わる場合の conformal prediction は、仮定や保証の強さと引き換えに拡張されている** [arxiv-1904.06019#c2](https://arxiv.org/pdf/1904.06019v3#page=4 "Assume that ePX is absolutely continuous with respect to PX") [arxiv-2202.13415#c2](https://arxiv.org/pdf/2202.13415v5#page=4 "In particular, if we use these methods, we are implicitly assuming that this weighted sum of total variation terms is small.") [arxiv-2106.00170#c3](https://arxiv.org/pdf/2106.00170v3#page=6 "Proposition 4.1 puts no constraints on the data generating distribution.")。

**この整理に含まれていないもの**: ガウス過程による不確実性、証拠的深層学習(evidential deep learning)、大規模言語モデルの確信度と較正、ラベルなしでの性能推定([フォールバックの記事](model-fallback-and-selection.md) で扱っている)、分布外検知の個別手法、Platt スケーリングと等張回帰の原典(arXiv にない)。

## 参照カード

- [arxiv-1506.02142](../../papers/arxiv-1506.02142.yaml) Gal & Ghahramani, "Dropout as a Bayesian Approximation: Representing Model Uncertainty in Deep Learning"
- [arxiv-1612.01474](../../papers/arxiv-1612.01474.yaml) Lakshminarayanan, Pritzel & Blundell, "Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles"
- [arxiv-1703.04977](../../papers/arxiv-1703.04977.yaml) Kendall & Gal, "What Uncertainties Do We Need in Bayesian Deep Learning for Computer Vision?"
- [arxiv-2002.02405](../../papers/arxiv-2002.02405.yaml) Wenzel et al., "How Good is the Bayes Posterior in Deep Neural Networks Really?"
- [arxiv-2107.03342](../../papers/arxiv-2107.03342.yaml) Gawlikowski et al., "A Survey of Uncertainty in Deep Neural Networks"
- [arxiv-1706.04599](../../papers/arxiv-1706.04599.yaml) Guo et al., "On Calibration of Modern Neural Networks"
- [arxiv-1904.01685](../../papers/arxiv-1904.01685.yaml) Nixon et al., "Measuring Calibration in Deep Learning"
- [arxiv-1909.10155](../../papers/arxiv-1909.10155.yaml) Kumar, Liang & Ma, "Verified Uncertainty Calibration"
- [arxiv-2106.07998](../../papers/arxiv-2106.07998.yaml) Minderer et al., "Revisiting the Calibration of Modern Neural Networks"
- [arxiv-1910.12656](../../papers/arxiv-1910.12656.yaml) Kull et al., "Beyond temperature scaling: Obtaining well-calibrated multiclass probabilities with Dirichlet calibration"
- [arxiv-1807.00263](../../papers/arxiv-1807.00263.yaml) Kuleshov, Fenner & Ermon, "Accurate Uncertainties for Deep Learning Using Calibrated Regression"
- [arxiv-1906.02530](../../papers/arxiv-1906.02530.yaml) Ovadia et al., "Can You Trust Your Model's Uncertainty? Evaluating Predictive Uncertainty Under Dataset Shift"
- [arxiv-2107.07511](../../papers/arxiv-2107.07511.yaml) Angelopoulos & Bates, "A Gentle Introduction to Conformal Prediction and Distribution-Free Uncertainty Quantification"
- [arxiv-1604.04173](../../papers/arxiv-1604.04173.yaml) Lei et al., "Distribution-Free Predictive Inference For Regression"
- [arxiv-1905.03222](../../papers/arxiv-1905.03222.yaml) Romano, Patterson & Candès, "Conformalized Quantile Regression"
- [arxiv-2009.14193](../../papers/arxiv-2009.14193.yaml) Angelopoulos et al., "Uncertainty Sets for Image Classifiers using Conformal Prediction"
- [arxiv-1904.06019](../../papers/arxiv-1904.06019.yaml) Tibshirani et al., "Conformal Prediction Under Covariate Shift"
- [arxiv-2202.13415](../../papers/arxiv-2202.13415.yaml) Barber et al., "Conformal prediction beyond exchangeability"
- [arxiv-2106.00170](../../papers/arxiv-2106.00170.yaml) Gibbs & Candès, "Adaptive Conformal Inference Under Distribution Shift"
- [arxiv-1910.03225](../../papers/arxiv-1910.03225.yaml) Duan et al., "NGBoost: Natural Gradient Boosting for Probabilistic Prediction"
- [arxiv-2006.10562](../../papers/arxiv-2006.10562.yaml) Malinin, Prokhorenkova & Ustimenko, "Uncertainty in Gradient Boosting via Ensembles"
- [arxiv-1610.01271](../../papers/arxiv-1610.01271.yaml) Athey, Tibshirani & Wager, "Generalized Random Forests"
- [arxiv-1510.04342](../../papers/arxiv-1510.04342.yaml) Wager & Athey, "Estimation and Inference of Heterogeneous Treatment Effects using Random Forests"
- [doi-10.1109_tsg.2026.3676842](../../papers/doi-10.1109_tsg.2026.3676842.yaml) He et al., "Probabilistic Disaggregation of Behind-the-Meter PV Systems Using Conformal Prediction"
