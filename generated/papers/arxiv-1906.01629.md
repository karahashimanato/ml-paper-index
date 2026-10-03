<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Exact Combinatorial Optimization with Graph Convolutional Neural Networks

- カード: [`arxiv-1906.01629`](../../papers/arxiv-1906.01629.yaml)
- 著者: Maxime Gasse, Didier Chételat, Nicola Ferroni, Laurent Charlin, Andrea Lodi
- 年・掲載: 2019
- 原論文: [PDF](https://arxiv.org/pdf/1906.01629v3)(arXiv v3、カード作成時に読んだ版)
- タグ: branch-and-bound, combinatorial-optimization, deep-learning, graph-neural-networks, supervised
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Relation to B&B: the paper uses ML to improve branch-and-bound, specifically learning the variable selection (branching) policy, with a graph convolutional network over the variable-constraint bipartite graph of the MILP.([Abstract, p.1](https://arxiv.org/pdf/1906.01629v3#page=1 "We propose a new graph convolutional neural network model for learning branch-and-bound variable selection policies, which leverages the natural variable-constraint bipartite graph representation of mixed-integer linear programs."))
- **c2** Learned decision and training target: the policy imitates strong branching via behavioral cloning with a cross-entropy loss, which the authors describe as an easier task than predicting strong branching scores or rankings (as done in earlier works they cite).([Introduction, p.2](https://arxiv.org/pdf/1906.01629v3#page=2 "Second, we approximate strong branching decisions by using behavioral cloning with a cross-entropy loss, a less difficult task than predicting strong branching scores [4] or rankings [30; 24]."))
- **c3** Exactness: in the B&B framework described, the solving process stops when upper and lower bounds are equal (or the feasible regions no longer decompose), giving a certificate of optimality or infeasibility. The learned policy replaces only the choice of the fractional variable to branch on, so B&B keeps this stopping rule (our reading; the paper calls B&B 'the exact method of choice' for MILPs but does not separately prove or state that the learned policy preserves exactness, and instances can remain unsolved within the 1-hour time limit).([Background, p.3](https://arxiv.org/pdf/1906.01629v3#page=3 "The solving process stops whenever both the upper and lower bounds are equal or when the feasible regions do not decompose anymore, thereby providing a certificate of optimality or infeasibility, respectively."))
- **c4** Solver settings: SCIP 6.0.1 is the backend with a 1-hour time limit; cutting planes are allowed at the root node only and solver restarts are deactivated (following prior work), with all other SCIP parameters at default.([Experiments, p.6](https://arxiv.org/pdf/1906.01629v3#page=6 "Throughout all experiments we use SCIP 6.0.1 as the backend solver, with a time limit of 1 hour."))
- **c5** Train vs test sizes: models are trained on small (Easy) instances and evaluated on Easy, Medium and Hard instances; e.g. for set covering (1,000 columns) training uses 500 rows and evaluation uses 500, 1,000 and 2,000 rows. The other benchmarks (combinatorial auction, capacitated facility location, maximum independent set) are scaled analogously.([Experiments, p.6](https://arxiv.org/pdf/1906.01629v3#page=6 "We train and test on instances with 500 rows, and we evaluate on instances with 500 (Easy), 1,000 (Medium) and 2,000 (Hard) rows."))
- **c6** Critique of prior learned-branching work (Khalil et al., Alvarez et al., Hansknecht et al.): those works evaluated on a simplified solver, whereas this paper compares against a full-fledged solver with primal heuristics, cuts and presolving activated (the authors also note those works did not evaluate generalization to larger instances).([Related work, p.2](https://arxiv.org/pdf/1906.01629v3#page=2 "Finally, in each case performance was evaluated on a simplified solver, whereas we compare, for the first time and favorably, against a full-fledged solver with primal heuristics, cuts and presolving activated."))
- **c7** Limitation (size generalization): the authors expect the improvement to decrease on progressively larger problems, and in early experiments on even larger ('huge') instances observed a performance drop for the model trained on small instances (a model trained on medium instances did perform well there).([Discussion, p.9](https://arxiv.org/pdf/1906.01629v3#page=9 "In early experiments with even larger instances (huge), we observed a performance drop for the model trained on our small instances."))

