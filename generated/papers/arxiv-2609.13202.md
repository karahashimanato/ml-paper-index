<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Do Tabular Foundation Models Still Need Feature Engineering?

- カード: [`arxiv-2609.13202`](../../papers/arxiv-2609.13202.yaml)
- 著者: Yifan WU, Pinjun Dong, Jiran Tao, Binyan Jiang
- 年・掲載: 2026
- 原論文: [PDF](https://arxiv.org/pdf/2609.13202v1)(arXiv v1、カード作成時に読んだ版)
- タグ: in-context-learning, tabular-classification, tabular-foundation-model, tabular-regression
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Feature engineering gains are concentrated in earlier TFM generations and become negligible for the strongest models.([Abstract, p.1](https://arxiv.org/pdf/2609.13202v1#page=1 "We find a consistent pattern: feature engineering gains are concentrated in earlier model generations and become negligible for the strongest models."))
- **c2** The classification datasets are restricted to TabPFN v1's limits (at most 1,024 training samples and 100 features) so that all model generations are evaluated on the same datasets (13 TabArena datasets in total).([Experiments, p.3](https://arxiv.org/pdf/2609.13202v1#page=3 "all selected classification datasets satisfy the sample and feature limits of TabPFN v1 (at most 1,024 training samples and 100 features), ensuring that every generation is evaluated on the same datasets."))
- **c3** Every condition is evaluated on the 30 official TabArena splits, and gains are paired against the identity representation on the same split.([Experiments, p.3](https://arxiv.org/pdf/2609.13202v1#page=3 "Every condition is evaluated on the 30 official TabArena splits (10 repeats × 3 folds)."))
- **c4** Each estimator is fixed at its checkpoint with its default configuration, ensemble procedure and native preprocessing. No tuning of the TFMs is part of the comparison.([Problem Setup and Estimand, p.2](https://arxiv.org/pdf/2609.13202v1#page=2 "Let m denote a fixed tabular foundation model estimator, including its checkpoint, default configuration, ensemble procedure, and native preprocessing pipeline."))
- **c5** The reported best-observed feature-engineering gain is an oracle maximum over conditions, not a validation-selected choice.([Results (Figure 1 caption), p.5](https://arxiv.org/pdf/2609.13202v1#page=5 "the maximum is oracle, not validation-selected"))
- **c6** The context-augmentation experiment with related source datasets covers only three target tasks and is a feasibility study, not a benchmark-wide evaluation.([Experiments, p.4](https://arxiv.org/pdf/2609.13202v1#page=4 "The analysis is therefore a feasibility study conditioned on source availability and schema compatibility, rather than a benchmark wide evaluation."))

