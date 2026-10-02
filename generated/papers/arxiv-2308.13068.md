<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Multivariate Time Series Anomaly Detection: Fancy Algorithms and Flawed Evaluation Methodology

- カード: [`arxiv-2308.13068`](../../papers/arxiv-2308.13068.yaml)
- 著者: Mohamed El Amine Sehili, Zonghua Zhang
- 年・掲載: 2023
- 原論文: [PDF](https://arxiv.org/pdf/2308.13068v2)(arXiv v2、カード作成時に読んだ版)
- タグ: classical-outlier-detectors, forecasting-based-detectors, reconstruction-based-detectors, tabular-attention, time-series-anomaly-detection, unsupervised
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Most MVTS anomaly detection methods are evaluated with inappropriate or highly flawed protocols.([Abstract, p.1](https://arxiv.org/pdf/2308.13068v2#page=1 "most proposed solutions are evaluated using either inappropriate or highly flawed protocols, with an apparent lack of scientific foundation."))
- **c2** Under the point-adjust protocol a random guess can systematically outperform all algorithms developed so far.([Abstract, p.1](https://arxiv.org/pdf/2308.13068v2#page=1 "So flawed is one very popular protocol, the so-called point-adjust protocol, that a random guess can be shown to systematically outperform all algorithms developed so far."))
- **c3** A simple PCA baseline outperforms many recent deep learning approaches on popular benchmarks.([Abstract, p.1](https://arxiv.org/pdf/2308.13068v2#page=1 "we propose a simple, yet challenging, baseline based on Principal Components Analysis (PCA) that surprisingly outperforms many recent Deep Learning (DL) based approaches on popular benchmark datasets."))
- **c4** Algorithms developed with point-adjust as the sole target fail to beat a random guess under other protocols (AnomalyTransformer, NCAD).([Section 5, p.13](https://arxiv.org/pdf/2308.13068v2#page=13 "Algorithms that were developed using point-adjust as the sole target fail to reach any score better than a random guess when evaluated with other"))
- **c5** Untrained versions of these models reached essentially the same high point-adjust scores.([Section 5, p.14](https://arxiv.org/pdf/2308.13068v2#page=14 "we also achieved essentially the same high scores using untrained versions of these models."))
- **c6** GDN, developed with the point-wise protocol, was more resilient under other protocols.([Section 5, p.14](https://arxiv.org/pdf/2308.13068v2#page=14 "GDN, however, which was developed based on the more realistic point-wise protocol, shows more resilience when evaluated with other protocols."))
- **c7** On datasets with very high contamination such as PSM, point-wise F1 can be misleading.([Section 5, p.14](https://arxiv.org/pdf/2308.13068v2#page=14 "Datasets that have a very high contamination rate, such as PSM, yield point-wise F1 scores that can be misleading."))
- **c8** All Table 1 metrics use the threshold that gives the best point-wise F1.([Table 1 caption, p.13](https://arxiv.org/pdf/2308.13068v2#page=13 "All metrics are computed based on the detection threshold that yields the best point-wise performance."))
- **c9** At its best point-adjust threshold, AnomalyTransformer raises an alarm about every 110 seconds on SWaT - barely useful in deployment.([Section 5, p.15](https://arxiv.org/pdf/2308.13068v2#page=15 "On average, it raises an alarm every 110 seconds, making it, in our opinion, barely useful for deployment."))
- **c10** The PCA pipeline uses simple pre- and post-processing (scaling, clipping, score smoothing) that significantly improves its score.([Section 5, p.14](https://arxiv.org/pdf/2308.13068v2#page=14 "we use simple pre-processing and post-processing blocks (input scaling, clipping and score smoothing) that significantly improve the score."))
- **c11** The point-wise protocol is not appropriate for all datasets and use cases; an event-wise protocol is proposed.([Introduction, p.2](https://arxiv.org/pdf/2308.13068v2#page=2 "We also review the more objective point-wise protocol and show that it is not appropriate for all kinds of datasets and use-cases."))
- **c12** Many works were developed without a simple but sufficiently challenging baseline.([Section 5, p.14](https://arxiv.org/pdf/2308.13068v2#page=14 "many works have been developed without establishing a simple but enough challenging baseline."))
- **c13** The authors urge more effort on data, experiment design and evaluation instead of increasingly complex algorithms.([Abstract, p.1](https://arxiv.org/pdf/2308.13068v2#page=1 "instead of putting the highest weight on the design of increasingly more complex"))

## 結果表

列ごとに比較条件が異なる。**同じ列の中だけ**比較できる。太字は列内の最良値。

#### f1-pointwise(大きいほど良い)

繰り返し: Not stated.

| method | `sehili2023-swat` | `sehili2023-wadi` | `sehili2023-psm` |
|---|---|---|---|
| AnomalyTransformer | 0.214 | 0.108 | 0.434 |
| NCAD | 0.217 | 0.114 | 0.429 |
| GDN | **0.821** | **0.567** | **0.594** |
| PCA (with scaling, clipping, score smoothing) | 0.81 | 0.374 | 0.538 |

出典: [Table 1, p.13](https://arxiv.org/pdf/2308.13068v2#page=13 "AT 0.214 0.214 0.000 35/0 0.108 0.108 0.000 14/0 0.434 0.434 0.000 72/0")

#### f1-composite(大きいほど良い)

繰り返し: Not stated.

| method | `sehili2023-swat` | `sehili2023-wadi` | `sehili2023-psm` |
|---|---|---|---|
| AnomalyTransformer | 0.214 | 0.108 | 0.434 |
| NCAD | 0.217 | 0.115 | 0.429 |
| GDN | 0.488 | **0.764** | **0.64** |
| PCA (with scaling, clipping, score smoothing) | **0.596** | 0.655 | 0.484 |

出典: [Table 1, p.13](https://arxiv.org/pdf/2308.13068v2#page=13 "AT 0.214 0.214 0.000 35/0 0.108 0.108 0.000 14/0 0.434 0.434 0.000 72/0")

#### f1-event(大きいほど良い)

繰り返し: Not stated.

| method | `sehili2023-swat` | `sehili2023-wadi` | `sehili2023-psm` |
|---|---|---|---|
| AnomalyTransformer | 0 | 0 | 0 |
| NCAD | 0.002 | 0.003 | 0 |
| GDN | 0.478 | 0.485 | 0.096 |
| PCA (with scaling, clipping, score smoothing) | **0.555** | **0.608** | **0.2** |

出典: [Table 1, p.13](https://arxiv.org/pdf/2308.13068v2#page=13 "AT 0.214 0.214 0.000 35/0 0.108 0.108 0.000 14/0 0.434 0.434 0.000 72/0")

## 論文内の勝敗(結果から導出)

同じ比較条件での数値の大小だけを数えたもの。**統計的有意性は考慮していない**。

| A | B | A勝ち | 引き分け | B勝ち |
|---|---|---|---|---|
| AnomalyTransformer | GDN | 0 | 0 | 9 |
| AnomalyTransformer | NCAD | 2 | 1 | 6 |
| AnomalyTransformer | PCA (with scaling, clipping, score smoothing) | 0 | 0 | 9 |
| GDN | NCAD | 9 | 0 | 0 |
| GDN | PCA (with scaling, clipping, score smoothing) | 5 | 0 | 4 |
| NCAD | PCA (with scaling, clipping, score smoothing) | 0 | 0 | 9 |

