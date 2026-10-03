<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# The CLRS Algorithmic Reasoning Benchmark

- カード: [`arxiv-2205.15659`](../../papers/arxiv-2205.15659.yaml)
- 著者: Petar Veličković, Adrià Puigdomènech Badia, David Budden, Razvan Pascanu, Andrea Banino, Misha Dashevskiy, Raia Hadsell, Charles Blundell
- 年・掲載: 2022
- 原論文: [PDF](https://arxiv.org/pdf/2205.15659v2)(arXiv v2、カード作成時に読んだ版)
- タグ: algorithm-learning, deep-learning, graph-neural-networks, supervised
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Contribution: CLRS-30 is a dataset of trajectories (inputs, outputs and optional intermediate targets) for 30 classical algorithms covering sorting, searching, dynamic programming, geometry, graphs and strings, proposed to unify evaluation that prior work did on bespoke data.([Introduction, p.2](https://arxiv.org/pdf/2205.15659v2#page=2 "we propose and evaluate on CLRS-30: a dataset containing trajectories—a trajectory is formed of inputs, the corresponding outputs and optional intermediary targets—of 30 classical algorithms"))
- **c2** Sorting algorithms included: insertion sort, bubble sort, heapsort and quicksort. (Searching includes minimum, binary search and quickselect; merge sort is excluded because it needs memory not attached to input objects.)([CLRS Algorithmic Reasoning Benchmark, p.4](https://arxiv.org/pdf/2205.15659v2#page=4 "Sorting: Insertion sort, bubble sort, heapsort (Williams, 1964), quicksort (Hoare, 1962)."))
- **c3** Greedy algorithms included: activity selection and task scheduling.([CLRS Algorithmic Reasoning Benchmark, p.4](https://arxiv.org/pdf/2205.15659v2#page=4 "Greedy: Activity selection (Gavril, 1972), task scheduling (Lawler, 1985)."))
- **c4** Train vs test sizes: training and validation inputs have 16 nodes (1,000 training and 32 validation trajectories; validation measures in-distribution generalisation), and the test set measures out-of-distribution generalisation with 32 trajectories on inputs of 64 nodes (more for graph-level outputs). Most graph-algorithm inputs are Erdos-Renyi graphs; scalar inputs are U(0,1).([Dataset statistics, p.8](https://arxiv.org/pdf/2205.15659v2#page=8 "For testing, we measure out-of-distribution generalisation, and sample 32 trajectories for inputs of 64 nodes."))
- **c5** Supervision with hints: baselines both decode hints (in the loss) and encode them as inputs, with noisy teacher forcing at training time (ground-truth hints fed back with probability 0.5); at evaluation the number of processor steps is set by the number of ground-truth hints, a requirement the authors say could be lifted, e.g., with termination networks.([Baseline models, p.7](https://arxiv.org/pdf/2205.15659v2#page=7 "The quantity of hints is still used to determine the number of processor steps to perform at evaluation time."))
- **c6** Out-of-distribution failure: MPNNs, which appear to dominate in-distribution for most tasks (Section 4.3: over 90% F1 for nearly all of them on validation), do not transfer their gains to graphs four times larger (64 vs 16 nodes); PGN becomes the most performant model when averaged across task types, which the authors say aligns with prior research (Veličković et al., 2020).([Test (out-of-distribution) performance, p.9](https://arxiv.org/pdf/2205.15659v2#page=9 "MPNNs are unable to transfer their impressive gains to graphs that are four times larger"))
- **c7** Stated failure modes: the authors say the OOD version of CLRS-30 is highly challenging and far from solved for most tasks; PGNs struggled on tasks requiring long-range rollouts (e.g. DFS) or recursive reasoning (e.g. Quicksort, Quickselect); string matching (e.g. KMP) may need more specialised inductive biases; the processor tended to do best on tasks with favourable (sublinear) hint counts such as BFS, Bellman-Ford and task scheduling.([Test (out-of-distribution) performance, p.9](https://arxiv.org/pdf/2205.15659v2#page=9 "In particular, PGNs struggled on tasks requiring long-range rollouts (such as DFS), or recursive reasoning (such as Quicksort and Quickselect)."))

