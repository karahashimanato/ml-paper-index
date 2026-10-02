<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Stop Explaining Black Box Machine Learning Models for High Stakes Decisions and Use Interpretable Models Instead

- カード: [`arxiv-1811.10154`](../../papers/arxiv-1811.10154.yaml)
- 著者: Cynthia Rudin
- 年・掲載: 2018
- 原論文: [PDF](https://arxiv.org/pdf/1811.10154v3)(arXiv v3、カード作成時に読んだ版)
- タグ: interpretable-models, model-explanation, supervised
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Rudin argues that trying to explain black box models, instead of building models that are interpretable in the first place, is likely to perpetuate bad practices and can potentially cause catastrophic harm to society.([Abstract, p.1](https://arxiv.org/pdf/1811.10154v3#page=1 "trying to explain black box models, rather than creating models that are interpretable in the first place, is likely to perpetuate bad practices and can potentially cause catastrophic harm to society"))
- **c2** The paper argues it is a myth that there is necessarily an accuracy-interpretability trade-off: for problems with structured data and meaningful features, there is often no significant performance difference between complex classifiers (deep nets, boosted trees, random forests) and much simpler ones (logistic regression, decision lists) after preprocessing.([Key Issues with Explainable ML, p.2](https://arxiv.org/pdf/1811.10154v3#page=2 "there is often no significant difference in performance between more complex classifiers (deep neural networks, boosted decision trees, random forests) and much simpler classifiers (logistic regression, decision lists) after preprocessing"))
- **c3** Post-hoc explanations cannot have perfect fidelity to the original model: a fully faithful explanation would equal the model itself, so an explanation may misrepresent the black box in parts of the feature space.([Key Issues with Explainable ML, p.3](https://arxiv.org/pdf/1811.10154v3#page=3 "If the explanation was completely faithful to what the original model computes, the explanation would equal the original model, and one would not need the original model in the first place, only the explanation."))
- **c4** The paper criticises saliency maps, which can look essentially the same for different classes, and the practice of showing explanations only for the correct label, which it calls misleading.([Key Issues with Explainable ML, p.4](https://arxiv.org/pdf/1811.10154v3#page=4 "Demonstrating a method using explanations only for the correct class is misleading."))
- **c5** As evidence, the paper compares the proprietary COMPAS model with a three-rule CORELS rule list using only age, priors and (optionally) gender, stating that both have similar true/false positive and negative rates on Broward County, Florida data.([Key Issues with Interpretable ML, p.6](https://arxiv.org/pdf/1811.10154v3#page=6 "Both models have similar true and false positive rates and true and false negative rates on data from Broward County, Florida."))
- **c6** The paper's 'Rashomon set' argument: when the data admit a large set of nearly equally accurate models, that set often contains at least one interpretable model.([A Technical Reason Why Accurate Interpretable Models Might Exist in Many Domains, p.14](https://arxiv.org/pdf/1811.10154v3#page=14 "Because this set of accurate models is large, it often contains at least one model that is interpretable."))
- **c7** Scope/limitation: Rudin concedes there could be application domains where a complete black box is required for a high-stakes decision, while stating she has not yet encountered one.([Key Issues with Explainable ML, p.3](https://arxiv.org/pdf/1811.10154v3#page=3 "It could be possible that there are application domains where a complete black box is required for a high stakes decision."))

