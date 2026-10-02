<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Evaluating Machine Learning Models for Post-Wildfire Debris-Flow Prediction

- カード: [`arxiv-2608.05265`](../../papers/arxiv-2608.05265.yaml)
- 著者: Quinn Ledingham, Zhengsen Xu, Yimin Zhu, Zack Dewis, Mabel Heffring, Saeid Taleghanidoozdoozan, Motasem Alkayid, Megan Greenwood, Lincoln Linlin Xu
- 年・掲載: 2026
- 原論文: [PDF](https://arxiv.org/pdf/2608.05265v1)(arXiv v1、カード作成時に読んだ版)
- タグ: deep-learning, feature-attribution, gradient-boosted-trees, kernel-methods, linear-models, model-explanation, random-forests, supervised, tabular-classification, tabular-foundation-model
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** The paper compares 15 models, including TabPFN, on basin-scale post-wildfire debris-flow observations across the western United States.([Abstract, p.1](https://arxiv.org/pdf/2608.05265v1#page=1 "Using basin-scale observations of post-wildfire debris-flow events across the western United States, we compare 15 models, including a new foundation model, the Tabular Prior-Data Fitted Network (TabPFN)."))
- **c2** Evaluation uses stratified 5-fold cross-validation repeated 10 times, with splits precomputed once and shared by all models.([Cross-Validation, p.7](https://arxiv.org/pdf/2608.05265v1#page=7 "In particular, we used stratified 5-fold cross-validation repeated 10 times, producing 50 outer evaluation splits with an equal percentage of no-debris-flow and debris-flow observations in each split."))
- **c3** Tuned models used Bayesian optimization with 100 trials and Hyperband pruning on an inner validation split, tuned separately for unaugmented and augmented training; some models used native tuning or none.([Hyperparameter Tuning, p.7](https://arxiv.org/pdf/2608.05265v1#page=7 "For each model and training condition, we used Bayesian optimization with 100 trials and Hyperband pruning to maximize validation threat score under fold-aware training (Akiba et al.; Li et al.)."))
- **c4** Decision thresholds were not optimized, and class-weight rebalancing was fixed rather than tuned.([Hyperparameter Tuning, p.7](https://arxiv.org/pdf/2608.05265v1#page=7 "Decision-threshold optimization was likewise not performed to avoid conflating hyperparameter selection with the metric used for model comparison."))
- **c5** TabPFN and the leading tree ensembles form a top tier whose within-tier order is not stable; TabPFN was run with static settings while tree models needed Bayesian search.([Discussion, p.18](https://arxiv.org/pdf/2608.05265v1#page=18 "Tree-based models such as ExtraTrees, CatBoost, and XGBoost required Bayesian hyperparameter search, whereas TabPFN was run with static settings with no dataset-specific tuning and still matched or exceeded them."))
- **c6** Limitation: the dataset is geographically concentrated in southern California fires, which may favor features and models that generalize within that region.([Discussion, p.19](https://arxiv.org/pdf/2608.05265v1#page=19 "The dataset is geographically concentrated, with 61% of records from southern California fires, which may favor features and model structures that generalize well within that region but perform differently in the drier, more continental environments represented by the remaining fires."))

