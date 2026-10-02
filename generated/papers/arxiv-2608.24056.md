<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# PhysicsBench: A Unified Leaderboard for Generative and Predictive Models in Engineering Design and Simulation

- カード: [`arxiv-2608.24056`](../../papers/arxiv-2608.24056.yaml)
- 著者: Sang Won Lee, Hyogu Jeong, Namwoo Kang
- 年・掲載: 2026
- 原論文: [PDF](https://arxiv.org/pdf/2608.24056v1)(arXiv v1、カード作成時に読んだ版)
- タグ: deep-learning, gaussian-processes, gradient-boosted-trees, supervised, tabular-foundation-model, tabular-regression
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** PhysicsBench is a unified benchmark and leaderboard that evaluates generative and predictive models under one standardized procedure.([Abstract, p.1](https://arxiv.org/pdf/2608.24056v1#page=1 "We present PhysicsBench, a unified benchmark and leaderboard that evaluates generative and predictive models under one standardized procedure."))
- **c2** An architecture's large-scale academic standing only weakly predicts its small-data ranking.([Abstract, p.1](https://arxiv.org/pdf/2608.24056v1#page=1 "Across tasks, an architecture’s large-scale academic standing weakly predicts its small-data ranking."))
- **c3** The tabular models in the 1D task include MLP, FT-Transformer, NODE, TabNet, TabPFN, gradient-boosted trees, Gaussian processes and ridge regression.([Experimental setup, p.8](https://arxiv.org/pdf/2608.24056v1#page=8 "The 1D tabular models are an MLP, FT-Transformer [46], NODE [77], TabNet [47], TabPFN [48], gradient-boosted trees [78, 79], Gaussian processes [80], and ridge regression [81]"))
- **c4** Tuning protocol: splits, epoch/batch budget, early stopping and normalization are shared, but each model's optimizer, learning rate and internal hyperparameters follow its source paper (no re-tuning).([Experimental setup, p.10](https://arxiv.org/pdf/2608.24056v1#page=10 "This fixes the shared procedure of data splits, resolution, epoch and batch budget, early stopping, and normalization, but not each model’s own optimizer, learning rate, and internal hyperparameters, which follow its source paper."))
- **c5** The tabular regression part uses Concrete and Airfoil and is ranked separately from time-series models.([Results, p.15](https://arxiv.org/pdf/2608.24056v1#page=15 "The 1D scalar task is reported as two rows, tabular regression on Concrete and Airfoil and time-series RUL on CMAPSS, because these span disjoint model sets, so a single pooled ranking would compare models that never competed head-to-head."))
- **c6** Conflict of interest: the leaderboard is vendor-hosted; author-affiliated in-house models are excluded from publication, and the authors say a fuller conflict-of-interest policy is needed.([Limitations, p.27](https://arxiv.org/pdf/2608.24056v1#page=27 "We exclude all author-affiliated in-house models from publication regardless of their measured rank, so the policy applies whether an in-house model would have won or lost, but a fuller governance and conflict-of-interest policy is needed."))

