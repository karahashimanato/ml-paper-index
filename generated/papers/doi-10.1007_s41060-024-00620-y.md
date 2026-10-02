<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# A benchmark and survey of fully unsupervised concept drift detectors on real-world data streams

- カード: [`doi-10.1007_s41060-024-00620-y`](../../papers/doi-10.1007_s41060-024-00620-y.yaml)
- 著者: Daniel Lukats, Oliver Zielinski, Axel Hahn, Frederic Stahl
- 年・掲載: 2024 International Journal of Data Science and Analytics
- 原論文: [PDF](https://elib.dlr.de/206088/1/Lukats_et_al-2024-International_Journal_of_Data_Science_and_Analytics.pdf)(DLR elib repository copy (OpenAlex labels it acceptedVersion; the PDF has the journal layout)、カード作成時に読んだ版)
- タグ: concept-drift-detection, streaming, two-sample-tests, window-based-drift-detectors
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Most drift detectors in the literature require immediately available true labels, which is unrealistic in many applications.([Abstract, p.1](https://elib.dlr.de/206088/1/Lukats_et_al-2024-International_Journal_of_Data_Science_and_Analytics.pdf#page=1 "Most algorithms proposed in the literature depend on the immediate availability of ground truth class labels."))
- **c2** Ten fully unsupervised detectors are analyzed (architecture, core ideas, assumptions about data).([Abstract, p.1](https://elib.dlr.de/206088/1/Lukats_et_al-2024-International_Journal_of_Data_Science_and_Analytics.pdf#page=1 "Ten algorithms are analyzed in terms of architectural choices, core ideas and assumptions about data"))
- **c3** Seven detectors are evaluated on eleven real-world data streams; three were too slow or depended on chance.([Abstract, p.1](https://elib.dlr.de/206088/1/Lukats_et_al-2024-International_Journal_of_Data_Science_and_Analytics.pdf#page=1 "Seven of these algorithms are evaluated with common concept drift detection metrics on eleven real-world data streams"))
- **c4** Depending on the target metric, D3, IBDD and SPLL are recommended.([Abstract, p.1](https://elib.dlr.de/206088/1/Lukats_et_al-2024-International_Journal_of_Data_Science_and_Analytics.pdf#page=1 "three concept drift detectors—Discriminative Drift Detector, Image-Based Drift Detector and Semi-Parametric Log-Likelihood—can be recommended depending on the desired target metric."))
- **c5** The evaluation metrics Mean Time Ratio and lift-per-drift have issues.([Abstract, p.1](https://elib.dlr.de/206088/1/Lukats_et_al-2024-International_Journal_of_Data_Science_and_Analytics.pdf#page=1 "This study further reveals issues with the evaluation metrics Mean Time Ratio and lift-per-drift."))
- **c6** Only one stream (INSECTS abrupt balanced) allows computing MTR, which needs ground-truth drift times.([Section 6.2, p.12](https://elib.dlr.de/206088/1/Lukats_et_al-2024-International_Journal_of_Data_Science_and_Analytics.pdf#page=12 "INSECTS (abrupt balanced) is the only data stream in this study which can be used to determine MTR."))
- **c7** In MTR, D3 outperformed the other detectors by a large margin.([Section 6.2, p.13](https://elib.dlr.de/206088/1/Lukats_et_al-2024-International_Journal_of_Data_Science_and_Analytics.pdf#page=13 "In these experiments, D3 outperforms other detectors by a large margin"))
- **c8** IBDD was among the worst in MTR despite having the most tested configurations.([Section 6.2, p.13](https://elib.dlr.de/206088/1/Lukats_et_al-2024-International_Journal_of_Data_Science_and_Analytics.pdf#page=13 "IBDD is among the worst performers, despite being the least filtered detector"))
- **c9** Classifier accuracy as a proxy metric is biased toward detectors that detect (and adapt) more often.([Section 8, p.18](https://elib.dlr.de/206088/1/Lukats_et_al-2024-International_Journal_of_Data_Science_and_Analytics.pdf#page=18 "classifier predictive performance is biased in favor of a higher number of detected concept drifts and adaptations."))
- **c10** The lift-per-drift metric is biased the other way, favoring fewer detections.([Section 8, p.18](https://elib.dlr.de/206088/1/Lukats_et_al-2024-International_Journal_of_Data_Science_and_Analytics.pdf#page=18 "lpdr=1 is likewise biased, as the version used in this study evidently favors fewer detected concept drifts."))
- **c11** IBDD gave strong classifier accuracy on many streams but did worse in lpd and MTR.([Section 8, p.18](https://elib.dlr.de/206088/1/Lukats_et_al-2024-International_Journal_of_Data_Science_and_Analytics.pdf#page=18 "Image-Based Drift Detector (IBDD) [46] achieves great classifier predictive performance on many data streams, although it does not perform as well when assessed with lpd and MTR."))
- **c12** D3 and SPLL gave the best results on most streams while also giving good classifier accuracy.([Section 8, p.18](https://elib.dlr.de/206088/1/Lukats_et_al-2024-International_Journal_of_Data_Science_and_Analytics.pdf#page=18 "Discriminative Drift Detector (D3) [45] and Semi-Parametric Log Likelihood (SPLL) [39] showed the best results on most data streams"))
- **c13** All configuration permutations were tried by grid search.([Section 5.3, p.10](https://elib.dlr.de/206088/1/Lukats_et_al-2024-International_Journal_of_Data_Science_and_Analytics.pdf#page=10 "A simple grid search is performed to test all permutations of the configuration parameters"))
- **c14** Several original publications describe no reset after a detection, so the authors added one where needed.([Section 5.3, p.10](https://elib.dlr.de/206088/1/Lukats_et_al-2024-International_Journal_of_Data_Science_and_Analytics.pdf#page=10 "several publications do not mention any reset mechanism to adapt to the new concept after the detection of a concept drift."))
- **c15** 61 publications on unsupervised drift detection were examined.([Section 8, p.17](https://elib.dlr.de/206088/1/Lukats_et_al-2024-International_Journal_of_Data_Science_and_Analytics.pdf#page=17 "This study examined 61 publications related to unsupervised concept drift detection."))
- **c16** Configurations with no detection or periodic detection were filtered out before analysis.([Section 6.1, p.11](https://elib.dlr.de/206088/1/Lukats_et_al-2024-International_Journal_of_Data_Science_and_Analytics.pdf#page=11 "the experimental results were filtered to remove those results which featured no detection or periodic concept drift detection"))
- **c17** Real-world streams with known drift ground truth (which drifts, start and end) are hard to obtain.([Section 5.1, p.8](https://elib.dlr.de/206088/1/Lukats_et_al-2024-International_Journal_of_Data_Science_and_Analytics.pdf#page=8 "data with known concept drift ground truth information—which concept drifts are present, when do they begin and end—are difficult to obtain."))

## 結果表

列ごとに比較条件が異なる。**同じ列の中だけ**比較できる。太字は列内の最良値。

#### mtr(大きいほど良い)

繰り返し: Non-deterministic detectors averaged (Section 6).

| method | `lukats2024-insects-abrupt-balanced` |
|---|---|
| BNDM | 33.7 |
| CSDDM | 10.6 ± 1.2 |
| D3 | **104.6 ± 0** |
| IBDD | 7 ± 0 |
| OCDD | 7.9 |
| SPLL | 31.2 ± 0 |
| UDetect | 4.7 |

出典: [Table 8, p.13](https://elib.dlr.de/206088/1/Lukats_et_al-2024-International_Journal_of_Data_Science_and_Analytics.pdf#page=13 "BNDM 33.7 4927.0 146.4 0.0")

#### mtfa(大きいほど良い)

繰り返し: Non-deterministic detectors averaged (Section 6).

| method | `lukats2024-insects-abrupt-balanced` |
|---|---|
| BNDM | 4927 |
| CSDDM | 2327.7 ± 298.2 |
| D3 | **20664 ± 0** |
| IBDD | 2450.6 ± 0 |
| OCDD | 3348.3 |
| SPLL | 5185 ± 0 |
| UDetect | 1445.7 |

出典: [Table 8, p.13](https://elib.dlr.de/206088/1/Lukats_et_al-2024-International_Journal_of_Data_Science_and_Analytics.pdf#page=13 "BNDM 33.7 4927.0 146.4 0.0")

#### mtd(小さいほど良い)

繰り返し: Non-deterministic detectors averaged (Section 6).

| method | `lukats2024-insects-abrupt-balanced` |
|---|---|
| BNDM | 146.4 |
| CSDDM | 219.6 ± 9.2 |
| D3 | **91.6 ± 28.2** |
| IBDD | 210.7 ± 0 |
| OCDD | 340 |
| SPLL | 132.8 ± 0 |
| UDetect | 247.8 |

出典: [Table 8, p.13](https://elib.dlr.de/206088/1/Lukats_et_al-2024-International_Journal_of_Data_Science_and_Analytics.pdf#page=13 "BNDM 33.7 4927.0 146.4 0.0")

#### mdr(小さいほど良い)

繰り返し: Non-deterministic detectors averaged (Section 6).

| method | `lukats2024-insects-abrupt-balanced` |
|---|---|
| BNDM | **0** |
| CSDDM | **0 ± 0** |
| D3 | 0.6 ± 0 |
| IBDD | 0.4 ± 0 |
| OCDD | 0.2 |
| SPLL | 0.2 ± 0 |
| UDetect | 0.2 |

出典: [Table 8, p.13](https://elib.dlr.de/206088/1/Lukats_et_al-2024-International_Journal_of_Data_Science_and_Analytics.pdf#page=13 "BNDM 33.7 4927.0 146.4 0.0")

## 論文内の勝敗(結果から導出)

同じ比較条件での数値の大小だけを数えたもの。**統計的有意性は考慮していない**。

| A | B | A勝ち | 引き分け | B勝ち |
|---|---|---|---|---|
| BNDM | CSDDM | 3 | 1 | 0 |
| BNDM | D3 | 1 | 0 | 3 |
| BNDM | IBDD | 4 | 0 | 0 |
| BNDM | OCDD | 4 | 0 | 0 |
| BNDM | SPLL | 2 | 0 | 2 |
| BNDM | UDetect | 4 | 0 | 0 |
| CSDDM | D3 | 1 | 0 | 3 |
| CSDDM | IBDD | 2 | 0 | 2 |
| CSDDM | OCDD | 3 | 0 | 1 |
| CSDDM | SPLL | 1 | 0 | 3 |
| CSDDM | UDetect | 4 | 0 | 0 |
| D3 | IBDD | 3 | 0 | 1 |
| D3 | OCDD | 3 | 0 | 1 |
| D3 | SPLL | 3 | 0 | 1 |
| D3 | UDetect | 3 | 0 | 1 |
| IBDD | OCDD | 1 | 0 | 3 |
| IBDD | SPLL | 0 | 0 | 4 |
| IBDD | UDetect | 3 | 0 | 1 |
| OCDD | SPLL | 0 | 1 | 3 |
| OCDD | UDetect | 2 | 1 | 1 |
| SPLL | UDetect | 3 | 1 | 0 |

