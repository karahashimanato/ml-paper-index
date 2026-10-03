<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Value Iteration Networks

- カード: [`arxiv-1602.02867`](../../papers/arxiv-1602.02867.yaml)
- 著者: Aviv Tamar, Yi Wu, Garrett Thomas, Sergey Levine, Pieter Abbeel
- 年・掲載: 2016
- 原論文: [PDF](https://arxiv.org/pdf/1602.02867v4)(arXiv v4、カード作成時に読んだ版)
- タグ: algorithm-learning, deep-learning, dynamic-programming, reinforcement-learning, supervised
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Contribution: a neural network with an embedded planning module, based on a differentiable approximation of value iteration that is represented as a CNN and trained end-to-end by backpropagation.([Abstract, p.1](https://arxiv.org/pdf/1602.02867v4#page=1 "Key to our approach is a novel differentiable approximation of the value-iteration algorithm, which can be represented as a convolutional neural network, and trained end-to-end using standard backpropagation."))
- **c2** How VI is embedded: one VI iteration is seen as a convolution layer (each channel a per-action Q function, kernel weights the discounted transition probabilities) followed by max-pooling over actions; recurrently applying it K times performs K VI iterations on a planning MDP whose reward and transitions are learned from the observation.([The Value Iteration Network Model, p.4](https://arxiv.org/pdf/1602.02867v4#page=4 "Thus by recurrently applying a convolution layer K times, K iterations of VI are effectively performed."))
- **c3** Guarantees: the planning MDP is not assumed known and its learned rewards/transitions need not match the true task; the authors describe the VI module only as an architecture capable of approximate VI (the convergence of exact VI to V* is cited in the background, not claimed for VIN).([The Value Iteration Network Model, p.4](https://arxiv.org/pdf/1602.02867v4#page=4 "The VI module is simply a NN architecture that has the capability of performing an approximate VI computation."))
- **c4** Generalization claim (authors' abstract): learning an explicit planning computation makes VIN policies generalize better to new, unseen domains. In the grid-world, 'unseen domains' are new random maps (obstacles, goal, start) of the same size as in training, evaluated per size (8x8, 16x16, 28x28, K set per size); in continuous control, 40 test instances from the same distribution as the 200 training instances. No evaluation on grids larger than those trained on was found.([Abstract, p.1](https://arxiv.org/pdf/1602.02867v4#page=1 "We show that by learning an explicit planning computation, VIN policies generalize better to new, unseen domains."))
- **c5** Protocol (grid-world): policies are trained by imitation learning on random grid-worlds (5000 instances with 7 shortest-path trajectories each per the appendix) and evaluated on a held-out test set of maps with random obstacles, goals and start states, separately for 8x8, 16x16 and 28x28 sizes (K set per size); baselines are a DQN-inspired CNN and an FCN; metrics are 0-1 action prediction loss, trajectory success rate and path-length difference to the optimal trajectory.([Experiments, p.5](https://arxiv.org/pdf/1602.02867v4#page=5 "In Table 1 we present the average 0 −1 prediction loss of each model, evaluated on a held-out test-set of maps with random obstacles, goals, and initial states, for different problem sizes."))
- **c6** Finding on reactive baselines: their prediction loss is comparable to VIN's while their success rate is much worse, which the authors interpret as VIN focusing errors on less important parts of the trajectory rather than ordinary over- or underfitting.([Experiments, p.6](https://arxiv.org/pdf/1602.02867v4#page=6 "Importantly, note that the prediction loss for the reactive policies is comparable to the VINs, although their success rate is signiﬁcantly worse."))
- **c7** Ablation and limitation of the planning prior: untying the weights of the K recurrent layers degrades performance, more so with less training data; in WebNav, VIN was only mildly better than the reactive baseline when starting from the root node (the authors conclude a reactive policy is sufficient there) and significantly better when starting from a random position in the graph.([Experiments, p.6](https://arxiv.org/pdf/1602.02867v4#page=6 "Our results, reported in the supplementary material, show that untying the weights degrades performance, with a stronger effect for smaller sizes of training data."))

