---
title: 概念ドリフトとデータシフトの検出手法の比較
kind: task
tags: [drift-detection, concept-drift-detection, dataset-shift-detection]
depends_on: [arxiv-2004.05785, arxiv-1810.11953, arxiv-2311.06396, arxiv-2606.07789, arxiv-2602.06456]
written_at: 2026-10-02
written_by: claude-opus-5-5 via Claude Code
---

# 概念ドリフトとデータシフトの検出手法の比較

<!-- generated:stale -->
> 未反映のカードはありません。
<!-- /generated:stale -->

## この課題とは

運用中の機械学習モデルは、学習時と同じデータが来続ける前提で作られている。その前提が崩れたことを検出するのがドリフト検出で、MLOps の監視の中核にあたる。

サーベイ(Lu et al.)は、概念ドリフトを入力と正解の同時分布の時間変化として定義し [arxiv-2004.05785#c3](https://arxiv.org/pdf/2004.05785v1#page=3 "concept drift at time t can be defined as the change of joint probability of X and y at time t.")、
入力の分布だけが変わり決定境界が動かないものを「仮想ドリフト」と呼んで区別している [arxiv-2004.05785#c4](https://arxiv.org/pdf/2004.05785v1#page=3 "drift does not affect the decision boundary, it has also been considered as virtual drift")。
また、ドリフトへの対処を「検出・理解・適応」の3要素に整理している [arxiv-2004.05785#c2](https://arxiv.org/pdf/2004.05785v1#page=1 "establishes a framework of learning under concept drift including three main components: concept drift detection, concept drift understanding, and concept drift adaptation.")。

ここでは系統の違う2つの問題を扱う。

- **概念ドリフト検出**(データストリーム): 予測誤差などを逐次監視し、変化の時点を検出する。
- **データシフト検出**(学習時と運用時の比較): 入力の分布が変わったかを統計的な検定で判定する。
  検出の問題は、二標本検定の問題とみなせる [arxiv-2004.05785#c5](https://arxiv.org/pdf/2004.05785v1#page=4 "the concept drift detection problem can be considered as a two-sample test problem which examines whether the population of two given sample sets are from the same distribution")。

## 手法の分類

サーベイは、検出器を検定統計量の種類で3つに分類している [arxiv-2004.05785#c6](https://arxiv.org/pdf/2004.05785v1#page=4 "This section surveys drift detection methods and algorithms, which are classified into three categories in terms of the test statistics they apply.")。

- **誤り率ベース**(DDM、EDDM、HDDM、Page-Hinkley など): 分類器の誤り率の変化を監視する。最も大きな系統である [arxiv-2004.05785#c7](https://arxiv.org/pdf/2004.05785v1#page=4 "error rate-based drift detection algorithms form the largest category of algorithms.")。DDM は警告レベルとドリフトレベルを初めて定義した [arxiv-2004.05785#c8](https://arxiv.org/pdf/2004.05785v1#page=4 "the first algorithm to define the warning level and drift")。
- **データ分布ベース**(ADWIN、KSWIN など、窓どうしの比較): 分布そのものの変化を捉え、場所も特定しうるが、計算コストが高く、窓の大きさを決める必要がある [arxiv-2004.05785#c9](https://arxiv.org/pdf/2004.05785v1#page=5 "these algorithms are usually reported as incurring higher computational cost than the algorithms mentioned in Section 3.2.1")。
- **多重仮説検定**: 複数の検定を組み合わせる比較的新しい系統。

もう1つの軸は、**正解ラベルが必要かどうか**である。多くの手法は予測の直後に正解が得られることを前提にしている [arxiv-2004.05785#c11](https://arxiv.org/pdf/2004.05785v1#page=14 "Most existing drift detection and adaptation algorithms assume the ground true label is available after classification/prediction, or extreme verification latency.")。
ラベルを使わない検出器は特徴量の変化は捉えられるが、正解だけが変わる変化は捉えられない [arxiv-2606.07789#c12](https://arxiv.org/pdf/2606.07789v1#page=8 "Unsupervised detectors (ABCD(X) and STUDD) perform better on feature-space drifts (feature permutation, feature filtering) than on label-based changes (class prior, class swaps)")。

## 比較条件の違い

論文ごとに条件が揃っていないため、数値を論文をまたいで並べてはいけない(このリポジトリの比較ルール)。

| 観点 | Aguiar & Cano 2023 | Cerqueira et al. 2026 | Gower-Winter et al. 2026 | Rabanser et al. 2019 |
|---|---|---|---|---|
| 問題 | 概念ドリフト検出 | 概念ドリフト検出 | 概念ドリフトへの適応(検出器の有用性) | データシフト検出 |
| データ | 合成ストリーム(2,760問題) [arxiv-2311.06396#c1](https://arxiv.org/pdf/2311.06396v2#page=1 "A systematic approach leads to a set of 2,760 benchmark problems") | 実データ7本にドリフトを人工的に注入 [arxiv-2606.07789#c2](https://arxiv.org/pdf/2606.07789v1#page=1 "We benchmark 14 widely used drift detection methods on 7 real-world datasets across 4 drift types") | 実データのストリーム11本 [arxiv-2602.06456#c13](https://arxiv.org/pdf/2602.06456v1#page=5 "we evaluate each model across 11 binary and multiclass data streams") | 画像(MNIST、CIFAR-10) [arxiv-1810.11953#c12](https://arxiv.org/pdf/1810.11953v4#page=9 "since we have mostly explored a standard image classification setting for our experiments") |
| 監視する信号 | Hoeffding Tree の誤り [arxiv-2311.06396#c9](https://arxiv.org/pdf/2311.06396v2#page=10 "we opted to use Hoeffding Tree (HT) [49] as our classifier.") | Hoeffding Tree の誤りなど [arxiv-2606.07789#c10](https://arxiv.org/pdf/2606.07789v1#page=6 "We select the Hoeffding Tree [10] as the classifier in the experiments") | 分類器ごとに検出器を組み合わせる | 次元削減した表現の分布 [arxiv-1810.11953#c4](https://arxiv.org/pdf/1810.11953v4#page=6 "In the multivariate-testing case, UAE performed best.") |
| ハイパーパラメータ | 記載を確認できず | データセットを1つ抜いたランダムサーチ [arxiv-2606.07789#c7](https://arxiv.org/pdf/2606.07789v1#page=4 "we propose a leave-one-dataset-out cross-validation approach for optimizing the hyperparameters of drift detectors.") [arxiv-2606.07789#c19](https://arxiv.org/pdf/2606.07789v1#page=6 "The optimization is conducted using 30 iterations of random search.") | 既定値のまま [arxiv-2602.06456#c12](https://arxiv.org/pdf/2602.06456v1#page=8 "We do not perform explicit parameter tuning for model on each data stream and instead use the default values") | 該当なし |
| 繰り返し | カテゴリ内の全ストリームで平均 | 50回のモンテカルロ試行 [arxiv-2606.07789#c9](https://arxiv.org/pdf/2606.07789v1#page=6 "For each dataset and drift type, we perform 50 Monte Carlo trials.") | 固定シード(繰り返し回数の記載は確認できず) | 5回の分割で平均 [arxiv-1810.11953#c10](https://arxiv.org/pdf/1810.11953v4#page=6 "shift detection performance is averaged over a total of 5 random splits") |
| 評価の対象 | ドリフト時点の検出(適合率・再現率・遅延) | ドリフト時点の検出(F1 の順位) | 分類性能(ドリフトを正しく検出したかは評価しない) [arxiv-2602.06456#c15](https://arxiv.org/pdf/2602.06456v1#page=5 "We acknowledge that accuracy is a potentially misleading metric in Drift Research") [arxiv-2602.06456#c4](https://arxiv.org/pdf/2602.06456v1#page=4 "Performance improvement is neither necessary nor sufficient evidence of successful drift detection") | シフトの有無の判定 |

## 論文内の勝敗の関係

- [Aguiar & Cano 2023 の結果表と勝敗](../../generated/papers/arxiv-2311.06396.md)
- [Cerqueira et al. 2026 の結果表と勝敗](../../generated/papers/arxiv-2606.07789.md)
- [Gower-Winter et al. 2026 の結果表と勝敗](../../generated/papers/arxiv-2602.06456.md)
- [Rabanser et al. 2019 の結果表と勝敗](../../generated/papers/arxiv-1810.11953.md)

### Aguiar & Cano 2023: 局所的なドリフトほど難しい

ドリフトが影響する範囲(一部のクラスか全体か)で分類した合成ベンチマークで、9つの検出器を比べた [arxiv-2311.06396#c2](https://arxiv.org/pdf/2311.06396v2#page=1 "We conduct a comparative assessment of 9 state-of-the-art drift detectors across diverse difficulties")。
ADWIN と Page-Hinkley(PH)が全シナリオで一貫して最良だった [arxiv-2311.06396#c4](https://arxiv.org/pdf/2311.06396v2#page=13 "ADWIN and PH consistently demonstrated superior detection performance across all evaluated scenarios.")。
EDDM は検出は速いが誤検知が非常に多く、適合率はほぼゼロだった [arxiv-2311.06396#c5](https://arxiv.org/pdf/2311.06396v2#page=12 "EDDM exhibited the lowest delay among all evaluated drift detectors and the second-highest recall, although this came at the cost of raising numerous drift alerts, leading to a precision of 0%.")。
STEPD も再現率は高いが適合率はきわめて低い [arxiv-2311.06396#r33](https://arxiv.org/pdf/2311.06396v2#page=13 "STEPD 0.01% 95.80% 0.03% 516")。
難易度は「複数クラス・全体」から「単一クラス・局所」の順に上がり [arxiv-2311.06396#c6](https://arxiv.org/pdf/2311.06396v2#page=13 "a hierarchy of difficulty emerges, from easiest to hardest detection as follows: Multi-Class Global, Single-Class Global, Multi-Class Local, Single-Class Local.")、局所的なドリフトほど誤検知が増える [arxiv-2311.06396#c7](https://arxiv.org/pdf/2311.06396v2#page=13 "scenarios with more localized drifts tended to generate a higher number of false alarms.")。
また、検出のたびに分類器を作り直すと、どのシナリオでも精度が下がった [arxiv-2311.06396#c8](https://arxiv.org/pdf/2311.06396v2#page=21 "completely retraining the classifier resulted in decreased accuracy across all evaluated scenarios.")。

### Cerqueira et al. 2026: 評価方法そのものを揃える

既存研究は、単純すぎる合成データ、互換性のない指標、不透明なハイパーパラメータ選択のために比較が成り立っていないと指摘する [arxiv-2606.07789#c1](https://arxiv.org/pdf/2606.07789v1#page=1 "studies rely on oversimplified synthetic data generators, adopt incompatible metrics, and lack transparency in hyperparameter selection")。
従来の指標は、ストリームの長さやドリフトの間隔に依存する [arxiv-2606.07789#c5](https://arxiv.org/pdf/2606.07789v1#page=3 "MTFA and MDT are highly dependent on stream length and drift spacing")。F1 だけでは遅すぎる検出も満点になりうる [arxiv-2606.07789#c6](https://arxiv.org/pdf/2606.07789v1#page=3 "its formulation ignores the temporal aspect: a detector with unacceptable delay can still achieve perfect F1.")。
さらに、同じデータでチューニングと評価をすると楽観的な結果になると述べる [arxiv-2606.07789#c8](https://arxiv.org/pdf/2606.07789v1#page=4 "using the same dataset for optimizing and evaluating the detector can cause overfitting and lead to overly optimistic performance estimates reported in the respective papers.")。

この枠組みで14の検出器を比べると、SEED・STEPD・ABCD が一貫して上位だった [arxiv-2606.07789#c3](https://arxiv.org/pdf/2606.07789v1#page=2 "Our results reveal that SEED [23], STEPD [25], and ABCD [22] consistently outperform other detectors across distinct drift types")。
PH と EWMA は、どう設定しても効果が出なかった [arxiv-2606.07789#c11](https://arxiv.org/pdf/2606.07789v1#page=8 "PH and EWMA remain ineffective regardless of configuration, suggesting fundamental limitations")。
ただし STEPD の強さは、チューニングによるところが大きい [arxiv-2606.07789#c14](https://arxiv.org/pdf/2606.07789v1#page=8 "STEPD's strong performance is largely attributable to effective tuning.")。
漸進的なドリフトは、急激なドリフトより一貫して検出が難しかった [arxiv-2606.07789#c13](https://arxiv.org/pdf/2606.07789v1#page=8 "Gradual drifts are systematically harder to detect than abrupt ones.")。

### 2本の結論の食い違い

**Page-Hinkley と STEPD の評価が、2本で正反対になっている。**

- Aguiar らでは、PH は最良の検出器の1つだった [arxiv-2311.06396#c4](https://arxiv.org/pdf/2311.06396v2#page=13 "ADWIN and PH consistently demonstrated superior detection performance across all evaluated scenarios.") [arxiv-2311.06396#r27](https://arxiv.org/pdf/2311.06396v2#page=13 "PH 5.18% 72.19% 9.66% 1867")。STEPD は誤検知が多く、適合率が極端に低かった [arxiv-2311.06396#r33](https://arxiv.org/pdf/2311.06396v2#page=13 "STEPD 0.01% 95.80% 0.03% 516")。
- Cerqueira らでは、PH はどう設定しても効果がなかった [arxiv-2606.07789#c11](https://arxiv.org/pdf/2606.07789v1#page=8 "PH and EWMA remain ineffective regardless of configuration, suggesting fundamental limitations") [arxiv-2606.07789#r40](https://arxiv.org/pdf/2606.07789v1#page=7 "PH 13.1 12.9 11.6 10.1")。STEPD は最上位だった [arxiv-2606.07789#c3](https://arxiv.org/pdf/2606.07789v1#page=2 "Our results reveal that SEED [23], STEPD [25], and ABCD [22] consistently outperform other detectors across distinct drift types") [arxiv-2606.07789#r52](https://arxiv.org/pdf/2606.07789v1#page=7 "STEPD 3.4 3.7 4.3 2.4")。

条件の違いは次の3点である。

- **データ**: 合成ストリームか、実データにドリフトを注入したものか。
- **ハイパーパラメータ**: Cerqueira らはデータセットを1つ抜いてチューニングしており、STEPD の強さはそのチューニングによると自ら述べている [arxiv-2606.07789#c14](https://arxiv.org/pdf/2606.07789v1#page=8 "STEPD's strong performance is largely attributable to effective tuning.")。
- **正しい検出とみなす時間窓の定義**: 2本で異なる。

どちらが「正しい」かは、この2本からは判断できない。ただし、**検出器の順位は評価の設計に強く依存する**ことは確かで、これは Cerqueira らが問題にしている点そのものである [arxiv-2606.07789#c1](https://arxiv.org/pdf/2606.07789v1#page=1 "studies rely on oversimplified synthetic data generators, adopt incompatible metrics, and lack transparency in hyperparameter selection")。

### Gower-Winter et al. 2026: そもそもドリフト検出は役に立っているのか

ドリフト検出は「問題の立て方として不良」だと主張する。
ドリフトに見えるものは窓の切り方の産物かもしれず [arxiv-2602.06456#c2](https://arxiv.org/pdf/2602.06456v1#page=1 "perceived drift is a product of windowing and not necessarily the underlying data generating process.")、実データではドリフトが本当に起きたかを確かめられないからである [arxiv-2602.06456#c3](https://arxiv.org/pdf/2602.06456v1#page=1 "drift detection is ill-posed, primarily because verification of drift events are implausible in practice.")。
検出器を付けた分類器の性能が上がっても、ドリフトを正しく検出した証拠にはならない [arxiv-2602.06456#c4](https://arxiv.org/pdf/2602.06456v1#page=4 "Performance improvement is neither necessary nor sufficient evidence of successful drift detection")。
頻繁に警報を出す検出器ほど性能が良くなる傾向も、新しいデータでこまめに学習し直す効果で説明できる [arxiv-2602.06456#c5](https://arxiv.org/pdf/2602.06456v1#page=4 "concept drift detectors that detect more frequently, tend to perform better (up to a point).")。

実験では、分類器の種類のほうがドリフトへの対応の有無より効いた [arxiv-2602.06456#c6](https://arxiv.org/pdf/2602.06456v1#page=1 "indicates that the type of classifier is often more important than drift-awareness.")。
ドリフトを考慮しない Aggregated Mondrian Forest は、考慮する Adaptive Random Forest と同等だった [arxiv-2602.06456#c8](https://arxiv.org/pdf/2602.06456v1#page=7 "the drift-unaware Aggregated Mondrian Forest (AMF) performed competitively with the drift-aware Adaptive Random Forest (ARF).")。
同じ更新頻度にそろえると、単純なバッチ学習がしばしば上回った [arxiv-2602.06456#c10](https://arxiv.org/pdf/2602.06456v1#page=7 "drift-aware stream learners are often inferior to simple batch learning procedures provided an appropriate classifier is chosen.") [arxiv-2602.06456#c1](https://arxiv.org/pdf/2602.06456v1#page=1 "is that traditional batch learning techniques often perform better than their drift-aware counterparts")。
検出器の中では D3(Hoeffding Tree 版)が最良だった [arxiv-2602.06456#c7](https://arxiv.org/pdf/2602.06456v1#page=7 "Of the drift detectors, D3-HT performed the best for both the NB and HT base models.")。

注意点として、比較対象の一部(定期的なリセット)はデータセットの知識を使って間隔を決めている [arxiv-2602.06456#c16](https://arxiv.org/pdf/2602.06456v1#page=8 "For resetting, some datasets possess domain knowledge that we could exploit.")。
精度は誤解を招きうる指標であることも著者が認めている [arxiv-2602.06456#c15](https://arxiv.org/pdf/2602.06456v1#page=5 "We acknowledge that accuracy is a potentially misleading metric in Drift Research")。
著者自身は「検出が無意味」とまでは言っておらず、「目的の置き方が誤っている」としている [arxiv-2602.06456#c11](https://arxiv.org/pdf/2602.06456v1#page=8 "Our findings do not mean that drift detection is pointless, rather that its current purpose is misplaced.")。

### Rabanser et al. 2019: 運用データのシフトをどう検出するか

学習済みの分類器の出力(ソフトマックス)を低次元の表現として使い、二標本検定をかける方法(BBSD)が最も良かった [arxiv-1810.11953#c1](https://arxiv.org/pdf/1810.11953v4#page=1 "a two-sample-testing-based approach, using pre-trained classifiers for dimensionality reduction, performs best.") [arxiv-1810.11953#c4](https://arxiv.org/pdf/1810.11953v4#page=6 "In the multivariate-testing case, UAE performed best.")。
その前提(ラベルシフト)が成り立たない場合でもよく機能した [arxiv-1810.11953#c2](https://arxiv.org/pdf/1810.11953v4#page=2 "We show (empirically) that BBSD works surprisingly well under a broad set of shifts, even when the label shift assumption is not met.")。
次元ごとの KS 検定を Bonferroni 補正でまとめる単純な方法が、多変量カーネル検定(MMD)と同程度だった [arxiv-1810.11953#c3](https://arxiv.org/pdf/1810.11953v4#page=6 "despite the heavy correction, multiple univariate testing seem to offer comparable performance to multivariate testing")。
一方、次元削減なしの多変量検定は性能が悪かった [arxiv-1810.11953#c6](https://arxiv.org/pdf/1810.11953v4#page=6 "the multivariate test performs poorly in the no reduction case")。
シフトを判別する分類器を学習する方法は、サンプルが少ないと弱いが、増えると追いつく [arxiv-1810.11953#c5](https://arxiv.org/pdf/1810.11953v4#page=6 "The domain classifier, a popular shift detection approach, performs badly in the low-sample regime (≤100 samples), but catches up as more samples are obtained.")。
また、検出されたシフトが必ずしも有害とは限らない [arxiv-1810.11953#c13](https://arxiv.org/pdf/1810.11953v4#page=9 "this shift does not harm the classifier's performance")。

## 現時点での整理

- **評価方法が未成熟**: 合成データへの依存、指標の不統一、チューニングの不透明さが指摘されている [arxiv-2606.07789#c1](https://arxiv.org/pdf/2606.07789v1#page=1 "studies rely on oversimplified synthetic data generators, adopt incompatible metrics, and lack transparency in hyperparameter selection")。実データではドリフトの有無自体を確かめにくい [arxiv-2602.06456#c3](https://arxiv.org/pdf/2602.06456v1#page=1 "drift detection is ill-posed, primarily because verification of drift events are implausible in practice.")。その結果、検出器の順位は論文によって正反対にもなる(上の食い違いを参照)。どれか1つの論文の「最良の検出器」を一般論として受け取るのは危険である。
- **監視する信号の選択**: 誤り率ベースの検出器は誤検知が多くなりやすい [arxiv-2311.06396#c10](https://arxiv.org/pdf/2311.06396v2#page=24 "Drift detectors that rely on error rates often generate numerous false alarms.")。ラベルを使わない検出器は、正解だけの変化を捉えられない [arxiv-2606.07789#c12](https://arxiv.org/pdf/2606.07789v1#page=8 "Unsupervised detectors (ABCD(X) and STUDD) perform better on feature-space drifts (feature permutation, feature filtering) than on label-based changes (class prior, class swaps)")。現実には正解ラベルがすぐ得られない場面も多い [arxiv-2004.05785#c11](https://arxiv.org/pdf/2004.05785v1#page=14 "Most existing drift detection and adaptation algorithms assume the ground true label is available after classification/prediction, or extreme verification latency.")。
- **検出の後の対応**: 検出のたびに作り直すのが最善とは限らない [arxiv-2311.06396#c8](https://arxiv.org/pdf/2311.06396v2#page=21 "completely retraining the classifier resulted in decreased accuracy across all evaluated scenarios.")。過去のデータを残して定期的に学習し直す単純な方法が強いという報告もある [arxiv-2602.06456#c9](https://arxiv.org/pdf/2602.06456v1#page=7 "our results suggest that keeping past data is often useful and periodically retraining a model on increasingly large training sets is often an effective strategy.")。
- **データシフトの監視(MLOps)**: 運用中のモデル自身の出力に単純な単変量検定をかける方法が、扱いやすく強い [arxiv-1810.11953#c1](https://arxiv.org/pdf/1810.11953v4#page=1 "a two-sample-testing-based approach, using pre-trained classifiers for dimensionality reduction, performs best.") [arxiv-1810.11953#c3](https://arxiv.org/pdf/1810.11953v4#page=6 "despite the heavy correction, multiple univariate testing seem to offer comparable performance to multivariate testing")。ただし検出は「有害かどうか」とは別の問題である [arxiv-1810.11953#c13](https://arxiv.org/pdf/1810.11953v4#page=9 "this shift does not harm the classifier's performance")。実際の機械学習パイプラインでは、入力のシフトの確認自体がほとんど行われていないという指摘もある [arxiv-1810.11953#c8](https://arxiv.org/pdf/1810.11953v4#page=1 "in practice, ML pipelines rarely inspect incoming data for signs of distribution shift.")。
- **答えられることの範囲**: 既存の検出器が答えられるのは「いつ」までで、「どこで」「どのように」はほとんど答えられない [arxiv-2004.05785#c10](https://arxiv.org/pdf/2004.05785v1#page=14 "all drift detection methods can answer 'When', but very few methods have the ability to answer 'How' and 'Where';")。

**この整理に含まれていないもの**: DDM・ADWIN・Page-Hinkley などの原論文(arXiv にないため未取得)、表データでのデータシフト検出のベンチマーク、ラベルシフト推定の手法、教師なし検出器の専用ベンチマーク。

## 参照カード

- [arxiv-2004.05785](../../papers/arxiv-2004.05785.yaml) Lu et al., "Learning under Concept Drift: A Review"
- [arxiv-1810.11953](../../papers/arxiv-1810.11953.yaml) Rabanser et al., "Failing Loudly: An Empirical Study of Methods for Detecting Dataset Shift" (NeurIPS 2019)
- [arxiv-2311.06396](../../papers/arxiv-2311.06396.yaml) Aguiar & Cano, "A comprehensive analysis of concept drift locality in data streams"
- [arxiv-2606.07789](../../papers/arxiv-2606.07789.yaml) Cerqueira et al., "A Framework for Evaluating and Benchmarking Concept Drift Detection Methods" (KDD 2026)
- [arxiv-2602.06456](../../papers/arxiv-2602.06456.yaml) Gower-Winter et al., "The Window Dilemma: Why Concept Drift Detection is Ill-Posed"
