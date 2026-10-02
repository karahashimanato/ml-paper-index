<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# The Disagreement Problem in Explainable Machine Learning: A Practitioner's Perspective

- カード: [`arxiv-2202.01602`](../../papers/arxiv-2202.01602.yaml)
- 著者: Satyapriya Krishna, Tessa Han, Alex Gu, Steven Wu, Shahin Jabbari, Himabindu Lakkaraju
- 年・掲載: 2022
- 原論文: [PDF](https://arxiv.org/pdf/2202.01602v6)(arXiv v6、カード作成時に読んだ版)
- タグ: deep-learning, feature-attribution, linear-models, model-explanation, post-hoc, saliency-maps, tabular-classification, tree-ensembles
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Six disagreement metrics are proposed, derived from practitioner interviews (top-k features, signs, ordering, and relative ordering of features of interest).([Formalizing the Notion of Explanation Disagreement, p.5](https://arxiv.org/pdf/2202.01602v6#page=5 "To capture these intuitions about explanation disagreement, we propose six different metrics: feature agreement, rank agreement, sign agreement, signed rank agreement, rank correlation, and pairwise rank agreement."))
- **c2** Tabular experiments explain logistic regression, a feed-forward neural network, random forest and gradient-boosted tree models (COMPAS and German Credit); text uses an LSTM and images a pre-trained ResNet-18.([Experimental Setup, p.6](https://arxiv.org/pdf/2202.01602v6#page=6 "For tabular data, we train four models: logistic regression, densely connected feed-forward neural network, random forest, and gradient-boosted tree."))
- **c3** Explainer sample sizes are set by running to convergence or using sizes above prior recommendations.([Experimental Setup, p.7](https://arxiv.org/pdf/2202.01602v6#page=7 "we either run the explanation method to convergence (i.e., select a sample size such that an increase in the number of samples does not significantly change the explanations)"))
- **c4** Main results: explanation methods often disagree, and practitioners often resolve disagreements with ad hoc heuristics.([Abstract, p.1](https://arxiv.org/pdf/2202.01602v6#page=1 "Our results indicate that (1) state-of-the-art explanation methods often disagree in terms of the explanations they output, and (2) machine learning practitioners often employ ad hoc heuristics when resolving such disagreements."))
- **c5** Disagreement may increase with model complexity (similar or stronger for the neural network than for logistic regression).([Tabular Data, p.8](https://arxiv.org/pdf/2202.01602v6#page=8 "These trends suggest that disagreement among explanation methods may increase with model complexity."))
- **c6** The measured extent of disagreement depends on the metric; variants of the metrics show slightly lower disagreement.([Discussion and Conclusion, p.15](https://arxiv.org/pdf/2202.01602v6#page=15 "Finally, the extent of explanation disagreement would also depend on the specific metric being used to measure the disagreement."))
- **c7** Scope: the paper prioritizes examining how prevalent disagreement is rather than its underlying causes, given the complexity of that analysis.([Discussion and Conclusion, p.14](https://arxiv.org/pdf/2202.01602v6#page=14 "In this work, we prioritized examining the prevalence of explanation disagreement rather than exploring its underlying causes, given the complexity of this analysis."))

