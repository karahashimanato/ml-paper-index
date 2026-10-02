<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# TabBench-Bio: A Living Benchmark for Machine Learning on High-Dimensional Biomedical Tables

- カード: [`arxiv-2609.07441`](../../papers/arxiv-2609.07441.yaml)
- 著者: Jules Kreuer, Sofiane Ouaari, Julia Hellmig, Julius Braitinger, Nico Pfeifer
- 年・掲載: 2026
- 原論文: [PDF](https://arxiv.org/pdf/2609.07441v2)(arXiv v2、カード作成時に読んだ版)
- タグ: automl-systems, gradient-boosted-trees, in-context-learning, linear-models, random-forests, supervised, tabular-classification, tabular-foundation-model, tabular-mlp, tabular-regression
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** TabBench-Bio is a living, interactive benchmark of 43 biomedical datasets.([Abstract, p.1](https://arxiv.org/pdf/2609.07441v2#page=1 "We introduce TabBench-Bio, a living and interactive benchmark of 43 biomedical datasets spanning multiple domains."))
- **c2** At the reference cell (10,000 features, 100 training samples), RealTabPFN 2.5 has the highest point estimate, closely followed by TabPFN 3 and Logistic Regression.([Abstract, p.1](https://arxiv.org/pdf/2609.07441v2#page=1 "At the reference cell of 10,000 features and 100 training samples, RealTabPFN 2.5 has the highest point estimate, closely followed by TabPFN 3 and Logistic Regression."))
- **c3** All peer models use the default configuration of their AutoGluon adapter without per-dataset hyperparameter search, with bagging/stacking/ensembling disabled; tuning effects are not evaluated.([Models and fitting regime, p.4](https://arxiv.org/pdf/2609.07441v2#page=4 "Results concern these fixed configurations; the effects of bagging and hyperparameter tuning are not evaluated."))
- **c4** Evaluation uses 5-fold cross-validation with folds shared across all grid cells and models (group folds when biological group identifiers are available).([Cross-validation and leakage control, p.4](https://arxiv.org/pdf/2609.07441v2#page=4 "We use 5-fold cross-validation, with complementary folds shared across all cells and models."))
- **c5** Under AUROC (TabArena's binary metric) instead of macro-F1, Logistic Regression drops out of the leading group, so part of the contrast with TabArena reflects threshold placement rather than the domain alone.([Discussion, p.8](https://arxiv.org/pdf/2609.07441v2#page=8 "under AUROC, the metric TabArena uses for binary classification, Logistic Regression drops out of the leading group and the top 6 places are held by tabular foundation models (Appendix E), so part of the contrast reflects threshold placement rather than the domain alone."))
- **c6** Three benchmark datasets come from the same collection that supplied datasets used in TabDPT pretraining, so TabDPT results on them should be interpreted with this overlap in mind.([Limitations, p.8](https://arxiv.org/pdf/2609.07441v2#page=8 "TabDPT performance on these related datasets should therefore be interpreted with this overlap in mind."))

