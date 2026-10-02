---
title: モデルと評価方法の弱点、それを改善した研究
kind: topic
tags: [tabular-classification, tabular-regression, drift-detection, concept-drift-detection, dataset-shift-detection, time-series-anomaly-detection]
depends_on: [arxiv-2106.03253, arxiv-2106.11959, arxiv-2207.08815, arxiv-2207.01848, arxiv-2305.02997, arxiv-2506.16791, doi-10.1038_s41586-024-08328-6, arxiv-2410.24210, arxiv-2407.04491, arxiv-2004.05785, arxiv-1810.11953, arxiv-2311.06396, arxiv-2606.07789, arxiv-2602.06456, doi-10.1007_s41060-024-00620-y, arxiv-2310.15826, arxiv-2109.05257, arxiv-2009.13807, arxiv-2308.13068, arxiv-2506.18046, arxiv-2211.05244]
written_at: 2026-10-02
written_by: claude-opus-5-5 via Claude Code
---

# モデルと評価方法の弱点、それを改善した研究

<!-- generated:stale -->
> 未反映のカードはありません。
<!-- /generated:stale -->

## この記事の読み方

このリポジトリにある論文から、「ある論文がモデルや評価方法の**弱点を指摘**し、別の(または同じ)論文が**改善策を提案して検証**した」という流れを、テーマを横断して集めた。

各項目は「問題点 → 改善策 → 検証 → 独立した確認」の順に書く。注意点が2つある。

- **論文をまたいで「この指摘にこの改善が対応する」と結び付けるのは、多くの場合この記事の整理**である。改善策の論文が、指摘した論文に明示的に応答しているとは限らない。そういう箇所は本文で明記する。
- **「独立した確認」**は、改善策を提案した著者と重ならない著者が、別の条件で同じ方向の結果を出しているかを指す。提案者自身による検証しかないものは、そう書く。

## 一覧

| 問題点 | 改善策 | 検証したのは | 独立した確認 |
|---|---|---|---|
| MLP は無関係な特徴量に弱く、特徴量の回転に不変 | 埋め込み層、特徴量ごとのスケーリング層 | RealMLP の著者自身 | 部分的 |
| MLP の過学習と最適化の難しさ | 重みを共有した効率的なアンサンブル(TabM) | TabM の著者自身 | TabArena(著者の重なりなし) |
| 初期の TabPFN は小規模・数値特徴のみ | TabPFN v2 | TabPFN v2 の著者自身 | TabArena(著者が重なる) |
| 論文ごとのデータセット選択とチューニングの偏り | チューニング用と評価用のデータを分ける | 表データとドリフト検出の両分野で、別々の著者 | 発想として一致 |
| 時系列異常検知の point-adjust による過大評価 | PA%K、イベント単位の評価、単純な基準線 | 提案した著者自身 | 指摘そのものは3本で一致 |
| ドリフト検出器の評価の不統一 | 実データへのドリフト注入、時間を考慮した指標 | 提案した著者自身 | 未確認 |
| ドリフト検出が正解ラベルに依存 | 教師なし検出器 | 比較研究 | D3 の強さは2本で一致 |

以下、項目ごとに根拠を示す。

## 表データのモデル

### MLP の弱点と、それを補う設計

**問題点**: Grinsztajn らは、MLP 系のモデルが無関係な特徴量に弱いこと [arxiv-2207.08815#c5](https://arxiv.org/pdf/2207.08815v1#page=7 "This shows that MLPs are less robust to uninformative features")、特徴量の回転に対して不変で列ごとの意味を活かせないこと [arxiv-2207.08815#c6](https://arxiv.org/pdf/2207.08815v1#page=7 "only Resnets are rotationally invariant")、滑らかな関数に偏ること [arxiv-2207.08815#c4](https://arxiv.org/pdf/2207.08815v1#page=6 "For small lengthscales, smoothing the target function on the train set decreases markedly the accuracy of tree-based models, but barely impacts that of NNs.") を、データを加工する実験で示した。
TabM の著者も、表データの MLP は過学習と最適化の問題を抑えて初めて力を発揮すると述べている [arxiv-2410.24210#c21](https://arxiv.org/pdf/2410.24210v3#page=2 "one has to deal with overfitting and optimization issues to reveal that potential.")。

**改善策と検証**:

- **埋め込み層**: Grinsztajn ら自身が、数値特徴量にも埋め込み層を入れる先行研究の改善は、回転不変性を壊すことで説明できるとしている [arxiv-2207.08815#c16](https://arxiv.org/pdf/2207.08815v1#page=8 "The fact that very different types of embeddings seem to improve performance suggests that the sheer presence of an embedding which breaks the invariance is a key part of these improvements.")。また、適切な正則化と最適化があれば、MLP も不規則なパターンを学べる可能性を認めている [arxiv-2207.08815#c17](https://arxiv.org/pdf/2207.08815v1#page=7 "as adequate regularization and careful optimization may allow NNs to learn irregular patterns.")。
- **RealMLP**: 特徴量ごとに学習するスケーリング層で、緩やかな特徴量選択を促す [arxiv-2407.04491#c22](https://arxiv.org/pdf/2407.04491v3#page=5 "To encourage (soft) feature selection, we introduce a scaling layer before the first linear layer")。外れ値は、頑健なスケーリングと滑らかなクリッピングで抑える [arxiv-2407.04491#c23](https://arxiv.org/pdf/2407.04491v3#page=4 "Intuitively, when features have large outliers, smooth clipping prevents the outliers from affecting the result too strongly")。著者の実験では、構造の改良だけでも素の MLP の性能は上がったが、学習方法や既定値などの構造以外の要素も同じくらい重要だった [arxiv-2407.04491#c24](https://arxiv.org/pdf/2407.04491v3#page=10 "our architectural improvements alone are beneficial when applied to MLP-D directly, although non-architectural aspects are at least as important.")。結果として、自分たちのベンチマークでは GBDT と競える水準になった [arxiv-2407.04491#c1](https://arxiv.org/pdf/2407.04491v3#page=1 "RealMLP offers a favorable time-accuracy tradeoff compared to other neural baselines and is competitive with GBDTs in terms of benchmark scores.")。
- **TabPFN v2**: 無関係な特徴量や外れ値に対して非常に頑健だと報告している [doi-10.1038_s41586-024-08328-6#c15](https://www.nature.com/articles/s41586-024-08328-6.pdf#page=6 "The results show that TabPFN is very robust to uninformative features and outliers")。

**この記事の整理として**: RealMLP のスケーリング層と TabPFN v2 の頑健性は、Grinsztajn らが指摘した「無関係な特徴量への弱さ」に対応する改善と読める。ただし、どちらの論文も、Grinsztajn らの指摘に応答する形では検証していない。

**独立した確認**: 部分的にある。RealMLP の改良が GBDT と競えるという結果は、Grinsztajn らのデータセットの分類では成り立たなかった(RealMLP 論文の勝敗表を参照)。条件によって効果が変わることを、著者自身が認めている [arxiv-2407.04491#c9](https://arxiv.org/pdf/2407.04491v3#page=10 "For classification, using AUROC instead of classification error (Figure 3, Appendix B.5) favors GBDTs.") [arxiv-2407.04491#c10](https://arxiv.org/pdf/2407.04491v3#page=10 "The use of different aggregation metrics than the shifted geometric mean reduces the advantage of TD methods")。

### 効率的なアンサンブルで MLP を強くする(TabM)

**改善策**: TabM は、重みの大半を共有した多数の MLP を同時に学習する [arxiv-2410.24210#c11](https://arxiv.org/pdf/2410.24210v3#page=2 "the two key reasons for TabM's high performance are the collective training of the underlying implicit MLPs and the weight sharing.")。重みの共有は、表データで効果的な正則化として働いた [arxiv-2410.24210#c10](https://arxiv.org/pdf/2410.24210v3#page=5 "Thus, constraining the ensemble with weight sharing turns out to be a highly effective regularization on tabular tasks.")。

**検証**: 著者の46データセットでの比較では、深層学習の中で最良だった [arxiv-2410.24210#c1](https://arxiv.org/pdf/2410.24210v3#page=1 "In particular, we find that TabM demonstrates the best performance among tabular DL models.")。GBDT とは「十分に競える」という表現にとどまる [arxiv-2410.24210#c5](https://arxiv.org/pdf/2410.24210v3#page=2 "TabM easily competes with GBDT and outperforms prior tabular DL models")。

**独立した確認**: TabArena では、設定のアンサンブルを含めて比べると、TabM を含むニューラルネットが最強の単一モデルになった [arxiv-2506.16791#c12](https://arxiv.org/pdf/2506.16791v4#page=7 "after post-hoc ensembling, neural networks are the strongest single models on average in TabArena-v0.1.")。TabArena の著者は TabM の著者と重ならない(TabArena の利益相反の開示に TabM は含まれない [arxiv-2506.16791#c22](https://arxiv.org/pdf/2506.16791v4#page=11 "D.H. is one of the authors of RealMLP and one of the authors of TabICL.") [arxiv-2506.16791#c23](https://arxiv.org/pdf/2506.16791v4#page=11 "L.P. and F.H. are a subset of the authors of TabPFNv2."))。この点で、TabM の強さには比較的独立した裏付けがある。

### 初期の TabPFN の制約と TabPFN v2

**問題点**: 2023年版の TabPFN は、訓練1,000件以下・数値特徴のみ・10クラス以下という小規模な問題が対象で [arxiv-2207.01848#c2](https://arxiv.org/pdf/2207.01848v6#page=2 "tasks (≤1 000 training examples, ≤100 purely numerical features without missing values and ≤10 classes)")、構造上大きなデータに広げにくかった [arxiv-2207.01848#c12](https://arxiv.org/pdf/2207.01848v6#page=10 "the underlying Transformer architecture only scales to small datasets")。カテゴリ特徴や欠損値があると弱くなった [arxiv-2207.01848#c7](https://arxiv.org/pdf/2207.01848v6#page=9 "Generally, TabPFN is less strong when categorical features or missing values are present.")。

**改善策と検証**: TabPFN v2 は、扱えるデータの規模を大きく広げ、回帰・カテゴリ特徴・欠損値に対応したと報告している [doi-10.1038_s41586-024-08328-6#c3](https://www.nature.com/articles/s41586-024-08328-6.pdf#page=2 "the new TabPFN scales to 50× larger datasets; supports regression tasks, categorical data and missing values; and is robust to unimportant features and outliers.")。1万件以下のデータでは、既存手法を大きく上回った [doi-10.1038_s41586-024-08328-6#c1](https://www.nature.com/articles/s41586-024-08328-6.pdf#page=1 "a tabular foundation model that outperforms all previous methods on datasets with up to 10,000 samples by a wide margin, using substantially less training time.")。ただし著者自身、この結果は1万件・500特徴を超える規模での性能の根拠にはならないと断っている [doi-10.1038_s41586-024-08328-6#c14](https://www.nature.com/articles/s41586-024-08328-6.pdf#page=6 "these results should not be taken as evidence that TabPFN scales well beyond the 10,000 samples and 500 features considered here.")。

**独立した確認**: TabArena も、適用条件内のデータで TabPFNv2 が大差で上位だったと報告している [arxiv-2506.16791#c13](https://arxiv.org/pdf/2506.16791v4#page=7 "TabPFNv2 outperforms related approaches by a large margin, establishing tabular foundation models as the go-to solution for datasets within their constraints.")。ただし、TabArena の著者2名は TabPFNv2 の著者でもあり [arxiv-2506.16791#c23](https://arxiv.org/pdf/2506.16791v4#page=11 "L.P. and F.H. are a subset of the authors of TabPFNv2.")、TabPFN v2 の著者2名は表データ基盤モデルの企業に所属している [doi-10.1038_s41586-024-08328-6#c18](https://www.nature.com/articles/s41586-024-08328-6.pdf#page=13 "F.H. and N.H. are affiliated with PriorLabs, a company focused on developing tabular foundation models.")。著者の重ならない検証としては、2023年版を対象にした TabZilla の結果がある。TabZilla では、訓練データを間引いて使っても、平均で全手法を上回った [arxiv-2305.02997#c3](https://arxiv.org/pdf/2305.02997v4#page=1 "we find that it outperforms all other algorithms on average, even when randomly sampling 3000 training datapoints.")。

### 注意機構ベースのモデルの計算コスト

**問題点**: FT-Transformer の提案者自身が、ResNet より多くの計算資源を要し、特徴量が非常に多いと扱いにくいと認めていた [arxiv-2106.11959#c9](https://arxiv.org/pdf/2106.11959v5#page=5 "FT-Transformer requires more resources (both hardware and time) for training than simple models such as ResNet")。

**その後の確認**: 同じグループの TabM 論文で、注意機構や検索ベースのモデルは、大規模データでは学習時間が極端に長いか、そのままでは適用できないことが示された [arxiv-2410.24210#c14](https://arxiv.org/pdf/2410.24210v3#page=8 "As expected, attention- and retrieval-based models struggle, yielding extremely long training times, or being simply inapplicable without additional effort.")。MLP 系が最速で、TabM がそれに次ぐ [arxiv-2410.24210#c13](https://arxiv.org/pdf/2410.24210v3#page=8 "Simple MLPs are the fastest DL models, with TabM being the runner-up.")。両論文に共通の著者がいるため、独立した確認ではない。

## 評価方法の弱点と改善

### チューニングと評価に同じデータを使う問題

**問題点**: Shwartz-Ziv らは、深層モデルが自分の論文のデータセットでだけ強く見えることを示し [arxiv-2106.03253#c4](https://arxiv.org/pdf/2106.03253v2#page=6 "Each deep model was better only on the datasets that appeared in its own paper.")、その理由として、データセット選択の偏り [arxiv-2106.03253#c5](https://arxiv.org/pdf/2106.03253v2#page=6 "The first possibility is selection bias.") とチューニング努力の差 [arxiv-2106.03253#c6](https://arxiv.org/pdf/2106.03253v2#page=6 "The second possibility is differences in the optimization of hyperparameters.") を挙げた。

**改善策**: 同じ発想の対策が、**別の分野で別の著者によって**提案されている。

- **表データ(RealMLP)**: 既定値を調整するメタ訓練用のデータと、評価するメタテスト用のデータを分けた [arxiv-2407.04491#c3](https://arxiv.org/pdf/2407.04491v3#page=1 "We tune RealMLP and the default parameters on a meta-train benchmark with 118 datasets and compare them to hyperparameter-optimized versions on a disjoint meta-test benchmark with 90 datasets")。調整済みの既定値はメタテストにもよく移った [arxiv-2407.04491#c7](https://arxiv.org/pdf/2407.04491v3#page=9 "indicating that the tuned defaults transfer very well to the meta-test benchmark.")。
- **ドリフト検出(Cerqueira ら)**: 同じデータでチューニングと評価をすると楽観的になると指摘し [arxiv-2606.07789#c8](https://arxiv.org/pdf/2606.07789v1#page=4 "using the same dataset for optimizing and evaluating the detector can cause overfitting and lead to overly optimistic performance estimates reported in the respective papers.")、データセットを1つ抜いてチューニングする方法を提案した [arxiv-2606.07789#c7](https://arxiv.org/pdf/2606.07789v1#page=4 "we propose a leave-one-dataset-out cross-validation approach for optimizing the hyperparameters of drift detectors.")。この方法でのチューニングは、既定の設定より検出性能を大きく上げた [arxiv-2606.07789#c4](https://arxiv.org/pdf/2606.07789v1#page=2 "hyperparameter optimization using our proposed approach significantly improves detection performance over default configurations.")。

**この記事の整理として**: 「調整に使ったデータで評価しない」という同じ原則が、2つの分野で独立に採用されていることは、この原則の一般性を示している。

### 時系列異常検知の point-adjust

**問題点**: point-adjust を使うと、ランダムなスコアでも最先端に見える。これは Kim ら [arxiv-2109.05257#c1](https://arxiv.org/pdf/2109.05257v2#page=1 "the PA protocol has a great possibility of overestimating the detection performance; that is, even a random anomaly score can easily turn into a state-of-the-art TAD method.")、Sehili ら [arxiv-2308.13068#c2](https://arxiv.org/pdf/2308.13068v2#page=1 "So flawed is one very popular protocol, the so-called point-adjust protocol, that a random guess can be shown to systematically outperform all algorithms developed so far.")、TAB [arxiv-2506.18046#c6](https://arxiv.org/pdf/2506.18046v2#page=2 "even random methods have a good chance to predict at least one point in larger anomaly windows") の3本が独立に指摘している。

**改善策**:

- **PA%K**(Kim ら): 区間の中で一定割合以上を検出したときだけ区間全体を検出とみなす。過大評価と過小評価の両方を和らげる [arxiv-2109.05257#c12](https://arxiv.org/pdf/2109.05257v2#page=4 "which can mitigate the overestimation effect of F1PA and the possibility of underestimation of F1.")。
- **単純な基準線**(Kim ら): 訓練していないモデルの性能を基準線にする [arxiv-2109.05257#c13](https://arxiv.org/pdf/2109.05257v2#page=4 "we suggest establishing a new baseline with the F1 measured from the prediction of a randomly initialized reconstruction model with simple architecture")。
- **イベント単位の評価**(Sehili ら): 点単位の評価がすべてのデータに適するわけではないとして提案された [arxiv-2308.13068#c11](https://arxiv.org/pdf/2308.13068v2#page=2 "We also review the more objective point-wise protocol and show that it is not appropriate for all kinds of datasets and use-cases.")。
- **PCA の基準線**(Sehili ら): 単純な前処理と後処理を加えた PCA を基準線にする [arxiv-2308.13068#c3](https://arxiv.org/pdf/2308.13068v2#page=1 "we propose a simple, yet challenging, baseline based on Principal Components Analysis (PCA) that surprisingly outperforms many recent Deep Learning (DL) based approaches on popular benchmark datasets.") [arxiv-2308.13068#c10](https://arxiv.org/pdf/2308.13068v2#page=14 "we use simple pre-processing and post-processing blocks (input scaling, clipping and score smoothing) that significantly improve the score.")。

**検証と独立した確認**: 改善策の検証は、それぞれ提案者自身によるものである。ただし、Sehili らの結果は Kim らの指摘と同じ方向を示している。point-adjust を前提に開発された手法が、他の評価方法ではランダムな推測と区別できなかった [arxiv-2308.13068#c4](https://arxiv.org/pdf/2308.13068v2#page=13 "Algorithms that were developed using point-adjust as the sole target fail to reach any score better than a random guess when evaluated with other")。この点で、問題点の指摘は独立に確認されている。

**改善策自身の限界**: 統一された評価パイプラインを作った TAB でも、すべての閾値のうち最良の値を報告している [arxiv-2506.18046#c9](https://arxiv.org/pdf/2506.18046v2#page=8 "we conduct metric calculations at all thresholds and report the best results.")。閾値をテストデータで選ぶという、より根本的な問題 [arxiv-2109.05257#c14](https://arxiv.org/pdf/2109.05257v2#page=7 "existing TAD methods set the threshold after investigating the test dataset or simply use the optimal threshold that yields the best F1.") は残っている。また、ベンチマークのデータ自体に欠陥があるという指摘 [arxiv-2009.13807#c1](https://arxiv.org/pdf/2009.13807v5#page=1 "These flaws are triviality, unrealistic anomaly density, mislabeled ground truth and run-to-failure bias.") に対しては、新しいアーカイブが作られた [arxiv-2009.13807#c9](https://arxiv.org/pdf/2009.13807v5#page=1 "with this paper we introduce the UCR Time Series Anomaly Archive.")。しかし、その上での比較はこのリポジトリにはまだない。

### ドリフト検出器の評価

**問題点**: 合成データへの依存、指標の不統一、不透明なチューニング [arxiv-2606.07789#c1](https://arxiv.org/pdf/2606.07789v1#page=1 "studies rely on oversimplified synthetic data generators, adopt incompatible metrics, and lack transparency in hyperparameter selection")。従来の指標がストリームの長さに依存すること [arxiv-2606.07789#c5](https://arxiv.org/pdf/2606.07789v1#page=3 "MTFA and MDT are highly dependent on stream length and drift spacing")、F1 では遅い検出も満点になりうること [arxiv-2606.07789#c6](https://arxiv.org/pdf/2606.07789v1#page=3 "its formulation ignores the temporal aspect: a detector with unacceptable delay can still achieve perfect F1.")。

**改善策**: 実データにドリフトを人工的に注入して正解を作り、時間を考慮した指標を使い、データセットを1つ抜いてチューニングする枠組みが提案された [arxiv-2606.07789#c7](https://arxiv.org/pdf/2606.07789v1#page=4 "we propose a leave-one-dataset-out cross-validation approach for optimizing the hyperparameters of drift detectors.")。

**改善策自身の限界**: 著者自身が、元のストリームを並べ替えるため時間構造が失われること [arxiv-2606.07789#c17](https://arxiv.org/pdf/2606.07789v1#page=8 "it also removes any inherent temporal structure.")、正解ラベルがすぐ得られると仮定していること [arxiv-2606.07789#c16](https://arxiv.org/pdf/2606.07789v1#page=8 "it assumes immediate feedback, with labels being readily available at each step after inference.") を限界として挙げている。この枠組みでの結論(SEED・STEPD が上位)は、Aguiar らの結論と食い違う。詳しくは[ドリフト検出の記事](../tasks/drift-detection.md)を参照。

### ドリフト検出が正解ラベルに依存する問題

**問題点**: 多くの検出器は、予測の直後に正解ラベルが得られると仮定している [arxiv-2004.05785#c11](https://arxiv.org/pdf/2004.05785v1#page=14 "Most existing drift detection and adaptation algorithms assume the ground true label is available after classification/prediction, or extreme verification latency.") [doi-10.1007_s41060-024-00620-y#c1](https://elib.dlr.de/206088/1/Lukats_et_al-2024-International_Journal_of_Data_Science_and_Analytics.pdf#page=1 "Most algorithms proposed in the literature depend on the immediate availability of ground truth class labels.")。誤り率ベースの検出器は誤検知も多い [arxiv-2311.06396#c10](https://arxiv.org/pdf/2311.06396v2#page=24 "Drift detectors that rely on error rates often generate numerous false alarms.")。

**改善策と検証**: 入力だけを見る教師なしの検出器が、実データで比較された [doi-10.1007_s41060-024-00620-y#c3](https://elib.dlr.de/206088/1/Lukats_et_al-2024-International_Journal_of_Data_Science_and_Analytics.pdf#page=1 "Seven of these algorithms are evaluated with common concept drift detection metrics on eleven real-world data streams")。D3 が直接の評価で最良だった [doi-10.1007_s41060-024-00620-y#c7](https://elib.dlr.de/206088/1/Lukats_et_al-2024-International_Journal_of_Data_Science_and_Analytics.pdf#page=13 "In these experiments, D3 outperforms other detectors by a large margin")。異常の監視が目的なら、誤差ベースの手法を避けるべきだという指針もある [arxiv-2310.15826#c8](https://arxiv.org/pdf/2310.15826v1#page=27 "loss-based strategies should be avoided when the target of the drift detection is monitoring for anomalous behavior.")。

**独立した確認**: D3 が良いという結果は、Window Dilemma の著者による別の実験でも得られている [arxiv-2602.06456#c7](https://arxiv.org/pdf/2602.06456v1#page=7 "Of the drift detectors, D3-HT performed the best for both the NB and HT base models.")。

**改善策自身の限界**: 教師なしの検出器は、正解だけが変わる変化を捉えられない [arxiv-2606.07789#c12](https://arxiv.org/pdf/2606.07789v1#page=8 "Unsupervised detectors (ABCD(X) and STUDD) perform better on feature-space drifts (feature permutation, feature filtering) than on label-based changes (class prior, class swaps)")。分類器の精度で検出器を評価すると、警報の多い検出器が有利になる [doi-10.1007_s41060-024-00620-y#c9](https://elib.dlr.de/206088/1/Lukats_et_al-2024-International_Journal_of_Data_Science_and_Analytics.pdf#page=18 "classifier predictive performance is biased in favor of a higher number of detected concept drifts and adaptations.")。

### データシフト検出の欠如

**問題点**: 実際の機械学習パイプラインでは、入力のシフトの確認がほとんど行われていない [arxiv-1810.11953#c8](https://arxiv.org/pdf/1810.11953v4#page=1 "in practice, ML pipelines rarely inspect incoming data for signs of distribution shift.")。

**改善策と検証**: 学習済みモデルの出力に二標本検定をかける方法が最も良かった [arxiv-1810.11953#c1](https://arxiv.org/pdf/1810.11953v4#page=1 "a two-sample-testing-based approach, using pre-trained classifiers for dimensionality reduction, performs best.")。前提条件が崩れても機能した [arxiv-1810.11953#c2](https://arxiv.org/pdf/1810.11953v4#page=2 "We show (empirically) that BBSD works surprisingly well under a broad set of shifts, even when the label shift assumption is not met.")。

**改善策自身の限界**: 検証は画像データが中心で [arxiv-1810.11953#c12](https://arxiv.org/pdf/1810.11953v4#page=9 "since we have mostly explored a standard image classification setting for our experiments")、ストリーミングデータへの拡張は今後の課題とされている [arxiv-1810.11953#c14](https://arxiv.org/pdf/1810.11953v4#page=9 "shift detection for online data, which would require us to account for and exploit the high degree of correlation between adjacent time steps")。

## 全体から見えること

- **改善の検証は、提案者自身によるものが多い**。著者の重ならない検証があるのは、TabM(TabArena)と D3(Window Dilemma と Lukats ら)など一部にとどまる。
- **同じ原則が分野をまたいで現れる**。「調整に使ったデータで評価しない」(RealMLP と Cerqueira ら)と「単純な基準線と比べる」(Kim ら、Sehili ら)は、別々の分野・著者から出ている。
- **改善策にも新しい限界がある**。TAB の最良閾値、Cerqueira らの並べ替え、教師なし検出器が正解の変化を捉えられないこと、などである。改善は一度で終わらず、次の指摘につながっている。

**この記事に含まれていないもの**: このリポジトリにまだカードのない、個々の手法の後続論文(TabPFN v2 以後の表データ基盤モデル、AnomalyTransformer などの改良版)。新着論文の候補 Issue には、それらしい論文(TabPFN 系の後継モデルなど)が多数挙がっている。

## 参照カード

この記事は、このリポジトリの21本すべてのカードを対象にしている。個々の根拠は本文のリンクから原論文の該当ページを開ける。カードの一覧は [generated/index.md](../../generated/index.md) を参照。
