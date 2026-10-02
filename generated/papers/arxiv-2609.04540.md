<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Mitra-v2 Technical Report

- カード: [`arxiv-2609.04540`](../../papers/arxiv-2609.04540.yaml)
- 著者: Yefan Tao, Xiyuan Zhang, Xinyi Liu, Boran Han, Danielle Maddix, Haoyang Fang, Zhen Han, Jiading Gai, Xuanqing Liu, Michael Bohlke-Schneider, Yuyang (Bernie) Wang, Gerald Friedland, Kevan Mah, Chris Lee, Chris Kong
- 年・掲載: 2026
- 原論文: [PDF](https://arxiv.org/pdf/2609.04540v1)(arXiv v1、カード作成時に読んだ版)
- タグ: in-context-learning, tabular-attention, tabular-classification, tabular-foundation-model, tabular-regression
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** On the full TabArena benchmark Mitra-v2 performs at the level of TabFM and EXAONE Tabular and surpasses TabPFN-3 by a wide margin in classification and regression.([Abstract, p.1](https://arxiv.org/pdf/2609.04540v1#page=1 "On the full TabArena benchmark, Mitra-v2 delivers state-of-the-art performance at the level of the industry-scale TabFM and EXAONE Tabular models, while surpassing TabPFN-3 by a wide margin in both classification and regression."))
- **c2** The headline system uses fine-tuning and eight-fold bagging; it is much slower than forward-pass models and should not be called zero-shot or Pareto-dominant.([Limitations, p.24](https://arxiv.org/pdf/2609.04540v1#page=24 "It is much slower than forward-pass foundation models and should not be described as zero-shot or Pareto-dominant (Figure 6)."))
- **c3** All Mitra-v2 results use TabArena's one-hour per-unit budget, while TabFM's default artifacts on the reference leaderboard include fits exceeding that budget, so TabFM's rating reflects a larger compute envelope.([TabArena setup and protocol, p.9](https://arxiv.org/pdf/2609.04540v1#page=9 "the TabFM (default) artifacts on the reference leaderboard include per-dataset fits whose fit time alone exceeds this budget (up to 5,886 s), so its rating reflects a larger compute envelope than ours."))
- **c4** TALENT is used as a check of whether the TabArena results hold outside the protocol Mitra-v2 was developed against.([TALENT, p.20](https://arxiv.org/pdf/2609.04540v1#page=20 "it tests whether Mitra-v2’s TabArena results hold up outside the protocol it was developed against."))
- **c5** The primary TALENT preset excludes 26 datasets that served as TabPFN-2/TabICLv2 development data, leaving 274.([TALENT protocol, p.20](https://arxiv.org/pdf/2609.04540v1#page=20 "Our primary preset, main274, is the 274 that remain after excluding the 26 datasets that served as TabPFN-2/TabICLv2 development data"))
- **c6** Choosing the configuration per dataset would score higher, but only as an oracle that amounts to tuning on the benchmark; all reported numbers use one uniform configuration.([Appendix (Negative results), p.33](https://arxiv.org/pdf/2609.04540v1#page=33 "But this only works as an oracle: it amounts to tuning on the benchmark."))

