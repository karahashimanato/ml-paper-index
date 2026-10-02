<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# High-Dimensional Online Change Point Detection with Adaptive Thresholding and Interpretability

- カード: [`arxiv-2609.24278`](../../papers/arxiv-2609.24278.yaml)
- 著者: Sven Jacob, Bardh Prenkaj, Weijia Shao, Gjergji Kasneci
- 年・掲載: 2026
- 原論文: [PDF](https://arxiv.org/pdf/2609.24278v1)(arXiv v1、カード作成時に読んだ版)
- タグ: change-point-detection, feature-attribution, streaming, two-sample-tests, unsupervised, window-based-drift-detectors
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** The paper proposes a self-adapting online change point detection algorithm combining a Sliced Wasserstein score with an adaptive quantile-based threshold.([Abstract, p.1](https://arxiv.org/pdf/2609.24278v1#page=1 "we propose a self-adapting online CPD algorithm that combines this SW-based score with an adaptive quantile-based threshold"))
- **c2** Main empirical claim: the method reduces false positives on average compared with popular online and offline CPD baselines while keeping competitive or better detection performance.([Abstract, p.1](https://arxiv.org/pdf/2609.24278v1#page=1 "Empirically, our method reduces false positives by at least 48% on average compared with popular online and offline CPD baselines, while maintaining competitive or superior detection performance"))
- **c3** Evaluation metrics: AUC and segmentation covering (following the evaluation protocol of Van den Burg & Williams and Ermshaus et al.), average detection delay and the average number of false positives, on one synthetic and four real datasets (MNIST, HAR, HASC, Occupancy) with annotated change points.([Experiments (Change point detection), p.9](https://arxiv.org/pdf/2609.24278v1#page=9 "We report Area Under the Curve (AUC), segmentation covering scores (COV), average detection delay (DD), and the average number of false positives (FP)."))
- **c4** Synthetic ground truth: change points are created by injecting mean offsets into randomly selected features of a simulated stream of segments.([Experiments (Synthetic Data), p.10](https://arxiv.org/pdf/2609.24278v1#page=10 "We randomly select a total of 3 features for which we inject a drift by offsetting the mean ci randomly sampled within (−3, 3) for each drifted feature."))
- **c5** SWCPD hyperparameters were set by a fixed set of heuristic rules (window shorter than the average segment length, small quantile level), with dataset-specific values reported.([Appendix (Hyperparameter selection), p.19](https://arxiv.org/pdf/2609.24278v1#page=19 "For all experiments, hyperparameters were selected according to a fixed set of heuristic rules."))
- **c6** For the RIO-CPD baselines, window size and CUSUM threshold were grid-searched and the reported settings are those giving the best AUC; a separate validation split for this selection was not found in the text.([Appendix (baseline hyperparameters, RIO), p.23](https://arxiv.org/pdf/2609.24278v1#page=23 "The following hyperparameter resulted in the best AUC scores for RIO-LE:"))

