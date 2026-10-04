<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# InterpretML: A Unified Framework for Machine Learning Interpretability

- カード: [`arxiv-1909.09223`](../../papers/arxiv-1909.09223.yaml)
- 著者: Harsha Nori, Samuel Jenkins, Paul Koch, Rich Caruana
- 年・掲載: 2019
- 原論文: [PDF](https://arxiv.org/pdf/1909.09223v1)(arXiv v1、カード作成時に読んだ版)
- タグ: feature-attribution, interpretable-models, model-explanation, post-hoc, supervised, tabular-classification
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** The package exposes two forms of interpretability: glassbox models designed for interpretability (e.g. linear models, rule lists, GAMs) and blackbox explanation techniques for existing systems (e.g. Partial Dependence, LIME), under a unified scikit-learn-style API with a visualization dashboard for comparing methods.([Abstract, p.1](https://arxiv.org/pdf/1909.09223v1#page=1 "InterpretML exposes two types of interpretability – glassbox, which are machine learning models designed for interpretability (ex: linear models, rule lists, generalized additive models), and blackbox explainability techniques for explaining existing systems (ex: Partial Dependence, LIME)."))
- **c2** EBM design: a GAM whose feature functions are learned with bagging and gradient boosting, with boosting restricted to one feature at a time in round-robin order and a very low learning rate so that feature order does not matter; round-robin cycling is said to mitigate the effects of co-linearity.([Section 3, p.3](https://arxiv.org/pdf/1909.09223v1#page=3 "The boosting procedure is carefully restricted to train on one feature at a time in round-robin fashion using a very low learning rate so that feature order does not matter."))
- **c3** EBM can automatically detect and include pairwise interaction terms; it is described as a fast, parallelizable C++/Python implementation of GA2M, citing Lou et al. (2013), with algorithmic details deferred to Lou et al. (2012, 2013) and Caruana et al. (2015).([Section 3, p.3](https://arxiv.org/pdf/1909.09223v1#page=3 "EBM is a fast implementation of the GA2M algorithm (Lou et al., 2013), written in C++ and Python."))
- **c4** Intelligibility argument: each feature's contribution can be visualized by plotting f_j, and because the model is additive each feature contributes modularly; individual predictions are sums of per-feature lookup-table contributions passed through the link function.([Section 3, p.3](https://arxiv.org/pdf/1909.09223v1#page=3 "Because EBM is an additive model, each feature contributes to predictions in a modular way that makes it easy to reason about the contribution of each feature to the prediction."))
- **c5** Accuracy claim (hedged): EBM often performs surprisingly well and is comparable with Random Forest and XGBoost; the evidence is an AUROC comparison on five classification datasets (heart-disease, breast-cancer, telecom-churn, adult-income, credit-fraud) shown in Figure 3, also including LightGBM and logistic regression.([Section 3, p.4](https://arxiv.org/pdf/1909.09223v1#page=4 "In terms of predictive power, EBM often performs surprisingly well, and is comparable with state of the art methods like Random Forest and XGBoost."))
- **c6** Evaluation protocol: all models were trained with their default parameters, and EBM's defaults are said to be chosen for computational speed; for best accuracy and interpretability the authors recommend reference parameters (100 inner bags, 100 outer bags, 5000 epochs, learning rate 0.01). No description of train/test splits or repetitions was found in the text (searched for split, fold, cross, test set, held).([Section 3 (footnote 1), p.4](https://arxiv.org/pdf/1909.09223v1#page=4 "All models were trained with their default parameters."))
- **c7** Cost: to keep terms additive EBM pays an additional training cost and is somewhat slower to train than similar methods, but prediction (additions and lookups) is among the fastest; computational performance is shown in Figure 4.([Section 3, p.4](https://arxiv.org/pdf/1909.09223v1#page=4 "To keep the individual terms additive, EBM pays an additional training cost, making it somewhat slower than similar methods."))
- **c8** Disclosure: the package (from Microsoft) includes what the authors call the first implementation of EBM, i.e. the evaluated glassbox model is the authors' own, compared against third-party baselines.([Abstract, p.1](https://arxiv.org/pdf/1909.09223v1#page=1 "InterpretML also includes the ﬁrst implementation of the Explainable Boosting Machine, a powerful, interpretable, glassbox model that can be as accurate as many blackbox models."))

