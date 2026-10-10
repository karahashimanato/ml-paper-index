<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# True to the Model or True to the Data?

- カード: [`arxiv-2006.16234`](../../papers/arxiv-2006.16234.yaml)
- 著者: Hugh Chen, Joseph D. Janizek, Scott Lundberg, Su-In Lee
- 年・掲載: 2020
- 原論文: [PDF](https://arxiv.org/pdf/2006.16234v1)(arXiv v1、カード作成時に読んだ版)
- タグ: feature-attribution, linear-models, model-explanation, post-hoc
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Responding to Kumar et al. (2020), who suggest the two value functions present an irreconcilable problem, the authors argue that interventional and observational Shapley values are each meaningful when applied in the proper context (the choice is application dependent).([Introduction, p.2](https://arxiv.org/pdf/2006.16234v1#page=2 "in this paper, we argue that rather than representing some critical flaw in using the Shapley value for feature attribution, each approach is meaningful when applied in the proper context"))
- **c2** Assumption: to compute observational Shapley values for linear models, inputs are assumed to be multivariate normal.([Linear SHAP, p.2](https://arxiv.org/pdf/2006.16234v1#page=2 "Estimating this conditional expectation is hard in general, so we assume the inputs x ∼N(µ, Σ) are multivariate normal."))
- **c3** On NHANES mortality data, a feature excluded from a linear model (BMI) receives importance under observational Shapley values because of its correlation with the used features.([Explaining a feature not used by the model, p.3](https://arxiv.org/pdf/2006.16234v1#page=3 "This implies that even though BMI is not included in the model, the correlation between BMI and other features makes BMI important under observational Shapley values."))
- **c4** 'True to the model' evaluation on LendingClub with logistic regression: features are ranked by Shapley value, mean-imputed one at a time (up to 10), and the change in predicted log-odds of default is measured.([True to the Model, p.5](https://arxiv.org/pdf/2006.16234v1#page=5 "We then measured the change in the model’s predicted log odds of default after each feature (up to 10 features) had been mean-imputed."))
- **c5** In that loan setting, interventional Shapley values led to significantly better results than observational ones.([True to the Model, p.5](https://arxiv.org/pdf/2006.16234v1#page=5 "We find that using the interventional conditional expectation leads to significantly better results than the observational conditional expectation (Figure 3)."))
- **c6** 'True to the data' evaluation with ground truth: drug-response labels are simulated from 40 randomly selected causal genes on real RNA-seq data; for a Lasso model, observational Shapley values recover more true causal genes than interventional ones.([True to the Data, p.5](https://arxiv.org/pdf/2006.16234v1#page=5 "To create an experimental setting where we have access to the ground truth, we take the real RNA-seq data and simulate a drug response label as a function of 40 randomly selected causal genes (out of 1000 total genes)."))
- **c7** Limitation: the best case for feature attribution is when the perturbed features are independent, in which case observational and interventional attributions coincide.([Conclusion, p.6](https://arxiv.org/pdf/2006.16234v1#page=6 "Currently, the best case for feature attribution is when the features that being perturbed are independent to start with."))
- **c8** Two value functions for Shapley-based local attribution: the observational conditional expectation v(S) = E[f(X) | X_S = x_S] (Eq. 2) and the interventional conditional expectation v(S) = E[f(x) | do(S)] (Eq. 3), which intervenes on the features by breaking the dependence between features in S and the remaining features.([Section 1.1 (Choice of value function), p.1](https://arxiv.org/pdf/2006.16234v1#page=1 "There are two ways the model’s output (f : x ∈R/N/×1 →R1) for a particular sample is used to deﬁne v(S):"))
- **c9** Shapley value as an average over orderings (Eq. 1): phi_i = (1/M!) sum over permutations R of [v(S_R union {i}) - v(S_R)], where S_R is the set of players joining before player i.([Section 1 (Shapley values), p.1](https://arxiv.org/pdf/2006.16234v1#page=1 "where R is one possible permutation of the order in which the players join the coalition, SR is the set of players joining the coalition before player i"))

