<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# One or Two Things We know about Concept Drift -- A Survey on Monitoring Evolving Environments

- カード: [`arxiv-2310.15826`](../../papers/arxiv-2310.15826.yaml)
- 著者: Fabian Hinder, Valerie Vaquet, Barbara Hammer
- 年・掲載: 2023
- 原論文: [PDF](https://arxiv.org/pdf/2310.15826v1)(arXiv v1、カード作成時に読んだ版)
- タグ: concept-drift-detection, streaming, two-sample-tests, window-based-drift-detectors
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Most surveys cover supervised streams; this survey reviews drift in unsupervised data streams, relevant for monitoring and anomaly detection.([Abstract, p.1](https://arxiv.org/pdf/2310.15826v1#page=1 "While many surveys focus on supervised data streams, so far, there is no work reviewing the unsupervised setting."))
- **c2** It provides a taxonomy of drift detection and a systematic review of drift localization.([Abstract, p.1](https://arxiv.org/pdf/2310.15826v1#page=1 "This survey provides a taxonomy of existing work on drift detection."))
- **c3** It includes standardized experiments on parametric artificial datasets to compare detection and localization strategies directly.([Abstract, p.1](https://arxiv.org/pdf/2310.15826v1#page=1 "contains standardized experiments on parametric artificial datasets allowing for a direct comparison of different strategies for detection and localization."))
- **c4** Guideline: incorporate as much domain knowledge as possible (preprocessing, features, descriptors).([Conclusion and Guidelines for Drift Detection, p.27](https://arxiv.org/pdf/2310.15826v1#page=27 "A main finding is that as much domain knowledge as possible should be incorporated when designing drift detection schemes."))
- **c5** Meta or block-based detection methods are advisable overall; choosing good split points is crucial.([Conclusion and Guidelines for Drift Detection, p.27](https://arxiv.org/pdf/2310.15826v1#page=27 "Over all experiments, we found that it is advisable to use meta or block-based methods."))
- **c6** Feature-wise analysis only if the drift is not expected to show up in correlations; otherwise ensemble-based techniques are better.([Conclusion and Guidelines for Drift Detection, p.27](https://arxiv.org/pdf/2310.15826v1#page=27 "A feature-wise analysis should only be performed if it is expected that the drift does not inflict itself in correlations."))
- **c7** For high-dimensional data avoid dimension-wise methods, especially when false alarms are costly.([Conclusion and Guidelines for Drift Detection, p.27](https://arxiv.org/pdf/2310.15826v1#page=27 "When working with high dimensional data, one should avoid using dimension-wise methodologies, especially if false alarms are costly in the considered application."))
- **c8** Loss-based strategies should be avoided when the goal is monitoring for anomalous behavior.([Conclusion and Guidelines for Drift Detection, p.27](https://arxiv.org/pdf/2310.15826v1#page=27 "loss-based strategies should be avoided when the target of the drift detection is monitoring for anomalous behavior."))
- **c9** Detecting the time of a drift is not sufficient for monitoring; one must also localize where it happens.([Drift Localization and Segmentation, p.27](https://arxiv.org/pdf/2310.15826v1#page=27 "Solely detecting and determining the time point of the drift is not sufficient in many monitoring settings."))
- **c10** More research is needed especially on drift localization and explanation.([Conclusion, p.39](https://arxiv.org/pdf/2310.15826v1#page=39 "Finally, we found that more research is required, in particular focusing on the localization and explanation tasks."))

