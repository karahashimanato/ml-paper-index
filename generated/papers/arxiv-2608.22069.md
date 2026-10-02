<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# AstroBind: Machine learning prediction of binding energy distributions on interstellar water ice from geometric surface descriptors

- カード: [`arxiv-2608.22069`](../../papers/arxiv-2608.22069.yaml)
- 著者: Aneesa Ahmad, Catherine Walsh
- 年・掲載: 2026
- 原論文: [PDF](https://arxiv.org/pdf/2608.22069v1)(arXiv v1、カード作成時に読んだ版)
- タグ: gaussian-processes, gradient-boosted-trees, kernel-methods, linear-models, random-forests, supervised, tabular-regression
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** An ML model is trained on 27 geometric descriptors of the local ice-adsorbate environment to predict binding energies.([Abstract, p.1](https://arxiv.org/pdf/2608.22069v1#page=1 "We trained a machine-learning model using 27 geometric descriptors of the local ice–adsorbate environment."))
- **c2** The model is trained on binding energies of 13 adsorbates and evaluated with pooled leave-one-cluster-out validation across 15 ice surfaces.([Abstract, p.1](https://arxiv.org/pdf/2608.22069v1#page=1 "The model was trained on binding energies for 13 adsorbates on amorphous solid water clusters and evaluated through pooled leave-one-cluster-out validation across 15 ice surfaces."))
- **c3** Linear regression, ridge regression, random forest and XGBoost were compared, and XGBoost had the highest test-set accuracy.([Methods (model training), p.3](https://arxiv.org/pdf/2608.22069v1#page=3 "XGBoost achieved the highest test-set accuracy"))
- **c4** XGBoost uses fixed hyperparameters. A randomized-search cross-validation over hyperparameter combinations improved results only marginally.([Methods (model training), p.3](https://arxiv.org/pdf/2608.22069v1#page=3 "Hyperparameter tuning via randomised-search cross-validation, in which 80 randomly sampled hyperparameter combinations are each scored by 5-fold cross-validation"))
- **c5** Gradient-boosted trees were chosen over deep learning because, at this data size, boosted trees are competitive on tabular data and their feature attributions give mechanistic insight.([Discussion, p.10](https://arxiv.org/pdf/2608.22069v1#page=10 "boosted trees are competitive on tabular data of this scale"))
- **c6** Limitation: performance collapses for dispersion-dominated adsorbates, which the authors describe as consistent with the absence of electronic information in the descriptors.([Discussion, p.10](https://arxiv.org/pdf/2608.22069v1#page=10 "performance collapses for dispersion-dominated adsorbates"))

