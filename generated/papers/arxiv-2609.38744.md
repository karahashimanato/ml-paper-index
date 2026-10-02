<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Molecular Property Prediction under Structural Shift with Tabular Foundation Models

- カード: [`arxiv-2609.38744`](../../papers/arxiv-2609.38744.yaml)
- 著者: Jinmo Lee, Dooho Lee, Minho Jeong, Jaemin Yoo
- 年・掲載: 2026
- 原論文: [PDF](https://arxiv.org/pdf/2609.38744v1)(arXiv v1、カード作成時に読んだ版)
- タグ: in-context-learning, tabular-classification, tabular-foundation-model, tabular-regression
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** MolPAIR uses a second frozen TFM that predicts error differences between a query and labeled reference molecules to refine the first TFM's prediction.([Abstract, p.1](https://arxiv.org/pdf/2609.38744v1#page=1 "A second frozen TFM predicts differences in prediction errors between the query and labeled reference molecules, using these comparisons to refine the initial prediction."))
- **c2** CheMeleon representations with TabPFN-3 alone already beat each evaluated baseline on a majority of the 58 tasks.([Abstract, p.1](https://arxiv.org/pdf/2609.38744v1#page=1 "Across 58 MoleculeACE and Polaris tasks, CheMeleon representations combined with TabPFN-3 already outperform each evaluated baseline on a majority of tasks."))
- **c3** The benchmark combines 30 MoleculeACE and 28 Polaris tasks (47 regression, 11 binary classification).([Evaluation protocol, p.5](https://arxiv.org/pdf/2609.38744v1#page=5 "We combine 30 MoleculeACE bioactivity tasks with 28 Polaris tasks (Van Tilborg et al., 2022; Polaris Hub, 2026), comprising 47 regression and 11 binary classification tasks."))
- **c4** Splits hold out scaffold groups and additionally filter out test molecules too similar to training molecules.([Evaluation protocol, p.6](https://arxiv.org/pdf/2609.38744v1#page=6 "The scaffold holdout separates structural groups, while the similarity filter removes close analogues that can remain across different scaffolds."))
- **c5** Tree baselines are tuned on training data only with Optuna (30 trials for RF/ExtraTrees, 50 for XGBoost/LightGBM).([Appendix, p.18](https://arxiv.org/pdf/2609.38744v1#page=18 "Random Forest and ExtraTrees use 30 Optuna trials; XGBoost and LightGBM use 50."))
- **c6** Limitation: real-world shifts may not be captured by scaffold and fingerprint-similarity splits; MolPAIR also increases inference cost.([Limitations and future work, p.9](https://arxiv.org/pdf/2609.38744v1#page=9 "Broader real-world distribution shifts may also involve changes that are not captured by scaffold separation and fingerprint-similarity-based splits."))

