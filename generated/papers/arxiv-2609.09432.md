<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# SCCM : Stream Cruise Control Method for Automated Drift Detection and Adaptation

- カード: [`arxiv-2609.09432`](../../papers/arxiv-2609.09432.yaml)
- 著者: Mohammad Abu-Shaira, Weishi Shi
- 年・掲載: 2026
- 原論文: [PDF](https://arxiv.org/pdf/2609.09432v1)(arXiv v1、カード作成時に読んだ版)
- タグ: concept-drift-detection, error-rate-drift-detectors, linear-models, streaming, supervised, tabular-regression, window-based-drift-detectors
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** The paper presents SCCM, a framework combining drift detection and adaptation for online regression.([Abstract, p.1](https://arxiv.org/pdf/2609.09432v1#page=1 "This paper presents the Stream Cruise Control Method (SCCM ), a comprehensive framework for drift detection and adaptation in online regression."))
- **c2** Evaluation scope: SCCM is attached to four online regressors and evaluated on synthetic streams with abrupt, incremental and alternating gradual drift plus real-world datasets.([Abstract, p.1](https://arxiv.org/pdf/2609.09432v1#page=1 "SCCM is integrated with four online regression models and evaluated on 18 synthetic datasets covering abrupt, incremental, and alternating gradual drift, together with eight real-world datasets."))
- **c3** Baselines combine ADWIN or KSWIN with four adaptation strategies; the detectors use scikit-multiflow default settings.([Experimental setup (Baseline Configuration Protocol), p.36](https://arxiv.org/pdf/2609.09432v1#page=36 "Specifically, ADWIN used δ = 0.002, while KSWIN used αKS = 0.005, WKS = 100, and SKS = 30."))
- **c4** No detector parameter search was done for the baselines; the authors argue that grid search over the evaluated stream would introduce look-ahead bias.([Experimental setup (Baseline Configuration Protocol), p.37](https://arxiv.org/pdf/2609.09432v1#page=37 "Consequently, no detector candidate grid, designated pilot seed, separate pilot stream, or data-driven detector-parameter selection procedure was used."))
- **c5** Detection metrics (TP, FP, missed drifts, delay, precision, recall, F1) are computed only on synthetic streams, because the real datasets have no annotated drift locations.([Drift-Alarm Quality Metrics and Alignment Protocol, p.40](https://arxiv.org/pdf/2609.09432v1#page=40 "Because the real-world datasets do not provide annotated drift locations or known concept boundaries, ground-truth alarm-quality metrics are evaluated only on the synthetic datasets."))
- **c6** The alarm-matching parameters were applied identically to SCCM, ADWIN and KSWIN and fixed before the final comparative analysis, with a separate sensitivity analysis.([Drift-Alarm Quality Metrics and Alignment Protocol, p.42](https://arxiv.org/pdf/2609.09432v1#page=42 "These values are applied identically to SCCM , ADWIN, and KSWIN and were fixed before the final comparative analysis."))

