<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Learning under Concept Drift: A Review

- カード: [`arxiv-2004.05785`](../../papers/arxiv-2004.05785.yaml)
- 著者: Jie Lu, Anjin Liu, Fan Dong, Feng Gu, João Gama, Guangquan Zhang
- 年・掲載: 2020
- 原論文: [PDF](https://arxiv.org/pdf/2004.05785v1)(arXiv v1、カード作成時に読んだ版)
- タグ: concept-drift-detection, error-rate-drift-detectors, streaming, two-sample-tests, window-based-drift-detectors
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** The survey reviews over 130 publications on concept drift.([Abstract, p.1](https://arxiv.org/pdf/2004.05785v1#page=1 "This paper reviews over 130 high quality publications in concept drift related research areas"))
- **c2** Learning under concept drift is organized into three components: drift detection, drift understanding and drift adaptation.([Abstract, p.1](https://arxiv.org/pdf/2004.05785v1#page=1 "establishes a framework of learning under concept drift including three main components: concept drift detection, concept drift understanding, and concept drift adaptation."))
- **c3** Concept drift is defined as a change of the joint distribution P(X, y) over time (covering covariate shift and changes in P(y|X)).([Concept drift definition, p.3](https://arxiv.org/pdf/2004.05785v1#page=3 "concept drift at time t can be defined as the change of joint probability of X and y at time t."))
- **c4** Drift in P(X) alone does not move the decision boundary and is called virtual drift.([Concept drift definition, p.3](https://arxiv.org/pdf/2004.05785v1#page=3 "drift does not affect the decision boundary, it has also been considered as virtual drift"))
- **c5** Without the data-retrieval stage, drift detection can be viewed as a two-sample test problem.([Drift detection framework, p.4](https://arxiv.org/pdf/2004.05785v1#page=4 "the concept drift detection problem can be considered as a two-sample test problem which examines whether the population of two given sample sets are from the same distribution"))
- **c6** Drift detectors are classified into three categories by their test statistic: error rate-based, data distribution-based, and multiple hypothesis test.([Section 3.2, p.4](https://arxiv.org/pdf/2004.05785v1#page=4 "This section surveys drift detection methods and algorithms, which are classified into three categories in terms of the test statistics they apply."))
- **c7** Error rate-based detectors (tracking the online error rate of a base classifier) are the largest category.([Section 3.2.1, p.4](https://arxiv.org/pdf/2004.05785v1#page=4 "error rate-based drift detection algorithms form the largest category of algorithms."))
- **c8** DDM was the first algorithm to define warning and drift levels.([Section 3.2.1, p.4](https://arxiv.org/pdf/2004.05785v1#page=4 "the first algorithm to define the warning level and drift"))
- **c9** Data distribution-based detectors address drift at its root (the distribution) and can locate it, but usually cost more computation and need predefined windows.([Data distribution-based drift detection, p.5](https://arxiv.org/pdf/2004.05785v1#page=5 "these algorithms are usually reported as incurring higher computational cost than the algorithms mentioned in Section 3.2.1"))
- **c10** All drift detectors can answer 'when', but very few can answer 'how' and 'where'.([Conclusions, p.14](https://arxiv.org/pdf/2004.05785v1#page=14 "all drift detection methods can answer 'When', but very few methods have the ability to answer 'How' and 'Where';"))
- **c11** Most detection and adaptation algorithms assume true labels are available right after prediction; unsupervised/semi-supervised drift detection is rarely studied.([Conclusions, p.14](https://arxiv.org/pdf/2004.05785v1#page=14 "Most existing drift detection and adaptation algorithms assume the ground true label is available after classification/prediction, or extreme verification latency."))
- **c12** There is no comprehensive analysis of real-world streams in terms of drift time, severity and regions.([Conclusions, p.14](https://arxiv.org/pdf/2004.05785v1#page=14 "There is no comprehensive analysis on real-world data streams from the concept drift aspect"))
- **c13** The survey lists 10 synthetic and 14 public real-world datasets used to evaluate drift handling.([Abstract, p.1](https://arxiv.org/pdf/2004.05785v1#page=1 "This paper lists and discusses 10 popular synthetic datasets and 14 publicly available benchmark datasets"))
- **c14** Research on retraining models with explicit drift detection has slowed; adaptive models and ensembles have become more important.([Conclusions, p.14](https://arxiv.org/pdf/2004.05785v1#page=14 "research of retraining models with explicit drift detection has slowed;"))

