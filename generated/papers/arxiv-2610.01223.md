<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Have an LLM Write Your Anomaly Detector: Autonomous Discovery of Compact, Interpretable Detectors for Time Series

- カード: [`arxiv-2610.01223`](../../papers/arxiv-2610.01223.yaml)
- 著者: David Berghaus
- 年・掲載: 2026
- 原論文: [PDF](https://arxiv.org/pdf/2610.01223v1)(arXiv v1、カード作成時に読んだ版)
- タグ: classical-outlier-detectors, time-series-anomaly-detection, unsupervised
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** An LLM is used as the author of a detector: it repeatedly edits a short NumPy program under a leakage-free objective.([Abstract, p.1](https://arxiv.org/pdf/2610.01223v1#page=1 "We use a large language model not as the detector but as the author of one"))
- **c2** The discovered compact detectors lead TSB-AD across metrics, ahead of classical, deep and foundation-model baselines, without training a network or using a GPU.([Abstract, p.1](https://arxiv.org/pdf/2610.01223v1#page=1 "yet they train no network and use no GPU"))
- **c3** On TSB-AD it reports affiliation F-measure, temporal F1, point-wise F1 and VUS-PR.([Metrics, p.4](https://arxiv.org/pdf/2610.01223v1#page=4 "On TSB-AD we follow the Time-RCD protocol and re- port the affiliation F-measure [11]"))

