<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# A Unified Approach to Interpreting Model Predictions

- カード: [`arxiv-1705.07874`](../../papers/arxiv-1705.07874.yaml)
- 著者: Scott Lundberg, Su-In Lee
- 年・掲載: 2017
- 原論文: [PDF](https://arxiv.org/pdf/1705.07874v2)(arXiv v2、カード作成時に読んだ版)
- タグ: deep-learning, feature-attribution, model-explanation, post-hoc
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** SHAP is presented as a unified framework for interpreting predictions that assigns each feature an importance value for a particular prediction.([Abstract, p.1](https://arxiv.org/pdf/1705.07874v2#page=1 "To address this problem, we present a unified framework for interpreting predictions, SHAP (SHapley Additive exPlanations)."))
- **c2** Within the class of additive feature attribution methods, the uniqueness result implies that methods not based on Shapley values violate local accuracy and/or consistency.([Simple Properties Uniquely Determine Additive Feature Attributions, p.4](https://arxiv.org/pdf/1705.07874v2#page=4 "This result implies that methods not based on Shapley values violate local accuracy and/or consistency (methods in Section 2 already respect missingness)."))
- **c3** Assumptions: the practical estimators may assume feature independence and model linearity to simplify computing the conditional expectations.([SHAP (SHapley Additive exPlanation) Values, p.5](https://arxiv.org/pdf/1705.07874v2#page=5 "When using these methods, feature independence and model linearity are two optional assumptions simplifying the computation of the expected values"))
- **c4** If DeepLIFT's reference value is interpreted as E[x], DeepLIFT approximates SHAP values assuming independent input features and a linear deep model; Deep SHAP adapts DeepLIFT on this basis.([Model-Specific Approximations (Deep SHAP), p.7](https://arxiv.org/pdf/1705.07874v2#page=7 "If we interpret the reference value in Equation 3 as representing E[x] in Equation 12, then DeepLIFT approximates SHAP values assuming that the input features are independent of one another and the deep model is linear."))
- **c5** Evaluation (computational): Kernel SHAP, Shapley sampling and LIME are compared on dense and sparse decision tree models, showing Kernel SHAP's sample efficiency and that LIME values can differ significantly from SHAP values.([Computational Efficiency, p.8](https://arxiv.org/pdf/1705.07874v2#page=8 "Comparing Shapley sampling, SHAP, and LIME on both dense and sparse decision tree models illustrates both the improved sample efficiency of Kernel SHAP and that values from LIME can differ significantly from SHAP values that satisfy local accuracy and consistency."))
- **c6** Evaluation (human): explanation quality is judged by agreement with explanations from Mechanical Turk users on simple models, assuming good explanations should match humans who understand the model.([Consistency with Human Intuition, p.8](https://arxiv.org/pdf/1705.07874v2#page=8 "Our testing assumes that good model explanations should be consistent with explanations from humans who understand that model."))
- **c7** Evaluation (MNIST): following DeepLIFT's example, 20% of pixels chosen by each method's attribution are masked to switch the predicted class from 8 to 3.([Explaining Class Differences, p.9](https://arxiv.org/pdf/1705.07874v2#page=9 "To match [7], we masked 20% of the pixels chosen to switch the predicted class from 8 to 3 according to the feature attribution given by each method."))

