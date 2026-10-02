<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Modeling nonlinear and interaction effects of spatiotemporal and nongenetic factors improves prediction for complex traits

- カード: [`doi-10.1038_s41467-026-76154-7`](../../papers/doi-10.1038_s41467-026-76154-7.yaml)
- 著者: Ross DeVito, Melissa Gymrek
- 年・掲載: 2026 Nature Communications
- 原論文: [PDF](https://www.nature.com/articles/s41467-026-76154-7_reference.pdf)(Publisher PDF via OpenAlex (publishedVersion)、カード作成時に読んだ版)
- タグ: gradient-boosted-trees, linear-models, supervised, tabular-mlp, tabular-regression
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** An auxiliary nonlinear 'null' model predicts the phenotype from covariates alone, and its prediction is added as a covariate in downstream analysis.([Abstract, p.1](https://www.nature.com/articles/s41467-026-76154-7_reference.pdf#page=1 "We adopt a null model approach where an auxiliary nonlinear model predicts phenotypes from covariates alone."))
- **c2** On 16 UK Biobank phenotypes, gradient-boosted tree null models with spatiotemporal features improve covariate modeling.([Abstract, p.1](https://www.nature.com/articles/s41467-026-76154-7_reference.pdf#page=1 "Using 16 phenotypes in the UK Biobank, we show gradient boosted decision tree nulls including spatiotemporal features improve covariate modeling."))
- **c3** Participants are randomly split 8:1:1 into train, validation and test sets; null models are trained and evaluated with five-fold cross-validation on the training set only, keeping validation and test sets for the downstream polygenic-score task.([Results, p.3](https://www.nature.com/articles/s41467-026-76154-7_reference.pdf#page=3 "just the training set was used to train and evaluate the null models on their own using ﬁve-fold cross-validation."))
- **c4** XGBoost variants were the default parameters plus two larger configurations (up to 1000 or 2500 estimators, lower learning rate, max depth 4), all with early stopping.([Results, p.2](https://www.nature.com/articles/s41467-026-76154-7_reference.pdf#page=2 "The three variations consisted of the default XGBoost parameters (a maximum of 100 estimators and a learning rate of 0.3), as well as two larger versions with up to 1000 or 2500 estimators, both using a learning rate reduced to 0.25 and a maximum depth of 4 to mitigate overﬁtting."))
- **c5** Under a Friedman test with Nemenyi post-hoc comparisons, the original DeepNull neural network ranked second-worst, ahead only of LASSO.([Results, p.4](https://www.nature.com/articles/s41467-026-76154-7_reference.pdf#page=4 "By average rank, the original DeepNull neural network was the second-worst performer, only outperforming the LASSO regression and signiﬁcantly worse than all other model variations."))
- **c6** Training and polygenic-score evaluation used only individuals of White British ancestry in the UK Biobank.([Discussion (limitations), p.9](https://www.nature.com/articles/s41467-026-76154-7_reference.pdf#page=9 "First, the training and PGS evaluation were conducted exclusively on individuals of White British ancestry in the UK Biobank."))

