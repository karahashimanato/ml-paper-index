<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Combinatorial Optimization with Graph Convolutional Networks and Guided Tree Search

- カード: [`arxiv-1810.10659`](../../papers/arxiv-1810.10659.yaml)
- 著者: Zhuwen Li, Qifeng Chen, Vladlen Koltun
- 年・掲載: 2018
- 原論文: [PDF](https://arxiv.org/pdf/1810.10659v1)(arXiv v1、カード作成時に読んだ版)
- タグ: combinatorial-optimization, deep-learning, graph-neural-networks, greedy-methods, local-search, supervised
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Core idea: a graph convolutional network is trained (supervised) to estimate, for each vertex, the likelihood that it belongs to the optimal solution.([Abstract, p.1](https://arxiv.org/pdf/1810.10659v1#page=1 "The central component is a graph convolutional network that is trained to estimate the likelihood, for each vertex in a graph, of whether this vertex is part of the optimal solution."))
- **c2** Relation to search: the trained GCN guides a parallelized tree search that generates many candidate solutions, one of which is chosen after refinement (the basic variant uses the GCN output as the heuristic in a greedy procedure).([Introduction, p.2](https://arxiv.org/pdf/1810.10659v1#page=2 "This trained GCN is used to guide a parallelized tree search procedure that rapidly generates a large number of candidate solutions, one of which is chosen after subsequent reﬁnement."))
- **c3** Classical components: two ideas adopted from classic heuristics are added, described as complementary to learning: 2-improvement local search to refine candidates and graph reduction that shrinks the graph while preserving the optimal MIS size.([Method, p.3](https://arxiv.org/pdf/1810.10659v1#page=3 "Finally, Section 4.3 describes two ideas adopted from classic heuristics that are complementary to the application of learning and are useful in accelerating computation and reﬁning candidate solutions."))
- **c4** Protocol (training): a single network is trained on SATLIB 3-SAT instances converted to MIS graphs (about 1,200 vertices each; 38,000/1,000/1,000 split) and applied to all other problems and datasets (SAT Competition 2017, BUAA-MC, SNAP social networks, citation networks).([Experimental setup, p.5](https://arxiv.org/pdf/1810.10659v1#page=5 "The network trained on this training set will be applied to all other problems and datasets described below."))
- **c5** Protocol (baselines and time): baselines are S2V-DQN, a classic greedy heuristic (also with graph reduction + local search), Z3, ReduMIS and Gurobi; the tree search runs with 16 threads and the other methods get 16x the running time (time limits 10 minutes on SAT datasets, 30 minutes on large graphs), on one desktop with an i7-5960X CPU and Titan X GPU.([Results, p.6](https://arxiv.org/pdf/1810.10659v1#page=6 "For fair comparison, we give the other methods 16× running time, though we don’t reboot them if they terminate earlier based on their stopping criteria."))
- **c6** Ablation (SATLIB validation set, single-threaded): Basic, Basic+Tree, no local search and no reduction variants are compared, and the authors state that all components contribute to the results.([Results, p.8](https://arxiv.org/pdf/1810.10659v1#page=8 "This experiment demonstrates that all components presented in this paper contribute to the results."))
- **c7** Generalization claim (Li et al.'s own reading of their MIS/MVC results on SNAP and citation graphs; see notes for the re-evaluation arxiv-2201.10494): the authors state the approach generalizes from synthetic to real graphs, from SAT graphs to social networks, and from about 1,000-node to about 100,000-node graphs; they add ReduMIS works as well, presumably because both find optimal solutions on those graphs.([Results, p.8](https://arxiv.org/pdf/1810.10659v1#page=8 "In particular, it generalizes from synthetic graphs to real ones, from SAT graphs to real-world social networks, and from graphs with roughly 1,000 to graphs with roughly 100,000 nodes and more than 10 million edges."))

