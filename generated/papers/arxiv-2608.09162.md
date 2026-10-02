<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Tabular Numeric Stretch Transformation

- カード: [`arxiv-2608.09162`](../../papers/arxiv-2608.09162.yaml)
- 著者: Zihao Ye, Juyong Kim, Johnna Sundberg, Burak Varici, Pradeep Ravikumar
- 年・掲載: 2026
- 原論文: [PDF](https://arxiv.org/pdf/2608.09162v1)(arXiv v1、カード作成時に読んだ版)
- タグ: supervised, tabular-attention, tabular-classification, tabular-mlp, tabular-regression
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** The stretch framework formulates numeric feature preprocessing as an optimization problem that makes the target function smoother and so more learnable.([Abstract, p.1](https://arxiv.org/pdf/2608.09162v1#page=1 "We introduce the stretch transformation framework, which formulates numeric feature preprocessing as an optimization problem to make the target function smoother and thus more learnable."))
- **c2** On 38 TALENT datasets, supervised stretch consistently outperforms all baseline transformations.([Abstract, p.1](https://arxiv.org/pdf/2608.09162v1#page=1 "Comprehensive experiments on 38 datasets from the TALENT benchmark demonstrate that supervised stretch consistently outperforms all baselines."))
- **c3** Every dataset-model-transformation combination gets 100 Optuna trials, jointly tuning model and transformation hyperparameters on the official TALENT train and validation partitions only.([Experimental setup, p.7](https://arxiv.org/pdf/2608.09162v1#page=7 "We conduct Bayesian optimization using Optuna [1] with 100 trials for each dataset-model-transformation combination, jointly tuning model and transformation hyperparameters (e.g., number of bins for stretch and PLE) using only the training and validation partitions."))
- **c4** Selected configurations are run with 15 seeds on one fixed split, so the reported variability covers initialization and optimization, not alternative data splits.([Experimental setup, p.7](https://arxiv.org/pdf/2608.09162v1#page=7 "Each selected configuration is evaluated with 15 random seeds on the fixed split; these seeds measure initialization, minibatch-order, and optimization variability, not variability over alternative data splits."))
- **c5** The 38 datasets come from the 42-dataset TALENT Benchmark 1 collection after excluding four datasets with only categorical features.([Appendix, p.15](https://arxiv.org/pdf/2608.09162v1#page=15 "From the original TALENT Benchmark 1 collection of 42 datasets, we exclude four datasets that contain only categorical features"))
- **c6** The transformation is marginal (per feature), so it does not optimize a joint or conditional smoothness objective and is not interaction-aware.([Limitations, p.10](https://arxiv.org/pdf/2608.09162v1#page=10 "The current transformation is marginal and therefore does not optimize a joint or conditional smoothness objective; the downstream model may learn feature interactions, but the preprocessing itself is not interaction-aware."))

