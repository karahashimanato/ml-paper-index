<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Generalize a Small Pre-trained Model to Arbitrarily Large TSP Instances

- カード: [`arxiv-2012.10658`](../../papers/arxiv-2012.10658.yaml)
- 著者: Zhang-Hua Fu, Kai-Bin Qiu, Hongyuan Zha
- 年・掲載: 2020
- 原論文: [PDF](https://arxiv.org/pdf/2012.10658v2)(arXiv v2、カード作成時に読んだ版)
- タグ: combinatorial-optimization, deep-learning, divide-and-conquer, graph-neural-networks, local-search, reinforcement-learning, supervised
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Proposal: train a small fixed-size model in a supervised way and reuse it repeatedly to build heat maps for TSP instances of arbitrary size via graph sampling, graph converting and heat-map merging, aimed at the lack of size generalization of supervised TSP models.([Abstract, p.1](https://arxiv.org/pdf/2012.10658v2#page=1 "this paper tries to train (in supervised manner) a small-scale model, which could be repetitively used to build heat maps for TSP instances of arbitrarily large size, based on a series of techniques such as graph sampling, graph converting and heat maps merging."))
- **c2** The division is not learned: sub-graphs of exactly m vertices are extracted by repeatedly taking the least-covered vertex as a centre and its k nearest neighbours (sub-graphs may overlap); only the sub heat-map predictor is learned, and merging uses a fixed formula over the sub-graphs containing each edge.([Building and merging heat maps, p.3](https://arxiv.org/pdf/2012.10658v2#page=3 "use the k-nearest neighbors algorithm [10] to extract a sub-graph G′ which consists of exactly m vertices (including the clustering center)."))
- **c3** Relation to local search: the search operates on complete tours, and every action is a k-opt move that deletes k edges and adds k new ones; 2-opt improvements are applied first, then MCTS samples larger k-opt moves guided by the heat map.([Reinforcement learning for solutions optimization, p.4](https://arxiv.org/pdf/2012.10658v2#page=4 "Since each TSP solution consists of a subset of n edges, any action could be viewed as a k-opt (2 ≤k ≤n) transformation, which deletes k edges at ﬁrst, and then adds k different edges to form a new tour."))
- **c4** Baseline protocol: learning-based baselines were not retrained; their public source code and pre-trained models were downloaded and rerun (some baselines' parameters such as beam width were adapted to prolong running time).([Experiments, p.5](https://arxiv.org/pdf/2012.10658v2#page=5 "Notice that, for the baselines, we just directly download and rerun the source codes, based on the pre-trained models (only for learning based baselines) which are publicly available."))
- **c5** Hardware asymmetry and scope: learning-based methods run on one GTX 1080 Ti GPU, while Concorde, Gurobi and LKH3 run on an 8-core CPU and are listed for indicative purposes only; the authors do not aim to strictly outperform the non-learning algorithms.([Experiments, p.5](https://arxiv.org/pdf/2012.10658v2#page=5 "Notice that our method is a learning based algorithm, thus we do not aim to strictly outperform the non-learning algorithms."))
- **c6** Main empirical claim: on instances with up to 10,000 vertices the approach is reported to clearly outperform existing machine-learning TSP algorithms and to significantly improve the trained model's generalization (the learning baselines were rerun from their public pre-trained models on the same GPU; the non-learning solvers Concorde, Gurobi and LKH3 are listed only as indicative CPU references).([Abstract, p.1](https://arxiv.org/pdf/2012.10658v2#page=1 "Experimental results based on a large number of instances (with up to 10,000 vertices) show that, this new approach clearly outperforms the existing machine learning based TSP algorithms, and signiﬁcantly improves the generalization ability of the trained model."))
- **c7** Copied baseline numbers: two MCTS-based TSP methods ([36] Shimomura and Takashima; [43] Xing and Tu) could not be rerun because their code is not publicly available; for [43] the authors compare against the average gaps that paper reports, evaluated on different platforms, and describe their method as roughly producing overall better results within reasonable time.([Results on data set 2, p.6](https://arxiv.org/pdf/2012.10658v2#page=6 "The source codes of these two papers are both not publicly available, thus we cannot evaluate them uniformly on the same platform to make strictly fair comparisons."))

