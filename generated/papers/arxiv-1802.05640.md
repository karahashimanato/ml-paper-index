<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Gradient Boosting With Piece-Wise Linear Regression Trees

- カード: [`arxiv-1802.05640`](../../papers/arxiv-1802.05640.yaml)
- 著者: Yu Shi, Jian Li, Zhize Li
- 年・掲載: 2018
- 原論文: [PDF](https://arxiv.org/pdf/1802.05640v3)(arXiv v3、カード作成時に読んだ版)
- タグ: gradient-boosted-trees, linear-models, supervised, tabular-classification, tabular-regression
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Contribution: gradient boosting is extended to use piecewise linear regression trees (PL Trees) instead of piecewise constant trees as base learners; the authors state that PL Trees can accelerate convergence and improve accuracy, with optimizations reducing training time at little sacrifice of accuracy.([Abstract, p.1](https://arxiv.org/pdf/1802.05640v3#page=1 "Speciﬁcally, we extend gradient boosting to use piecewise linear regression trees (PL Trees), instead of piecewise constant regression trees, as base learners."))
- **c2** Regularization: the second-order (XGBoost-style) objective is used with an L2 penalty on the parameters of each leaf's linear model; leaf linear models are fitted analytically and split gain is the loss reduction when both children are refitted.([Gradient Boosting with PL Trees, p.2](https://arxiv.org/pdf/1802.05640v3#page=2 "This prevents the linear models in the leaves from being too steep."))
- **c3** Difference from M5/M5' model trees (used in Weka and Cubist), which fit linear models after the tree structure is fixed: the PL Tree chooses each split by the largest loss reduction considering the linear models in both children. Citing Sun et al., the authors also contrast their second-order gradients with the first-order algorithm of Wang and Hastie (2014).([Related Work and Discussions, p.5](https://arxiv.org/pdf/1802.05640v3#page=5 "By contrast, PL Tree used in our work is designed to greedily reduce the loss at each step of its growing."))
- **c4** Cost of the speedups: incremental feature selection (regressors limited to split features of ancestor nodes, up to a preset number) restricts the linear model size, and half-additive fitting gives suboptimal linear-model parameters; the authors report great speedup with a small sacrifice of accuracy (Table 1, one dataset setting).([Effects of Optimization Techniques on Accuracy, p.5](https://arxiv.org/pdf/1802.05640v3#page=5 "Incremental feature selection restricts the size of linear models, and half-additive ﬁtting results in suboptimal linear model parameters."))
- **c5** Evaluation protocol: 10 public datasets (6 regression with RMSE, 4 binary classification with AUC) against XGBoost, LightGBM and CatBoost over a grid of leaves, bins, min sum hessians, learning rate and L2 regularization, with number of trees set by learning rate x num trees = 50 (200 for CatBoost SymmetricTree) and the number of regressors fixed at 5; for the three baselines the best iteration over all settings on the test set is recorded, whereas GBDT-PL's setting is picked on a 20% validation split of the training data.([Accuracy, p.5](https://arxiv.org/pdf/1802.05640v3#page=5 "For XGBoost, LightGBM and CatBoost, result of the best iteration over all settings on test set is recorded."))
- **c6** The authors state that GBDT-PL achieves better accuracy on these dense numerical datasets, with a greater advantage on regression tasks.([Accuracy, p.5](https://arxiv.org/pdf/1802.05640v3#page=5 "With linear models on leaves, GBDT-PL achieves better accuracy in these dense numerical datasets."))
- **c7** Convergence (fixed setting: 256 leaves, 63 bins, 500 iterations, learning rate 0.1; shown only as figures): in most datasets GBDT-PL needs fewer trees to reach comparable accuracy.([Convergence Rate, p.5](https://arxiv.org/pdf/1802.05640v3#page=5 "In most datasets, GBDT-PL uses fewer trees to reach a comparable accuracy."))
- **c8** Limitation: GBDT-PL currently handles only numerical features; the authors suggest categorical features could first be converted to numerical ones as CatBoost does; GPU support is left for future work.([Related Work and Discussions, p.5](https://arxiv.org/pdf/1802.05640v3#page=5 "Currently GBDT-PL only handles numerical features."))

