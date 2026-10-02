<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Cross-economy stability of predictor rankings for adolescent school belonging and mathematics anxiety: an explainable machine-learning analysis of PISA 2022

- カード: [`doi-10.3389_fpsyg.2026.1875261`](../../papers/doi-10.3389_fpsyg.2026.1875261.yaml)
- 著者: Yuan Liao, Peng Qin, Runlin Li
- 年・掲載: 2026 Frontiers in Psychology
- 原論文: [PDF](https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2026.1875261/pdf)(Publisher PDF via OpenAlex (publishedVersion)、カード作成時に読んだ版)
- タグ: feature-attribution, gradient-boosted-trees, linear-models, supervised, tabular-regression
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Data and models: PISA 2022 student data were analysed with one LightGBM model per economy, and TreeSHAP rankings were used to estimate the relative predictive salience of predictors for school belonging and mathematics anxiety.([Abstract, p.1](https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2026.1875261/pdf#page=1 "Per-economy LightGBM models and TreeSHAP rankings estimated relative predictive salience."))
- **c2** Pooled model comparison protocol: LightGBM (fixed hyperparameters, economy code as a categorical feature) was compared with ridge regression using ten student-level folds stratified by economy; the paper notes this design does not evaluate transfer to unseen economies.([Methods (pooled comparators), p.8](https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2026.1875261/pdf#page=8 "Performance was estimated with ten student-level folds stratified by economy; this design preserves each economy's proportion in every fold and does not evaluate transfer to unseen economies."))
- **c3** Per-economy models used a fixed LightGBM configuration on a 64%/16%/20% train/validation/test split with early stopping on validation loss; no hyperparameter search is described.([Methods (per-economy LightGBM with TreeSHAP), p.8](https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2026.1875261/pdf#page=8 "fit an independent LightGBM regressor on a 64%/16%/20% train/validation/test split with early stopping on validation loss."))
- **c4** Deep tabular networks (e.g. FT-Transformer, TabPFN) were not evaluated; the authors chose LightGBM citing prior findings that GBDTs match or exceed deep tabular networks on data like PISA.([Methods (pooled comparators), p.8](https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2026.1875261/pdf#page=8 "The choice of LightGBM over deep tabular networks (e.g., FT-Transformer, TabPFN Hollmann et al., 2025) was motivated by the empirical finding that gradient-boosted decision trees match or exceed deep tabular networks on heterogeneous tabular data of the size and structure of PISA"))
- **c5** In the pooled comparison on untouched outer test folds, LightGBM had higher R2 than ridge regression with penalized economy indicators for both outcomes.([Results, p.9](https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2026.1875261/pdf#page=9 "In the pooled comparison evaluated on untouched outer test folds, LightGBM produced higher R2 than ridge regression with penalized economy indicators"))
- **c6** Limitation: SHAP values were summarized over the entire per-economy sample rather than only the test split, so the rankings may partly reflect sample-internal fitted structure.([Limitations, p.17](https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2026.1875261/pdf#page=17 "SHAP values were summarized across the entire per-economy sample rather than the test split alone, so the rankings may partly reflect sample-internal fitted structure"))

