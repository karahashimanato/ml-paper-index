<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Lost in Aggregation: How Benchmarks Overlook Irreplaceable Model Strengths

- カード: [`arxiv-2608.18919`](../../papers/arxiv-2608.18919.yaml)
- 著者: Andrej Tschalzev, Stefan Lüdtke, Heiner Stuckenschmidt, Christian Bartelt
- 年・掲載: 2026
- 原論文: [PDF](https://arxiv.org/pdf/2608.18919v1)(arXiv v1、カード作成時に読んだ版)
- タグ: gradient-boosted-trees, in-context-learning, supervised, tabular-classification, tabular-foundation-model, tabular-mlp, tabular-regression
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Benchmark evaluation should also consider a per-dataset peak performance frontier, defined by the best statistically supported performance on each dataset.([Abstract, p.1](https://arxiv.org/pdf/2608.18919v1#page=1 "We argue that benchmark evaluation should also consider the data-centric peak performance frontier, defined by the best statistically supported performance achieved on each dataset."))
- **c2** On TabArena, common aggregation metrics are highly correlated, mostly measure consistency and failure avoidance, and are much less aligned with dataset-level irreplaceability.([Abstract, p.1](https://arxiv.org/pdf/2608.18919v1#page=1 "Applying this framework to the TabArena benchmark, we find that common aggregation metrics are highly correlated and largely measure consistency and avoiding failures, while being much less aligned with dataset-level irreplaceability."))
- **c3** The analysis uses TabArena, a maintained benchmark with a live leaderboard and public evaluation results, which currently comprises 27 models on 51 curated datasets.([Experimental setup, p.2](https://arxiv.org/pdf/2608.18919v1#page=2 "using a stricter data curation and more extensive evaluation protocol, and currently comprises 27 models evaluated on 51 carefully curated datasets."))
- **c4** All models benefit from tuning on most datasets; foundation models can only be compared adequately when traditional alternatives are appropriately tuned.([Appendix, p.11](https://arxiv.org/pdf/2608.18919v1#page=11 "This implies that, even though modern foundation models often perform well by default, they can only be compared adequately when the traditional alternatives are appropriately tuned."))
- **c5** RealMLP, ranked first at TabArena's publication, is never irreplaceable in this analysis; its strength lies mainly in avoiding poor outcomes.([Results, p.3](https://arxiv.org/pdf/2608.18919v1#page=3 "yet in our analysis it ranks 13th on sufficiency, is never irreplaceable"))
- **c6** The first author (Tschalzev) is listed as a co-author of the TabArena paper whose results are analysed; the paper does not discuss this as a conflict of interest.([References, p.5](https://arxiv.org/pdf/2608.18919v1#page=5 "Erickson, N., Purucker, L., Tschalzev, A.,"))

