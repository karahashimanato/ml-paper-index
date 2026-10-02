<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Current Time Series Anomaly Detection Benchmarks are Flawed and are Creating the Illusion of Progress

- カード: [`arxiv-2009.13807`](../../papers/arxiv-2009.13807.yaml)
- 著者: Renjie Wu, Eamonn J. Keogh
- 年・掲載: 2020
- 原論文: [PDF](https://arxiv.org/pdf/2009.13807v5)(arXiv v5、カード作成時に読んだ版)
- タグ: classical-outlier-detectors, deep-learning, time-series-anomaly-detection, unsupervised
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Most exemplars of popular TSAD benchmarks (Yahoo, Numenta, NASA, ...) have one or more of four flaws: triviality, unrealistic anomaly density, mislabeled ground truth, run-to-failure bias.([Introduction, p.1](https://arxiv.org/pdf/2009.13807v5#page=1 "These flaws are triviality, unrealistic anomaly density, mislabeled ground truth and run-to-failure bias."))
- **c2** Because of these flaws, most published comparisons of anomaly detectors may be unreliable and apparent progress may be illusory.([Introduction, p.1](https://arxiv.org/pdf/2009.13807v5#page=1 "we believe that most published comparisons of anomaly detection algorithms may be unreliable"))
- **c3** Triviality: 316 of the 367 Yahoo time series can be solved by a 'one-liner' (a single line of basic code).([Flaw: triviality, p.3](https://arxiv.org/pdf/2009.13807v5#page=3 "316 out of 367 (86.1%) can be easily solved with a one-liner"))
- **c4** Ideally each test time series should contain exactly one anomaly, communicated with the dataset.([Flaw: unrealistic anomaly density, p.4](https://arxiv.org/pdf/2009.13807v5#page=4 "We believe that the ideal number of anomalies in a single testing time series is exactly one."))
- **c5** All benchmark datasets appear to contain mislabeled data (false positives and false negatives).([Flaw: mislabeled ground truth, p.4](https://arxiv.org/pdf/2009.13807v5#page=4 "All of the benchmark datasets appear to have mislabeled data, both false positives and false negatives."))
- **c6** Run-to-failure bias: anomalies cluster near the end, so naively flagging the last point scores well.([Flaw: run-to-failure bias, p.6](https://arxiv.org/pdf/2009.13807v5#page=6 "A naïve algorithm that simply labels the last point as an anomaly"))
- **c7** The classic TSAD archives are irretrievably flawed.([Summary of the flaws, p.6](https://arxiv.org/pdf/2009.13807v5#page=6 "the classic time series anomaly detection archives are irretrievably flawed."))
- **c8** On these datasets no level of reported performance can demonstrate an algorithm's utility.([Summary of the flaws, p.6](https://arxiv.org/pdf/2009.13807v5#page=6 "Thus, there is simply no level of performance that would suggest the utility of a"))
- **c9** The paper introduces the UCR Time Series Anomaly Archive as a benchmark for meaningful comparisons.([Abstract, p.1](https://arxiv.org/pdf/2009.13807v5#page=1 "with this paper we introduce the UCR Time Series Anomaly Archive."))
- **c10** Some researchers seem to rarely look at the time series and only at F1 scores; the flaws are visible by plotting.([Recommendations, p.8](https://arxiv.org/pdf/2009.13807v5#page=8 "We suspect that some researchers rarely view the time series, they simply pass objects to a black box and look at the F1 scores"))
- **c11** Scoring without tolerance can systematically penalize an algorithm that places its anomaly peak at a different position in the subsequence.([Recommendations, p.8](https://arxiv.org/pdf/2009.13807v5#page=8 "we run the risk of a systemic bias against an algorithm that simply formats its output differently to its rival."))
- **c12** Many recent papers presuppose that deep learning is the answer to anomaly detection.([Recommendations, p.8](https://arxiv.org/pdf/2009.13807v5#page=8 "Many recent papers seem to pose their research question as"))

