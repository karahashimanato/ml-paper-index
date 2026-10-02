<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Message Passing Does More with Less for In-Context Learning on Graphs

- カード: [`arxiv-2609.37057`](../../papers/arxiv-2609.37057.yaml)
- 著者: Dooho Lee, Jinmo Lee, Minho Jeong, Kijung Shin, Jaemin Yoo
- 年・掲載: 2026
- 原論文: [PDF](https://arxiv.org/pdf/2609.37057v1)(arXiv v1、カード作成時に読んだ版)
- タグ: graph-neural-networks, graph-node-prediction, in-context-learning
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Ephris is a graph in-context learner built on sparse message passing that scales linearly with feature entries and edges, pretrained entirely on synthetic graphs.([Abstract, p.1](https://arxiv.org/pdf/2609.37057v1#page=1 "In this work, we present Ephris, a new graph in-context learner built on sparse message passing, scaling linearly with the number of node-feature entries and graph edges."))
- **c2** Evaluated on 51 node-classification datasets against 15 extensively tuned GNNs and existing graph ICL methods, Ephris ranks first on all four aggregate measures.([Abstract, p.1](https://arxiv.org/pdf/2609.37057v1#page=1 "Across both settings, Ephris ranks first on all four aggregate measures: Elo, improvability, average rank, and accuracy."))
- **c3** Following TabArena, each GNN is evaluated with default hyperparameters and tuned (best of 200 configurations by validation); high- and low-label regimes with five splits each.([Evaluation protocol, p.7](https://arxiv.org/pdf/2609.37057v1#page=7 "Following TabArena (Erickson et al., 2026), each GNN is evaluated under two tuning budgets: default, using default hyperparameters, and tuned, selecting the best of 200 configurations by validation performance."))
- **c4** Under this broader evaluation, advantages reported for existing graph foundation models do not hold against tuned GNNs such as GCNII and GPRGNN.([Results, p.8](https://arxiv.org/pdf/2609.37057v1#page=8 "Therefore, the advantages reported for existing GFMs do not hold for broader datasets and stronger baselines."))
- **c5** Limitations: ablations use reduced-budget proxy pretraining; robustness under non-IID grouped and temporal splits remains to be improved; scope limited to node classification.([Limitations, p.9](https://arxiv.org/pdf/2609.37057v1#page=9 "Our ablation studies use reduced-budget proxy pretraining, so their conclusions may not fully transfer to full-scale training."))
- **c6** Among the GFM baselines, Node4All is authored by two of this paper's authors (per the reference list); this overlap is not discussed as a conflict of interest.([References, p.12](https://arxiv.org/pdf/2609.37057v1#page=12 "Dooho Lee and Jaemin Yoo. Node4all: Learning node representation beyond datasets."))

