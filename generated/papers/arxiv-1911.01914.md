<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# A Comparative Analysis of XGBoost

- カード: [`arxiv-1911.01914`](../../papers/arxiv-1911.01914.yaml)
- 著者: Candice Bentéjac, Anna Csörgő, Gonzalo Martínez-Muñoz
- 年・掲載: 2019
- 原論文: [PDF](https://arxiv.org/pdf/1911.01914v1)(arXiv v1、カード作成時に読んだ版)
- タグ: gradient-boosted-trees, random-forests, supervised, tabular-classification
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Setup: 28 UCI classification datasets; scikit-learn random forest and gradient boosting and the XGBoost package, each evaluated with package defaults and with grid-search tuning; accuracy estimated by stratified 10-fold cross-validation, with tuning by a nested stratified 10-fold cross-validation inside each training set.([Experimental results, p.6](https://arxiv.org/pdf/1911.01914v1#page=6 "The comparison was carried out using stratiﬁed 10-fold cross-validation."))
- **c2** Fixed choices: all ensembles had 200 trees (the authors argue ensemble size need not be tuned), and XGBoost's own missing-value handling was not used; missing values were mean-imputed for a fairer comparison with scikit-learn trees.([Experimental results, p.8](https://arxiv.org/pdf/1911.01914v1#page=8 "All ensembles were composed of 200 decision trees."))
- **c3** Tuning budgets differ between methods: the grids had 3840, 256 and 1920 configurations for XGBoost, random forest and gradient boosting, so the tuning time is not directly comparable between classifiers.([Experimental results, p.11](https://arxiv.org/pdf/1911.01914v1#page=11 "Since the size of the grid is diﬀerent for diﬀerent classiﬁers (i.e. 3840, 256 and 1920 for XGB, RF and GB respectively), the time dedicated to ﬁnding the best parameters is not directly comparable between classiﬁers."))
- **c4** Default vs tuned: default random forest performs closest to its tuned counterpart, while default XGBoost and gradient boosting generally perform worse than tuned versions, though not always.([Experimental results, p.9](https://arxiv.org/pdf/1911.01914v1#page=9 "Default random forest is the method that performs more evenly with respect to its tuned counterpart."))
- **c5** On some datasets default XGBoost beat tuned XGBoost; the authors attribute this to noisy data plus good defaults, noting that parameter estimation, even within training cross-validation, may overfit the training set especially on noisy datasets.([Experimental results, p.9](https://arxiv.org/pdf/1911.01914v1#page=9 "The parameter esti- mation process, even though it is performed within train cross-validation, may overﬁt the training set specially in noisy datasets."))
- **c6** No statistically significant differences in average rank among the six tested configurations (Nemenyi test).([Experimental results, p.9](https://arxiv.org/pdf/1911.01914v1#page=9 "From Figure 1, it can be observed that there are not any statistically sig- niﬁcant diﬀerences among the average ranks of the six tested methods."))
- **c7** Conclusion on tuning: a meticulous parameter search is necessary for accurate gradient-boosting-based models, but not for random forest, whose performance was slightly better on average with default (Breiman's) values.([Conclusion, p.17](https://arxiv.org/pdf/1911.01914v1#page=17 "In consequence, we conclude that a meticulous parameter search is necessary to create accurate models based on gradient boosting."))
- **c8** Which XGBoost hyperparameters matter: tuning the randomization parameters (subsampling rate, features per split) seems unnecessary provided reasonable values are used; including the gamma complexity term may give a small, not statistically significant edge.([Analysis of XGBoost parametrization, p.15](https://arxiv.org/pdf/1911.01914v1#page=15 "A conclusion that may be clearer is that it seems unnecessary to tune the number of random features and the subsampling rate provided that those techniques are applied with reasonable values (in our case subsampling to 0.75 and feature sampling to sqrt)."))

