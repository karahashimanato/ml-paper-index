---
title: 概念ドリフトとデータシフトの検出手法の比較
kind: task
tags: [drift-detection, concept-drift-detection, dataset-shift-detection, change-point-detection]
depends_on: [arxiv-2004.05785, arxiv-1810.11953, arxiv-2311.06396, arxiv-2606.07789, arxiv-2602.06456, doi-10.1007_s41060-024-00620-y, arxiv-2310.15826, arxiv-2609.04388, arxiv-2609.24278, arxiv-2609.25340, doi-10.1007_s44163-026-02063-9, arxiv-2609.09432, arxiv-2608.23893, arxiv-2608.17824, arxiv-2608.16659, arxiv-2608.08245, arxiv-2610.00649, arxiv-2609.39473, arxiv-2609.36594, arxiv-2609.35703, arxiv-2609.33940]
written_at: 2026-10-03
written_by: claude-opus-5-5 via Claude Code
---

# 概念ドリフトとデータシフトの検出手法の比較

<!-- generated:stale -->
> ⚠ この記事の執筆日(2026-10-03)以降に作成された関連カードが 9 件あります(未反映。執筆日と同じ日に作成されたカードを含む): `arxiv-1011.2932`, `arxiv-1801.00718`, `arxiv-1812.04606`, `arxiv-2003.06222`, `arxiv-2006.15532`, `arxiv-2102.12938`, `arxiv-2211.14097`, `arxiv-2306.05265`, `arxiv-2507.01558`
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
- [Lukats et al. 2024 の結果表と勝敗](../../generated/papers/doi-10.1007_s41060-024-00620-y.md)

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

### Lukats et al. 2024 と Hinder et al. 2023: 正解ラベルを使わない検出

正解ラベルがすぐには得られない運用環境では、入力だけを見る**教師なし**の検出器が必要になる。
Lukats らは、多くの検出器が即時のラベルを前提にしていることを問題にし [doi-10.1007_s41060-024-00620-y#c1](https://elib.dlr.de/206088/1/Lukats_et_al-2024-International_Journal_of_Data_Science_and_Analytics.pdf#page=1 "Most algorithms proposed in the literature depend on the immediate availability of ground truth class labels.")、
完全に教師なしの検出器10個を整理して、7個を実データのストリーム11本で比べた [doi-10.1007_s41060-024-00620-y#c2](https://elib.dlr.de/206088/1/Lukats_et_al-2024-International_Journal_of_Data_Science_and_Analytics.pdf#page=1 "Ten algorithms are analyzed in terms of architectural choices, core ideas and assumptions about data") [doi-10.1007_s41060-024-00620-y#c3](https://elib.dlr.de/206088/1/Lukats_et_al-2024-International_Journal_of_Data_Science_and_Analytics.pdf#page=1 "Seven of these algorithms are evaluated with common concept drift detection metrics on eleven real-world data streams")。

正解のドリフト時点がわかる唯一のストリームで直接評価すると、D3 が大差で最良だった [doi-10.1007_s41060-024-00620-y#c7](https://elib.dlr.de/206088/1/Lukats_et_al-2024-International_Journal_of_Data_Science_and_Analytics.pdf#page=13 "In these experiments, D3 outperforms other detectors by a large margin")。
一方、分類器の精度で間接的に評価すると、IBDD が良く見えた [doi-10.1007_s41060-024-00620-y#c11](https://elib.dlr.de/206088/1/Lukats_et_al-2024-International_Journal_of_Data_Science_and_Analytics.pdf#page=18 "Image-Based Drift Detector (IBDD) [46] achieves great classifier predictive performance on many data streams, although it does not perform as well when assessed with lpd and MTR.")。
著者は、**精度による評価は検出の回数が多い検出器に有利に偏り**、別の指標(lift-per-drift)は逆に少ない検出器に偏ると指摘している [doi-10.1007_s41060-024-00620-y#c9](https://elib.dlr.de/206088/1/Lukats_et_al-2024-International_Journal_of_Data_Science_and_Analytics.pdf#page=18 "classifier predictive performance is biased in favor of a higher number of detected concept drifts and adaptations.") [doi-10.1007_s41060-024-00620-y#c10](https://elib.dlr.de/206088/1/Lukats_et_al-2024-International_Journal_of_Data_Science_and_Analytics.pdf#page=18 "lpdr=1 is likewise biased, as the version used in this study evidently favors fewer detected concept drifts.")。
これは、Window Dilemma の「頻繁に警報を出す検出器ほど良く見える」という指摘 [arxiv-2602.06456#c5](https://arxiv.org/pdf/2602.06456v1#page=4 "concept drift detectors that detect more frequently, tend to perform better (up to a point).") と同じ現象を、別の著者が別の実験で示したものである。
また D3 が最良という点も、Window Dilemma の結果 [arxiv-2602.06456#c7](https://arxiv.org/pdf/2602.06456v1#page=7 "Of the drift detectors, D3-HT performed the best for both the NB and HT base models.") と一致している。
ただし Lukats らの表の値は、同じストリーム上での各検出器の最良の設定であり、楽観的に出ている [doi-10.1007_s41060-024-00620-y#c13](https://elib.dlr.de/206088/1/Lukats_et_al-2024-International_Journal_of_Data_Science_and_Analytics.pdf#page=10 "A simple grid search is performed to test all permutations of the configuration parameters")。

Hinder らのサーベイは、監視の目的では「いつ」だけでなく「どこで」変化したかが重要だとする [arxiv-2310.15826#c9](https://arxiv.org/pdf/2310.15826v1#page=27 "Solely detecting and determining the time point of the drift is not sufficient in many monitoring settings.")。
使い分けの指針として、次の点を挙げている。

- ドメイン知識をできるだけ取り込む [arxiv-2310.15826#c4](https://arxiv.org/pdf/2310.15826v1#page=27 "A main finding is that as much domain knowledge as possible should be incorporated when designing drift detection schemes.")
- 高次元のデータでは次元ごとの手法を避ける [arxiv-2310.15826#c7](https://arxiv.org/pdf/2310.15826v1#page=27 "When working with high dimensional data, one should avoid using dimension-wise methodologies, especially if false alarms are costly in the considered application.")
- 異常の監視が目的なら損失(誤差)ベースの手法を避ける [arxiv-2310.15826#c8](https://arxiv.org/pdf/2310.15826v1#page=27 "loss-based strategies should be avoided when the target of the drift detection is monitoring for anomalous behavior.")

### Rabanser et al. 2019: 運用データのシフトをどう検出するか

学習済みの分類器の出力(ソフトマックス)を低次元の表現として使い、二標本検定をかける方法(BBSD)が最も良かった [arxiv-1810.11953#c1](https://arxiv.org/pdf/1810.11953v4#page=1 "a two-sample-testing-based approach, using pre-trained classifiers for dimensionality reduction, performs best.") [arxiv-1810.11953#c4](https://arxiv.org/pdf/1810.11953v4#page=6 "In the multivariate-testing case, UAE performed best.")。
その前提(ラベルシフト)が成り立たない場合でもよく機能した [arxiv-1810.11953#c2](https://arxiv.org/pdf/1810.11953v4#page=2 "We show (empirically) that BBSD works surprisingly well under a broad set of shifts, even when the label shift assumption is not met.")。
次元ごとの KS 検定を Bonferroni 補正でまとめる単純な方法が、多変量カーネル検定(MMD)と同程度だった [arxiv-1810.11953#c3](https://arxiv.org/pdf/1810.11953v4#page=6 "despite the heavy correction, multiple univariate testing seem to offer comparable performance to multivariate testing")。
一方、次元削減なしの多変量検定は性能が悪かった [arxiv-1810.11953#c6](https://arxiv.org/pdf/1810.11953v4#page=6 "the multivariate test performs poorly in the no reduction case")。
シフトを判別する分類器を学習する方法は、サンプルが少ないと弱いが、増えると追いつく [arxiv-1810.11953#c5](https://arxiv.org/pdf/1810.11953v4#page=6 "The domain classifier, a popular shift detection approach, performs badly in the low-sample regime (≤100 samples), but catches up as more samples are obtained.")。
また、検出されたシフトが必ずしも有害とは限らない [arxiv-1810.11953#c13](https://arxiv.org/pdf/1810.11953v4#page=9 "this shift does not harm the classifier's performance")。

## 2026年の新しい論文に見る評価の実態

候補 Issue #2 で承認した2026年の論文14本をカード化した。
ドリフト検出器そのものの比較研究は少なく、多くは**検出を部品として使う論文**か、隣接する問題(変化点検出、ストリーム分類、運用監視)の論文だった。
そのため、ここでは「どの検出器が強いか」ではなく、**評価のやり方**に注目して整理する。

### 古典的な検出器は既定値のまま比較される

カード化した論文では、DDM や ADWIN は、比較対象としては**既定値のまま**か、設定の記載なしに使われる例が多い。

- 侵入検知システムの再学習の研究では、DDM と ADWIN を river の既定値で使った [arxiv-2609.04388#c4](https://arxiv.org/pdf/2609.04388v1#page=11 "the river reference implementations of DDM and ADWIN [17, 29] as retraining triggers with always-deploy on fire, run at their registered reference parameters — the implementations’ default DDM thresholds and ADWIN δ = 0.002 — on 8 monitoring labels per window (800 per stream)")。著者自身が、調整していないので結果はこの設定についてのものにすぎず、手法の性質として読むにはパラメータの探索が必要だと断っている [arxiv-2609.04388#c5](https://arxiv.org/pdf/2609.04388v1#page=24 "DDM and ADWIN were run at their registered reference parameters and were not tuned; their cells characterize that configuration, and a parameter sweep would be required before reading them as properties of the methods.")。
- オンライン回帰の SCCM の論文では、ADWIN と KSWIN を scikit-multiflow の既定値で使った [arxiv-2609.09432#c3](https://arxiv.org/pdf/2609.09432v1#page=36 "Specifically, ADWIN used δ = 0.002, while KSWIN used αKS = 0.005, WKS = 100, and SKS = 30.")。評価するストリーム上でグリッドサーチすると先読みのバイアスが入るため、あえて探索しなかったと説明している [arxiv-2609.09432#c4](https://arxiv.org/pdf/2609.09432v1#page=37 "Consequently, no detector candidate grid, designated pilot seed, separate pilot stream, or data-driven detector-parameter selection procedure was used.")。
- ほかにも、DDM [arxiv-2609.25340#c4](https://arxiv.org/pdf/2609.25340v1#page=12 "we measure the predictive performance of the Hoeffding Tree (HT) classifier (Domingos & Hulten, 2000) under different drift scenarios in a test-then-train manner, considering a prompt label availability after the test, as well as when label availability is delayed by 100 samples") や ADWIN [arxiv-2608.23893#c5](https://arxiv.org/pdf/2608.23893v1#page=10 "We further include an ADWIN-triggered adaptation pipeline as a representative drift-detection baseline.") のパラメータの記載が本文に見当たらない論文がある。

上の Cerqueira らは、評価と同じデータでチューニングすると楽観的になると指摘している [arxiv-2606.07789#c8](https://arxiv.org/pdf/2606.07789v1#page=4 "using the same dataset for optimizing and evaluating the detector can cause overfitting and lead to overly optimistic performance estimates reported in the respective papers.")。
この記事の見方では、SCCM の判断はこの指摘と同じ方向だが、その代わりに比較対象は既定値のままになる。
**「調整しない」と「評価データで調整する」の間に、別データで調整するという選択肢がある**。Cerqueira らは、その方法としてデータセットを1つ抜いてチューニングする交差検証を提案している [arxiv-2606.07789#c7](https://arxiv.org/pdf/2606.07789v1#page=4 "we propose a leave-one-dataset-out cross-validation approach for optimizing the hyperparameters of drift detectors.")。

### 提案手法と比較対象の調整のかけ方が違う

- 変化点検出の SWCPD は、自分のハイパーパラメータを固定の経験則で決めている [arxiv-2609.24278#c5](https://arxiv.org/pdf/2609.24278v1#page=19 "For all experiments, hyperparameters were selected according to a fixed set of heuristic rules.")。一方、比較対象の RIO-CPD は窓幅と閾値をグリッドサーチし、AUC が最良の設定を報告している。この選択に別の検証用データを使ったという記述は、本文に見当たらない [arxiv-2609.24278#c6](https://arxiv.org/pdf/2609.24278v1#page=23 "The following hyperparameter resulted in the best AUC scores for RIO-LE:")。この記事の見方では、この場合の非対称は**比較対象の側に有利**に働く。
- 多変量の変化点検出の論文では、比較手法は既定値または原論文の推奨値で動かしている [arxiv-2609.36594#c3](https://arxiv.org/pdf/2609.36594v1#page=12 "For the competing methods, we use their default or paper-recommended tuning parameters and their associated data-driven selection procedures.")。自手法の閾値と次数は、正解の変化点を使わずに標本分割で選んでいる [arxiv-2609.36594#c4](https://arxiv.org/pdf/2609.36594v1#page=12 "To select the candidate pair in a data-driven manner, we evaluate these segments on the even-indexed observations using an empirical kernel score (Steinwart and Ziegel, 2021).")。

### 正解のドリフト時点は、ほとんどが人工的に注入したもの

実データではドリフトが本当に起きたかをほとんど確かめられない [arxiv-2602.06456#c3](https://arxiv.org/pdf/2602.06456v1#page=1 "drift detection is ill-posed, primarily because verification of drift events are implausible in practice.")。そのため、カード化した論文では、正解の時点を使う評価は合成データか人工的な注入に頼っている。

- 生成器の中でドリフトを起こす [arxiv-2608.16659#c2](https://arxiv.org/pdf/2608.16659v1#page=12 "We performed experiments with 13 real-world datasets made available in [32] and 24 synthetic datasets retrieved from [33].") [arxiv-2609.25340#c3](https://arxiv.org/pdf/2609.25340v1#page=11 "For this analysis, we generate streams of 20,000 samples with a drift event introduced every 2,000 samples.")
- 実データに、決めた区間で小さなずれを注入する [doi-10.1007_s44163-026-02063-9#c3](https://link.springer.com/content/pdf/10.1007/s44163-026-02063-9.pdf#page=8 "The selected interval was an experimental segmentation choice rather than an estimated drift location in the original datasets.") [doi-10.1007_s44163-026-02063-9#c4](https://link.springer.com/content/pdf/10.1007/s44163-026-02063-9.pdf#page=11 "At maximum drift intensity, every standardized feature was multiplied by 1.05 and shifted by 0.05 standardized units.")。著者は、これは再現可能なストレステストであって、一般的な検出性能を示すものではないと述べている [doi-10.1007_s44163-026-02063-9#c5](https://link.springer.com/content/pdf/10.1007/s44163-026-02063-9.pdf#page=29 "It is useful as a reproducible stress test, but it does not establish general concept-drift detection")
- 実データの異なる状態のデータを徐々に混ぜる [arxiv-2609.04388#c6](https://arxiv.org/pdf/2609.04388v1#page=24 "The core drift trajectories are gradual mixing ramps between real regime pools (covariate/regime drift); we do not isolate a p(y/x) change, and recurrent drift is untested.")
- 特徴量の平均をずらす [arxiv-2609.24278#c4](https://arxiv.org/pdf/2609.24278v1#page=10 "We randomly select a total of 3 features for which we inject a drift by offsetting the mean ci randomly sampled within (−3, 3) for each drifted feature.")、既知の位置に変化点を入れる [arxiv-2609.36594#c5](https://arxiv.org/pdf/2609.36594v1#page=13 "We use D = 100 and 100 independent repetitions per setting.")
- SCCM は、実データには注釈付きのドリフト時点がないため、検出の指標を合成ストリームだけで計算している [arxiv-2609.09432#c5](https://arxiv.org/pdf/2609.09432v1#page=40 "Because the real-world datasets do not provide annotated drift locations or known concept boundaries, ground-truth alarm-quality metrics are evaluated only on the synthetic datasets.")
- Microsoft の運用事例(ProxyDrift) [arxiv-2608.08245#c6](https://arxiv.org/pdf/2608.08245v1#page=2 "PROXYDRIFT has been deployed in a major cloud-based productivity suite serving hundreds of millions of users, where it monitors multiple application scenarios continuously and generates synthetic evaluation data on a weekly cadence.") には、ラベル付きのドリフトの事例がない [arxiv-2608.08245#c4](https://arxiv.org/pdf/2608.08245v1#page=7 "Reference distributions were computed from a week of production traffic (2026-04-02 to 2026-04-08).")

### 閾値をどこで決めるか

- ドリフト前の較正用の窓で、検出スコアの 0.95 分位点を閾値にする [arxiv-2609.04388#c3](https://arxiv.org/pdf/2609.04388v1#page=8 "thresholds are the 0.95 quantile of detector scores over 30 pre-drift calibration windows; the trigger is 3 consecutive alarms with a 10-window cooldown; windows contain 128 flows.")
- 分布内のデータだけで閾値を較正する [arxiv-2609.33940#c4](https://arxiv.org/pdf/2609.33940v1#page=6 "Both thresholds are calibrated from in-distribution data alone with no labeled failures, and yield zero in-distribution false positives on Push-T and a 1% false-alarm rate on TwoRoom.")。ただし、どの層の信号を使うかは、事後的に最良だった層と比べて報告している [arxiv-2609.33940#c5](https://arxiv.org/pdf/2609.33940v1#page=9 "Layer-0 suffices for Push-T (AUC within 0.02 of oracle in-distribution, within 0.01 out-of-distribution), whereas layer-5 (deepest) is consistently oracle-optimal across all seeds and regimes on TwoRoom.")
- 報告する指標は閾値に依存しない AUROC で、実際の使用では閾値を1つ置けばよいとしている [arxiv-2609.39473#c4](https://arxiv.org/pdf/2609.39473v1#page=20 "In practice, FAME requires no such ground-truth labels; thresholding the normalized projection of the concept drift onto the readout direction is sufficient for distinguishing faithful from false memories, as described in Alg. 1.")
- 音声の偽造検出の論文は、シフト先のデータで閾値を掃引した指標(EER)と、学習時の閾値をそのまま使った正解率を両方出している。両者の差は「閾値をシフトの向こう側へ持ち越すコスト」であり、閾値はシフト先のラベル付きデータで推定し直すべきだと述べている [arxiv-2610.00649#c4](https://arxiv.org/pdf/2610.00649v1#page=5 "The threshold should be re-estimated on a small labeled sample from the target domain rather than carried over from training.")

### 検出しても、それで終わりではない

- 侵入検知の論文は、**ドリフトの検出と、再学習したモデルへの入れ替えの判断とを分けて考える**べきだとする [arxiv-2609.04388#c1](https://arxiv.org/pdf/2609.04388v1#page=1 "Adaptive network intrusion detection systems retrain classifiers after drift alarms, but an alarm detects change; it does not establish that a challenger should replace the deployed incumbent.")。前処理を古いモデルのまま凍結していたことが、入れ替えの見かけの害を大きくしていた [arxiv-2609.04388#c2](https://arxiv.org/pdf/2609.04388v1#page=1 "Incumbent-owned frozen preprocessing amplified apparent promotion harm; with self-contained challenger pipelines the mean full-drift harm did not persist.")。
- 因果の観点からドリフトを分類した論文では、ある条件(内生的なドリフト、非線形の写像)で、DDM による作り直しが Hoeffding Tree の役に立っていないように見えた [arxiv-2609.25340#c5](https://arxiv.org/pdf/2609.25340v1#page=12 "DDM does not seem to provide any advantage over the HT – the triggers in concept drift actually seem to decrease the immediate accuracy more than if not using DDM.")。この記事の見方では、条件は違うが、検出器を付けても性能が上がるとは限らないという点で、Window Dilemma [arxiv-2602.06456#c6](https://arxiv.org/pdf/2602.06456v1#page=1 "indicates that the type of classifier is often more important than drift-awareness.") や Aguiar & Cano [arxiv-2311.06396#c8](https://arxiv.org/pdf/2311.06396v2#page=21 "completely retraining the classifier resulted in decreased accuracy across all evaluated scenarios.") と同じ方向の観察である。
- ProxyDrift は、人手で作った従来のオフライン評価セットが、実際の運用のデータと大半の観点でずれていたと報告している [arxiv-2608.08245#c5](https://arxiv.org/pdf/2608.08245v1#page=8 "By contrast, the legacy hand-curated test set fails on most dimensions, with individual per-dimension alignment scores typically below 0.40 and the overall alignment score in the bad range.")。

### 検出そのものではないが関連する論文

- **ストリーム分類**: ドリフトに適応する決定木。内部の検出器には、著者らの以前の比較に基づいて HDDM_A を選んでいる [arxiv-2608.16659#c5](https://arxiv.org/pdf/2608.16659v1#page=15 "The detector used in all LAST versions was HDDMA [44], given the analysis done in [6].")。合成のドリフトではほとんど効果がなく、改善は主に実データで出た [arxiv-2608.16659#c6](https://arxiv.org/pdf/2608.16659v1#page=18 "Figure 6 shows that on synthetic data the proposed trees have little effect, with the F1-Score difference to HT staying close to zero for all ensembles.")。
- **定義が明示的に改訂される場合の更新**: [arxiv-2608.23893#c1](https://arxiv.org/pdf/2608.23893v1#page=1 "We introduce a provenance-guided incremental learning framework that compiles consecutive concept definitions into a structured rule delta, traces the changed components through historical provenance")
- **運用プロセスの概念的な整理**: 監視を制御ループの一部とみなす [arxiv-2608.17824#c2](https://arxiv.org/pdf/2608.17824v1#page=7 "In lifecycle terms, drift converts maintenance from a reactive, ticket-driven activity into the closed-loop control problem of Equation (1): monitors estimate the deployed configuration’s distance from its validated operating envelope")。著者自身が、根拠の多くはレビューや事例報告で、比較可能な実験はほとんどないと述べている [arxiv-2608.17824#c4](https://arxiv.org/pdf/2608.17824v1#page=9 "However, the evidence base is dominated by literature reviews, taxonomies, interview and survey studies, and single-organization experience reports; comparable experiments, participant-level statistics, and pooled effect sizes are largely absent.")。
- **グラフのシフト下での不確実性** [arxiv-2609.35703#c2](https://arxiv.org/pdf/2609.35703v1#page=1 "Standalone DSS-GNN achieves the lowest Brier score among the compared uncertainty-aware baselines on all 14 node classification benchmarks without post-hoc correction")、**LLM エージェントの誤った記憶の検出** [arxiv-2609.39473#c2](https://arxiv.org/pdf/2609.39473v1#page=1 "Empirical experiments reveal that simply monitoring answers often fails to detect false memory, while FAME achieves AUROCs of 76.2% – 96.7% across false-memory settings")、**世界モデルの失敗予測** [arxiv-2609.33940#c2](https://arxiv.org/pdf/2609.33940v1#page=1 "Moreover, centroid-based methods outperform baseline methods as distribution-shift detectors."): 「シフト」「ドリフト」という言葉は使っているが、データストリームのドリフト検出とは別の問題である。

## 現時点での整理

- **評価方法が未成熟**: 合成データへの依存、指標の不統一、チューニングの不透明さが指摘されている [arxiv-2606.07789#c1](https://arxiv.org/pdf/2606.07789v1#page=1 "studies rely on oversimplified synthetic data generators, adopt incompatible metrics, and lack transparency in hyperparameter selection")。実データではドリフトの有無自体を確かめにくい [arxiv-2602.06456#c3](https://arxiv.org/pdf/2602.06456v1#page=1 "drift detection is ill-posed, primarily because verification of drift events are implausible in practice.")。その結果、検出器の順位は論文によって正反対にもなる(上の食い違いを参照)。どれか1つの論文の「最良の検出器」を一般論として受け取るのは危険である。
- **監視する信号の選択**: 誤り率ベースの検出器は誤検知が多くなりやすい [arxiv-2311.06396#c10](https://arxiv.org/pdf/2311.06396v2#page=24 "Drift detectors that rely on error rates often generate numerous false alarms.")。ラベルを使わない検出器は、正解だけの変化を捉えられない [arxiv-2606.07789#c12](https://arxiv.org/pdf/2606.07789v1#page=8 "Unsupervised detectors (ABCD(X) and STUDD) perform better on feature-space drifts (feature permutation, feature filtering) than on label-based changes (class prior, class swaps)")。現実には正解ラベルがすぐ得られない場面も多い [arxiv-2004.05785#c11](https://arxiv.org/pdf/2004.05785v1#page=14 "Most existing drift detection and adaptation algorithms assume the ground true label is available after classification/prediction, or extreme verification latency.") [doi-10.1007_s41060-024-00620-y#c1](https://elib.dlr.de/206088/1/Lukats_et_al-2024-International_Journal_of_Data_Science_and_Analytics.pdf#page=1 "Most algorithms proposed in the literature depend on the immediate availability of ground truth class labels.")。教師なしの検出器では、D3 が2本の独立した研究で良い結果を出している [doi-10.1007_s41060-024-00620-y#c7](https://elib.dlr.de/206088/1/Lukats_et_al-2024-International_Journal_of_Data_Science_and_Analytics.pdf#page=13 "In these experiments, D3 outperforms other detectors by a large margin") [arxiv-2602.06456#c7](https://arxiv.org/pdf/2602.06456v1#page=7 "Of the drift detectors, D3-HT performed the best for both the NB and HT base models.")。
- **間接的な評価指標の偏り**: 分類器の精度でドリフト検出器を評価すると、警報の多い検出器が有利になる [doi-10.1007_s41060-024-00620-y#c9](https://elib.dlr.de/206088/1/Lukats_et_al-2024-International_Journal_of_Data_Science_and_Analytics.pdf#page=18 "classifier predictive performance is biased in favor of a higher number of detected concept drifts and adaptations.") [arxiv-2602.06456#c5](https://arxiv.org/pdf/2602.06456v1#page=4 "concept drift detectors that detect more frequently, tend to perform better (up to a point).")。検出器の比較では、正解のドリフト時点を使った直接の評価かどうかを確認する必要がある。
- **検出の後の対応**: 検出のたびに作り直すのが最善とは限らない [arxiv-2311.06396#c8](https://arxiv.org/pdf/2311.06396v2#page=21 "completely retraining the classifier resulted in decreased accuracy across all evaluated scenarios.")。過去のデータを残して定期的に学習し直す単純な方法が強いという報告もある [arxiv-2602.06456#c9](https://arxiv.org/pdf/2602.06456v1#page=7 "our results suggest that keeping past data is often useful and periodically retraining a model on increasingly large training sets is often an effective strategy.")。
- **データシフトの監視(MLOps)**: 運用中のモデル自身の出力に単純な単変量検定をかける方法が、扱いやすく強い [arxiv-1810.11953#c1](https://arxiv.org/pdf/1810.11953v4#page=1 "a two-sample-testing-based approach, using pre-trained classifiers for dimensionality reduction, performs best.") [arxiv-1810.11953#c3](https://arxiv.org/pdf/1810.11953v4#page=6 "despite the heavy correction, multiple univariate testing seem to offer comparable performance to multivariate testing")。ただし検出は「有害かどうか」とは別の問題である [arxiv-1810.11953#c13](https://arxiv.org/pdf/1810.11953v4#page=9 "this shift does not harm the classifier's performance")。実際の機械学習パイプラインでは、入力のシフトの確認自体がほとんど行われていないという指摘もある [arxiv-1810.11953#c8](https://arxiv.org/pdf/1810.11953v4#page=1 "in practice, ML pipelines rarely inspect incoming data for signs of distribution shift.")。
- **評価の設計の偏り(2026年の論文)**: カード化した論文では、古典的な検出器を調整せず既定値のまま比較対象にする例が多い [arxiv-2609.04388#c5](https://arxiv.org/pdf/2609.04388v1#page=24 "DDM and ADWIN were run at their registered reference parameters and were not tuned; their cells characterize that configuration, and a parameter sweep would be required before reading them as properties of the methods.") [arxiv-2609.09432#c4](https://arxiv.org/pdf/2609.09432v1#page=37 "Consequently, no detector candidate grid, designated pilot seed, separate pilot stream, or data-driven detector-parameter selection procedure was used.")。提案手法と比較対象のチューニングが非対称な論文もある [arxiv-2609.24278#c6](https://arxiv.org/pdf/2609.24278v1#page=23 "The following hyperparameter resulted in the best AUC scores for RIO-LE:")。正解の時点を使う評価は、合成データか人工的な注入によるものがほとんどだった(上の節を参照。例: [arxiv-2609.09432#c5](https://arxiv.org/pdf/2609.09432v1#page=40 "Because the real-world datasets do not provide annotated drift locations or known concept boundaries, ground-truth alarm-quality metrics are evaluated only on the synthetic datasets."))。論文を読むときは、**比較対象をどう設定し、正解の時点をどう作り、閾値をどのデータで決めたか**を確認する。
- **答えられることの範囲**: 既存の検出器が答えられるのは「いつ」までで、「どこで」「どのように」はほとんど答えられない [arxiv-2004.05785#c10](https://arxiv.org/pdf/2004.05785v1#page=14 "all drift detection methods can answer 'When', but very few methods have the ability to answer 'How' and 'Where';")。

**この整理に含まれていないもの**: DDM・ADWIN・Page-Hinkley などの原論文(arXiv にないため未取得)、表データでのデータシフト検出のベンチマーク、ラベルシフト推定の手法。

## 参照カード

- [arxiv-2004.05785](../../papers/arxiv-2004.05785.yaml) Lu et al., "Learning under Concept Drift: A Review"
- [arxiv-1810.11953](../../papers/arxiv-1810.11953.yaml) Rabanser et al., "Failing Loudly: An Empirical Study of Methods for Detecting Dataset Shift" (NeurIPS 2019)
- [arxiv-2311.06396](../../papers/arxiv-2311.06396.yaml) Aguiar & Cano, "A comprehensive analysis of concept drift locality in data streams"
- [arxiv-2606.07789](../../papers/arxiv-2606.07789.yaml) Cerqueira et al., "A Framework for Evaluating and Benchmarking Concept Drift Detection Methods" (KDD 2026)
- [arxiv-2602.06456](../../papers/arxiv-2602.06456.yaml) Gower-Winter et al., "The Window Dilemma: Why Concept Drift Detection is Ill-Posed"
- [doi-10.1007_s41060-024-00620-y](../../papers/doi-10.1007_s41060-024-00620-y.yaml) Lukats et al., "A benchmark and survey of fully unsupervised concept drift detectors on real-world data streams" (Int. J. Data Sci. Anal.)
- [arxiv-2310.15826](../../papers/arxiv-2310.15826.yaml) Hinder et al., "One or Two Things We know about Concept Drift -- A Survey on Monitoring Evolving Environments"
- [arxiv-2609.04388](../../papers/arxiv-2609.04388.yaml) Fernández-Barrios et al., "Candidate Comparability Before Promotion: Conditional Validation in Adaptive Network Intrusion Detection"
- [arxiv-2609.24278](../../papers/arxiv-2609.24278.yaml) Jacob et al., "High-Dimensional Online Change Point Detection with Adaptive Thresholding and Interpretability"
- [arxiv-2609.25340](../../papers/arxiv-2609.25340.yaml) Barboza et al., "Concept Drift from a Causal Perspective"
- [doi-10.1007_s44163-026-02063-9](../../papers/doi-10.1007_s44163-026-02063-9.yaml) Jawad et al., "Awareness based internal reliability monitoring of streaming models using incremental principal component analysis"
- [arxiv-2609.09432](../../papers/arxiv-2609.09432.yaml) Abu-Shaira et al., "SCCM : Stream Cruise Control Method for Automated Drift Detection and Adaptation"
- [arxiv-2608.23893](../../papers/arxiv-2608.23893.yaml) Lamaakal, "Provenance Guided Incremental Learning Under Evolving Concept Definitions"
- [arxiv-2608.17824](../../papers/arxiv-2608.17824.yaml) Alenezi, "Reshaping the SDLC for Data- and AI-Centric Systems"
- [arxiv-2608.16659](../../papers/arxiv-2608.16659.yaml) Assis et al., "Hoeffding adaptive splitting trees for data stream classification with concept drift and ensemble learning"
- [arxiv-2608.08245](../../papers/arxiv-2608.08245.yaml) Levit et al., "Privacy-Preserving Data Drift Detection and Recovery for Large-Scale LLM Applications via Proxy Representations"
- [arxiv-2610.00649](../../papers/arxiv-2610.00649.yaml) Amin et al., "On Evaluating Quantum Kernel Robustness for Low-Resource Cross-Corpus Audio Deepfake Detection"
- [arxiv-2609.39473](../../papers/arxiv-2609.39473.yaml) Tran et al., "Beyond the Shadows of Plato's Cave: Evaluating False Memory in Autonomous Agents via Counterfactual Reasoning"
- [arxiv-2609.36594](../../papers/arxiv-2609.36594.yaml) Luo et al., "Optimal detection of general moment changes: Simultaneous mean and covariance change detection and beyond"
- [arxiv-2609.35703](../../papers/arxiv-2609.35703.yaml) Xu et al., "A Unified Uncertainty Representation for Graph Neural Networks via Doubly-Spectral Stochastic Expansion"
- [arxiv-2609.33940](../../papers/arxiv-2609.33940.yaml) Walker et al., "Behavioral Monitoring of JEPA World Models with Jacobian Centroids"
