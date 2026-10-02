<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Causilo Technical Report

- カード: [`arxiv-2609.22866`](../../papers/arxiv-2609.22866.yaml)
- 著者: Minyong Cho, Minho Jeong, Dooho Lee, Jinmo Lee, Jaemin Yoo
- 年・掲載: 2026
- 原論文: [PDF](https://arxiv.org/pdf/2609.22866v1)(arXiv v1、カード作成時に読んだ版)
- タグ: in-context-learning, tabular-attention, tabular-classification, tabular-foundation-model, tabular-regression
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Causilo is a tabular foundation model aiming at frontier predictive performance with very fast inference.([Abstract, p.1](https://arxiv.org/pdf/2609.22866v1#page=1 "We introduce Causilo, a tabular foundation model (TFM) that combines frontier predictive performance with exceptionally fast inference."))
- **c2** Causilo follows TabICL's column-then-row architecture and adds a row-refinement module before row compression.([Abstract, p.1](https://arxiv.org/pdf/2609.22866v1#page=1 "Causilo follows TabICL’s column-then-row architecture but introduces another row-refinement module before row compression."))
- **c3** Pretrained on about 36M synthetic tables, Causilo reports frontier-level performance with substantially faster inference on TabArena, BeyondArena and ScoringBench.([Abstract, p.1](https://arxiv.org/pdf/2609.22866v1#page=1 "Pretrained on approximately 36M synthetic tables, Causilo delivers strong benchmark results across TabArena, BeyondArena, and ScoringBench, achieving frontier-level performance with substantially faster inference."))
- **c4** TabArena comparisons use the latest public results as of 18 September 2026, with Elo computed over the full leaderboard including system submissions such as AutoGluon.([Evaluation (TabArena), p.7](https://arxiv.org/pdf/2609.22866v1#page=7 "We use the latest public results as of 18 September 2026 and Elo ratings are computed over the full leaderboard, including system submissions such as AutoGluon [21]"))
- **c5** BeyondArena has 142 curated datasets with IID, temporal and grouped splits, varied sizes, and tables with text or high-cardinality categoricals.([Evaluation (BeyondArena), p.9](https://arxiv.org/pdf/2609.22866v1#page=9 "Its 142 curated datasets span IID, temporal, and grouped splits, a wide range of sample sizes and feature counts, and tables with text or high-cardinality categorical features."))
- **c6** For BeyondArena, published baseline results are reused and only Causilo is evaluated locally.([Evaluation (BeyondArena), p.9](https://arxiv.org/pdf/2609.22866v1#page=9 "We therefore use its published baseline results and add only Causilo, which we evaluate locally."))

