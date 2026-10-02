<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# PISCES: Physics-Informed Solar-wind Convolutional autoEncoder for Space-weather Anomaly Detection and Early Warning

- カード: [`arxiv-2609.28022`](../../papers/arxiv-2609.28022.yaml)
- 著者: Kevin Lee, Alison J. March
- 年・掲載: 2026
- 原論文: [PDF](https://arxiv.org/pdf/2609.28022v1)(arXiv v1、カード作成時に読んだ版)
- タグ: reconstruction-based-detectors, time-series-anomaly-detection, unsupervised
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** PISCES is trained without catalog labels under physics constraints and decomposes the anomaly score into physical contributions.([Abstract, p.1](https://arxiv.org/pdf/2609.28022v1#page=1 "At inference, PISCES separates the anomaly score into magnetic and plasma reconstruction errors, physics relations, and resid- ual corrections"))
- **c2** PR-AUC over all thresholds is used; the paper also notes that point-adjusted F1 can make random scores look competitive.([Evaluation, p.10](https://arxiv.org/pdf/2609.28022v1#page=10 "Point-adjusted F1 can make random anomaly scores appear competitive [41]"))
- **c3** Attenuating skip connections improves average precision of trained models while untrained scores stay nearly the same.([Abstract, p.1](https://arxiv.org/pdf/2609.28022v1#page=1 "Attenuation of the skip connections, selected on validation data, improves average precision for the trained models, while the untrained scores remain nearly the same."))
- **c4** Threshold-based alarms use the 99th percentile of anomaly scores on a separate validation period (not the test labels).([Evaluation, p.10](https://arxiv.org/pdf/2609.28022v1#page=10 "The detection threshold is the 99th percentile of composite anomaly scores in the 2016 to 2017 validation set."))

