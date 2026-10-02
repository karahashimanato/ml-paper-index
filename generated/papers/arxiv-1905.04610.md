<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Explainable AI for Trees: From Local Explanations to Global Understanding

- カード: [`arxiv-1905.04610`](../../papers/arxiv-1905.04610.yaml)
- 著者: Scott M. Lundberg, Gabriel Erion, Hugh Chen, Alex DeGrave, Jordan M. Prutkin, Bala Nair, Ronit Katz, Jonathan Himmelfarb, Nisha Bansal, Su-In Lee
- 年・掲載: 2019
- 原論文: [PDF](https://arxiv.org/pdf/1905.04610v1)(arXiv v1、カード作成時に読んだ版)
- タグ: feature-attribution, gradient-boosted-trees, model-explanation, post-hoc, tabular-classification, tabular-regression, tree-ensembles
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** TreeExplainer is a local explanation method for trees that computes optimal local explanations, defined by game-theoretic properties, in tractable (polynomial) time.([Introduction, p.3](https://arxiv.org/pdf/1905.04610v1#page=3 "Here we propose TreeExplainer, a new local explanation method for trees that enables the tractable computation of optimal local explanations, as defined by desirable properties from game theory (Section 2.5)."))
- **c2** Axiomatic justification: within additive feature attribution methods, Shapley values are the only way to satisfy local accuracy, consistency and missingness.([Results (TreeExplainer), p.5](https://arxiv.org/pdf/1905.04610v1#page=5 "results from game theory imply the Shapley values are the only way to satisfy three important properties: local accuracy, consistency, and missingness (Methods 9)"))
- **c3** By default TreeExplainer computes conditional expectations by tree traversal; an option enforces feature independence and supports explaining the model's loss.([Results (TreeExplainer), p.6](https://arxiv.org/pdf/1905.04610v1#page=6 "By default, TreeExplainer computes conditional expectations using tree traversal, but it also provides an option that enforces feature independence and supports explaining a model’s loss function (Methods 10)."))
- **c4** Explanation quality was evaluated with 21 metrics designed by the authors, applied to eight explanation methods across three model types and three datasets.([Results (TreeExplainer), p.6](https://arxiv.org/pdf/1905.04610v1#page=6 "We designed 21 metrics to comprehensively evaluate the performance of local explanation methods, and applied these metrics to eight different explanation methods across three different model types and three datasets (Methods 11)."))
- **c5** The benchmark hides features by mean masking, by resampling under feature independence, or by imputation; metrics based on retraining the model were deliberately excluded because they can be misleading in certain situations.([Methods (Benchmark evaluation metrics), p.24](https://arxiv.org/pdf/1905.04610v1#page=24 "After extensive consideration, we did not include metrics based on retraining the original model since, while informative, these can produce misleading results in certain situations."))
- **c6** A user-study benchmark of 12 scenarios compared methods with human consensus explanations of simple models; Shapley-value-based methods agreed with human intuition in all tested scenarios, unlike the Saabas heuristic.([Results (TreeExplainer), p.6](https://arxiv.org/pdf/1905.04610v1#page=6 "In contrast to the heuristic Saabas values, Shapley value based explanation methods agree with human intuition in all the scenarios we tested (Methods 12)."))
- **c7** Failure mode of the prior Saabas heuristic: it is inconsistent, i.e. a model can be changed to make a feature clearly more important while the Saabas attribution of that feature decreases.([Results, p.5](https://arxiv.org/pdf/1905.04610v1#page=5 "This causes Saabas values to be inconsistent, which means we can modify a model to make a feature clearly more important, and yet the Saabas value attributed to that feature will decrease (Supplementary Figure 2)."))

