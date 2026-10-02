<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Neural Additive Models: Interpretable Machine Learning with Neural Nets

- カード: [`arxiv-2004.13912`](../../papers/arxiv-2004.13912.yaml)
- 著者: Rishabh Agarwal, Levi Melnick, Nicholas Frosst, Xuezhou Zhang, Ben Lengerich, Rich Caruana, Geoffrey Hinton
- 年・掲載: 2020
- 原論文: [PDF](https://arxiv.org/pdf/2004.13912v2)(arXiv v2、カード作成時に読んだ版)
- タグ: deep-learning, interpretable-models, model-explanation, supervised, tabular-classification, tabular-regression
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** NAMs learn a linear combination of neural networks, each of which takes a single input feature (a generalized additive model with neural-net shape functions), trained jointly.([Abstract, p.1](https://arxiv.org/pdf/2004.13912v2#page=1 "NAMs learn a linear combination of neural networks that each attend to a single input feature."))
- **c2** Interpretability argument: the per-feature shape-function plots are not just an explanation but an exact description of how the NAM computes a prediction.([Intelligibility and Modularity of NAMs, p.4](https://arxiv.org/pdf/2004.13912v2#page=4 "Please note these shape function plots are not just an explanation but an exact description of how NAMs compute a prediction."))
- **c3** As an example of intelligibility, the authors state that they validated the behaviour of NAMs on MIMIC-II with a doctor (Appendix A.1, a qualitative discussion of shape functions).([Intelligibility and Modularity of NAMs, p.4](https://arxiv.org/pdf/2004.13912v2#page=4 "A decision-maker can easily interpret such models and understand exactly how they make decisions, for example, we validated the behavior of NAMs on the MIMIC-II dataset [38] with a doctor (Appendix A.1)."))
- **c4** NAMs achieve performance comparable to Explainable Boosting Machines on the classification and regression datasets, evaluated by 5-fold cross validation.([Evaluating the Accuracy of NAMs, p.6](https://arxiv.org/pdf/2004.13912v2#page=6 "NAMs achieve comparable performance to EBMs on both classification and regression datasets, making them a competitive alternative to EBMs."))
- **c5** NAM hyperparameters (learning rate, output penalty, weight decay, dropout, feature dropout) are tuned by Bayesian optimization based on cross-validation performance with a single train-validation split per fold.([Appendix (Experimental Details), p.18](https://arxiv.org/pdf/2004.13912v2#page=18 "For computational efficiency, we tune these hyperparameters using Bayesian optimization [11, 39] based on cross-validation performance with a single train-validation split for each fold."))
- **c6** Baseline tuning: EBMs use the open-source implementation with parameters specified by prior work (linear models and decision trees are tuned by grid search).([Appendix (Hyperparameters), p.18](https://arxiv.org/pdf/2004.13912v2#page=18 "We use the open-source implementation [26] with the parameters specified by prior work [5] for a fair comparison."))
- **c7** Limitation/scope: pairwise feature interactions are not considered, to keep the paper focused on additive modelling.([Related Work, p.9](https://arxiv.org/pdf/2004.13912v2#page=9 "We don’t consider such interactions to keep the paper focused on additive modeling with neural nets."))

