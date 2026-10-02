<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# What the Detector Can See: Evaluating CPS Anomaly Detectors Independently of the Decision Rule

- カード: [`arxiv-2608.02821`](../../papers/arxiv-2608.02821.yaml)
- 著者: Peiran Shi, Jian Xiang, Xiang Zhang, Chenglong Fu
- 年・掲載: 2026
- 原論文: [PDF](https://arxiv.org/pdf/2608.02821v1)(arXiv v1、カード作成時に読んだ版)
- タグ: deep-learning, time-series-anomaly-detection, unsupervised
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Precision/recall/F1 at one operating point mix two things: how well the detector represents the process and how well its alarm threshold is set.([Abstract, p.1](https://arxiv.org/pdf/2608.02821v1#page=1 "These scores mix two separate things: how well the detector represents the physical process, and how well its alarm threshold is set."))
- **c2** The paper evaluates the detector's residuals directly, independent of any alarm rule (threshold, CUSUM, point adjustment).([Abstract, p.1](https://arxiv.org/pdf/2608.02821v1#page=1 "Instead of scoring only the final alarms, we evaluate Stage 1 directly using normalized residual energy"))
- **c3** Detectors with similar ROC-AUC on SWaT differ by more than an order of magnitude at a common false-alarm rate.([Abstract, p.1](https://arxiv.org/pdf/2608.02821v1#page=1 "Although the detectors have similar ROC-AUC values on SWaT, their performance differs by more than an order of magnitude at a common false-alarm rate."))
- **c4** Rankings change across testbeds (e.g. TranAD first on HAI but last on SWaT).([Abstract, p.1](https://arxiv.org/pdf/2608.02821v1#page=1 "Rankings also change across testbeds: TranAD ranks first on HAI but last on SWaT, while NSIBF ranks first on WADI but last on HAI."))
- **c5** Detection failures can stem from a weak representation, poor threshold calibration, or an attack with little physical effect.([Abstract, p.1](https://arxiv.org/pdf/2608.02821v1#page=1 "These results show that detection failure can come from different sources: a weak representation, poor threshold calibration, or an attack with little physical effect."))

