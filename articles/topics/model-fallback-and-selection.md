---
title: 予測モデルのフォールバックとモデル選択 — 運用でモデルを切り替える仕組み
kind: topic
tags: [model-selection, selective-prediction, mlops]
depends_on: [arxiv-1810.03548, arxiv-1210.7959, arxiv-2007.04074, arxiv-1810.01270, arxiv-1802.04967, arxiv-1705.08500, arxiv-1901.09192, arxiv-2006.01862, arxiv-1711.06664, arxiv-1610.02136, arxiv-1706.04599, arxiv-1906.02530, arxiv-2201.04234, arxiv-2107.03315, arxiv-2305.05176, arxiv-2406.18665, arxiv-2404.14618, arxiv-2205.02302, arxiv-2011.09926, arxiv-2007.06299, arxiv-2003.01668, arxiv-1810.11953, arxiv-2004.05785, arxiv-2609.04388]
written_at: 2026-10-04
written_by: claude-opus-5-5 via Claude Code
---

# 予測モデルのフォールバックとモデル選択 — 運用でモデルを切り替える仕組み

<!-- generated:stale -->
> ⚠ この記事の執筆日(2026-10-04)以降に作成された関連カードが 8 件あります(未反映。執筆日と同じ日に作成されたカードを含む): `arxiv-1208.3719`, `arxiv-1603.06212`, `arxiv-1612.01474`, `arxiv-1804.05146`, `arxiv-1911.04706`, `arxiv-2003.06505`, `arxiv-2106.07998`, `arxiv-2107.05847`
<!-- /generated:stale -->

## この記事の読み方

本番で動く予測モデルが信用できなくなったとき、別のモデル(または人)に切り替える仕組みを、ここでは**フォールバック**と呼ぶ。
この記事は、その設計に関わる研究を24本の論文から整理する。問いは4つである。

1. **いつ切り替えるか**: 何を信号にするか(確信度、分布の変化、ラベルなしでの性能推定、ルールによる検査)
2. **何に切り替えるか**: 別のモデル、より安全な既定の方針、より強い(高価な)モデル、人間
3. **どう選ぶか**: 固定の規則、入力ごとの選択、メタ学習器による選択、ルーター
4. **切り替えの仕組み自体をどう評価するか**

### 「メタ学習器」という言葉について

この記事で「メタ学習器」と言うときは、**どのモデルを使うかを、入力やデータの特徴から予測するモデル**を指す(以下の用語の整理は本記事による)。

- 複数モデルの予測を混ぜる2段目のモデル(スタッキング)とは区別する。スタッキングは「切り替える」のではなく「常に混ぜる」方式である。
- 少数のデータで速く適応するための「メタ学習(learning to learn)」とも区別する。ただし、過去のタスクの経験からモデル選択を学ぶという点では重なる [arxiv-1810.03548#c1](https://arxiv.org/pdf/1810.03548v1#page=1 "Meta-learning, or learning to learn, is the science of systematically observing how diﬀerent machine learning approaches perform on a wide range of learning tasks, and then learning from this experience, or meta-data, to learn new tasks much faster than otherwise possible.")。

### 先に結論の一部を

この記事で扱う MLOps の論文4本には、**本番で前のモデルに戻す(ロールバック)、または別のモデルに切り替える(フォールバック)仕組みの記述が見当たらなかった**。カードの notes に、各論文の全文をそれらの語で検索した結果を記録している。書かれているのは、監視・アラート・再学習・本番への昇格までである [arxiv-2205.02302#c4](https://arxiv.org/pdf/2205.02302v3#page=7 "Once a certain threshold is reached, such as detection of low prediction accuracy, the information is forwarded via the feedback loop.") [arxiv-2205.02302#c5](https://arxiv.org/pdf/2205.02302v3#page=8 "Retraining is not only triggered automatically when a statistical threshold is reached; it can also be triggered when new feature data is available, or it can be scheduled periodically.") [arxiv-2205.02302#c6](https://arxiv.org/pdf/2205.02302v3#page=7 "Once the status of a well-performing model is switched from staging to production, it is automatically handed over to the DevOps engineer or ML engineer for model deployment.") [arxiv-2007.06299#c5](https://arxiv.org/pdf/2007.06299v1#page=3 "Drift detection informs the user when the model should be retrained which is especially important in applications where model performance feedback is not readily available.")。
そのためこの記事は、隣接する研究(モデル選択、予測の保留と委譲、性能低下の検知、モデルのルーティング)を組み合わせて、フォールバックの設計で**何がわかっていて、何がわかっていないか**を組み立てる(この構成は本記事の判断)。

## 1. どのモデルを使うかを選ぶ — アルゴリズム選択とメタ学習

### 枠組み

Kotthoff のサーベイは、Rice(1976)の枠組みを紹介している。問題とアルゴリズムの組から性能への対応を学び、それを使って最良のアルゴリズムを選ぶ。問題の特徴量を加えることが、多くの場合この方法を実用的にする決定的な違いだとサーベイは述べる [arxiv-1210.7959#c1](https://arxiv.org/pdf/1210.7959v1#page=1 "The basic model described in the paper is very simple – given a space of problems and a space of algorithms, map each problem-algorithm pair to its performance.")。

Vanschoren のサーベイは、過去のタスクでの経験(メタデータ)を、モデルの評価結果・タスクの性質・過去のモデルの3種類に分けて整理する [arxiv-1810.03548#c1](https://arxiv.org/pdf/1810.03548v1#page=1 "Meta-learning, or learning to learn, is the science of systematically observing how diﬀerent machine learning approaches perform on a wide range of learning tasks, and then learning from this experience, or meta-data, to learn new tasks much faster than otherwise possible.")。

### 単一の選択の危うさと、既定へのフォールバック

アルゴリズム選択の文献には、フォールバックに直接関わる指摘がある。

- **選んだら取り返せない**: 入力ごとに1つのアルゴリズムを選ぶ方式では、選択を誤るとそれを緩和できず、他にもっと良いアルゴリズムがあっても性能の悪いものから抜け出せない [arxiv-1210.7959#c3](https://arxiv.org/pdf/1210.7959v1#page=12 "If an algorithm is chosen that exhibits bad performance on the problem, the system is “stuck” with it and no adjustments are made, even if all other portfolio algorithms would perform much better.")。
- **オフラインの選択は誤りに気づかない**: 事前に選ぶだけの方式は、選んだアルゴリズムを監視しないので、誤りを緩和できず、多くの場合検知すらしない。オンラインで選び直す方式は細かく判断できるが、その分の負荷がかかる [arxiv-1210.7959#c4](https://arxiv.org/pdf/1210.7959v1#page=13 "Purely oﬄine approaches are inherently vulnerable to bad choices.")。
- **選択器は安くなければならない**: 選ぶのに解くより時間がかかるなら、選ぶ意味がない [arxiv-1210.7959#c5](https://arxiv.org/pdf/1210.7959v1#page=15 "Apart from accuracy, one of the main requirements for such a selector is that it is relatively cheap to run – if selecting an algorithm for solving a problem is more expensive than solving the problem, there is no point in doing so.")。
- **既定のアルゴリズムへのフォールバック**: SATzilla のような仕組みでは、特徴量の計算に時間がかかりすぎると予測された場合、そこそこの性能の既定のアルゴリズムを選ぶ [arxiv-1210.7959#c6](https://arxiv.org/pdf/1210.7959v1#page=15 "If the predicted required analysis time is too high, a default algorithm with reasonable performance is chosen and run on the problem.")。

### Auto-sklearn 2.0: 学習した選択器と固定のフォールバック

Auto-sklearn 2.0 は、データセットごとに AutoML の方針(検証の仕方と予算の使い方の組み合わせ)を選ぶ選択器を学習する [arxiv-2007.04074#c2](https://arxiv.org/pdf/2007.04074v3#page=19 "for each pair of AutoML policies, we ﬁt a random forest to predict whether policy πA outperforms policy πB given the current dataset’s meta-features.")。使うメタ特徴量は、データ点の数と特徴量の数の2つだけである [arxiv-2007.04074#c3](https://arxiv.org/pdf/2007.04074v3#page=20 "reliably computed in linear time for every dataset: 1) the number of datapoints and 2) the number of features.")。

この論文は、本記事の主題に最も近い仕組みを持っている。

- **フォールバックの規則**: 選択器が学習時の範囲の外を外挿できる保証はない。そこで、新しいデータセットの2つのメタ特徴量が、どの学習用データセットよりも大きい場合には、最も安い方針に切り替える。このフォールバックは学習したものではなく、固定の規則である [arxiv-2007.04074#c4](https://arxiv.org/pdf/2007.04074v3#page=20 "Since there is no guarantee that our model-based policy selector will extrapolate well to datasets outside of the meta-datasets, we implement a fallback measure to avoid failures.")。
- **フォールバックの効果**: フォールバックを外すと、どの選択の方式でも性能が下がった。著者はこれを、選択器が外挿できない少数の巨大なデータセットで主に説明できるとし、実行中に方針を切り替える適応的なフォールバックの研究を提案している [arxiv-2007.04074#c5](https://arxiv.org/pdf/2007.04074v3#page=23 "The rather stark performance degradation compared to the regular model-based policy selector can mainly be explained by a few, huge datasets, to which the model-based policy selector cannot extrapolate (and which the single best does not account for).")。
- **保証の範囲**: ポートフォリオの貪欲な構成には近似の保証があるが、それは学習用のデータセットの上でのものである。新しいデータセットについては、同じ分布から来るという仮定のもとで良い既定値になる、と述べるにとどまる [arxiv-2007.04074#c1](https://arxiv.org/pdf/2007.04074v3#page=9 "Under the assumption that we apply the portfolio to datasets from the same distribution of datasets, we have a strong set of default ML pipelines.")。

つまり、**学習した選択器が範囲外の入力で誤りうることを前提に、固定の規則で安全側に倒す**という二段構えになっている(この読みは本記事による)。評価は、学習用と重ならない39のデータセットで、どの方針が最良だったかを知っている「オラクル」とも比べている [arxiv-2007.04074#c6](https://arxiv.org/pdf/2007.04074v3#page=13 "Finally, we manually checked for overlap with Dtest and ended up with a total of 208 training datasets and used them to train our method.")。
限界として、予算・指標・設定空間が固定であること、メタ特徴量が2つで十分かは未解決であること、学習用のメタデータの構築に費用がかかることが挙げられている [arxiv-2007.04074#c7](https://arxiv.org/pdf/2007.04074v3#page=33 "However, our system also introduces some shortcomings since it optimizes performance towards a given optimization budget, performance metric and conﬁguration space.")。

### メタ特徴量とタスクの類似性の限界

- 過去のタスクが似ているほどメタデータを活かせるが、新しいタスクが無関係なら過去の経験は役に立たない。タスクの類似性をどう定義するかが大きな課題とされる [arxiv-1810.03548#c2](https://arxiv.org/pdf/1810.03548v1#page=1 "When a new task represents completely unrelated phenomena, or random noise, leveraging prior experience will not be eﬀective.")。
- 最適なメタ特徴量の組は用途によって変わる(先行研究の引用) [arxiv-1810.03548#c4](https://arxiv.org/pdf/1810.03548v1#page=8 "Studies on OpenML meta-data have shown that the optimal set of meta-features depends on the application (Bilalli et al., 2017).")。
- 最終的には、メタ特徴量の類似性に頼るより、新しいタスクで実際に評価を集める方が効果的だとサーベイは述べる(先行研究の引用) [arxiv-1810.03548#c6](https://arxiv.org/pdf/1810.03548v1#page=11 "While meta-features could also be used to combine per-task predictions based on task similarity, it is ultimately more eﬀective to gather new observations Pi,new, since these allow to reﬁne the task similarity estimates with every new observation")。
- 学習に使う問題の標本が代表的でなかったり、特徴量が問題の種類を区別できなかったりすると、良い選択の対応はほとんど望めない(Rice の議論の紹介) [arxiv-1210.7959#c2](https://arxiv.org/pdf/1210.7959v1#page=4 "If the sample is not representative, or the features do not facilitate a good separation of the problem classes in the feature space, there is little hope of ﬁnding the best or even a good selection mapping.")。

### 入力ごとの動的な選択(Dynamic Ensemble Selection)

入力ごとに「その近くで得意なモデル」を選ぶ方式もある。

- 各モデルはそれぞれ特徴空間の異なる局所領域の専門家である、という前提に立つ [arxiv-1802.04967#c1](https://arxiv.org/pdf/1802.04967v3#page=1 "The rationale for such techniques is that not every classiﬁer in the pool is an expert in classifying all unknown samples; rather, each base classiﬁer is an expert in a different local region of the feature space.")。最も有能な1つを選ぶ方式と、一定以上の有能さを持つものをすべて選ぶ方式がある [arxiv-1802.04967#c3](https://arxiv.org/pdf/1802.04967v3#page=3 "All base classiﬁers that attain a minimum competence level are selected to compose the ensemble of classiﬁers.")。
- META-DES は、入力の近傍などから作るメタ特徴量で、各モデルがその入力に有能かを予測するメタ分類器を学習する [arxiv-1810.01270#c1](https://arxiv.org/pdf/1810.01270v1#page=1 "The meta-features are extracted from the training data and used to train a meta-classiﬁer to predict whether or not a base classiﬁer is competent enough to classify an input instance.") [arxiv-1810.01270#c2](https://arxiv.org/pdf/1810.01270v1#page=13 "Three meta-features, f1, f2 and f3, are computed using information extracted from the region of competence θj.")。
- **分布の変化への弱さ**: 局所的な正解率で有能さを測る方法は、検証データとテストデータの分布の違いで性能が下がりうる、と著者は述べる [arxiv-1810.01270#c3](https://arxiv.org/pdf/1810.01270v1#page=6 "Moreover, any difference between the distribution of validation and test datasets may negatively affect the system performance.")。META-DES 自身の評価は、同じデータセットの無作為な分割で行われており、分布の変化はない [arxiv-1810.01270#c4](https://arxiv.org/pdf/1810.01270v1#page=16 "The experiments were conducted using 20 replications.")。
- **評価の条件**: ハイパーパラメータは30のデータセットのうち11を使って決め、その11は比較の対象にも含まれる [arxiv-1810.01270#c5](https://arxiv.org/pdf/1810.01270v1#page=19 "Only a subset with eleven of the thirty datasets are used for parameters setting procedure: Pima, Liver, Breast, Blood Transfusion, Banana, Vehicle, Lithuanian, Sonar, Ionosphere, Wine, Haberman’s Survival.")。比較手法の設定は以前の論文の値で、この論文での再調整は記述されていない [arxiv-1810.01270#c6](https://arxiv.org/pdf/1810.01270v1#page=21 "For all techniques, the pool of classiﬁers C is composed of 100 Perceptrons as base classiﬁer (M = 100).")。

## 2. 予測を控える・人に委ねる

フォールバックの最も基本的な形は、**このモデルでは予測しない**と判断することである。その先は、既定の方針、別のモデル、人間のいずれでもよい。

### 選択的分類: 予測を控えてリスクを抑える

- Geifman & El-Yaniv は、学習済みのモデルの確信度にしきい値を設けて予測を控え、利用者が指定したリスク(誤り率)を高い確率で保証する方法を示した [arxiv-1705.08500#c1](https://arxiv.org/pdf/1705.08500v2#page=1 "At test time, the classiﬁer rejects instances as needed, to grant the desired risk (with high probability).") [arxiv-1705.08500#c2](https://arxiv.org/pdf/1705.08500v2#page=2 "To this end, we consider the above two known techniques for rejection (SR and MC-dropout), and devise a learning method that chooses an appropriate threshold that ensures the desired risk.")。
  - **保証の仮定**: しきい値を決めるラベル付きデータが、本番と同じ分布から独立に取られていること。損失は0/1の誤りである [arxiv-1705.08500#c3](https://arxiv.org/pdf/1705.08500v2#page=5 "Theorem 3.2 (SGR) Let Sm be a given labeled set, sampled i.i.d. from P, and consider an application of the SGR procedure.")。
  - **確信度の質**: 保証自体は常に成り立つが、確信度が大きく歪んでいると、得られる上界は目標のリスクから遠くなる [arxiv-1705.08500#c4](https://arxiv.org/pdf/1705.08500v2#page=6 "While Theorem 3.2 always holds, we note that if κf is severely skewed (far from ideal), the bound of the resulting selective classiﬁer can be far from the target risk.")。
  - **評価の条件**: テストは同じ検証データの無作為な半分で、分布の変化はない [arxiv-1705.08500#c6](https://arxiv.org/pdf/1705.08500v2#page=8 "The other half, which was not consumed by SGR for training, was reserved for testing the resulting bounds.")。
- SelectiveNet は、予測と「控えるかどうか」を同時に学習する [arxiv-1901.09192#c1](https://arxiv.org/pdf/1901.09192v4#page=1 "In contrast, SelectiveNet is trained to optimize both classiﬁcation (or regression) and rejection simultaneously") [arxiv-1901.09192#c2](https://arxiv.org/pdf/1901.09192v4#page=3 "At inference time, a sample x is fed to SelectiveNet, which predicts f(x) if and only if g(x) ≥0.5; otherwise, SelectiveNet abstains from predicting the label of x.")。
  - **保証の範囲**: 事後の較正で得られる保証は「どれだけの割合を予測するか(カバレッジ)」についてのもので、リスクについてではない [arxiv-1901.09192#c4](https://arxiv.org/pdf/1901.09192v4#page=4 "This goal can be achieved easily using the following simple post-training coverage calibration technique, which relies on an independent unlabeled validation set Vn containing n samples.")。
  - 学習時に目標のカバレッジを指定しても、テストではその目標から外れた [arxiv-1901.09192#c3](https://arxiv.org/pdf/1901.09192v4#page=4 "Clearly, both SR and SelectiveNet violate the target coverage rate in all cases.")。

### Learning to defer: 人や別のモデルに委ねる

- Madras et al. は、予測を控えるだけでなく、**委ねた先の意思決定者(人間や外部のモデル)の性質**を考えて学習する枠組みを示した。予測を控える学習は、意思決定者の損失が一定である特別な場合にあたる [arxiv-1711.06664#c1](https://arxiv.org/pdf/1711.06664v3#page=1 "We extend this concept by proposing learning to defer, which generalizes rejection learning by considering the eﬀect of other agents in the decision-making process.") [arxiv-1711.06664#c2](https://arxiv.org/pdf/1711.06664v3#page=5 "The proof in Sec. 2.3 shows the central point of learning to defer: rejection learning is exactly a special case of learning to defer: a DM with constant loss α on each example.")。委ねるかどうかは、入力ごとに意思決定者の得意不得意を考えて決められる [arxiv-1711.06664#c3](https://arxiv.org/pdf/1711.06664v3#page=6 "This is advantageous because a DM’s actions may depend heterogenously on the data: the DM’s expected loss may change as a function of X, and it may do so diﬀerently than the model’s.")。
  - 意思決定者は、追加の情報を持つ別の分類器としてシミュレーションしたものである [arxiv-1711.06664#c4](https://arxiv.org/pdf/1711.06664v3#page=8 "Due to diﬃculty obtaining and evaluating real-life decision-making data, we use “semi-synthetic data”: real datasets, and simulated DM data by training a separate classiﬁer under slightly diﬀerent conditions (see Experiment Details).")。
  - 学習時と異なる意思決定者への汎化は、先行研究を根拠に示唆されているだけで、検証されていない [arxiv-1711.06664#c7](https://arxiv.org/pdf/1711.06664v3#page=5 "Research suggests that common trends exist in DM behavior [6, 11], suggesting that a model trained on some DM could generalize to unseen DMs.")。
  - 事後的な変種のしきい値は、テストデータの半分で選び、残りの半分で評価している [arxiv-1711.06664#c6](https://arxiv.org/pdf/1711.06664v3#page=17 "We sampled 1000 combinations of thresholds, picked the thresholds which minimized the loss on one half of the test set, and evaluated these thresholds on the other half of the test set.")。
- Mozannar & Sontag は、予測するか専門家に委ねるかを学ぶ損失関数を示し [arxiv-2006.01862#c1](https://arxiv.org/pdf/2006.01862v3#page=1 "Our approach is based on a novel reduction to cost sensitive learning where we give a consistent surrogate loss for cost sensitive learning that generalizes the cross entropy loss.")、その最小化が理想的な委ね方(専門家が正しい確率が自分の確信度以上なら委ねる)に一致することを示した。ただしこれは、全ての可測関数の中での、母集団レベルの保証である [arxiv-2006.01862#c2](https://arxiv.org/pdf/2006.01862v3#page=5 "The proposed surrogate LCE is in fact consistent and upper bounds L0−1 as the following theorem demonstrates.")。著者自身、実際に使う限られたモデルの中では、この保証はあまり多くを保証しないかもしれないと注意している [arxiv-2006.01862#c3](https://arxiv.org/pdf/2006.01862v3#page=8 "So far we have focused on classiﬁcation consistency to verify the soundness of proposed approaches, however, we usually have speciﬁc hypothesis classes H, R in mind, and if the Bayes predictor is not in our class then consistency might not guarantee much [BDLSS12].")。
  - 専門家は、すべての実験でシミュレーションされたものである [arxiv-2006.01862#c5](https://arxiv.org/pdf/2006.01862v3#page=11 "We simulate multiple synthetic experts of varying competence in the following way: let k ∈[10], then if the image belongs to the ﬁrst k classes the expert predicts perfectly, otherwise the expert predicts uniformly over all classes.")。
  - Mozannar & Sontag が実装した、Madras et al. の方式の多クラス版は、CIFAR-10 の実験で「全く委ねない」ように学習してしまった。これは Mozannar & Sontag による結果である [arxiv-2006.01862#c4](https://arxiv.org/pdf/2006.01862v3#page=12 "the mixtures of experts loss of [MPZ18] fails in this setup and learns never to defer.")。
  - 入力の一部を消す実験では、どの方法も性能が下がった [arxiv-2006.01862#c7](https://arxiv.org/pdf/2006.01862v3#page=19 "In the second experiment, we train with the original chest X-rays but evaluate with noisy X-rays with noise in the form of erasing a randomly placed rectangular region of the X-ray.")。

**フォールバックへの示唆**(本記事の整理): 委ねる先の性質を考えずに自分の確信度だけで決めると、組み合わせた全体の性能や公平性が改善しないことがある [arxiv-2006.01862#c6](https://arxiv.org/pdf/2006.01862v3#page=14 "While our method does not achieve signiﬁcantly lower discrimination than the baseline")。フォールバック先が何を得意とするかを、切り替えの判断に入れる必要がある。

## 3. 切り替えの引き金は信用できるか

正解ラベルは本番ではすぐには手に入らないことが多い [arxiv-2007.06299#c2](https://arxiv.org/pdf/2007.06299v1#page=1 "In the absence of labels it is critical to monitor the statistics of input data and output predictions as these can serve as a proxy for model performance (Breck et al., 2017).")。そのため切り替えの引き金は、確信度、入力の分布の変化、ラベルなしでの性能推定、ルールによる検査などに頼ることになる。

### 確信度

- 最大のソフトマックス確率は、誤分類や分布外の入力で低くなる傾向があり、検知の基準(ベースライン)になる [arxiv-1610.02136#c1](https://arxiv.org/pdf/1610.02136v3#page=1 "Correctly classiﬁed examples tend to have greater maximum softmax probabilities than erroneously classiﬁed and out-of-distribution examples, allowing for their detection.")。ただし、その値そのものは確信度とよく対応しない。役に立つのは順位づけとしてである [arxiv-1610.02136#c2](https://arxiv.org/pdf/1610.02136v3#page=1 "Throughout our experiments we establish that the prediction probability from a softmax distribution has a poor direct correspondence to conﬁdence.")。分布の変化が正解率をわずかにしか下げない場合、この信号は分布外の入力の検知に役立たなかった [arxiv-1610.02136#c5](https://arxiv.org/pdf/1610.02136v3#page=8 "Because the classiﬁcation degradation was only slight, the softmax statistics alone did not provide useful out-of-distribution detection.")。
- 現代のニューラルネットは較正が悪い(確信度が正解の確率と合わない) [arxiv-1706.04599#c1](https://arxiv.org/pdf/1706.04599v2#page=1 "We discover that modern neural networks, unlike those from a decade ago, are poorly calibrated.")。温度スケーリングで改善できるが [arxiv-1706.04599#c3](https://arxiv.org/pdf/1706.04599v2#page=6 "In other words, temperature scaling does not affect the model’s accuracy.")、この論文の評価は、学習・検証・テストが同じ分布という仮定のもとでのものである [arxiv-1706.04599#c4](https://arxiv.org/pdf/1706.04599v2#page=4 "We assume that the training, validation, and test sets are drawn from the same distribution.")。
- **分布が変わると較正は崩れる**: Ovadia et al. は、同じ分布の検証データで較正しても、分布の変化が大きくなるにつれて較正誤差が大きく増えることを示した [arxiv-1906.02530#c4](https://arxiv.org/pdf/1906.02530v2#page=7 "Interestingly, while temperature scaling achieves low ECE for low values of shift, the ECE increases signiﬁcantly as the shift increases, which indicates that calibration on the i.i.d. validation dataset does not guarantee calibration under distributional shift.")。広告クリックのデータでは、温度スケーリングが較正をかえって悪くした [arxiv-1906.02530#c5](https://arxiv.org/pdf/1906.02530v2#page=9 "Strikingly, temperature scaling has a worse Brier score than Vanilla indicating that post-hoc calibration on the validation set actually harms calibration under dataset shift.")。分布の変化とともに、正解率だけでなく不確実性の質も、試した全ての方法で下がった [arxiv-1906.02530#c6](https://arxiv.org/pdf/1906.02530v2#page=9 "Along with accuracy, the quality of uncertainty consistently degrades with increasing dataset shift regardless of method.")。

**フォールバックへの示唆**(本記事の整理): 選択的分類のリスクの保証は、同じ分布のデータで決めたしきい値を前提にしている [arxiv-1705.08500#c3](https://arxiv.org/pdf/1705.08500v2#page=5 "Theorem 3.2 (SGR) Let Sm be a given labeled set, sampled i.i.d. from P, and consider an application of the SGR procedure.")。分布が変わる本番では、確信度にもとづく「控える」判断の信頼性も下がりうる [arxiv-1906.02530#c4](https://arxiv.org/pdf/1906.02530v2#page=7 "Interestingly, while temperature scaling achieves low ECE for low values of shift, the ECE increases signiﬁcantly as the shift increases, which indicates that calibration on the i.i.d. validation dataset does not guarantee calibration under distributional shift.")。フォールバックが最も必要な場面で、引き金が最も信用できなくなるおそれがある。

### ラベルなしでの性能推定

- Garg et al. の ATC は、ラベルのない本番データで、確信度があるしきい値を超える割合から正解率を推定する [arxiv-2201.04234#c1](https://arxiv.org/pdf/2201.04234v3#page=1 "We propose Average Thresholded Conﬁdence (ATC), a practical method that learns a threshold on the model’s conﬁdence, predicting accuracy as the fraction of unlabeled examples for which model conﬁdence exceeds that threshold.") [arxiv-2201.04234#c2](https://arxiv.org/pdf/2201.04234v3#page=2 "ATC selects a threshold on validation source data such that the fraction of source examples that receive the score above the threshold match the accuracy of those examples.")。
  - **不可能性**: 分類器に仮定を置かなければ、**あらゆる種類の分布の変化に対して正解率を推定できる方法はない**ことを示した [arxiv-2201.04234#c3](https://arxiv.org/pdf/2201.04234v3#page=5 "Corollary 1. Absent assumptions on the classiﬁer f, no method of estimating accuracy will work in all scenarios, i.e., for different nature of distribution shifts.")。ATC も、ある種類の変化では必ず失敗する [arxiv-2201.04234#c4](https://arxiv.org/pdf/2201.04234v3#page=3 "Finally, we note that although ATC achieves superior performance in our empirical evaluation, like all methods, it must fail (returns inconsistent estimates) on certain types of distribution shifts, per our impossibility result.")。
  - 新しい部分集団が現れる変化では、全ての方法で推定誤差が大きかった [arxiv-2201.04234#c6](https://arxiv.org/pdf/2201.04234v3#page=8 "While we observe a small MAE (i.e., comparable to our observations on other datasets) on BREEDS with natural and synthetic shifts from the same sub-population, MAE on shifts with novel population is signiﬁcantly higher with all methods.")。
- Guillory et al. の DoC は、元のデータと本番データの平均確信度の差を使う [arxiv-2107.03315#c1](https://arxiv.org/pdf/2107.03315v2#page=4 "We propose difference of conﬁdences DoC as a way to quantify distribution shifts:")。一部の人工的な変化では推定がかえって悪くなり [arxiv-2107.03315#c4](https://arxiv.org/pdf/2107.03315v2#page=7 "While DoC improves upon the AC baseline for each form of natural distribution shift, we note that in 2 of the 8 synthetic shifts explored (Defocus Blur and Gaussian Blur) DoC actually decreases the accuracy of the predictions.")、敵対的に集めたデータでは全ての方法で誤差が最も大きかった [arxiv-2107.03315#c6](https://arxiv.org/pdf/2107.03315v2#page=7 "In Figure 7, we observe that this distribution shift produces the highest predicted accuracy error of shifts we have studied across all approaches.")。著者は、この問題は解決にはほど遠いと述べる [arxiv-2107.03315#c7](https://arxiv.org/pdf/2107.03315v2#page=8 "While our results present a promising step forward for detecting performance drop under distribution shift, we note that the problem is far from solved.")。
  - Garg et al. は、DoC の回帰の方式が、未知の変化が既知の変化と強く線形に相関していることに依存すると指摘し、自分たちの設定で再評価した。これは Garg et al. による評価である [arxiv-2201.04234#c7](https://arxiv.org/pdf/2201.04234v3#page=2 "methods that leverage labeled data from target domains rely on the fact that unseen target domains exhibit strong linear correlation with seen target domains on the underlying distance measure")。

### 分布の変化の検知

- Rabanser et al. は、実際の ML パイプラインで入ってくるデータの分布の変化が調べられることはまれだと述べる [arxiv-1810.11953#c8](https://arxiv.org/pdf/1810.11953v4#page=1 "in practice, ML pipelines rarely inspect incoming data for signs of distribution shift.")。また、検知された変化が必ずしも有害とは限らない(画像のデータで、検知された変化が分類器の性能を下げなかった例) [arxiv-1810.11953#c13](https://arxiv.org/pdf/1810.11953v4#page=9 "this shift does not harm the classifier's performance")。
- 概念ドリフトのレビューは、多くの検知・適応の方法が、予測の直後に正解ラベルが手に入ることを仮定していると指摘する [arxiv-2004.05785#c11](https://arxiv.org/pdf/2004.05785v1#page=14 "Most existing drift detection and adaptation algorithms assume the ground true label is available after classification/prediction, or extreme verification latency.")。

**フォールバックへの示唆**(本記事の整理): 分布の変化の検知は「変わった」ことを知らせるが、「性能が落ちた」ことを意味するとは限らない [arxiv-1810.11953#c13](https://arxiv.org/pdf/1810.11953v4#page=9 "this shift does not harm the classifier's performance")。検知だけを引き金にすると、不要な切り替えが起きうる。

### ルールによる検査とアラート

- Model Assertions は、入力と出力に対する利用者定義の関数で誤りの兆候を検出する [arxiv-2003.01668#c1](https://arxiv.org/pdf/2003.01668v3#page=1 "Model assertions are arbitrary functions over a model’s input and output that indicate when errors may be occurring, e.g., a function that triggers if an object rapidly changes its class in a video.")。確信度にもとづく監視では捕まらない、確信度の高い誤りを見つけたと著者は述べる [arxiv-2003.01668#c5](https://arxiv.org/pdf/2003.01668v3#page=8 "Importantly, uncertainty-based methods of monitoring would not catch these errors.")。
  - 実行時に自動で是正措置(例: 自動操縦の停止)を起こせると述べるが、そうした実行時の措置を試した実験は見当たらない [arxiv-2003.01668#c2](https://arxiv.org/pdf/2003.01668v3#page=2 "First, we show that model assertions can be used for runtime monitoring: they can be used to log unexpected behavior or automatically trigger corrective actions, e.g., shutting down an autopilot.")。
  - 報告しているのは、検出した点のうちの正解の割合(精度)だけで、見逃しの割合は見当たらない [arxiv-2003.01668#c4](https://arxiv.org/pdf/2003.01668v3#page=8 "To test this, we randomly sampled 50 data points that triggered each assertion and manually checked whether that data point had an incorrect output from the ML model.")。
- Klaise et al. は、アラートのしきい値の設定には分野の知識が必要で、誤報を抑えるように設定するのは難しいと述べる [arxiv-2007.06299#c3](https://arxiv.org/pdf/2007.06299v1#page=2 "Such thresholds require domain knowledge and can be difﬁcult to set appropriately to limit the number of false alarms.")。外れ値として検出された予測は、本番で信用すべきでないとしている [arxiv-2007.06299#c4](https://arxiv.org/pdf/2007.06299v1#page=2 "Outlier detection is therefore key to ﬂag anomalies whose model predictions we cannot trust and should not use in a production setting.")。ラベルに依存しない監視の指標を、モデルの性能に直接結びつけることは未解決とされる [arxiv-2007.06299#c6](https://arxiv.org/pdf/2007.06299v1#page=4 "One of the main open research topics is to more directly relate the label-independent measures obtained from the metrics, outlier and drift detectors to the model performance.")。

## 4. カスケードとルーティング — 安いモデルと強いモデルの切り替え

LLM の分野では、問い合わせごとに安いモデルと強い(高価な)モデルを切り替える研究が活発である。フォールバックを「上位のモデルに回す」方向で考えると、同じ構造になる(この対応づけは本記事による)。

| 研究 | 切り替えの判断 | 判断の時点 | 「コスト」の定義 |
|---|---|---|---|
| FrugalGPT | 安いモデルの回答を、学習した採点器で評価し、しきい値を下回れば次のモデルを呼ぶ [arxiv-2305.05176#c1](https://arxiv.org/pdf/2305.05176v1#page=5 "The scoring function can be obtained by training a simple regression model that learns whether a generation is correct from the query and a generated answer.") | 回答の**後** | API の価格表(2023年3月時点)から計算した金額 [arxiv-2305.05176#c3](https://arxiv.org/pdf/2305.05176v1#page=6 "We have selected 12 LLM APIs from 5 mainstream providers, namely, OpenAI [Ope], AI21 [AI2], CoHere [CoH], Textsynth [Tex], and ForeFrontAI [FFA].") |
| RouteLLM | 強いモデルが勝つ確率を予測し、しきい値以上なら強いモデルに送る [arxiv-2406.18665#c1](https://arxiv.org/pdf/2406.18665v4#page=3 "The threshold α controls the trade-off between quality and cost: a higher value of α enforces stricter cost constraints by favoring weak models more often, while a lower α biases toward higher-quality (but more expensive) strong models.") | 呼び出しの**前** | 強いモデルを呼んだ割合 [arxiv-2406.18665#c3](https://arxiv.org/pdf/2406.18665v4#page=4 "For each ci, we determine the threshold αi that satisfies the cost constraint.") |
| Hybrid LLM | 小さいモデルの品質が大きいモデルに近いと予測されれば小さいモデルに送る [arxiv-2404.14618#c2](https://arxiv.org/pdf/2404.14618v1#page=6 "At test time we achieve the desired performance accuracy tradeoff by tuning a threshold on the score and routing queries with score above the threshold to the small model.") | 呼び出しの**前** | 小さいモデルに送った割合 [arxiv-2404.14618#c3](https://arxiv.org/pdf/2404.14618v1#page=9 "We use BART score [Yuan et al., 2021] as the quality metric and use fraction of queries routed to the small model (cost advantage) as the efficiency metric (see Section 2.3).") |

論文によって「コスト」の定義が異なるので、数値をそのまま比べることはできない(この注意は本記事による)。

### 学習した切り替え器は、分布が変わると働くか

- RouteLLM の切り替え器は、Chatbot Arena の投票データだけで学習すると、MMLU ではランダムな切り替えと同程度で、著者はこれを質問の多くが学習データの分布の外にあるためだとしている。少量の対象分野のデータを足すと改善した [arxiv-2406.18665#c5](https://arxiv.org/pdf/2406.18665v4#page=8 "On MMLU (Table 2), all routers perform poorly at the level of the random router when trained only on Arena dataset, which we attribute to most MMLU questions being out-of-distribution (see Section 5.3).")。未知のモデルの組への転用は、MT Bench でだけ示されている [arxiv-2406.18665#c6](https://arxiv.org/pdf/2406.18665v4#page=8 "Importantly, we use the same routers as before without any retraining, and only replace the strong and weak model routed to.")。
- Hybrid LLM の切り替え器は、新しいモデルの組の品質差が学習時の組と強く相関しているときにだけ、うまく転用できた [arxiv-2404.14618#c6](https://arxiv.org/pdf/2404.14618v1#page=14 "Similar to our observation in Section 4.6, our routers can generalize well if the quality gaps of testing LLM pairs exhibit strong positive correlation with the quality gaps of the training pairs.")。2つのモデルの差が大きいと、学習の信号が弱くなり、ランダムとほとんど変わらなかった [arxiv-2404.14618#c4](https://arxiv.org/pdf/2404.14618v1#page=8 "Because q(S(x)) << q(L(x)) for most queries in this case, it provides an extremely weak signal for training using Equation (2) and as shown in Section 4 both rdet and rprob fail to provide much improvement over random query assignment in this case.")。
- 3本とも限界として、学習と評価で分布が同じであること、または本番の分布が評価と大きく異なりうることを挙げている [arxiv-2305.05176#c7](https://arxiv.org/pdf/2305.05176v1#page=10 "And in order for the cascade to work well, the training examples should be from the same or similar distribution as the test examples.") [arxiv-2406.18665#c7](https://arxiv.org/pdf/2406.18665v4#page=10 "First, although we evaluate on a diverse set of benchmarks, real-world applications may have distributions that differ substantially from these benchmarks.") [arxiv-2404.14618#c7](https://arxiv.org/pdf/2404.14618v1#page=15 "In this work, the model pair and data distribution is fixed across training and testing.")。FrugalGPT の評価は無作為な分割だけで、しきい値は学習用の分割で決めている [arxiv-2305.05176#c4](https://arxiv.org/pdf/2305.05176v1#page=6 "Each dataset is randomly split into a training set to learn the LLM cascade and a test set for evaluation.")。

### 切り替えの仕組み自体の失敗

- FrugalGPT は、全てのモデルが同じ答えを出す場合でも、最初のモデルが正しいか確信できず、全てのモデルを呼んでしまうことがある。著者はこれを未解決の問題としている [arxiv-2305.05176#c6](https://arxiv.org/pdf/2305.05176v1#page=10 "However, FrugalGPT is unsure if the ﬁrst LLMs are correct, resulting in the need to query all LLMs in the chain.")。
- RouteLLM は、同じデータで学習した異なる切り替え器の性能が、はっきりした理由なく大きく異なることを限界に挙げる [arxiv-2406.18665#c7](https://arxiv.org/pdf/2406.18665v4#page=10 "First, although we evaluate on a diverse set of benchmarks, real-world applications may have distributions that differ substantially from these benchmarks.")。

## 5. 運用の中でのモデルの入れ替え

### MLOps の文献が書いていること

- Kreuzberger et al. は、MLOps の構成要素として監視を挙げ [arxiv-2205.02302#c3](https://arxiv.org/pdf/2205.02302v3#page=4 "The monitoring component takes care of the continuous monitoring of the model serving performance (e.g., prediction accuracy).")、しきい値を超えたら上流にフィードバックし [arxiv-2205.02302#c4](https://arxiv.org/pdf/2205.02302v3#page=7 "Once a certain threshold is reached, such as detection of low prediction accuracy, the information is forwarded via the feedback loop.")、ドリフトや新しいデータ、定期的な予定で再学習を起動し [arxiv-2205.02302#c5](https://arxiv.org/pdf/2205.02302v3#page=8 "Retraining is not only triggered automatically when a statistical threshold is reached; it can also be triggered when new feature data is available, or it can be scheduled periodically.")、モデル登録簿で検証段階から本番に昇格させる流れを示した [arxiv-2205.02302#c6](https://arxiv.org/pdf/2205.02302v3#page=7 "Once the status of a well-performing model is switched from staging to production, it is automatically handed over to the DevOps engineer or ML engineer for model deployment.")。根拠は、文献レビュー・ツールの調査・8人の専門家へのインタビューである [arxiv-2205.02302#c1](https://arxiv.org/pdf/2205.02302v3#page=2 "In total, we conduct eight interviews with experts (α - θ), whose details are depicted in Table 2 of the Appendix.")。
- Paleyes et al. は、監視すべき指標とアラートの起動の仕方の理解はまだ初期段階だとする文献を引用し [arxiv-2011.09926#c3](https://arxiv.org/pdf/2011.09926v3#page=13 "Monitoring of evolving input data, prediction bias and overall performance of ML models is an open problem.")、モデルの更新が利用者や下流のシステムに害を与えうる(後方互換性のない更新など)ことを指摘する(先行研究の引用) [arxiv-2011.09926#c6](https://arxiv.org/pdf/2011.09926v3#page=14 "While updating is necessary for keeping a model up to date with recent ﬂuctuations in the data, it may also inﬂict damage on users or downstream systems because of the changes in the model’s behavior, even without causing obvious software errors.")。事例では、監視の仕組みを一から作る必要があった [arxiv-2011.09926#c5](https://arxiv.org/pdf/2011.09926v3#page=13 "However, the authors explain that they had to build all these checks from scratch in order to maintain good model performance.")。
- 冒頭で述べたとおり、これらの論文に、本番での前のモデルへの切り戻しや、別のモデルへの切り替えの記述は見当たらない(カードの notes の検索結果)。

### 「ドリフトを検知した」と「モデルを入れ替えるべき」は別

Fernández-Barrios et al. は、侵入検知の適応的なシステムで、**ドリフトの警報は変化を検知するが、再学習した挑戦者のモデルが本番のモデルを置き換えるべきことまでは示さない**として、検知と昇格を分けて扱った [arxiv-2609.04388#c1](https://arxiv.org/pdf/2609.04388v1#page=1 "Adaptive network intrusion detection systems retrain classifiers after drift alarms, but an alarm detects change; it does not establish that a challenger should replace the deployed incumbent.")。
前処理を本番のモデル側に固定したまま比べると、昇格の害が見かけ上大きくなったと報告している [arxiv-2609.04388#c2](https://arxiv.org/pdf/2609.04388v1#page=1 "Incumbent-owned frozen preprocessing amplified apparent promotion harm; with self-contained challenger pipelines the mean full-drift harm did not persist.")。検知器のしきい値は昇格の前の期間のデータで決め、連続した警報と待ち時間を条件にしている [arxiv-2609.04388#c3](https://arxiv.org/pdf/2609.04388v1#page=8 "thresholds are the 0.95 quantile of detector scores over 30 pre-drift calibration windows; the trigger is 3 consecutive alarms with a 10-window cooldown; windows contain 128 flows.")。比較に使った検知器は調整しておらず、結果はその設定についてのものだと注意している [arxiv-2609.04388#c5](https://arxiv.org/pdf/2609.04388v1#page=24 "DDM and ADWIN were run at their registered reference parameters and were not tuned; their cells characterize that configuration, and a parameter sweep would be required before reading them as properties of the methods.")。

概念ドリフトのレビューは、明示的なドリフト検知による再学習の研究は減速し、適応的なモデルやアンサンブルが重要になってきたと述べる [arxiv-2004.05785#c14](https://arxiv.org/pdf/2004.05785v1#page=14 "research of retraining models with explicit drift detection has slowed;")。

## フォールバック設計への示唆

以下は、上の論文の記述を組み合わせた本記事の整理であり、フォールバックの設計を直接評価した研究の結論ではない。

| 設計上の問い | 関係する知見 |
|---|---|
| 学習した選択器が範囲外の入力で誤ったらどうするか | 固定の規則で安全側に倒す例がある [arxiv-2007.04074#c4](https://arxiv.org/pdf/2007.04074v3#page=20 "Since there is no guarantee that our model-based policy selector will extrapolate well to datasets outside of the meta-datasets, we implement a fallback measure to avoid failures.")。外すと性能が下がった [arxiv-2007.04074#c5](https://arxiv.org/pdf/2007.04074v3#page=23 "The rather stark performance degradation compared to the regular model-based policy selector can mainly be explained by a few, huge datasets, to which the model-based policy selector cannot extrapolate (and which the single best does not account for).") |
| 選択を誤ったら取り返せるか | 事前に1回選ぶ方式は誤りに気づかず取り返せない。監視しながら選び直すには負荷がかかる [arxiv-1210.7959#c4](https://arxiv.org/pdf/1210.7959v1#page=13 "Purely oﬄine approaches are inherently vulnerable to bad choices.") |
| 確信度を引き金にしてよいか | 同じ分布のデータでは保証があるが [arxiv-1705.08500#c3](https://arxiv.org/pdf/1705.08500v2#page=5 "Theorem 3.2 (SGR) Let Sm be a given labeled set, sampled i.i.d. from P, and consider an application of the SGR procedure.")、分布が変わると較正が崩れる [arxiv-1906.02530#c4](https://arxiv.org/pdf/1906.02530v2#page=7 "Interestingly, while temperature scaling achieves low ECE for low values of shift, the ECE increases signiﬁcantly as the shift increases, which indicates that calibration on the i.i.d. validation dataset does not guarantee calibration under distributional shift.") |
| ラベルなしで性能低下を検知できるか | 全ての変化に通用する方法はない [arxiv-2201.04234#c3](https://arxiv.org/pdf/2201.04234v3#page=5 "Corollary 1. Absent assumptions on the classiﬁer f, no method of estimating accuracy will work in all scenarios, i.e., for different nature of distribution shifts.")。新しい部分集団の出現などで誤差が大きい [arxiv-2201.04234#c6](https://arxiv.org/pdf/2201.04234v3#page=8 "While we observe a small MAE (i.e., comparable to our observations on other datasets) on BREEDS with natural and synthetic shifts from the same sub-population, MAE on shifts with novel population is signiﬁcantly higher with all methods.") |
| 分布の変化を検知したら切り替えるべきか | 検知された変化が無害なこともある [arxiv-1810.11953#c13](https://arxiv.org/pdf/1810.11953v4#page=9 "this shift does not harm the classifier's performance")。検知と昇格(入れ替え)は別の判断である [arxiv-2609.04388#c1](https://arxiv.org/pdf/2609.04388v1#page=1 "Adaptive network intrusion detection systems retrain classifiers after drift alarms, but an alarm detects change; it does not establish that a challenger should replace the deployed incumbent.") |
| フォールバック先の性質を考えるか | 委ねる先の得意不得意を考える枠組みがある [arxiv-1711.06664#c1](https://arxiv.org/pdf/1711.06664v3#page=1 "We extend this concept by proposing learning to defer, which generalizes rejection learning by considering the eﬀect of other agents in the decision-making process.")。考えないと全体が改善しないことがある [arxiv-2006.01862#c6](https://arxiv.org/pdf/2006.01862v3#page=14 "While our method does not achieve signiﬁcantly lower discrimination than the baseline") |
| 切り替え器自体は分布の変化に耐えるか | 学習データの分布の外ではランダムと同程度になった例がある [arxiv-2406.18665#c5](https://arxiv.org/pdf/2406.18665v4#page=8 "On MMLU (Table 2), all routers perform poorly at the level of the random router when trained only on Arena dataset, which we attribute to most MMLU questions being out-of-distribution (see Section 5.3).") [arxiv-2404.14618#c6](https://arxiv.org/pdf/2404.14618v1#page=14 "Similar to our observation in Section 4.6, our routers can generalize well if the quality gaps of testing LLM pairs exhibit strong positive correlation with the quality gaps of the training pairs.") |
| 切り替えの仕組みのコスト | 選ぶのに解くより時間がかかってはいけない [arxiv-1210.7959#c5](https://arxiv.org/pdf/1210.7959v1#page=15 "Apart from accuracy, one of the main requirements for such a selector is that it is relatively cheap to run – if selecting an algorithm for solving a problem is more expensive than solving the problem, there is no point in doing so.")。カスケードは全モデルを呼んでしまうことがある [arxiv-2305.05176#c6](https://arxiv.org/pdf/2305.05176v1#page=10 "However, FrugalGPT is unsure if the ﬁrst LLMs are correct, resulting in the need to query all LLMs in the chain.") |
| モデルの更新自体のリスク | 後方互換性のない更新が下流に害を与えうる [arxiv-2011.09926#c6](https://arxiv.org/pdf/2011.09926v3#page=14 "While updating is necessary for keeping a model up to date with recent ﬂuctuations in the data, it may also inﬂict damage on users or downstream systems because of the changes in the model’s behavior, even without causing obvious software errors.") |

## わかっていないこと

この記事の範囲の論文からは、次のことはわからなかった(本記事の整理)。

- **フォールバックの仕組みを本番で評価した研究**: MLOps の論文4本にロールバックやフォールバックの記述がなく、選択・委譲・ルーティングの研究の評価の多くは、同じ分布の無作為な分割で行われている [arxiv-1705.08500#c6](https://arxiv.org/pdf/1705.08500v2#page=8 "The other half, which was not consumed by SGR for training, was reserved for testing the resulting bounds.") [arxiv-1810.01270#c4](https://arxiv.org/pdf/1810.01270v1#page=16 "The experiments were conducted using 20 replications.") [arxiv-2305.05176#c4](https://arxiv.org/pdf/2305.05176v1#page=6 "Each dataset is randomly split into a training set to learn the LLM cascade and a test set for evaluation.")。
- **普段使われないフォールバック先のモデルの劣化**: フォールバック先も時間とともに劣化しうるが、それを監視・評価した研究はこの範囲にない。
- **切り替え器(メタ学習器)自体の監視**: 選択器やルーターの性能を本番でどう監視するかを扱った研究はこの範囲にない。分布の外で弱くなることは示されている [arxiv-2406.18665#c5](https://arxiv.org/pdf/2406.18665v4#page=8 "On MMLU (Table 2), all routers perform poorly at the level of the random router when trained only on Arena dataset, which we attribute to most MMLU questions being out-of-distribution (see Section 5.3).")。
- **切り替えを繰り返すことの影響**: 切り替えが頻繁に起きたときの安定性(行ったり来たり)を扱った研究はこの範囲にない。

## 現時点での整理

- **モデル選択のメタ学習は、範囲外の入力での誤りを前提に、固定の規則によるフォールバックと組み合わせる例がある** [arxiv-2007.04074#c4](https://arxiv.org/pdf/2007.04074v3#page=20 "Since there is no guarantee that our model-based policy selector will extrapolate well to datasets outside of the meta-datasets, we implement a fallback measure to avoid failures.")。事前に1回選ぶだけの方式は、誤りに気づかず取り返せない [arxiv-1210.7959#c4](https://arxiv.org/pdf/1210.7959v1#page=13 "Purely oﬄine approaches are inherently vulnerable to bad choices.")。
- **予測を控える・委ねる方法の保証は、同じ分布という仮定つき**である [arxiv-1705.08500#c3](https://arxiv.org/pdf/1705.08500v2#page=5 "Theorem 3.2 (SGR) Let Sm be a given labeled set, sampled i.i.d. from P, and consider an application of the SGR procedure.") [arxiv-2006.01862#c2](https://arxiv.org/pdf/2006.01862v3#page=5 "The proposed surrogate LCE is in fact consistent and upper bounds L0−1 as the following theorem demonstrates.")。分布が変わると確信度の較正は崩れ [arxiv-1906.02530#c4](https://arxiv.org/pdf/1906.02530v2#page=7 "Interestingly, while temperature scaling achieves low ECE for low values of shift, the ECE increases signiﬁcantly as the shift increases, which indicates that calibration on the i.i.d. validation dataset does not guarantee calibration under distributional shift.")、ラベルなしの性能推定にも原理的な限界がある [arxiv-2201.04234#c3](https://arxiv.org/pdf/2201.04234v3#page=5 "Corollary 1. Absent assumptions on the classiﬁer f, no method of estimating accuracy will work in all scenarios, i.e., for different nature of distribution shifts.")。
- **学習した切り替え器(ルーター)は、学習データの分布の外で弱くなりうる** [arxiv-2406.18665#c5](https://arxiv.org/pdf/2406.18665v4#page=8 "On MMLU (Table 2), all routers perform poorly at the level of the random router when trained only on Arena dataset, which we attribute to most MMLU questions being out-of-distribution (see Section 5.3).")。
- **検知と入れ替えは別の判断である** [arxiv-2609.04388#c1](https://arxiv.org/pdf/2609.04388v1#page=1 "Adaptive network intrusion detection systems retrain classifiers after drift alarms, but an alarm detects change; it does not establish that a challenger should replace the deployed incumbent.")。検知された変化が無害なこともある [arxiv-1810.11953#c13](https://arxiv.org/pdf/1810.11953v4#page=9 "this shift does not harm the classifier's performance")。
- **フォールバックの設計そのものを評価した研究は、この範囲には見当たらない**。現状では、隣接する研究の知見を組み合わせて設計するしかない(本記事の整理)。

**この整理に含まれていないもの**: 時系列予測でのモデル選択・重みづけのメタ学習(FFORMA など。arXiv で見つからず未取得)、動的分類器選択の総合的なサーベイ(Cruz et al. 2018。同上)、オンライン学習での専門家の重みづけ(Hedge など)、強化学習の安全な方策の切り替え、A/B テストやカナリアリリースの統計的な設計、因果推論の「メタ学習器」(T-learner など。名前は同じだが別の概念)。

## 参照カード

- [arxiv-1810.03548](../../papers/arxiv-1810.03548.yaml) Vanschoren, "Meta-Learning: A Survey"
- [arxiv-1210.7959](../../papers/arxiv-1210.7959.yaml) Kotthoff, "Algorithm Selection for Combinatorial Search Problems: A Survey"
- [arxiv-2007.04074](../../papers/arxiv-2007.04074.yaml) Feurer et al., "Auto-Sklearn 2.0: Hands-free AutoML via Meta-Learning"
- [arxiv-1810.01270](../../papers/arxiv-1810.01270.yaml) Cruz et al., "META-DES: A Dynamic Ensemble Selection Framework using Meta-Learning"
- [arxiv-1802.04967](../../papers/arxiv-1802.04967.yaml) Cruz et al., "DESlib: A Dynamic ensemble selection library in Python"
- [arxiv-1705.08500](../../papers/arxiv-1705.08500.yaml) Geifman & El-Yaniv, "Selective Classification for Deep Neural Networks"
- [arxiv-1901.09192](../../papers/arxiv-1901.09192.yaml) Geifman & El-Yaniv, "SelectiveNet: A Deep Neural Network with an Integrated Reject Option"
- [arxiv-2006.01862](../../papers/arxiv-2006.01862.yaml) Mozannar & Sontag, "Consistent Estimators for Learning to Defer to an Expert"
- [arxiv-1711.06664](../../papers/arxiv-1711.06664.yaml) Madras et al., "Predict Responsibly: Improving Fairness and Accuracy by Learning to Defer"
- [arxiv-1610.02136](../../papers/arxiv-1610.02136.yaml) Hendrycks & Gimpel, "A Baseline for Detecting Misclassified and Out-of-Distribution Examples in Neural Networks"
- [arxiv-1706.04599](../../papers/arxiv-1706.04599.yaml) Guo et al., "On Calibration of Modern Neural Networks"
- [arxiv-1906.02530](../../papers/arxiv-1906.02530.yaml) Ovadia et al., "Can You Trust Your Model's Uncertainty? Evaluating Predictive Uncertainty Under Dataset Shift"
- [arxiv-2201.04234](../../papers/arxiv-2201.04234.yaml) Garg et al., "Leveraging Unlabeled Data to Predict Out-of-Distribution Performance"
- [arxiv-2107.03315](../../papers/arxiv-2107.03315.yaml) Guillory et al., "Predicting with Confidence on Unseen Distributions"
- [arxiv-2305.05176](../../papers/arxiv-2305.05176.yaml) Chen et al., "FrugalGPT: How to Use Large Language Models While Reducing Cost and Improving Performance"
- [arxiv-2406.18665](../../papers/arxiv-2406.18665.yaml) Ong et al., "RouteLLM: Learning to Route LLMs with Preference Data"
- [arxiv-2404.14618](../../papers/arxiv-2404.14618.yaml) Ding et al., "Hybrid LLM: Cost-Efficient and Quality-Aware Query Routing"
- [arxiv-2205.02302](../../papers/arxiv-2205.02302.yaml) Kreuzberger et al., "Machine Learning Operations (MLOps): Overview, Definition, and Architecture"
- [arxiv-2011.09926](../../papers/arxiv-2011.09926.yaml) Paleyes et al., "Challenges in Deploying Machine Learning: a Survey of Case Studies"
- [arxiv-2007.06299](../../papers/arxiv-2007.06299.yaml) Klaise et al., "Monitoring and explainability of models in production"
- [arxiv-2003.01668](../../papers/arxiv-2003.01668.yaml) Kang et al., "Model Assertions for Monitoring and Improving ML Models"
- [arxiv-1810.11953](../../papers/arxiv-1810.11953.yaml) Rabanser et al., "Failing Loudly: An Empirical Study of Methods for Detecting Dataset Shift"
- [arxiv-2004.05785](../../papers/arxiv-2004.05785.yaml) Lu et al., "Learning under Concept Drift: A Review"
- [arxiv-2609.04388](../../papers/arxiv-2609.04388.yaml) Fernández-Barrios et al., "Candidate Comparability Before Promotion: Conditional Validation in Adaptive Network Intrusion Detection"
