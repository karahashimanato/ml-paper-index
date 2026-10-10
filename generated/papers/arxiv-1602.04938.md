<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# "Why Should I Trust You?": Explaining the Predictions of Any Classifier

- カード: [`arxiv-1602.04938`](../../papers/arxiv-1602.04938.yaml)
- 著者: Marco Tulio Ribeiro, Sameer Singh, Carlos Guestrin
- 年・掲載: 2016
- 原論文: [PDF](https://arxiv.org/pdf/1602.04938v3)(arXiv v3、カード作成時に読んだ版)
- タグ: feature-attribution, linear-models, model-explanation, post-hoc
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** LIME explains predictions of any classifier by learning an interpretable model locally around the prediction.([Abstract, p.1](https://arxiv.org/pdf/1602.04938v3#page=1 "In this work, we propose LIME, a novel explanation technique that explains the predictions of any classifier in an interpretable and faithful manner, by learning an interpretable model locally around the prediction."))
- **c2** Assumption and stated drawback: with sparse linear explanations, a model that is highly non-linear even locally may have no faithful explanation.([Sparse Linear Explanations, p.4](https://arxiv.org/pdf/1602.04938v3#page=4 "Second, our choice of G (sparse linear models) means that if the underlying model is highly non-linear even in the locality of the prediction, there may not be a faithful explanation."))
- **c3** Faithfulness evaluation uses classifiers that are interpretable by construction (sparse logistic regression, decision trees) limited to 10 features per instance, so a gold set of important features is known and its recall is measured.([Are explanations faithful to the model?, p.6](https://arxiv.org/pdf/1602.04938v3#page=6 "In particular, we train both classifiers such that the maximum number of features they use for any instance is 10, and thus we know the gold set of features that the are considered important by these models."))
- **c4** In the simulated-user experiments, hyperparameters of LIME and the parzen baseline are set by cross validation.([Simulated user experiments: Experiment Setup, p.6](https://arxiv.org/pdf/1602.04938v3#page=6 "We set the hyper-parameters for parzen and LIME using cross validation"))
- **c5** The trust-in-prediction experiment relies on artificially designated untrustworthy features; the authors acknowledge this while concluding LIME helps assess trust.([Should I trust this prediction?, p.7](https://arxiv.org/pdf/1602.04938v3#page=7 "Even though we artificially select which features are untrustworthy, these results indicate that LIME is helpful in assessing trust in individual predictions."))
- **c6** In the human-subject experiment on choosing between two classifiers, subjects are recruited on Mechanical Turk and are not machine learning experts (people with basic knowledge about religion).([Can users select the best classifier?, p.7](https://arxiv.org/pdf/1602.04938v3#page=7 "We recruit human subjects on Amazon Mechanical Turk – by no means machine learning experts, but instead people with basic knowledge about religion."))
- **c7** Stated limitation: how to perform the pick step for images is left open.([Conclusion and future work, p.10](https://arxiv.org/pdf/1602.04938v3#page=10 "One issue that we do not mention in this work was how to perform the pick step for images, and we would like to address this limitation in the future."))
- **c8** LIME objective (Eq. 1): xi(x) = argmin over g in G of L(f, g, pi_x) + Omega(g), where pi_x(z) is a proximity measure defining locality around x, L measures how unfaithful g is in approximating f in that locality, and Omega(g) is the complexity of the explanation (e.g. number of non-zero weights for linear models).([Fidelity-Interpretability Trade-off, p.3](https://arxiv.org/pdf/1602.04938v3#page=3 "The explanation produced by LIME is obtained by the following:"))
- **c9** LIME approximates the locality-aware loss by sampling perturbed instances around x' (drawing nonzero elements of x' uniformly at random), weighting them by pi_x, and using the model output f(z) as labels for fitting the explanation model.([Sampling for Local Exploration, p.3](https://arxiv.org/pdf/1602.04938v3#page=3 "Thus, in order to learn the local behavior of f as the interpretable inputs vary, we approximate L(f, g, πx) by drawing samples, weighted by πx."))

