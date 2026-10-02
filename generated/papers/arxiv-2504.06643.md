<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# AMAD: AutoMasked Attention for Unsupervised Multivariate Time Series Anomaly Detection

- カード: [`arxiv-2504.06643`](../../papers/arxiv-2504.06643.yaml)
- 著者: Tiange Huang, Yongjun Li
- 年・掲載: 2025
- 原論文: [PDF](https://arxiv.org/pdf/2504.06643v3)(arXiv v3、カード作成時に読んだ版)
- タグ: deep-learning, reconstruction-based-detectors, time-series-anomaly-detection, unsupervised
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Existing attention-based detectors assume specific anomaly patterns (e.g. concentrated or peak anomalies), limiting generalization.([Abstract, p.1](https://arxiv.org/pdf/2504.06643v3#page=1 "the sequence anomaly association assumptions underlying these models are of- ten limited to specific predefined patterns and scenarios"))
- **c2** It reports precision, recall and F1 after the point-adjustment ('post adjustment') step of earlier works, using the same adjustment as Anomaly Transformer.([Experiments, p.10](https://arxiv.org/pdf/2504.06643v3#page=10 "we decided not to break this tradition, with the same adjustment method as [30]"))
- **c3** The threshold is a percentile of the anomaly score set by a dataset-preset prior anomaly ratio, as in Anomaly Transformer.([Experiments, p.9](https://arxiv.org/pdf/2504.06643v3#page=9 "Thresholding the p-th percentile of the AnomalyScore"))

