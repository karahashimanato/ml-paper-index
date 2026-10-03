<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Learning a Large Neighborhood Search Algorithm for Mixed Integer Programs

- カード: [`arxiv-2107.10201`](../../papers/arxiv-2107.10201.yaml)
- 著者: Nicolas Sonnerat, Pengming Wang, Ira Ktena, Sergey Bartunov, Vinod Nair
- 年・掲載: 2021
- 原論文: [PDF](https://arxiv.org/pdf/2107.10201v3)(arXiv v3、カード作成時に読んだ版)
- タグ: combinatorial-optimization, graph-neural-networks, local-search, supervised
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Contribution and relation to local search: a learned LNS for MIPs where a Neural Neighborhood Selection policy chooses the search neighbourhood (variables to unassign) at each step, and the neighbourhood itself is searched with a MIP solver (SCIP 7.0.1).([Abstract, p.1](https://arxiv.org/pdf/2107.10201v3#page=1 "Formulating the subsequent search steps as a Markov Decision Process, we train a Neural Neighborhood Selection policy to select a search neighborhood at each step, which is searched using a MIP solver to ﬁnd the next assignment."))
- **c2** Training (imitation, not RL): the imitation target is an expert that, under certain assumptions, is guaranteed to pick the neighbourhood containing the optimal next assignment (local branching within a Hamming ball); the expert is too slow for use at test time and is only used offline to generate data.([Introduction, p.2](https://arxiv.org/pdf/2107.10201v3#page=2 "We propose an imitation learning approach to train the neighborhood selection policy using as the imitation target an expert policy that, under certain assumptions, is guaranteed to select the neighborhood containing the optimal next assignment at a given LNS step."))
- **c3** Guarantees given up: the method is a primal heuristic (it seeks a good feasible assignment, not a proof of optimality or a lower bound), motivated by production applications.([Background, p.3](https://arxiv.org/pdf/2107.10201v3#page=3 "This work focuses on primal heuristics as production applications often only require ﬁnding a good feasible assignment quickly."))
- **c4** Baseline tuning: SCIP's metaparameters (presolve, cuts, heuristics) are tuned per dataset by grid search to give the best validation average primal gap curves, to make it behave more like a primal heuristic; other baselines are random neighbourhood selection (with Neural Diving start) and Neural Diving alone. Gurobi is not used.([Baselines, p.6](https://arxiv.org/pdf/2107.10201v3#page=6 "for each dataset separately using grid search to achieve the best validation set average primal gap curves."))
- **c5** Compute is not matched across all methods: the learned heuristics and random-LNS baselines get the same parallel resources, but SCIP is run single-core only.([Baselines, p.6](https://arxiv.org/pdf/2107.10201v3#page=6 "SCIP is evaluated only in the single core setting, as the main focus of this work is to evaluate the beneﬁt of easily parallelizable primal heuristics."))
- **c6** Datasets and affiliation: five datasets (Neural Network Verification, Electric Grid Optimization, Production Packing, Production Planning, MIPLIB), each split 70/15/15 with a separate model per dataset; two come from the production systems of a large technology company, which the text does not name (author affiliations: DeepMind, Charm Therapeutics, Google Research).([Datasets, p.5](https://arxiv.org/pdf/2107.10201v3#page=5 "In particular, Production Packing and Planning datasets are obtained from a large technology company’s production systems."))
- **c7** Limitations: models are not trained end-to-end on the final metric (average primal gap), and the conditionally independent policy does not approximate the expert perfectly; the authors suggest RL/offline RL and autoregressive models as possible remedies.([Discussion, p.8](https://arxiv.org/pdf/2107.10201v3#page=8 "Our approach does not currently train models in an end-to-end fashion to directly optimize a ﬁnal performance metric such as the average primal gap."))

