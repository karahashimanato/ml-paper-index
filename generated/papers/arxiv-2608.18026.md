<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# TabNSM: Neural Sparse Mixer for Tabular Regression

- カード: [`arxiv-2608.18026`](../../papers/arxiv-2608.18026.yaml)
- 著者: Ali Eslamian, Qiang Cheng
- 年・掲載: 2026
- 原論文: [PDF](https://arxiv.org/pdf/2608.18026v1)(arXiv v1、カード作成時に読んだ版)
- タグ: deep-learning, supervised, tabular-attention, tabular-regression
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** TabNSM is a regression framework that extends the authors' own earlier sparse-attention and mixer architectures (named TabNSA and TabMixer in the Introduction).([Abstract, p.1](https://arxiv.org/pdf/2608.18026v1#page=1 "We propose TabNSM, a scalable regression framework that extends our earlier sparse-attention and mixer architectures."))
- **c2** Across nine real-world regression benchmarks, TabNSM shows strong predictive performance and scalability, with consistent gains on high-dimensional and heterogeneous datasets.([Abstract, p.1](https://arxiv.org/pdf/2608.18026v1#page=1 "Across nine real-world regression benchmarks, TabNSM achieves strong predictive performance and practical scalability, with consistent gains on high-dimensional and heterogeneous datasets."))
- **c3** Evaluation uses a single 72/8/20 train/validation/test split with fixed random partitions across methods.([Experiments and Results, p.7](https://arxiv.org/pdf/2608.18026v1#page=7 "We use a 72/8/20 train/validation/test split with fixed random partitions across methods."))
- **c4** TabNSM's ASIM hyperparameters are selected with Optuna on the validation set.([Experiments and Results, p.7](https://arxiv.org/pdf/2608.18026v1#page=7 "The ASIM hyperparameters are selected via Optuna [46] on the validation set and fixed thereafter."))
- **c5** Baselines are tuned with Optuna using 3-fold CV on training+validation and 20 trials.([Appendix, p.22](https://arxiv.org/pdf/2608.18026v1#page=22 "Hyperparameter optimization was performed with Optuna (3-fold CV on training+validation, 20 trials, maximizing negative RMSE)."))
- **c6** Some baselines were not tuned for most large-dataset benchmarks (non-convergence or outlier results) and are not reported in Table 2.([Appendix, p.22](https://arxiv.org/pdf/2608.18026v1#page=22 "were not tuned for most large-dataset benchmarks, often resulting in non-convergence or outlier performance"))

