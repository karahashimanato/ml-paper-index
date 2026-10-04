<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# CatBoost: gradient boosting with categorical features support

- カード: [`arxiv-1810.11363`](../../papers/arxiv-1810.11363.yaml)
- 著者: Anna Veronika Dorogush, Vasily Ershov, Andrey Gulin
- 年・掲載: 2018
- 原論文: [PDF](https://arxiv.org/pdf/1810.11363v1)(arXiv v1、カード作成時に読んだ版)
- タグ: gradient-boosted-trees, supervised, tabular-classification
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** One-hot encoding of categorical features can be done at preprocessing or during training; CatBoost does it during training, which the authors say is more efficient in training time.([Categorical features, p.2](https://arxiv.org/pdf/1810.11363v1#page=2 "One-hot encoding can be done during the preprocessing phase or during training, the latter can be implemented more efﬁciently in terms of training time and is implemented in CatBoost."))
- **c2** Feature combinations: since the number of combinations of categorical features grows exponentially, CatBoost considers them greedily: none for the first split, then combinations of categorical features already in the current tree with all categorical features, converted to numbers on the fly; splits on numerical features are also used in combinations as two-valued categorical features.([Categorical features, p.2](https://arxiv.org/pdf/1810.11363v1#page=2 "When constructing a new split for the current tree, CatBoost considers combinations in a greedy way."))
- **c3** Gradient bias: gradients at each step are estimated on the same data points the current model was built on, which the authors say shifts the distribution of estimated gradients and leads to overfitting; the formal analysis is referenced to the authors' earlier paper [5] (arXiv:1706.09516).([Fighting Gradient Bias, p.3](https://arxiv.org/pdf/1810.11363v1#page=3 "Gradients used at each step are estimated using the same data points the current model was built on."))
- **c4** CatBoost uses the modified (unbiased-gradient) scheme only for choosing the tree structure, setting leaf values with the traditional GBDT scheme; the per-example models are relaxed so that all share the same tree structures.([Fighting Gradient Bias, p.3](https://arxiv.org/pdf/1810.11363v1#page=3 "CatBoost implementation uses the following relaxation of this idea: all Mi share the same tree structures."))
- **c5** Quality comparison protocol against XGBoost, LightGBM and H2O: categorical features preprocessed with statistics on a random permutation, tuning and training on 4/5 of the data, testing on 1/5, final training repeated with 5 seeds and logloss averaged; the detailed setup (including the tuning procedure) is said to be on the authors' GitHub rather than in the paper.([Experiments, p.5](https://arxiv.org/pdf/1810.11363v1#page=5 "The parameter tunning and training was performed on 4/5 of the data and the testing was performed on the other 1/5."))
- **c6** The authors state CatBoost outperforms the other algorithms on all datasets in the classification comparison, and point to their GitHub repository (not shown in the paper) for results of default-parameter CatBoost against tuned baselines.([Experiments, p.5](https://arxiv.org/pdf/1810.11363v1#page=5 "In our repo on github you can also see that CatBoost with default parameters outperforms tunned XGBoost and H2O on all datasets and LightGBM on all but one datasets."))
- **c7** The authors say training speed is very hard to compare across boosting libraries because parameters affect speed, quality and model size in non-obvious ways, so they only compare the time to train ensembles of fixed size (8000 trees on Epsilon, 15 bins, depth 6 or 64 leaves).([GPU training performance: comparison with baselines, p.6](https://arxiv.org/pdf/1810.11363v1#page=6 "As a result, we can’t compare libraries by time we need to obtain certain level of quality."))
- **c8** Cost of the bias-fighting scheme: by design 2-3 times slower than classical boosting; the GPU speed benchmark used the classic scheme instead.([GPU training performance: comparison with baselines, p.6](https://arxiv.org/pdf/1810.11363v1#page=6 "This scheme is by design 2-3 times slower then classical boosting approach."))

