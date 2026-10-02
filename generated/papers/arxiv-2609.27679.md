<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# What Do Tabular Foundation Models Compute In Context? In-Situ Representation Refinement through Attention-Gated Updates

- カード: [`arxiv-2609.27679`](../../papers/arxiv-2609.27679.yaml)
- 著者: Tian Zhou, Beverly Jin, Linxiao Yang, Xue Wang, Wenwei Wang, Bingqing Peng, Mengni Ye, Jinjie Gu, Liang Sun
- 年・掲載: 2026
- 原論文: [PDF](https://arxiv.org/pdf/2609.27679v2)(arXiv v2、カード作成時に読んだ版)
- タグ: in-context-learning, tabular-attention, tabular-classification, tabular-foundation-model
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** A leave-one-out derivation separates attention-based reading from state-dependent scaling, which motivates REFINEICL, an attention-gated FFN-free stack with low-rank feature interaction and typed memory.([Abstract, p.1](https://arxiv.org/pdf/2609.27679v2#page=1 "The leading term separates attention-based reading from state-dependent scaling, motivating REFINEICL: an attention-gated, FFN-free contextual stack with selected low-rank feature interac- tion and typed memory."))
- **c2** The benchmark-informed REFINEICL continuation also improves all four reported metrics over TabPFN-v3 on both TabZilla views.([Abstract, p.1](https://arxiv.org/pdf/2609.27679v2#page=1 "It also improves all four reported metrics over TabPFN-v3 on both TabZilla views."))
- **c3** Evaluation protocol (TabArena): REFINEICL is evaluated on fold 0 only, with eight ensemble members and one support ordering.([Appendix, p.14](https://arxiv.org/pdf/2609.27679v2#page=14 "REFINEICL uses fold 0, eight ensemble members, and one support ordering shared across model sizes."))
- **c4** The TabArena comparison uses a fixed v0.1 snapshot with reference methods, which is not interchangeable with the live leaderboard.([Appendix, p.14](https://arxiv.org/pdf/2609.27679v2#page=14 "This fixed benchmark snapshot contains 77 reference methods and is not interchangeable with the live leaderboard."))
- **c5** The TabArena checkpoint is a benchmark-informed continuation; the authors call the TabArena result a development-exposed comparison.([Appendix, p.15](https://arxiv.org/pdf/2609.27679v2#page=15 "continuation’s prior choice; this is a development-exposed comparison."))
- **c6** The native AMLB29 inference protocol follows the archived TabPFNv2 classifier defaults (fixed number of estimators, seed, temperature and a row ceiling).([Appendix, p.15](https://arxiv.org/pdf/2609.27679v2#page=15 "The AMLB29 native protocol follows the archived TabPFNv2 classifier defaults: four estimators, seed 0, temperature 0.9, and a 10,000-row ceiling."))

