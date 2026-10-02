<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# From Synthetic Priors to Model Behavior: Structural Coverage in Tabular Foundation Models

- カード: [`arxiv-2609.06912`](../../papers/arxiv-2609.06912.yaml)
- 著者: He Zhao, Ryan Thompson, Daniel M. Steinberg, Ashfaqur Rahman, Edwin V. Bonilla, Cheng Soon Ong
- 年・掲載: 2026
- 原論文: [PDF](https://arxiv.org/pdf/2609.06912v1)(arXiv v1、カード作成時に読んだ版)
- タグ: in-context-learning, tabular-classification, tabular-foundation-model, tabular-regression
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** The paper recovers or reconstructs the synthetic data generators of four TFMs and compares their generated tasks with datasets from two tabular benchmarks.([Abstract, p.1](https://arxiv.org/pdf/2609.06912v1#page=1 "We recover or reconstruct the synthetic data generators of four TFMs and compare their generated tasks with datasets from two widely used tabular benchmarks."))
- **c2** Stronger synthetic-to-benchmark support is generally associated with better relative model performance.([Abstract, p.1](https://arxiv.org/pdf/2609.06912v1#page=1 "Moreover, stronger synthetic-to-benchmark support is generally associated with better relative model performance."))
- **c3** TALENT contributes 200 classification and 100 regression datasets (January 15, 2025 archive, single official training split); TabArena contributes 38 classification and 13 regression datasets.([Experimental settings, p.5](https://arxiv.org/pdf/2609.06912v1#page=5 "TALENT contributes 200 classification and 100 regression datasets from its January 15, 2025 archive, using the single official training split."))
- **c4** The two benchmark collections are not independent: 26 TabArena dataset names also appear in TALENT.([Experimental settings, p.5](https://arxiv.org/pdf/2609.06912v1#page=5 "The two benchmark collections are not independent: 26 TABARENA dataset names also appear in TALENT with the same prediction type."))
- **c5** Predictive results come from released checkpoints; on TabArena they mix leaderboard results, an official processed artifact and a direct run, depending on the model.([Appendix, p.12](https://arxiv.org/pdf/2609.06912v1#page=12 "on TABARENA, we use leaderboard results for TABICLV2 and TABSWIFT, the official processed artifact for MITRA, and a direct run for TABICLV1."))
- **c6** The analysis is descriptive, not causal: generator identity is confounded with architecture, optimization, ensembling and inference choices.([Method, p.5](https://arxiv.org/pdf/2609.06912v1#page=5 "This analysis is descriptive rather than causal: generator identity is confounded with model architecture, optimization, ensembling, inference, and other model-specific choices."))

