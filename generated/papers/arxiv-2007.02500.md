<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Deep Learning for Anomaly Detection: A Review

- カード: [`arxiv-2007.02500`](../../papers/arxiv-2007.02500.yaml)
- 著者: Guansong Pang, Chunhua Shen, Longbing Cao, Anton van den Hengel
- 年・掲載: 2020 ACM Computing Surveys
- 原論文: [PDF](https://arxiv.org/pdf/2007.02500v3)(arXiv v3、カード作成時に読んだ版)
- タグ: anomaly-detection, autoencoders, deep-learning, reconstruction-based-detectors, semi-supervised, supervised, unsupervised
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** The authors argue that deep methods offer end-to-end optimization and representations tailored to anomaly detection, which traditional methods lack, and that although shallow methods exist for complex data (high-dimensional, image, video, graph, heterogeneous sources), they are generally substantially weaker and less adaptive than deep methods (summarized in Table 1). This is an argument in the review, not an empirical comparison carried out in it.([Section 2.2, p.5](https://arxiv.org/pdf/2007.02500v3#page=5 "Although there are shallow methods for handling those complex data, they are generally substantially weaker and less adaptive than the deep methods."))
- **c2** Terminology: methods trained on purely normal training data, which some studies call unsupervised, are referred to in this review as semi-supervised (following [2, 28]); weakly-supervised detection instead assumes partial, inexact or inaccurate anomaly labels.([Section 2.2, p.4](https://arxiv.org/pdf/2007.02500v3#page=4 "To avoid unnecessary confusion, following [2, 28], these methods are referred to as semi-supervised methods hereafter."))
- **c3** Challenge CH3: fully supervised detection is often impractical because labeled anomalies are costly, and unsupervised methods have no prior knowledge of true anomalies and rely heavily on their assumption about the anomaly distribution; leveraging readily available labeled normal data and some labeled anomalies is therefore suggested.([Section 2.2, p.4](https://arxiv.org/pdf/2007.02500v3#page=4 "However, unsupervised methods do not have any prior knowledge of true anomalies."))
- **c4** Disadvantages of using deep models only as feature extractors (e.g. pre-trained networks followed by a conventional detector): fully disjoint feature extraction and scoring often give suboptimal anomaly scores, and pre-trained deep models are typically limited to specific types of data; the projection may not preserve enough information for detection.([Section 4, p.8](https://arxiv.org/pdf/2007.02500v3#page=8 "Pre-trained deep models are typically limited to specific types of data."))
- **c5** No meta-analysis of performance: because the methods are evaluated on diverse datasets, the review does not compare their empirical performance; it observes instead that most methods are unsupervised or semi-supervised, deep-learning tricks (augmentation, dropout, pre-training) are under-explored, and most networks have no more than five layers.([Section 7.1, p.27](https://arxiv.org/pdf/2007.02500v3#page=27 "Since these methods are evaluated on diverse datasets, it is difficult to have an universal meta-analysis of their empirical performance."))
- **c6** Evaluation datasets: a main obstacle is the lack of real-world datasets with real anomalies; many studies evaluate on datasets converted from classification data, which may fail to reflect performance in real-world applications. The review lists 21 public datasets with real anomalies, restricted to large-scale and/or high-dimensional ones.([Section 7.2, p.27](https://arxiv.org/pdf/2007.02500v3#page=27 "This way may fail to reflect the performance of the methods in real-world anomaly detection applications."))
- **c7** Most methods learning representations of normality implicitly assume that the training data is clean (free of anomalies), so large-scale normality learning needs anomaly-free unlabeled data or robustness to contamination.([Section 8.3, p.30](https://arxiv.org/pdf/2007.02500v3#page=30 "This is because most methods in Sections 5 implicitly assume that the training data is clean and does not contain any noise/anomaly instances."))
- **c8** The review states that most deep anomaly detection methods focus on point anomalies and show substantially better performance than traditional methods, while deep models for conditional/group anomalies are much less explored. No supporting comparison is given in this sentence, and Section 7.1 says a universal meta-analysis is difficult.([Section 8.4, p.30](https://arxiv.org/pdf/2007.02500v3#page=30 "Most deep anomaly detection methods focus on point anomalies, showing substantially better performance than traditional methods."))

