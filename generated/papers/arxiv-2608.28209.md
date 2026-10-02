<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Generalized Context in Cross Attention for Transfer Learning of Disjoint Tabular Data

- カード: [`arxiv-2608.28209`](../../papers/arxiv-2608.28209.yaml)
- 著者: Kazi F. Akhter, Ibna Kowsar, Manar D. Samad
- 年・掲載: 2026
- 原論文: [PDF](https://arxiv.org/pdf/2608.28209v1)(arXiv v1、カード作成時に読んだ版)
- タグ: deep-learning, self-supervised, supervised, tabular-attention, tabular-classification
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** The paper introduces generalized context learning to remove the requirement of shared features across source and target domains.([Abstract, p.1](https://arxiv.org/pdf/2608.28209v1#page=1 "This paper introduces generalized context learning to remove the requirement of shared features across domains."))
- **c2** On ten disjoint source-target pairs, CATTLE learns generalized context from a single source dataset and is rank-wise and statistically superior to nine baselines.([Abstract, p.1](https://arxiv.org/pdf/2608.28209v1#page=1 "show that CATTLE can learn generalized context from a single source data set and is rank-wise and statistically superior to nine state-of-the-art baselines"))
- **c3** The study uses 14 OpenML datasets (nine source, five target) with 540 to 70000 samples and 8 to 76 features.([Experiments, p.6](https://arxiv.org/pdf/2608.28209v1#page=6 "The data sets have varying mixes of numerical and categorical features, sample sizes ranging from 540 to 70000, and feature dimensions ranging from 8 to 76."))
- **c4** Data are split 70:10:20 and resampled with ten random seeds.([Model implementation and evaluation, p.7](https://arxiv.org/pdf/2608.28209v1#page=7 "Data with 70:10:20 splits are randomly sampled ten times using ten random seeds to facilitate statistical comparison of model performance."))
- **c5** Models are tuned with 100 Optuna trials of random sampling evaluated on the validation set; the best validated model is reported on the test fold.([Model implementation and evaluation, p.8](https://arxiv.org/pdf/2608.28209v1#page=8 "In each of the 100 Optuna trials, a set of hyperparameter values is randomly sampled and evaluated on the validation set."))
- **c6** Traditional ML (XGBoost, logistic regression) performs strongly across most datasets, ranking better than the deep learning baselines without transfer.([Results, p.10](https://arxiv.org/pdf/2608.28209v1#page=10 "Traditional machine learning methods, particularly XGBoost and logistic regression, consistently achieve strong performance across most data sets."))

