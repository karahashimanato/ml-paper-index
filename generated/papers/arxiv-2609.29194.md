<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Continuous Online Fault Detection for Mobile Robots via Adaptive Edge Models

- カード: [`arxiv-2609.29194`](../../papers/arxiv-2609.29194.yaml)
- 著者: Jordan Levy, Nicolas Verstaevel, Vincent Talon, Benoit Gaudou
- 年・掲載: 2026
- 原論文: [PDF](https://arxiv.org/pdf/2609.29194v1)(arXiv v1、カード作成時に読んだ版)
- タグ: classical-outlier-detectors, streaming, time-series-anomaly-detection, time-series-foundation-model, unsupervised
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** A foundation-model teacher (TSPulse) labels data offline and a lightweight student runs online on the robot.([Abstract, p.1](https://arxiv.org/pdf/2609.29194v1#page=1 "An offline foundation model (TSPulse) generates pseudo-labels from unlabeled time series augmented with fault injections."))
- **c2** Evaluation uses VUS-PR, which penalizes late detections and prolonged false alarms.([Evaluation, p.4](https://arxiv.org/pdf/2609.29194v1#page=4 "Unlike standard point-wise metrics, VUS-PR is explicitly designed for range-based time series"))

