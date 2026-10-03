<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Solving Mixed Integer Programs Using Neural Networks

- カード: [`arxiv-2012.13349`](../../papers/arxiv-2012.13349.yaml)
- 著者: Vinod Nair, Sergey Bartunov, Felix Gimeno, Ingrid von Glehn, Pawel Lichocki, Ivan Lobov, Brendan O'Donoghue, Nicolas Sonnerat, Christian Tjandraatmadja, Pengming Wang, Ravichandra Addanki, Tharindi Hapuarachchi, Thomas Keck, James Keeling, Pushmeet Kohli, Ira Ktena, Yujia Li, Oriol Vinyals, Yori Zwols
- 年・掲載: 2020
- 原論文: [PDF](https://arxiv.org/pdf/2012.13349v3)(arXiv v3、カード作成時に読んだ版)
- タグ: branch-and-bound, combinatorial-optimization, deep-learning, graph-neural-networks, supervised
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Relation to B&B: two learned components are plugged into a base MIP solver (SCIP): Neural Diving for finding high-quality assignments (primal side) and Neural Branching for variable selection in branch-and-bound (bounding the gap).([Abstract, p.1](https://arxiv.org/pdf/2012.13349v3#page=1 "Our approach constructs two corresponding neural network-based components, Neural Diving and Neural Branching, to use in a base MIP solver such as SCIP."))
- **c2** Neural Branching's expert: because a CPU-based Full Strong Branching implementation can be too expensive on large-scale MIPs even for offline data generation, the authors build an FSB variant using ADMM that batches the LP computations on GPU (solving the LPs approximately) to generate imitation data.([Introduction, p.3](https://arxiv.org/pdf/2012.13349v3#page=3 "We develop a variant of FSB using the alternating directions method of multipliers (ADMM) (Boyd et al. 2011) that scales to large-scale MIPs by performing the required computation in a batch manner on GPU."))
- **c3** Exactness / metric: B&B tracks global primal and dual bounds; a zero primal-dual gap certifies optimality, but in practice B&B is terminated at an application-dependent relative gap, and evaluation reports average primal, dual or primal-dual gap over time plus survival plots.([Background, p.7](https://arxiv.org/pdf/2012.13349v3#page=7 "The gap is always nonnegative by construction, and if it is zero then we have solved the problem, the feasible point that corresponds to the primal bound is optimal and the dual bound is a certificate of optimality."))
- **c4** Baseline and tuning: the main baseline is SCIP 7.0.1 with its presolving, primal heuristics and cuts emphasis settings tuned per dataset by exhaustive grid search on 200 validation MIPs with a 3-hour limit ('Tuned SCIP').([Evaluation, p.13](https://arxiv.org/pdf/2012.13349v3#page=13 "The main baseline we compare against is SCIP 7.0.1 with its parameters tuned for each test dataset."))
- **c5** Hardware fairness: in the joint comparison (only the sequential version of Neural Diving), Neural Diving (Sequential) and Neural Branching each use a CPU core and a GPU, so their combination uses two cores and two GPUs; Tuned SCIP is given two cores, used as two independent solves with different seeds (best bounds across the two runs), and GPU use is explicitly not controlled for.([Joint evaluation, p.31](https://arxiv.org/pdf/2012.13349v3#page=31 "Since SCIP does not use GPUs, we do not control for that resource when comparing Tuned SCIP and Neural Solvers."))
- **c6** Data splits: all datasets except MIPLIB are split randomly into disjoint 70/15/15% train/validation/test subsets (so, in our reading, test instances come from the same dataset rather than from a larger size class); for MIPLIB the 2017 Benchmark Set is the test set, and the 2017 Collection Set and the 2010 set (after removing overlaps with the Benchmark Set) are the training and validation sets, respectively.([Datasets, p.12](https://arxiv.org/pdf/2012.13349v3#page=12 "For MIPLIB, we use instances from the MIPLIB 2017 Benchmark Set as the test set, since that is the set on which solvers are evaluated."))
- **c7** Limitation (Neural Diving): the authors believe its strength is finding good solutions quickly but that it sometimes fails to find optimal or near-optimal solutions, e.g. losing to SCIP at the end on Electric Grid Optimization and MIPLIB survival plots.([Neural Diving results, p.21](https://arxiv.org/pdf/2012.13349v3#page=21 "We believe that the strength of our approach is in quickly finding good solutions, but it sometimes fails to find an optimal or near-optimal solution."))

