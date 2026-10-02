<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# A Framework for Evaluating and Benchmarking Concept Drift Detection Methods

- カード: [`arxiv-2606.07789`](../../papers/arxiv-2606.07789.yaml)
- 著者: Vitor Cerqueira, Heitor Murilo Gomes, Marco Heyden, Bernhard Pfahringer, Albert Bifet
- 年・掲載: 2026 KDD 2026
- 原論文: [PDF](https://arxiv.org/pdf/2606.07789v1)(arXiv v1、カード作成時に読んだ版)
- タグ: concept-drift-detection, error-rate-drift-detectors, streaming, window-based-drift-detectors
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Drift detector evaluation is inconsistent: oversimplified synthetic generators, incompatible metrics, and opaque hyperparameter selection.([Abstract, p.1](https://arxiv.org/pdf/2606.07789v1#page=1 "studies rely on oversimplified synthetic data generators, adopt incompatible metrics, and lack transparency in hyperparameter selection"))
- **c2** 14 widely used detectors are benchmarked on 7 real-world datasets with 4 injected drift types, each abrupt and gradual.([Abstract, p.1](https://arxiv.org/pdf/2606.07789v1#page=1 "We benchmark 14 widely used drift detection methods on 7 real-world datasets across 4 drift types"))
- **c3** SEED, STEPD and ABCD consistently outperformed the other detectors across drift types.([Introduction, p.2](https://arxiv.org/pdf/2606.07789v1#page=2 "Our results reveal that SEED [23], STEPD [25], and ABCD [22] consistently outperform other detectors across distinct drift types"))
- **c4** Hyperparameter optimization with the proposed protocol significantly improved detection over default configurations.([Introduction, p.2](https://arxiv.org/pdf/2606.07789v1#page=2 "hyperparameter optimization using our proposed approach significantly improves detection performance over default configurations."))
- **c5** Classic metrics MTFA and MDT depend on stream length and drift spacing, preventing cross-dataset comparison.([Related work, p.3](https://arxiv.org/pdf/2606.07789v1#page=3 "MTFA and MDT are highly dependent on stream length and drift spacing"))
- **c6** An F1 score for drift detection ignores timing: a detector with unacceptable delay can still get perfect F1.([Related work, p.3](https://arxiv.org/pdf/2606.07789v1#page=3 "its formulation ignores the temporal aspect: a detector with unacceptable delay can still achieve perfect F1."))
- **c7** Detector hyperparameters are tuned with leave-one-dataset-out cross-validation.([Section 3.3, p.4](https://arxiv.org/pdf/2606.07789v1#page=4 "we propose a leave-one-dataset-out cross-validation approach for optimizing the hyperparameters of drift detectors."))
- **c8** Tuning and evaluating detectors on the same dataset can overfit and make reported results overly optimistic.([Section 3.3, p.4](https://arxiv.org/pdf/2606.07789v1#page=4 "using the same dataset for optimizing and evaluating the detector can cause overfitting and lead to overly optimistic performance estimates reported in the respective papers."))
- **c9** Each dataset and drift type is evaluated with 50 Monte Carlo trials (random drift onset).([Experimental setup, p.6](https://arxiv.org/pdf/2606.07789v1#page=6 "For each dataset and drift type, we perform 50 Monte Carlo trials."))
- **c10** A Hoeffding Tree with default hyperparameters is the monitored classifier.([Experimental setup, p.6](https://arxiv.org/pdf/2606.07789v1#page=6 "We select the Hoeffding Tree [10] as the classifier in the experiments"))
- **c11** PH and EWMA were ineffective regardless of configuration.([Main findings, p.8](https://arxiv.org/pdf/2606.07789v1#page=8 "PH and EWMA remain ineffective regardless of configuration, suggesting fundamental limitations"))
- **c12** Unsupervised detectors (ABCD(X), STUDD) detect feature-space drifts but not label-only changes.([Main findings, p.8](https://arxiv.org/pdf/2606.07789v1#page=8 "Unsupervised detectors (ABCD(X) and STUDD) perform better on feature-space drifts (feature permutation, feature filtering) than on label-based changes (class prior, class swaps)"))
- **c13** Gradual drifts are systematically harder to detect than abrupt ones.([Main findings, p.8](https://arxiv.org/pdf/2606.07789v1#page=8 "Gradual drifts are systematically harder to detect than abrupt ones."))
- **c14** STEPD's strong results are largely due to effective tuning.([Main findings, p.8](https://arxiv.org/pdf/2606.07789v1#page=8 "STEPD's strong performance is largely attributable to effective tuning."))
- **c15** Limitations: one classifier (Hoeffding tree), four drift types, seven datasets.([Limitations, p.8](https://arxiv.org/pdf/2606.07789v1#page=8 "the experiments are limited to one classifier (Hoeffding tree) and four drift types simulated in 7 real-world datasets."))
- **c16** Limitation: labels are assumed to be available immediately after each prediction (no verification delay).([Limitations, p.8](https://arxiv.org/pdf/2606.07789v1#page=8 "it assumes immediate feedback, with labels being readily available at each step after inference."))
- **c17** Shuffling the real streams before injecting drift removes their natural temporal structure.([Limitations, p.8](https://arxiv.org/pdf/2606.07789v1#page=8 "it also removes any inherent temporal structure."))
- **c18** Practical guidance: SEED and STEPD are robust defaults when drift characteristics are unknown.([Main findings, p.8](https://arxiv.org/pdf/2606.07789v1#page=8 "SEED and STEPD are robust defaults when drift characteristics are unknown"))
- **c19** Hyperparameters are searched with 30 iterations of random search.([Experimental setup, p.6](https://arxiv.org/pdf/2606.07789v1#page=6 "The optimization is conducted using 30 iterations of random search."))
- **c20** The main objective is a standardized evaluation protocol, not identifying the best detector.([Experimental setup, p.6](https://arxiv.org/pdf/2606.07789v1#page=6 "our main objective is to establish a standardized evaluation protocol rather than to identify the best performing detector."))

## 結果表

列ごとに比較条件が異なる。**同じ列の中だけ**比較できる。太字は列内の最良値。

#### avg-rank-f1(小さいほど良い)

繰り返し: 50 Monte Carlo trials per dataset and drift type; average rank across the 7 datasets (Tables 1-2).

| method | `cerqueira2026-abrupt-feature-filtering` | `cerqueira2026-abrupt-feature-permutation` | `cerqueira2026-abrupt-class-prior` | `cerqueira2026-abrupt-class-swap` | `cerqueira2026-gradual-feature-filtering` | `cerqueira2026-gradual-feature-permutation` | `cerqueira2026-gradual-class-prior` | `cerqueira2026-gradual-class-swap` |
|---|---|---|---|---|---|---|---|---|
| ABCD | 8.1 | 3.9 | 8 | 3.6 | 11.7 | 4.1 | 9.8 | 5.1 |
| ABCD(X) | 12.7 | **1** | 13.1 | 13.1 | 13 | 3.3 | 13 | 13.1 |
| ADWIN | 4.1 | 7.6 | 4.1 | 7.1 | 6 | 11.2 | 6.8 | 7.9 |
| CUSUM | 5.6 | 11.9 | 6.1 | 9.2 | 6.3 | 11.9 | 7.3 | 9.7 |
| DDM | 7.3 | 11.4 | 6 | 9.9 | 6.1 | 9.4 | **4.7** | 8.1 |
| EWMA | 9.7 | 12.9 | 9.4 | 10.9 | 11.7 | 12.4 | 10.6 | 12 |
| GMA | 9 | 7.7 | 8.7 | 7.3 | **3.9** | 6.6 | 6.1 | 4.7 |
| HDDMA | 7.4 | 5.6 | 6.3 | 5.4 | 9.7 | 7.9 | 7.8 | 10.5 |
| HDDMW | 7.1 | 6.9 | 5.8 | 6 | 5.5 | 6.3 | 5.2 | 5.4 |
| PH | 13.1 | 12.9 | 11.6 | 10.1 | 10.9 | 12.4 | 9.7 | 11.1 |
| RDDM | 6.6 | 10.2 | 7.9 | 9.1 | 4.7 | 6.4 | 6.6 | 5.3 |
| SEED | 4.4 | 2.7 | **3.9** | **1.1** | 5.9 | **2.7** | 5 | **1.9** |
| STEPD | **3.4** | 3.7 | 4.3 | 2.4 | 5.4 | 2.8 | 5.2 | 2 |
| STUDD | 6.4 | 6.8 | 9.9 | 9.6 | 4.2 | 7.6 | 7.1 | 8.1 |

出典: [Table 1, p.7](https://arxiv.org/pdf/2606.07789v1#page=7 "ABCD 8.1 3.9 8.0 3.6") / [Table 2, p.7](https://arxiv.org/pdf/2606.07789v1#page=7 "ABCD 11.7 4.1 9.8 5.1")

## 論文内の勝敗(結果から導出)

同じ比較条件での数値の大小だけを数えたもの。**統計的有意性は考慮していない**。

| A | B | A勝ち | 引き分け | B勝ち |
|---|---|---|---|---|
| ABCD | ABCD(X) | 6 | 0 | 2 |
| ABCD | ADWIN | 4 | 0 | 4 |
| ABCD | CUSUM | 4 | 0 | 4 |
| ABCD | DDM | 4 | 0 | 4 |
| ABCD | EWMA | 7 | 1 | 0 |
| ABCD | GMA | 5 | 0 | 3 |
| ABCD | HDDMA | 4 | 0 | 4 |
| ABCD | HDDMW | 4 | 0 | 4 |
| ABCD | PH | 6 | 0 | 2 |
| ABCD | RDDM | 4 | 0 | 4 |
| ABCD | SEED | 0 | 0 | 8 |
| ABCD | STEPD | 0 | 0 | 8 |
| ABCD | STUDD | 5 | 0 | 3 |
| ABCD(X) | ADWIN | 2 | 0 | 6 |
| ABCD(X) | CUSUM | 2 | 0 | 6 |
| ABCD(X) | DDM | 2 | 0 | 6 |
| ABCD(X) | EWMA | 2 | 0 | 6 |
| ABCD(X) | GMA | 2 | 0 | 6 |
| ABCD(X) | HDDMA | 2 | 0 | 6 |
| ABCD(X) | HDDMW | 2 | 0 | 6 |
| ABCD(X) | PH | 3 | 0 | 5 |
| ABCD(X) | RDDM | 2 | 0 | 6 |
| ABCD(X) | SEED | 1 | 0 | 7 |
| ABCD(X) | STEPD | 1 | 0 | 7 |
| ABCD(X) | STUDD | 2 | 0 | 6 |
| ADWIN | CUSUM | 8 | 0 | 0 |
| ADWIN | DDM | 6 | 0 | 2 |
| ADWIN | EWMA | 8 | 0 | 0 |
| ADWIN | GMA | 4 | 0 | 4 |
| ADWIN | HDDMA | 5 | 0 | 3 |
| ADWIN | HDDMW | 2 | 0 | 6 |
| ADWIN | PH | 8 | 0 | 0 |
| ADWIN | RDDM | 4 | 0 | 4 |
| ADWIN | SEED | 1 | 0 | 7 |
| ADWIN | STEPD | 1 | 0 | 7 |
| ADWIN | STUDD | 5 | 0 | 3 |
| CUSUM | DDM | 2 | 0 | 6 |
| CUSUM | EWMA | 8 | 0 | 0 |
| CUSUM | GMA | 2 | 0 | 6 |
| CUSUM | HDDMA | 5 | 0 | 3 |
| CUSUM | HDDMW | 1 | 0 | 7 |
| CUSUM | PH | 8 | 0 | 0 |
| CUSUM | RDDM | 2 | 0 | 6 |
| CUSUM | SEED | 0 | 0 | 8 |
| CUSUM | STEPD | 0 | 0 | 8 |
| CUSUM | STUDD | 3 | 0 | 5 |
| DDM | EWMA | 8 | 0 | 0 |
| DDM | GMA | 3 | 0 | 5 |
| DDM | HDDMA | 5 | 0 | 3 |
| DDM | HDDMW | 1 | 0 | 7 |
| DDM | PH | 8 | 0 | 0 |
| DDM | RDDM | 2 | 0 | 6 |
| DDM | SEED | 1 | 0 | 7 |
| DDM | STEPD | 1 | 0 | 7 |
| DDM | STUDD | 2 | 1 | 5 |
| EWMA | GMA | 0 | 0 | 8 |
| EWMA | HDDMA | 0 | 0 | 8 |
| EWMA | HDDMW | 0 | 0 | 8 |
| EWMA | PH | 2 | 2 | 4 |
| EWMA | RDDM | 0 | 0 | 8 |
| EWMA | SEED | 0 | 0 | 8 |
| EWMA | STEPD | 0 | 0 | 8 |
| EWMA | STUDD | 1 | 0 | 7 |
| GMA | HDDMA | 4 | 0 | 4 |
| GMA | HDDMW | 2 | 0 | 6 |
| GMA | PH | 8 | 0 | 0 |
| GMA | RDDM | 5 | 0 | 3 |
| GMA | SEED | 1 | 0 | 7 |
| GMA | STEPD | 1 | 0 | 7 |
| GMA | STUDD | 6 | 0 | 2 |
| HDDMA | HDDMW | 2 | 0 | 6 |
| HDDMA | PH | 8 | 0 | 0 |
| HDDMA | RDDM | 3 | 0 | 5 |
| HDDMA | SEED | 0 | 0 | 8 |
| HDDMA | STEPD | 0 | 0 | 8 |
| HDDMA | STUDD | 3 | 0 | 5 |
| HDDMW | PH | 8 | 0 | 0 |
| HDDMW | RDDM | 5 | 0 | 3 |
| HDDMW | SEED | 1 | 0 | 7 |
| HDDMW | STEPD | 0 | 1 | 7 |
| HDDMW | STUDD | 5 | 0 | 3 |
| PH | RDDM | 0 | 0 | 8 |
| PH | SEED | 0 | 0 | 8 |
| PH | STEPD | 0 | 0 | 8 |
| PH | STUDD | 0 | 0 | 8 |
| RDDM | SEED | 1 | 0 | 7 |
| RDDM | STEPD | 1 | 0 | 7 |
| RDDM | STUDD | 5 | 0 | 3 |
| SEED | STEPD | 6 | 0 | 2 |
| SEED | STUDD | 7 | 0 | 1 |
| STEPD | STUDD | 7 | 0 | 1 |

