<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Problems with Shapley-value-based explanations as feature importance measures

- カード: [`arxiv-2002.11097`](../../papers/arxiv-2002.11097.yaml)
- 著者: I. Elizabeth Kumar, Suresh Venkatasubramanian, Carlos Scheidegger, Sorelle Friedler
- 年・掲載: 2020
- 原論文: [PDF](https://arxiv.org/pdf/2002.11097v2)(arXiv v2、カード作成時に読んだ版)
- タグ: feature-attribution, model-explanation, post-hoc
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Mathematical problems arise when Shapley values are used for feature importance, and mitigating them necessarily adds complexity such as the need for causal reasoning.([Abstract, p.1](https://arxiv.org/pdf/2002.11097v2#page=1 "We show that mathematical problems arise when Shapley values are used for feature importance, and that the solutions to mitigate these necessarily induce further complexity, such as the need for causal reasoning."))
- **c2** Choosing between conditional and interventional value functions is a catch-22: conditional methods require extra modelling of feature dependencies, interventional methods induce an out-of-distribution problem.([Conditional versus interventional distributions, p.3](https://arxiv.org/pdf/2002.11097v2#page=3 "Unfortunately, the decision between the two types of value functions is a catch-22."))
- **c3** With conditional value functions, adding a redundant copy of a feature changes the relative attributions of the other features, even though the model is effectively the same.([Issues with conditional distributions, p.4](https://arxiv.org/pdf/2002.11097v2#page=4 "The relative apparent importances of A and B thus depend on whether C is considered to be a third feature, even though the two functions are effectively the same."))
- **c4** Interventional value functions fundamentally rely on evaluating the model on out-of-distribution samples, which makes them highly sensitive to model properties not relevant to what it learned about the training data.([Issues with interventional distributions, p.5](https://arxiv.org/pdf/2002.11097v2#page=5 "Methods which use an interventional value function fundamentally rely on evaluating a model on out-of-distribution samples (Figure 1)."))
- **c5** Additivity issue: for multiplicative functions of independent, zero-centred features, every feature receives the same Shapley value regardless of its value.([Additivity constraints, p.6](https://arxiv.org/pdf/2002.11097v2#page=6 "This property will, in fact, hold for all multiplicative functions of independently distributed, zero-centered data."))
- **c6** A large Shapley influence of a feature does not necessarily imply that changing that feature will change the outcome favourably, and Shapley-value frameworks do not explicitly attempt to guide how a user might alter their situation (unlike actionable-recourse methods).([Using Shapley-valued based methods to enable action, p.8](https://arxiv.org/pdf/2002.11097v2#page=8 "Further, observing that a certain feature carries a large influence over the model does not necessarily imply that changing that feature (even significantly) will change the outcome favorably."))
- **c7** Evaluation evidence is drawn from the literature rather than new experiments; e.g. a cited human-grounded evaluation of SHAP found no evidence that it helped users assess prediction correctness.([Shapley-based explanations for normative evaluation, p.9](https://arxiv.org/pdf/2002.11097v2#page=9 "Weerts et al. (2019), for instance, conducted a human-grounded evaluation of SHAP and did not find evidence that it helped users assess the correctness of predictions."))

