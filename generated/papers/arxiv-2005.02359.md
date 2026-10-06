<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Classification-Based Anomaly Detection for General Data

- カード: [`arxiv-2005.02359`](../../papers/arxiv-2005.02359.yaml)
- 著者: Liron Bergman, Yedid Hoshen
- 年・掲載: 2020 ICLR 2020
- 原論文: [PDF](https://arxiv.org/pdf/2005.02359v1)(arXiv v1、カード作成時に読んだ版)
- タグ: anomaly-detection, deep-learning, self-supervised
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Setting: the paper addresses what it calls the semi-supervised scenario, where the training set contains only normal examples and the test data contain both normal and anomalous examples.([Introduction, p.1](https://arxiv.org/pdf/2005.02359v1#page=1 "In this setting, we have a training set of normal examples (which contains no anomalies)."))
- **c2** Problem with transformation classification (GEOM): the learned classifier is only valid for samples from the normal training subspace; for anomalies all transformed points fall outside every subspace, which the authors say makes the score have very high variance for anomalies. Using anomaly examples (Outlier Exposure) would fix this but is not possible in general, e.g. for tabular data.([Classification-Based Anomaly Detection, p.3](https://arxiv.org/pdf/2005.02359v1#page=3 "This makes the anomaly score P(m′/T(x, m)) have very high variance for anomalies."))
- **c3** Transformations and architecture: random affine matrices did not perform competitively on CIFAR-10 because they do not preserve pixel order, which CNNs exploit; as a rule of thumb, fully-connected networks can fully utilize random affine matrices. Image experiments therefore use the geometric transformations of GEOM.([Image Experiments, p.5](https://arxiv.org/pdf/2005.02359v1#page=5 "Random afﬁne matrices did not perform competitively as they are not pixel order preserving, this information is effectively used by CNNs and removing this information hurts performance."))
- **c4** Tabular protocol (Arrhythmia, Thyroid, KDDCUP99, KDDRev, following Zong et al. 2018): train on 50% of the normal data, evaluate on the other 50% plus all anomalies. OC-SVM, E2E-AE and DAGMM results are copied from Zong et al.; LOF and the feature-bagging autoencoder were computed by the authors. Large-scale experiments are repeated 5 times and small-scale GOAD experiments 500 times (due to high variance).([Tabular Data Experiments, p.7](https://arxiv.org/pdf/2005.02359v1#page=7 "OC-SVM, E2E-AE and DAGMM results are directly taken from those reported by Zong et al. (2018)."))
- **c5** Threshold for F1: following Zong et al. (2018), the decision threshold is set so that the number of test samples classified as anomalous equals the true number of anomalies in the test set (the top-N_a scores).([Tabular Data Experiments, p.7](https://arxiv.org/pdf/2005.02359v1#page=7 "Following the protocol in Zong et al. (2018), the decision threshold value is chosen to result in the correct number of anomalies e.g. if the test set contains Na anomalies, the threshold is selected so that the highest Na scoring examples are classiﬁed as anomalies."))
- **c6** Per-dataset choices: on Arrhythmia a linear classifier performed better than deeper networks (which overfit) and early stopping after a single epoch gave the best results; the same held on Thyroid; on KDDCUP99 and KDDRev deep networks are used and results are reported after 25 epochs. How these choices were selected (e.g. a validation set) was not found in the text (searched for validation, held-out, select).([Tabular Data Experiments, p.7](https://arxiv.org/pdf/2005.02359v1#page=7 "Early stopping after a single epoch generated the best results."))
- **c7** Deep vs shallow: the authors state that deep networks are beneficial for large datasets (particularly full KDDCUP99) but not needed for the smaller ones, indicating deep learning has not benefited the smaller datasets; the approach may be used in a linear setting for performance-critical operations.([Discussion, p.9](https://arxiv.org/pdf/2005.02359v1#page=9 "For performance critical operations, our approach may be used in a linear setting."))
- **c8** Contamination: although most results assume anomaly-free training data, on KDDCUP99 with X% anomalies added to training GOAD outperforms DAGMM at all impurity levels (figure), and it degrades gracefully on other datasets (Thyroid omitted for lack of anomalies; there, anomalies are split between training contamination and test); the authors say it might therefore be considered for unsupervised settings.([Discussion, p.9](https://arxiv.org/pdf/2005.02359v1#page=9 "Our method might therefore be considered in the unsupervised settings."))

