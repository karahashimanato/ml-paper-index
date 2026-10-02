<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# A comprehensive analysis of concept drift locality in data streams

- カード: [`arxiv-2311.06396`](../../papers/arxiv-2311.06396.yaml)
- 著者: Gabriel J. Aguiar, Alberto Cano
- 年・掲載: 2023
- 原論文: [PDF](https://arxiv.org/pdf/2311.06396v2)(arXiv v2、カード作成時に読んだ版)
- タグ: concept-drift-detection, error-rate-drift-detectors, streaming, window-based-drift-detectors
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** A locality/scale-based categorization of concept drift yields 2,760 benchmark problems.([Abstract, p.1](https://arxiv.org/pdf/2311.06396v2#page=1 "A systematic approach leads to a set of 2,760 benchmark problems"))
- **c2** Nine supervised drift detectors are compared across the difficulties.([Abstract, p.1](https://arxiv.org/pdf/2311.06396v2#page=1 "We conduct a comparative assessment of 9 state-of-the-art drift detectors across diverse difficulties"))
- **c3** ADWIN, DDM and PH were strong overall: few false alarms on stationary streams and good detection with drift.([Section 5.1, p.12](https://arxiv.org/pdf/2311.06396v2#page=12 "ADWIN, DDM, and PH stood out as strong performers in both evaluated scenarios."))
- **c4** ADWIN and PH consistently showed the best detection performance across all scenarios.([Results, p.13](https://arxiv.org/pdf/2311.06396v2#page=13 "ADWIN and PH consistently demonstrated superior detection performance across all evaluated scenarios."))
- **c5** EDDM had the lowest delay and second-highest recall but so many alarms that its precision was 0%.([Section 5.1, p.12](https://arxiv.org/pdf/2311.06396v2#page=12 "EDDM exhibited the lowest delay among all evaluated drift detectors and the second-highest recall, although this came at the cost of raising numerous drift alerts, leading to a precision of 0%."))
- **c6** Difficulty from easiest to hardest: multi-class global, single-class global, multi-class local, single-class local.([Results, p.13](https://arxiv.org/pdf/2311.06396v2#page=13 "a hierarchy of difficulty emerges, from easiest to hardest detection as follows: Multi-Class Global, Single-Class Global, Multi-Class Local, Single-Class Local."))
- **c7** More localized drifts produce more false alarms for all detectors.([Results, p.13](https://arxiv.org/pdf/2311.06396v2#page=13 "scenarios with more localized drifts tended to generate a higher number of false alarms."))
- **c8** Completely retraining the classifier after detection reduced accuracy in all evaluated scenarios.([Results (classifier impact), p.21](https://arxiv.org/pdf/2311.06396v2#page=21 "completely retraining the classifier resulted in decreased accuracy across all evaluated scenarios."))
- **c9** A Hoeffding Tree is the monitored classifier; detectors monitor its binary error signal.([Experimental setup, p.10](https://arxiv.org/pdf/2311.06396v2#page=10 "we opted to use Hoeffding Tree (HT) [49] as our classifier."))
- **c10** Error-rate-based detectors often raise many false alarms, even on positive changes in the error rate.([Lessons learned, p.24](https://arxiv.org/pdf/2311.06396v2#page=24 "Drift detectors that rely on error rates often generate numerous false alarms."))
- **c11** On stationary streams, ADWIN and DDM raised the fewest false alarms.([Section 5.1, p.12](https://arxiv.org/pdf/2311.06396v2#page=12 "DDM and ADWIN displayed the lowest values of false alerts"))
- **c12** Experiments, stream generators and detectors were implemented in Python with the river library.([Experimental setup, p.11](https://arxiv.org/pdf/2311.06396v2#page=11 "All the experiments, generators and drift detectors were implemented using Python 3.8 and the river [50] package."))

## 結果表

列ごとに比較条件が異なる。**同じ列の中だけ**比較できる。太字は列内の最良値。

#### precision-pct(大きいほど良い)

繰り返し: Averaged over all benchmark streams in the respective category (Tables 4-9).

| method | `aguiar2023-all-drifts` | `aguiar2023-single-class-local` | `aguiar2023-single-class-global` | `aguiar2023-multi-class-local` | `aguiar2023-multi-class-global` |
|---|---|---|---|---|---|
| ADWIN | **7.4** | **5.48** | **8.15** | **7.19** | **7.95** |
| DDM | 1.82 | 1.88 | 2.21 | 1.58 | 1.94 |
| ECDD | 0.03 | 0.03 | 0.02 | 0.04 | 0.03 |
| EDDM | 0 | 0 | 0 | 0 | 0 |
| HDDM | 1.65 | 1.69 | 1.81 | 1.67 | 1.56 |
| KSWIN | 3.32 | 2.91 | 3.3 | 3.31 | 3.48 |
| PH | 5.18 | 5.21 | 5.87 | 5.18 | 4.91 |
| RDDM | 0.89 | 1.13 | 1.01 | 0.92 | 0.72 |
| STEPD | 0.01 | 0.02 | 0.01 | 0.02 | 0.01 |

出典: [Table 5, p.13](https://arxiv.org/pdf/2311.06396v2#page=13 "ADWIN 7.40% 34.50% 12.19% 2192") / [Table 6, p.13](https://arxiv.org/pdf/2311.06396v2#page=13 "ADWIN 5.48% 22.40% 8.80% 2728") / [Table 7, p.13](https://arxiv.org/pdf/2311.06396v2#page=13 "ADWIN 8.15% 39.06% 13.48% 1909") / [Table 8, p.14](https://arxiv.org/pdf/2311.06396v2#page=14 "ADWIN 7.19% 30.40% 11.63% 2360") / [Table 9, p.14](https://arxiv.org/pdf/2311.06396v2#page=14 "ADWIN 7.95% 42.92% 13.41% 2033")

#### recall-pct(大きいほど良い)

繰り返し: Averaged over all benchmark streams in the respective category (Tables 4-9).

| method | `aguiar2023-all-drifts` | `aguiar2023-single-class-local` | `aguiar2023-single-class-global` | `aguiar2023-multi-class-local` | `aguiar2023-multi-class-global` |
|---|---|---|---|---|---|
| ADWIN | 34.5 | 22.4 | 39.06 | 30.4 | 42.92 |
| DDM | 5.45 | 5.47 | 6.25 | 4.67 | 6.05 |
| ECDD | 36.48 | 29.17 | 26.3 | 40.29 | 39.38 |
| EDDM | 95.18 | **97.4** | 91.41 | 95.51 | 95.43 |
| HDDM | 76.61 | 67.45 | 69.01 | 80.68 | 78.88 |
| KSWIN | 42.54 | 31.51 | 34.11 | 44.32 | 48.86 |
| PH | 72.19 | 64.06 | 75.78 | 70.88 | 75.8 |
| RDDM | 25.99 | 31.77 | 28.39 | 26.37 | 21.92 |
| STEPD | **95.8** | 91.15 | **93.75** | **96.7** | **97.6** |

出典: [Table 5, p.13](https://arxiv.org/pdf/2311.06396v2#page=13 "ADWIN 7.40% 34.50% 12.19% 2192") / [Table 6, p.13](https://arxiv.org/pdf/2311.06396v2#page=13 "ADWIN 5.48% 22.40% 8.80% 2728") / [Table 7, p.13](https://arxiv.org/pdf/2311.06396v2#page=13 "ADWIN 8.15% 39.06% 13.48% 1909") / [Table 8, p.14](https://arxiv.org/pdf/2311.06396v2#page=14 "ADWIN 7.19% 30.40% 11.63% 2360") / [Table 9, p.14](https://arxiv.org/pdf/2311.06396v2#page=14 "ADWIN 7.95% 42.92% 13.41% 2033")

#### f1-pct(大きいほど良い)

繰り返し: Averaged over all benchmark streams in the respective category (Tables 4-9).

| method | `aguiar2023-all-drifts` | `aguiar2023-single-class-local` | `aguiar2023-single-class-global` | `aguiar2023-multi-class-local` | `aguiar2023-multi-class-global` |
|---|---|---|---|---|---|
| ADWIN | **12.19** | 8.8 | **13.48** | **11.63** | **13.41** |
| DDM | 2.73 | 2.8 | 3.27 | 2.36 | 2.93 |
| ECDD | 0.06 | 0.07 | 0.05 | 0.07 | 0.06 |
| EDDM | 0 | 0 | 0 | 0 | 0 |
| HDDM | 3.23 | 3.3 | 3.52 | 3.28 | 3.06 |
| KSWIN | 6.16 | 5.32 | 6.02 | 6.16 | 6.49 |
| PH | 9.66 | **9.63** | 10.9 | 9.66 | 9.22 |
| RDDM | 1.72 | 2.18 | 1.96 | 1.77 | 1.39 |
| STEPD | 0.03 | 0.04 | 0.02 | 0.03 | 0.03 |

出典: [Table 5, p.13](https://arxiv.org/pdf/2311.06396v2#page=13 "ADWIN 7.40% 34.50% 12.19% 2192") / [Table 6, p.13](https://arxiv.org/pdf/2311.06396v2#page=13 "ADWIN 5.48% 22.40% 8.80% 2728") / [Table 7, p.13](https://arxiv.org/pdf/2311.06396v2#page=13 "ADWIN 8.15% 39.06% 13.48% 1909") / [Table 8, p.14](https://arxiv.org/pdf/2311.06396v2#page=14 "ADWIN 7.19% 30.40% 11.63% 2360") / [Table 9, p.14](https://arxiv.org/pdf/2311.06396v2#page=14 "ADWIN 7.95% 42.92% 13.41% 2033")

#### delay(小さいほど良い)

繰り返し: Averaged over all benchmark streams in the respective category (Tables 4-9).

| method | `aguiar2023-all-drifts` | `aguiar2023-single-class-local` | `aguiar2023-single-class-global` | `aguiar2023-multi-class-local` | `aguiar2023-multi-class-global` |
|---|---|---|---|---|---|
| ADWIN | 2192 | 2728 | 1909 | 2360 | 2033 |
| DDM | 2168 | 2287 | 2286 | 2036 | 2195 |
| ECDD | 235 | 201 | 315 | 192 | 277 |
| EDDM | **15** | **4** | **11** | **21** | **14** |
| HDDM | 1271 | 1359 | 1321 | 1207 | 1299 |
| KSWIN | 1866 | 1991 | 1879 | 1873 | 1819 |
| PH | 1867 | 2176 | 1737 | 1956 | 1706 |
| RDDM | 2027 | 2016 | 1982 | 2083 | 1977 |
| STEPD | 516 | 649 | 517 | 508 | 469 |

出典: [Table 5, p.13](https://arxiv.org/pdf/2311.06396v2#page=13 "ADWIN 7.40% 34.50% 12.19% 2192") / [Table 6, p.13](https://arxiv.org/pdf/2311.06396v2#page=13 "ADWIN 5.48% 22.40% 8.80% 2728") / [Table 7, p.13](https://arxiv.org/pdf/2311.06396v2#page=13 "ADWIN 8.15% 39.06% 13.48% 1909") / [Table 8, p.14](https://arxiv.org/pdf/2311.06396v2#page=14 "ADWIN 7.19% 30.40% 11.63% 2360") / [Table 9, p.14](https://arxiv.org/pdf/2311.06396v2#page=14 "ADWIN 7.95% 42.92% 13.41% 2033")

#### false-positives(小さいほど良い)

繰り返し: Averaged over all benchmark streams in the respective category (Tables 4-9).

| method | `aguiar2023-no-drift` |
|---|---|
| ADWIN | 3.79 |
| DDM | **2.71** |
| ECDD | 904.58 |
| EDDM | 62914 |
| HDDM | 41.83 |
| KSWIN | 10.25 |
| PH | 12.46 |
| RDDM | 27.96 |
| STEPD | 4628.13 |

出典: [Table 4, p.12](https://arxiv.org/pdf/2311.06396v2#page=12 "ADWIN 0.00 3.79")

## 論文内の勝敗(結果から導出)

同じ比較条件での数値の大小だけを数えたもの。**統計的有意性は考慮していない**。

| A | B | A勝ち | 引き分け | B勝ち |
|---|---|---|---|---|
| ADWIN | DDM | 17 | 0 | 4 |
| ADWIN | ECDD | 13 | 0 | 8 |
| ADWIN | EDDM | 11 | 0 | 10 |
| ADWIN | HDDM | 11 | 0 | 10 |
| ADWIN | KSWIN | 12 | 0 | 9 |
| ADWIN | PH | 10 | 0 | 11 |
| ADWIN | RDDM | 16 | 0 | 5 |
| ADWIN | STEPD | 11 | 0 | 10 |
| DDM | ECDD | 11 | 0 | 10 |
| DDM | EDDM | 11 | 0 | 10 |
| DDM | HDDM | 5 | 0 | 16 |
| DDM | KSWIN | 1 | 0 | 20 |
| DDM | PH | 1 | 0 | 20 |
| DDM | RDDM | 12 | 0 | 9 |
| DDM | STEPD | 11 | 0 | 10 |
| ECDD | EDDM | 11 | 0 | 10 |
| ECDD | HDDM | 5 | 0 | 16 |
| ECDD | KSWIN | 5 | 0 | 16 |
| ECDD | PH | 5 | 0 | 16 |
| ECDD | RDDM | 8 | 0 | 13 |
| ECDD | STEPD | 16 | 0 | 5 |
| EDDM | HDDM | 10 | 0 | 11 |
| EDDM | KSWIN | 10 | 0 | 11 |
| EDDM | PH | 10 | 0 | 11 |
| EDDM | RDDM | 10 | 0 | 11 |
| EDDM | STEPD | 6 | 0 | 15 |
| HDDM | KSWIN | 10 | 0 | 11 |
| HDDM | PH | 9 | 0 | 12 |
| HDDM | RDDM | 20 | 0 | 1 |
| HDDM | STEPD | 11 | 0 | 10 |
| KSWIN | PH | 4 | 0 | 17 |
| KSWIN | RDDM | 20 | 0 | 1 |
| KSWIN | STEPD | 11 | 0 | 10 |
| PH | RDDM | 20 | 0 | 1 |
| PH | STEPD | 11 | 0 | 10 |
| RDDM | STEPD | 11 | 0 | 10 |

