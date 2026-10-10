<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# DoWhy: An End-to-End Library for Causal Inference

- カード: [`arxiv-2011.04216`](../../papers/arxiv-2011.04216.yaml)
- 著者: Amit Sharma, Emre Kiciman
- 年・掲載: 2020
- 原論文: [PDF](https://arxiv.org/pdf/2011.04216v1)(arXiv v1、カード作成時に読んだ版)
- タグ: causal-effect-estimation, causal-meta-learners, linear-models
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** API organization: four steps required for any causal analysis, Model (prior knowledge as a causal graph), Identify (graph-based identification), Estimate (statistical estimation of the identified estimand) and Refute (testing robustness to the model's assumptions).([Introduction, p.1](https://arxiv.org/pdf/2011.04216v1#page=1 "Speciﬁcally, DoWhy’s API is organized around the four key steps that are required for any causal analysis: Model, Identify, Estimate, and Refute."))
- **c2** Motivation: unlike supervised models validated on held-out test data, causal tasks often have no ground-truth answer, so checking core assumptions and applying sensitivity tests is described as critical to gaining confidence in results.([Introduction, p.1](https://arxiv.org/pdf/2011.04216v1#page=1 "Unlike supervised machine learning models that can be validated using held-out test data, causal tasks often have no ground truth answer available."))
- **c3** Positioning: the authors state that covering all four steps is DoWhy's key differentiator compared with many Python and R libraries that focus only on estimation and leave modeling, identification and robustness checks to the analyst.([Introduction, p.2](https://arxiv.org/pdf/2011.04216v1#page=2 "The focus on all the four steps, going from data to the ﬁnal causal estimate (along with a measure of its robustness) is the key differentiator for DoWhy, compared to many existing libraries for causal inference in Python and R that only focus on estimation (the third step)."))
- **c4** Model and identification: the causal graph need not be complete; an analyst may give a partial graph and DoWhy treats the remaining variables as potential confounders. Supported identification criteria are back-door, front-door, instrumental variables and mediation.([DoWhy and the Four Steps of Causal Inference, p.2](https://arxiv.org/pdf/2011.04216v1#page=2 "DoWhy automatically considers the rest of the variables as potential confounders."))
- **c5** Estimation: back-door and IV methods (propensity stratification, matching and IPW; linear regression and GLMs; Wald estimator, two-stage least squares, regression discontinuity; two-stage linear regression for front-door/mediation), with non-parametric confidence intervals and a permutation test; CATE estimators from EconML and CausalML can be called directly (the example uses EconML's double machine learning estimator for high-dimensional confounders).([DoWhy and the Four Steps of Causal Inference, p.3](https://arxiv.org/pdf/2011.04216v1#page=3 "All estimators from these libraries can be directly called from DoWhy."))
- **c6** Refutation tests and their expected outcomes: add a random common cause (estimate should not change), placebo treatment and dummy outcome (effect should go to zero), simulated outcome from a known DGP closest to the data (should match the DGP's effect), add an unobserved common cause correlated with treatment and outcome (should not be too sensitive), and data-subset and bootstrap validation (should not change significantly).([DoWhy and the Four Steps of Causal Inference, p.3](https://arxiv.org/pdf/2011.04216v1#page=3 "Having access to multiple refutation methods to validate an effect estimate from a causal estimator is a key beneﬁt of using DoWhy."))
- **c7** Scope of the refuters: some (e.g. placebo treatment, dummy outcome) aim to refute the full analysis including modeling, identification and estimation, whereas data-subset and bootstrap validation test only the estimation step.([DoWhy and the Four Steps of Causal Inference, p.4](https://arxiv.org/pdf/2011.04216v1#page=4 "Many of the above methods aim to refute the full causal analysis, including modeling, identiﬁcation and estimation (as in Placebo Treatment or Dummy Outcome) whereas others refute a speciﬁc step (e.g., Data Subsets and Bootstrap Validation that test only the estimation step)."))
- **c8** Separation of identification and estimation: the authors state that, given the model, identification is a causal problem and estimation a statistical one, and DoWhy treats them separately so that multiple estimation methods can be used for a single identified estimand and vice versa.([An Example Causal Analysis, p.4](https://arxiv.org/pdf/2011.04216v1#page=4 "Given the model, identiﬁcation is a causal problem."))

