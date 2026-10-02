<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Towards a Rigorous Evaluation of Time-series Anomaly Detection

- カード: [`arxiv-2109.05257`](../../papers/arxiv-2109.05257.yaml)
- 著者: Siwon Kim, Kukjin Choi, Hyun-Soo Choi, Byunghan Lee, Sungroh Yoon
- 年・掲載: 2022 AAAI 2022
- 原論文: [PDF](https://arxiv.org/pdf/2109.05257v2)(arXiv v2、カード作成時に読んだ版)
- タグ: forecasting-based-detectors, reconstruction-based-detectors, time-series-anomaly-detection, unsupervised
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Point adjustment (PA) can greatly overestimate detection performance: even a random anomaly score can look state of the art.([Abstract, p.1](https://arxiv.org/pdf/2109.05257v2#page=1 "the PA protocol has a great possibility of overestimating the detection performance; that is, even a random anomaly score can easily turn into a state-of-the-art TAD method."))
- **c2** Even without PA, an untrained model performs comparably to existing methods.([Abstract, p.1](https://arxiv.org/pdf/2109.05257v2#page=1 "an untrained model obtains comparable detection performance to the existing methods even when PA is forbidden."))
- **c3** PA: if any point in a ground-truth anomaly segment is detected, the whole segment counts as detected.([Introduction, p.1](https://arxiv.org/pdf/2109.05257v2#page=1 "if at least one moment in a contiguous anomaly segment is detected as an anomaly, the entire segment is then considered to be correctly predicted as anomaly."))
- **c4** PA can only increase precision, recall and F1.([Section 3, p.3](https://arxiv.org/pdf/2109.05257v2#page=3 "after the PA, the P, R and consequently F1 score can only increase."))
- **c5** With random scores, F1PA can be pushed close to 1 by choosing the threshold, unless anomaly segments are short.([Section 3, p.3](https://arxiv.org/pdf/2109.05257v2#page=3 "except for the case when the length of the anomaly segment is short."))
- **c6** The overestimation by PA depends on the test set and is weaker with shorter anomaly segments (e.g. SMD).([Section 5, p.6](https://arxiv.org/pdf/2109.05257v2#page=6 "the overestimation effect of PA depends on the test dataset distribution, and its effect becomes less conspicuous with shorter anomaly segments."))
- **c7** Only GDN consistently exceeded the untrained baselines on all datasets.([Section 5, p.7](https://arxiv.org/pdf/2109.05257v2#page=7 "Only the GDN consistently exceeded the baselines for all datasets."))
- **c8** Without PA, existing methods were mostly worse than the untrained baselines (Case 2 and 3).([Section 5, p.7](https://arxiv.org/pdf/2109.05257v2#page=7 "mostly inferior to Case 2 and 3, implying that the currently proposed methods may have obtained marginal or even no advancement against the baselines."))
- **c9** All thresholds were chosen to give the best score (optimistic for every method).([Section 5, p.6](https://arxiv.org/pdf/2109.05257v2#page=6 "All thresholds were obtained from those that yielded the best score."))
- **c10** Existing methods' numbers are the best reported in the original papers or official reproductions; missing ones were reproduced (†).([Section 5, p.6](https://arxiv.org/pdf/2109.05257v2#page=6 "For the existing methods, we used the best numbers reported in the original papers and officially reproduced results"))
- **c11** MSL and SMAP contain unlabeled anomalies in the training data.([Section 5, p.5](https://arxiv.org/pdf/2109.05257v2#page=5 "Unlike other datasets, unlabeled anomalies are contained in the training data, which makes training difficult."))
- **c12** Proposed PA%K protocol: apply PA only if the fraction of detected points in a segment exceeds K, mitigating both over- and underestimation.([Section 4, p.4](https://arxiv.org/pdf/2109.05257v2#page=4 "which can mitigate the overestimation effect of F1PA and the possibility of underestimation of F1."))
- **c13** Proposed baseline: the F1 of a randomly initialized simple reconstruction model (e.g. untrained single-layer LSTM autoencoder).([Section 4, p.4](https://arxiv.org/pdf/2109.05257v2#page=4 "we suggest establishing a new baseline with the F1 measured from the prediction of a randomly initialized reconstruction model with simple architecture"))
- **c14** Existing TAD methods set thresholds after looking at the test set or use the F1-optimal threshold.([Discussion (directions for evaluation), p.7](https://arxiv.org/pdf/2109.05257v2#page=7 "existing TAD methods set the threshold after investigating the test dataset or simply use the optimal threshold that yields the best F1."))
- **c15** Threshold-independent metrics such as AUROC or AUPR are recommended in addition.([Discussion (directions for evaluation), p.7](https://arxiv.org/pdf/2109.05257v2#page=7 "Additional metrics with the reduced dependency such as AUROC or area under precision-recall (AUPR) curve will help in rigorous evaluation."))
- **c16** Incomplete test labeling: some labeled anomalies look like normal data.([Section 4, p.4](https://arxiv.org/pdf/2109.05257v2#page=4 "due to the incomplete test set labeling, some signals labeled as anomalies share more statistics with normal signals."))
- **c17** Reported F1PA and F1 are not reliably correlated on SWaT and WADI.([Section 5, p.5](https://arxiv.org/pdf/2109.05257v2#page=5 "these numbers are insufficient to assure the existence of correlation"))
- **c18** Point anomalies are the dominant anomaly type in current TAD datasets.([Background, p.2](https://arxiv.org/pdf/2109.05257v2#page=2 "Point anomaly is the most dominant type in the current TAD datasets."))

## 結果表

列ごとに比較条件が異なる。**同じ列の中だけ**比較できる。太字は列内の最良値。

#### f1-pa(大きいほど良い)

繰り返し: Cases 1 and 3 averaged over five seeds (Section 5).

| method | `kim2022-swat` | `kim2022-wadi` | `kim2022-msl` | `kim2022-smap` | `kim2022-smd` |
|---|---|---|---|---|---|
| USAD | 0.846 | 0.429 | 0.927 | 0.818 | 0.938 |
| DAGMM | 0.853 | 0.209 | 0.701 | 0.712 | 0.723 |
| LSTM-VAE | 0.805 | 0.38 | 0.678 | 0.756 | 0.808 |
| OmniAnomaly | 0.866 | 0.417 | 0.899 | 0.805 | **0.944** |
| MSCRED | 0.868 | 0.346 | 0.775 | 0.942 | 0.389 |
| THOC | 0.88 | 0.506 | 0.891 | 0.781 | 0.541 |
| GDN | 0.935 | 0.855 | 0.903 | 0.708 | 0.716 |
| Case 1: random anomaly score | **0.969** | **0.965** | **0.931** | **0.961** | 0.804 |
| Case 2: input itself as anomaly score | 0.873 | 0.694 | 0.812 | 0.675 | 0.896 |
| Case 3: untrained (randomly initialized) LSTM encoder-decoder | 0.869 | 0.695 | 0.427 | 0.699 | 0.893 |

出典: [Table 2, p.6](https://arxiv.org/pdf/2109.05257v2#page=6 "USAD 0.846 (↓) 0.791 (↑) 0.429 (↓) 0.232 (↓) 0.927 (↓) 0.211† (↓) 0.818 (↓) 0.228† (↓) 0.938(↑) 0.426† (↓)")

#### f1(大きいほど良い)

繰り返し: Cases 1 and 3 averaged over five seeds (Section 5).

| method | `kim2022-swat` | `kim2022-wadi` | `kim2022-msl` | `kim2022-smap` | `kim2022-smd` |
|---|---|---|---|---|---|
| USAD | 0.791 | 0.232 | 0.211 | 0.228 | 0.426 |
| DAGMM | 0.55 | 0.121 | 0.199 | **0.333** | 0.238 |
| LSTM-VAE | 0.775 | 0.227 | 0.212 | 0.235 | 0.435 |
| OmniAnomaly | 0.782 | 0.223 | 0.207 | 0.227 | 0.474 |
| MSCRED | 0.662 | 0.087 | 0.199 | 0.232 | 0.097 |
| THOC | 0.612 | 0.13 | 0.19 | 0.24 | 0.168 |
| GDN | **0.81** | **0.57** | 0.217 | 0.252 | **0.529** |
| Case 1: random anomaly score | 0.216 | 0.109 | 0.19 | 0.227 | 0.08 |
| Case 2: input itself as anomaly score | 0.781 | 0.353 | **0.239** | 0.229 | 0.494 |
| Case 3: untrained (randomly initialized) LSTM encoder-decoder | 0.789 | 0.331 | 0.236 | 0.229 | 0.466 |

出典: [Table 2, p.6](https://arxiv.org/pdf/2109.05257v2#page=6 "USAD 0.846 (↓) 0.791 (↑) 0.429 (↓) 0.232 (↓) 0.927 (↓) 0.211† (↓) 0.818 (↓) 0.228† (↓) 0.938(↑) 0.426† (↓)")

## 論文内の勝敗(結果から導出)

同じ比較条件での数値の大小だけを数えたもの。**統計的有意性は考慮していない**。

| A | B | A勝ち | 引き分け | B勝ち |
|---|---|---|---|---|
| Case 1: random anomaly score | Case 2: input itself as anomaly score | 4 | 0 | 6 |
| Case 1: random anomaly score | Case 3: untrained (randomly initialized) LSTM encoder-decoder | 4 | 0 | 6 |
| Case 1: random anomaly score | DAGMM | 5 | 0 | 5 |
| Case 1: random anomaly score | GDN | 5 | 0 | 5 |
| Case 1: random anomaly score | LSTM-VAE | 4 | 0 | 6 |
| Case 1: random anomaly score | MSCRED | 6 | 0 | 4 |
| Case 1: random anomaly score | OmniAnomaly | 4 | 1 | 5 |
| Case 1: random anomaly score | THOC | 5 | 1 | 4 |
| Case 1: random anomaly score | USAD | 4 | 0 | 6 |
| Case 2: input itself as anomaly score | Case 3: untrained (randomly initialized) LSTM encoder-decoder | 6 | 1 | 3 |
| Case 2: input itself as anomaly score | DAGMM | 8 | 0 | 2 |
| Case 2: input itself as anomaly score | GDN | 2 | 0 | 8 |
| Case 2: input itself as anomaly score | LSTM-VAE | 8 | 0 | 2 |
| Case 2: input itself as anomaly score | MSCRED | 8 | 0 | 2 |
| Case 2: input itself as anomaly score | OmniAnomaly | 6 | 0 | 4 |
| Case 2: input itself as anomaly score | THOC | 6 | 0 | 4 |
| Case 2: input itself as anomaly score | USAD | 6 | 0 | 4 |
| Case 3: untrained (randomly initialized) LSTM encoder-decoder | DAGMM | 7 | 0 | 3 |
| Case 3: untrained (randomly initialized) LSTM encoder-decoder | GDN | 2 | 0 | 8 |
| Case 3: untrained (randomly initialized) LSTM encoder-decoder | LSTM-VAE | 7 | 0 | 3 |
| Case 3: untrained (randomly initialized) LSTM encoder-decoder | MSCRED | 7 | 0 | 3 |
| Case 3: untrained (randomly initialized) LSTM encoder-decoder | OmniAnomaly | 6 | 0 | 4 |
| Case 3: untrained (randomly initialized) LSTM encoder-decoder | THOC | 6 | 0 | 4 |
| Case 3: untrained (randomly initialized) LSTM encoder-decoder | USAD | 6 | 0 | 4 |
| DAGMM | GDN | 3 | 0 | 7 |
| DAGMM | LSTM-VAE | 3 | 0 | 7 |
| DAGMM | MSCRED | 4 | 1 | 5 |
| DAGMM | OmniAnomaly | 1 | 0 | 9 |
| DAGMM | THOC | 4 | 0 | 6 |
| DAGMM | USAD | 2 | 0 | 8 |
| GDN | LSTM-VAE | 8 | 0 | 2 |
| GDN | MSCRED | 9 | 0 | 1 |
| GDN | OmniAnomaly | 8 | 0 | 2 |
| GDN | THOC | 9 | 0 | 1 |
| GDN | USAD | 7 | 0 | 3 |
| LSTM-VAE | MSCRED | 7 | 0 | 3 |
| LSTM-VAE | OmniAnomaly | 3 | 0 | 7 |
| LSTM-VAE | THOC | 5 | 0 | 5 |
| LSTM-VAE | USAD | 3 | 0 | 7 |
| MSCRED | OmniAnomaly | 3 | 0 | 7 |
| MSCRED | THOC | 3 | 0 | 7 |
| MSCRED | USAD | 3 | 0 | 7 |
| OmniAnomaly | THOC | 7 | 0 | 3 |
| OmniAnomaly | USAD | 3 | 0 | 7 |
| THOC | USAD | 3 | 0 | 7 |

