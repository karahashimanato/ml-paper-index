<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Learning to Perform Local Rewriting for Combinatorial Optimization

- カード: [`arxiv-1810.00337`](../../papers/arxiv-1810.00337.yaml)
- 著者: Xinyun Chen, Yuandong Tian
- 年・掲載: 2018
- 原論文: [PDF](https://arxiv.org/pdf/1810.00337v5)(arXiv v5、カード作成時に読んだ版)
- タグ: combinatorial-optimization, deep-learning, local-search, reinforcement-learning
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Contribution: NeuRewriter learns a policy that picks heuristics and rewrites local components of the current solution, iteratively improving it until convergence (instead of constructing a solution from scratch).([Abstract, p.1](https://arxiv.org/pdf/1810.00337v5#page=1 "In this paper, we propose NeuRewriter that learns a policy to pick heuristics and rewrite the local components of the current solution to iteratively improve it until convergence."))
- **c2** Training: the policy factorizes into a region-picking and a rule-picking component, each a neural network trained with actor-critic reinforcement learning (reward = cost reduction per rewriting step).([Abstract, p.1](https://arxiv.org/pdf/1810.00337v5#page=1 "The policy factorizes into a region-picking and a rule-picking component, each parameterized by a neural network trained with actor-critic methods in reinforcement learning."))
- **c3** Relation to local search: the authors describe the framework as closely connected to the local search pipeline, with the learned RL policy guiding the local search by deciding which neighbour solution to move to.([Related Work, p.2](https://arxiv.org/pdf/1810.00337v5#page=2 "Speciﬁcally, we can leverage our learned RL policy to guide the local search, i.e., to decide which neighbor solution to move to."))
- **c4** Protocol (time budgets and hardware): all algorithms run on the same server; neural networks use 1 GPU while search algorithms use 4 CPU cores, and search algorithms get a 10-second timeout per instance; no wall-clock limit is stated for the neural networks, so hardware (GPU vs CPU) and budgets are not matched.([Experiments, p.6](https://arxiv.org/pdf/1810.00337v5#page=6 "We set the timeout of search algorithms to be 10 seconds per instance."))
- **c5** Runtime caveat stated by the authors: OR-Tools' VRP solver is highly tuned and implemented in C++, while the RL approaches are in Python and their runtimes are measured decoding one instance at a time; the authors note potential room for speed-up by batching.([Vehicle Routing Problem, p.9](https://arxiv.org/pdf/1810.00337v5#page=9 "Note that the OR-Tools solver for vehicle routing problems is highly tuned and implemented in C++, while the RL-based approaches in comparison are implemented in Python."))
- **c6** Job-scheduling baseline setting: OR-Tools (offline setting) gets a 10-second timeout per workload; the authors state it cannot reach good performance even with a larger timeout (Appendix E attributes this to schedules that prioritize long jobs).([Job Scheduling Problem, p.8](https://arxiv.org/pdf/1810.00337v5#page=8 "For OR-tools, we set the timeout to be 10 seconds per workload, but we ﬁnd that it can not achieve a good performance even with a larger timeout, and we defer the discussion to Appendix E."))
- **c7** Limitation: because the approach rewrites locally it can become time-consuming when large changes are needed per iteration; in extreme cases where each step must change the global structure, starting from scratch becomes preferable.([Conclusion, p.9](https://arxiv.org/pdf/1810.00337v5#page=9 "In extreme cases where each rewriting step needs to change the global structure, starting from scratch becomes preferrable."))

