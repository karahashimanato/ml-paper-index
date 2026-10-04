<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Monitoring and explainability of models in production

- カード: [`arxiv-2007.06299`](../../papers/arxiv-2007.06299.yaml)
- 著者: Janis Klaise, Arnaud Van Looveren, Clive Cox, Giovanni Vacanti, Alexandru Coca
- 年・掲載: 2020
- 原論文: [PDF](https://arxiv.org/pdf/2007.06299v1)(arXiv v1、カード作成時に読んだ版)
- タグ: dataset-shift-detection, dimensionality-reduction-for-shift, feature-attribution, mlops, model-explanation, post-hoc, two-sample-tests
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Framing (citing Diethe et al.): a big MLOps challenge is designing systems that monitor live deployments and take action or raise alerts when events affecting model performance occur.([Introduction, p.1](https://arxiv.org/pdf/2007.06299v1#page=1 "One of the big challenges in MLOps is to design systems that monitor live deployments and take action or raise alerts when events impacting model performance are encountered (Diethe et al., 2019)."))
- **c2** Without labels (citing Breck et al.), statistics of input data and output predictions are monitored as a proxy for model performance; labels for live data are seldom available in time due to operational and financial constraints.([Introduction, p.1](https://arxiv.org/pdf/2007.06299v1#page=1 "In the absence of labels it is critical to monitor the statistics of input data and output predictions as these can serve as a proxy for model performance (Breck et al., 2017)."))
- **c3** Alert thresholds: even with label-dependent metrics, a threshold or decision rule for alerts must be set; such thresholds need domain knowledge and are hard to set to limit false alarms, and the authors say alternatives based on change-point detection may prove more robust (citing Bifet, 2017).([Performance and metrics, p.2](https://arxiv.org/pdf/2007.06299v1#page=2 "Such thresholds require domain knowledge and can be difﬁcult to set appropriately to limit the number of false alarms."))
- **c4** Outlier detection is motivated by prior work (citing Recht et al., Engstrom et al., Hendrycks & Dietterich; Guo et al.; Lakshminarayanan et al.) showing models often fail to generalize outside the training distribution and are typically not well calibrated, which can lead to overconfident out-of-distribution predictions; flagged predictions are ones the authors say should not be trusted or used in production. They add that unsupervised anomaly detection on real-world data is far from solved.([Outlier detection, p.2](https://arxiv.org/pdf/2007.06299v1#page=2 "Outlier detection is therefore key to ﬂag anomalies whose model predictions we cannot trust and should not use in a production setting."))
- **c5** Acting on drift: drift detection (described with citations, e.g. Rabanser et al. 2019 for the pre-processing: dimensionality reduction followed by a two-sample test such as MMD with permutation p-values, or feature-wise KS tests with Bonferroni/FDR correction) informs the user when the model should be retrained, which the authors call especially important when performance feedback is not readily available.([Drift detection, p.3](https://arxiv.org/pdf/2007.06299v1#page=3 "Drift detection informs the user when the model should be retrained which is especially important in applications where model performance feedback is not readily available."))
- **c6** Stated open problem: relating the label-independent measures from metrics, outlier and drift detectors more directly to model performance.([Conclusion, p.4](https://arxiv.org/pdf/2007.06299v1#page=4 "One of the main open research topics is to more directly relate the label-independent measures obtained from the metrics, outlier and drift detectors to the model performance."))
- **c7** Affiliation: all five authors carry the affiliation Seldon Technologies Ltd (seldon.io e-mail addresses). Self-citation of tools: Seldon Core (Cox et al., 2018), Alibi (Klaise, Van Looveren, Vacanti, Coca, 2019) and Alibi Detect (Van Looveren, Vacanti, Klaise, Coca, 2020), all with github.com/SeldonIO URLs in the references, have authors of this paper among their authors and are among the open-source solutions highlighted in the Conclusion (alongside KFServing and creme by other authors). The paper contains no separate conflict-of-interest statement.([Title page (affiliation footnote), p.1](https://arxiv.org/pdf/2007.06299v1#page=1 "Seldon Technologies Ltd, London, United Kingdom"))

