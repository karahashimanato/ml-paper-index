<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Tabular Deep Learning for Algorithmic Trading: Cross-Regime Bayesian Optimisation for Equity Signal Generation

- カード: [`arxiv-2608.27076`](../../papers/arxiv-2608.27076.yaml)
- 著者: Joshua Le Grice
- 年・掲載: 2026
- 原論文: [PDF](https://arxiv.org/pdf/2608.27076v1)(arXiv v1、カード作成時に読んだ版)
- タグ: gradient-boosted-trees, heterogeneous-ensembles, linear-models, supervised, tabular-attention, tabular-classification, tabular-mlp
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Existing evaluations of equity prediction models do not explicitly target regime robustness in hyperparameter selection.([Abstract, p.1](https://arxiv.org/pdf/2608.27076v1#page=1 "Existing evaluations of equity prediction models do not explicitly target regime robustness during hyperparameter selection."))
- **c2** No single tabular deep learning architecture outperforms gradient-boosted trees; combining XGBoost and TabNet by rank aggregation gives the Hybrid ensemble.([Abstract, p.1](https://arxiv.org/pdf/2608.27076v1#page=1 "No individual tabular deep learning architecture outperforms gradient-boosted trees, but combining XGBoost and TabNet using rank aggregation produces a Hybrid ensemble"))
- **c3** Tuning protocol: all models are tuned with Optuna TPE, with the same trial budget per model.([Experimental setup, p.8](https://arxiv.org/pdf/2608.27076v1#page=8 "Hyperparameters for all models are selected using Bayesian optimisation via the Optuna framework [54], utilising a Tree-structured Parzen Estimator (TPE) [55] sampler with 30 trials per model."))
- **c4** The out-of-sample year is excluded from model development and hyperparameter selection.([Experimental setup, p.7](https://arxiv.org/pdf/2608.27076v1#page=7 "The 2025 period was excluded from model development and hyperparameter selection to provide an uninfluenced estimate of real-world performance."))
- **c5** Limitation: using index constituents identified at the end of the sample introduces survivorship bias.([Limitations, p.18](https://arxiv.org/pdf/2608.27076v1#page=18 "Using S&P 500 constituents identified at the end of the sample period introduces survivorship bias."))
- **c6** Limitation: the reported figures come from selecting the best configuration among many trialled configurations (no deflated Sharpe correction).([Limitations, p.18](https://arxiv.org/pdf/2608.27076v1#page=18 "Also, reported figures reflect the selection of the best-performing configuration from approximately 161 trialled across the five model classes and their ensemble combinations."))

