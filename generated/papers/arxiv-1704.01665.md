<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Learning Combinatorial Optimization Algorithms over Graphs

- カード: [`arxiv-1704.01665`](../../papers/arxiv-1704.01665.yaml)
- 著者: Hanjun Dai, Elias B. Khalil, Yuyu Zhang, Bistra Dilkina, Le Song
- 年・掲載: 2017
- 原論文: [PDF](https://arxiv.org/pdf/1704.01665v4)(arXiv v4、カード作成時に読んだ版)
- タグ: combinatorial-optimization, graph-neural-networks, greedy-methods, reinforcement-learning
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Relation to greedy algorithms: the learned algorithm keeps the classical greedy pattern (build a feasible solution by successively adding nodes, maintained to satisfy the problem's constraints); only the node-evaluation function is learned instead of hand-crafted.([Introduction, p.2](https://arxiv.org/pdf/1704.01665v4#page=2 "We will adopt a greedy meta-algorithm design, whereby a feasible solution is constructed by successive addition of nodes based on the graph structure, and is maintained so as to satisfy the problem’s graph constraints."))
- **c2** Training: the greedy policy is learned with fitted Q-learning (n-step Q-learning with experience replay), parametrized by the structure2vec graph embedding network, optimizing the original objective directly.([Introduction, p.2](https://arxiv.org/pdf/1704.01665v4#page=2 "We will use ﬁtted Q-learning to learn a greedy policy that is parametrized by the graph embedding network."))
- **c3** Framing on guarantees: the authors describe heuristics as fast and effective but lacking theoretical guarantees; no approximation guarantee for the learned heuristic is stated in the text (the MVC baselines are 2-approximations).([Introduction, p.1](https://arxiv.org/pdf/1704.01665v4#page=1 "Heuristics are often fast, effective algorithms that lack theoretical guarantees, and may also require substantial problem-speciﬁc research and trial-and-error on the part of algorithm designers."))
- **c4** Protocol: instances are synthetic (Erdos-Renyi and Barabasi-Albert graphs for MVC/MaxCut; DIMACS-generator uniform or clustered points for TSP); 100 validation and 1000 test graphs; approximation ratios are relative to the best solution found by CPLEX (MVC, MaxCut) or Concorde (TSP) within 1 hour, which may not be optimal.([Experimental Evaluation, p.7](https://arxiv.org/pdf/1704.01665v4#page=7 "All approximation ratios reported in the paper are with respect to the best (possibly optimal) solution found by the solvers within 1 hour."))
- **c5** Train vs test sizes: to test size generalization, S2V-DQN is trained on graphs with 50-100 nodes and tested on graphs of up to 1200 nodes.([Generalization to larger instances, p.8](https://arxiv.org/pdf/1704.01665v4#page=8 "To investigate this, we train S2V-DQN on graphs with 50–100 nodes, and test its generalization ability on graphs with up to 1200 nodes."))
- **c6** TSP caveat: on synthetic random TSP the hand-designed Farthest insertion and 2-opt perform as well as S2V-DQN and slightly better in some cases (the authors add that S2V-DQN still performs better on real-world TSP data; that TSPLIB comparison uses per-instance Active Search rather than the greedy policy used on synthetic test sets, see c7).([Comparison of solution quality, p.8](https://arxiv.org/pdf/1704.01665v4#page=8 "For TSP, The Farthest and 2-opt algorithm perform as well as S2V-DQN, and slightly better in some cases."))
- **c7** TSPLIB protocol differs from the synthetic one: on 38 TSPLIB instances (51-318 cities) S2V-DQN is run in 'Active Search' mode, i.e. RL is applied on the fly to each instance without upfront training, keeping the best tour found; larger instances were not attempted due to single-GPU memory.([Appendix C.3, p.14](https://arxiv.org/pdf/1704.01665v4#page=14 "We apply S2V-DQN in “Active Search' mode, similarly to [6]: no upfront training phase is required, and the reinforcement learning algorithm 1 is applied on-the-ﬂy on each instance."))

