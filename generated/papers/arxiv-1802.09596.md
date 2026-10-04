<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Tunability: Importance of Hyperparameters of Machine Learning Algorithms

- カード: [`arxiv-1802.09596`](../../papers/arxiv-1802.09596.yaml)
- 著者: Philipp Probst, Bernd Bischl, Anne-Laure Boulesteix
- 年・掲載: 2018
- 原論文: [PDF](https://arxiv.org/pdf/1802.09596v3)(arXiv v3、カード作成時に読んだ版)
- タグ: decision-trees, gradient-boosted-trees, kernel-methods, linear-models, random-forests, supervised, tabular-classification
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Definition: the tunability of an algorithm on a dataset is the difference between the risk of a reference default configuration (package defaults or the data-based optimal defaults) and the risk of the best configuration on that dataset; per-hyperparameter tunability tunes only that hyperparameter with the others at defaults.([Measuring overall tunability of a ML algorithm, p.4](https://arxiv.org/pdf/1802.09596v3#page=4 "A general measure of the tunability of an algorithm per dataset can then be computed based on the diﬀerence between the risk of an overall reference conﬁguration (e.g., either the software defaults or deﬁnition (3)) and the risk of the best possible conﬁguration on that dataset:"))
- **c2** Data: the 38 binary classification tasks without missing values from the OpenML100 suite; algorithms: glmnet, rpart, kknn, svm, ranger (random forest) and xgboost.([Datasets from the OpenML platform, p.5](https://arxiv.org/pdf/1802.09596v3#page=5 "For our study we only use the 38 binary classiﬁcation tasks that do not contain any missing values."))
- **c3** Protocol: configurations are sampled uniformly at random within the ranges of Table 1 by an OpenML bot and evaluated by 10-fold cross-validation; a random-forest surrogate per dataset is fitted to the results, and defaults and per-dataset optima are found by random search on the surrogates.([Random Bot sampling strategy for meta data, p.7](https://arxiv.org/pdf/1802.09596v3#page=7 "In an embarrassingly parallel manner it chooses in each iteration a random dataset, a random classiﬁcation al- gorithm, samples a random conﬁguration and evaluates it via cross-validation."))
- **c4** Overfitting caveat: the new defaults are chosen with the same datasets used to measure performance, so the authors also evaluate them by a 10-fold cross-validation across datasets.([Optimizing surrogates to obtain optimal defaults, p.7](https://arxiv.org/pdf/1802.09596v3#page=7 "Of course one has to be careful with overﬁtting here, as our new defaults are chosen with the help of the same datasets that are used to determine the performance."))
- **c5** Algorithm-level result (AUC): glmnet and svm are much more tunable than the others, while ranger (random forest) is the least tunable; some datasets are outliers where tuning has a much larger impact.([Optimal defaults and tunability, p.8](https://arxiv.org/pdf/1802.09596v3#page=8 "Clearly, some algorithms such as glmnet and svm are much more tunable than the others, while ranger is the algorithm with the smallest tunability, which is in line with common knowledge in the web community."))
- **c6** Hyperparameter-level result (AUC, w.r.t. optimal defaults): for xgboost, eta and booster (tree vs linear model) are quite tunable; for ranger, mtry is the most tunable; for rpart, minbucket and minsplit seem the most important.([Tunability of speciﬁc hyperparameters, p.10](https://arxiv.org/pdf/1802.09596v3#page=10 "For xgboost there are two parameters that are quite tunable: eta and the booster."))
- **c7** For random forest, the best mtry values on quite a few datasets seem much higher than the package default; all optimal defaults fall inside the proposed tuning space while some package defaults do not.([Hyperparameter space for tuning, p.10](https://arxiv.org/pdf/1802.09596v3#page=10 "Note that for quite a few data sets much higher values than the package defaults seem advantageous."))
- **c8** Stated limitations: only binary classification; uniform random sampling may not scale to very high-dimensional spaces; defaults are static and cannot depend on dataset characteristics; initial ranges must still be set.([Conclusion and Discussion, p.14](https://arxiv.org/pdf/1802.09596v3#page=14 "Our study has some limitations that could be addressed in the future: a) We only con- sidered binary classiﬁcation, where we tried to include a wider variety of datasets from diﬀerent domains."))

