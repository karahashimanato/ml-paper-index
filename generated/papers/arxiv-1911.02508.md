<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Fooling LIME and SHAP: Adversarial Attacks on Post hoc Explanation Methods

- カード: [`arxiv-1911.02508`](../../papers/arxiv-1911.02508.yaml)
- 著者: Dylan Slack, Sophie Hilgard, Emily Jia, Sameer Singh, Himabindu Lakkaraju
- 年・掲載: 2019
- 原論文: [PDF](https://arxiv.org/pdf/1911.02508v2)(arXiv v2、カード作成時に読んだ版)
- タグ: feature-attribution, model-explanation, post-hoc, tabular-classification
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** A scaffolding technique hides the biases of any classifier by letting an adversary craft an arbitrary desired explanation.([Abstract, p.1](https://arxiv.org/pdf/1911.02508v2#page=1 "Specifically, we propose a novel scaffolding technique that effectively hides the biases of any given classifier by allowing an adversarial entity to craft an arbitrary desired explanation."))
- **c2** Failure mode exploited: a PCA view shows LIME-style perturbed samples distributed differently from the input data; the authors conclude detecting perturbations is not challenging, so approaches relying heavily on perturbations, such as LIME, can be gamed.([Proposed Framework (intuition), p.3](https://arxiv.org/pdf/1911.02508v2#page=3 "This result indicates that detecting whether a data point is a result of a perturbation or not is not a challenging task, and thus approaches that rely heavily on these perturbations, such as LIME, can be gamed."))
- **c3** Setup: default LIME tabular (no discretization) and default Kernel SHAP with a 10-cluster k-means background are attacked; the biased model uses only the sensitive feature.([Experimental Setup, p.4](https://arxiv.org/pdf/1911.02508v2#page=4 "We use default LIME tabular implementation without discretization, and the default Kernel SHAP implementation with kmeans with 10 clusters as the background distribution."))
- **c4** Evaluation metric: the share of test points where the sensitive feature or the decoy features appear in the top 3 of the explanation's ranking.([Effectiveness of Adversarial Classifiers, p.5](https://arxiv.org/pdf/1911.02508v2#page=5 "we compute the percentage of data points for which race, uncorrelated features (in case of COMPAS and CC) or Loan Rate % Income (in case of German credit data) show up in top 3 when features are ranked based on feature attributions output by LIME and SHAP"))
- **c5** Against SHAP, the attack using two uncorrelated features is less successful at removing the sensitive feature from first place in the ranking; the authors attribute this to SHAP's local accuracy property.([Effectiveness of Adversarial Classifiers, p.5](https://arxiv.org/pdf/1911.02508v2#page=5 "This is due to SHAP’s local accuracy property that ensures that feature attributions must add up to the difference between a given prediction and the average prediction for the background distribution."))
- **c6** The attack works as long as perturbed points can be distinguished from input data with reasonable accuracy.([Effect of Perturbation Detection Accuracy, p.6](https://arxiv.org/pdf/1911.02508v2#page=6 "These results indicate that our attacks are effective as long as it is possible to differentiate between perturbed instances and input data points with a reasonable accuracy."))
- **c7** Main conclusion: on criminal justice and credit data the attack fools post hoc explainers, with LIME more vulnerable than SHAP.([Conclusions and Future Work, p.7](https://arxiv.org/pdf/1911.02508v2#page=7 "Extensive experimentation with real world data from criminal justice and credit scoring domains demonstrates that our approach is effective at generating adversarial classifiers that can fool post hoc explanation techniques, finding that LIME is more vulnerable than SHAP."))

