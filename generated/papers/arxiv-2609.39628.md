<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# MIND: Marginal-Invariant Neural Dependency Diffusion for Mixed-Type Tabular Generation

- カード: [`arxiv-2609.39628`](../../papers/arxiv-2609.39628.yaml)
- 著者: Pengfei Li, Mohammad Khalil
- 年・掲載: 2026
- 原論文: [PDF](https://arxiv.org/pdf/2609.39628v1)(arXiv v1、カード作成時に読んだ版)
- タグ: deep-learning, diffusion-models, tabular-data-generation, unsupervised
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** MIND maps different variable types into a unified latent dependency space via column-wise marginal transport instead of learning the joint distribution in the raw feature space.([Abstract, p.1](https://arxiv.org/pdf/2609.39628v1#page=1 "Instead, it first maps different variable types into a unified latent dependency space via column-wise marginal transport."))
- **c2** Across nine tabular benchmarks, MIND is reported to consistently improve marginal fidelity and dependency preservation over existing unified approaches.([Abstract, p.1](https://arxiv.org/pdf/2609.39628v1#page=1 "Experiments across nine diverse tabular benchmarks show that MIND consistently improves marginal fidelity and dependency preservation over existing unified approaches."))
- **c3** For each of three seeds, all methods share the same stratified 64/16/20 train/validation/test split.([Experiment setup, p.4](https://arxiv.org/pdf/2609.39628v1#page=4 "For each seed in {42, 43, 44}, all methods use the same stratified 64%/16%/20% train/validation/test split"))
- **c4** TSTR utility is averaged over XGBoost, LightGBM and MLP downstream models, using AUC for classification and R2 for regression.([Results, p.6](https://arxiv.org/pdf/2609.39628v1#page=6 "Scores are averaged over XGBoost, LightGBM, and MLP, using AUC for classification datasets and R2 for regression datasets"))
- **c5** The aggregate TSTR advantage of MIND is substantially influenced by Covertype, so the authors interpret MIND as competitive with diffusion-based SOTA rather than dominant.([Discussion, p.6](https://arxiv.org/pdf/2609.39628v1#page=6 "Although the aggregate TSTR mean favours MIND, this difference is influenced substantially by Covertype."))
- **c6** MIND assumes a designated target column and batch-level generation, limiting direct use in target-free or multi-target settings.([Limitations, p.7](https://arxiv.org/pdf/2609.39628v1#page=7 "Currently, we assume a designated target column and perform batch-level generation, which limits direct use in target-free or multi-target settings."))

