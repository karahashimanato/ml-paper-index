<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# TaskBridge: Bridging Unsupervised Tabular Anomaly Detection and In-Context Learning via Virtual Tasks

- カード: [`arxiv-2609.36968`](../../papers/arxiv-2609.36968.yaml)
- 著者: Doyun Choi, Dooho Lee, Jaemin Yoo
- 年・掲載: 2026
- 原論文: [PDF](https://arxiv.org/pdf/2609.36968v1)(arXiv v1、カード作成時に読んだ版)
- タグ: classical-outlier-detectors, in-context-learning, tabular-classification, tabular-foundation-model, unsupervised
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** TaskBridge repurposes pretrained general-purpose TFMs for unsupervised tabular anomaly detection by constructing virtual supervised tasks for in-context inference.([Abstract, p.1](https://arxiv.org/pdf/2609.36968v1#page=1 "we introduce TASKBRIDGE, a new framework that efficiently repurposes pretrained general-purpose TFMs for unsupervised TAD by constructing virtual supervised tasks that directly recast anomaly detection as supervised in-context inference of TFMs"))
- **c2** Across 790 real-world datasets it outperforms 30 baselines without anomaly-specific pretraining or dataset-specific optimization.([Abstract, p.1](https://arxiv.org/pdf/2609.36968v1#page=1 "Across 790 real-world datasets, TASKBRIDGE consistently outperforms 30 baselines, including state-of-the-art TFM-based approaches, without anomaly-specific TFM pretraining or dataset-specific model optimization."))
- **c3** Evaluation is on ODDBench (790 datasets) with AUCROC/AUCPR and Elo, five seeds; framework hyperparameters are calibrated once per backbone on ADBench datasets disjoint from the main benchmark.([Experiment, p.7](https://arxiv.org/pdf/2609.36968v1#page=7 "we perform a one-time backbone-specific calibration of the framework-level hyperparameters governing Selectintra, Selectinter, and Ensemble using a set of real-world datasets from ADBench (Han et al., 2022), which are disjoint from the main benchmark"))
- **c4** Classical and shallow baselines use default PyOD hyperparameters; others follow original papers / the DTE repository.([Appendix (Baseline settings), p.25](https://arxiv.org/pdf/2609.36968v1#page=25 "we use the default PyOD hyperparameter configurations for all classical and shallow baselines"))
- **c5** Datasets are subsampled to at most 100,000 total samples for a consistent computational budget.([Appendix (Evaluation datasets), p.25](https://arxiv.org/pdf/2609.36968v1#page=25 "To ensure a consistent computational budget across datasets, we limit the total number of samples in each dataset to at most 100,000."))
- **c6** Limitation: it assumes a clean normal context; performance degrades under heavy anomaly contamination.([Conclusion, p.9](https://arxiv.org/pdf/2609.36968v1#page=9 "As shown in our appendix experiments, performance degrades when the context is heavily contaminated with anomalies."))

