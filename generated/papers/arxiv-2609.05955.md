<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# LoGIC: Budgeted Context Construction for Node-Level Graph In-Context Learning with Tabular Foundation Models

- カード: [`arxiv-2609.05955`](../../papers/arxiv-2609.05955.yaml)
- 著者: Mingqi Yang, Zidong Guo, Jihui Yang, Wenming Zuo
- 年・掲載: 2026
- 原論文: [PDF](https://arxiv.org/pdf/2609.05955v1)(arXiv v1、カード作成時に読んだ版)
- タグ: graph-neural-networks, graph-node-prediction, in-context-learning, tabular-foundation-model
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** LoGIC retrieves labeled nodes by structural, feature and coverage channels, shares contexts within graph-local query clusters, adds an unlabeled halo for adapter backbones, and selects channel and budget without test labels.([Abstract, p.1](https://arxiv.org/pdf/2609.05955v1#page=1 "We present LoGIC, which retrieves labeled nodes via structural, feature-based, and coverage channels, shares each context across the queries in a graph-local cluster, incorporates an unlabeled halo for adapter backbones, and chooses the channel and context budget without test labels."))
- **c2** Budgeted contexts keep locally runnable full-context performance, remain competitive with published large-dataset results, and markedly reduce peak memory.([Abstract, p.1](https://arxiv.org/pdf/2609.05955v1#page=1 "budgeted contexts maintain locally runnable full-context performance, stay competitive with published large-dataset results, and markedly lower peak memory requirements compared with full-context and whole-graph inference."))
- **c3** Evaluation uses eight GraphLand node-level benchmarks (12k-168k nodes) with classification (AP) and regression (R2) targets.([Experimental Setup, p.6](https://arxiv.org/pdf/2609.05955v1#page=6 "We conduct evaluations on eight GraphLand benchmarks [16] covering 12k–168k nodes, classification (AP) and regression (R2), and both assortative and disassortative targets."))
- **c4** The retrieval channel and budget k are chosen per dataset on held-out validation data from a coarse budget ladder.([Channel and Budget Configuration, p.6](https://arxiv.org/pdf/2609.05955v1#page=6 "For the reported LoGIC configurations, we assess a coarse ×4 budget ladder using held-out validation data and preserve one (channel, k) pair for each dataset."))
- **c5** Per-dataset trained baselines (LightGBM-NFA and GNNs) are published numbers taken from the G2T-FM evaluation, not rerun.([Predictive Performance on GraphLand, p.7](https://arxiv.org/pdf/2609.05955v1#page=7 "The first block lists individually trained LightGBM-NFA and GNN references from the G2T-FM evaluation."))
- **c6** The authors state that LoGIC is not a universal accuracy substitute for per-dataset training; it lags the strongest trained baselines on several datasets.([Predictive Performance on GraphLand, p.7](https://arxiv.org/pdf/2609.05955v1#page=7 "The contribution consequently does not constitute a universal accuracy substitute for per-dataset training."))

