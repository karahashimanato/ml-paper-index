<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# No Scale Left Behind: Multi-Scale Autoencoder with Bi-directional Attention for Time Series Anomaly Detection

- カード: [`arxiv-2609.38004`](../../papers/arxiv-2609.38004.yaml)
- 著者: Jiaheng Guo, Haochen Zhang, Yu-Chao Huang, Jinhao Duan, Nicholas Konz, Tianlong Chen
- 年・掲載: 2026
- 原論文: [PDF](https://arxiv.org/pdf/2609.38004v1)(arXiv v1、カード作成時に読んだ版)
- タグ: deep-learning, reconstruction-based-detectors, time-series-anomaly-detection, unsupervised
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Most TSAD methods use a single temporal granularity; MSCAD exchanges information among parallel autoencoders at different patch sizes.([Abstract, p.1](https://arxiv.org/pdf/2609.38004v1#page=1 "most existing TSAD methods commit to a single temporal granularity"))
- **c2** On TSB-AD, MSCAD reports large gains over 50 baselines (VUS-PR on univariate and multivariate splits).([Abstract, p.1](https://arxiv.org/pdf/2609.38004v1#page=1 "MSCAD achieves large performance gains against 50 baselines across multiple metrics"))
- **c3** VUS-PR is the primary metric because, unlike point-adjusted F1, it is threshold-free and not gameable by random scores.([Evaluation, p.6](https://arxiv.org/pdf/2609.38004v1#page=6 "unlike Point-Adjusted F1 (PA-F1) it is threshold-free and not gameable by random scores."))
- **c4** Thresholded F1 variants of the TSB-AD implementation (reported at the best threshold when no fixed threshold is supplied) can be sensitive to threshold selection and, in some cases, point adjustment.([Evaluation metrics (appendix), p.19](https://arxiv.org/pdf/2609.38004v1#page=19 "These metrics are useful for diagnosing detector behavior but can be sensitive to threshold selection and, in some cases, to point-adjustment effects."))

