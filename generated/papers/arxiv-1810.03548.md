<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Meta-Learning: A Survey

- カード: [`arxiv-1810.03548`](../../papers/arxiv-1810.03548.yaml)
- 著者: Joaquin Vanschoren
- 年・掲載: 2018
- 原論文: [PDF](https://arxiv.org/pdf/1810.03548v1)(arXiv v1、カード作成時に読んだ版)
- タグ: automl-systems, meta-learning, model-selection
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Framing: meta-learning observes how different ML approaches perform on a wide range of tasks and learns from this meta-data to learn new tasks faster; the Introduction then categorizes techniques by the type of meta-data they leverage (model evaluations, task properties, prior models).([Abstract, p.1](https://arxiv.org/pdf/1810.03548v1#page=1 "Meta-learning, or learning to learn, is the science of systematically observing how diﬀerent machine learning approaches perform on a wide range of learning tasks, and then learning from this experience, or meta-data, to learn new tasks much faster than otherwise possible."))
- **c2** Caveat (no free lunch): the more similar previous tasks are, the more meta-data can be leveraged, and defining task similarity is called a key overarching challenge; when a new task is unrelated or random noise, leveraging prior experience will not be effective.([Introduction, p.1](https://arxiv.org/pdf/1810.03548v1#page=1 "When a new task represents completely unrelated phenomena, or random noise, leveraging prior experience will not be eﬀective."))
- **c3** Per-set (task-independent) recommendation, as described by the survey with citations to prior work: without evaluations on the new task, a candidate set of configurations (a portfolio) is evaluated on many prior tasks, ranked per task and aggregated into a global ranking (e.g. average rank, citing Lin 2010 and Abdulrahman et al. 2018); a simple anytime method (citing Brazdil et al. 2003a) then evaluates the top-K on the new task in turn.([Task-Independent Recommendations, p.2](https://arxiv.org/pdf/1810.03548v1#page=2 "This is typically done by discretizing Θ into a set of candidate conﬁgurations θi, also called a portfolio, evaluated on a large number of tasks tj."))
- **c4** Meta-feature caveat (citing Bilalli et al., 2017): studies on OpenML meta-data showed the optimal set of meta-features depends on the application; meta-features need aggregation, normalization and feature selection or dimensionality reduction when computing task similarity.([Meta-Features, p.8](https://arxiv.org/pdf/1810.03548v1#page=8 "Studies on OpenML meta-data have shown that the optimal set of meta-features depends on the application (Bilalli et al., 2017)."))
- **c5** Meta-models for algorithm selection (prior work, citing Kalousis and Hilario 2001 and Kopf and Iglezakis 2002): those experiments showed boosted and bagged trees often gave the best meta-model predictions, although much depends on the exact meta-features used.([Meta-Models, p.10](https://arxiv.org/pdf/1810.03548v1#page=10 "Experiments showed that boosted and bagged trees often yielded the best predictions, although much depends on the exact meta-features used"))
- **c6** Meta-features versus observations on the new task: the survey states (citing Feurer et al. 2018b, Wistuba et al. 2018, Leite et al. 2012) that, rather than combining per-task predictions by meta-feature similarity, it is ultimately more effective to gather new evaluations on the new task, which refine the task-similarity estimates.([Performance Prediction, p.11](https://arxiv.org/pdf/1810.03548v1#page=11 "While meta-features could also be used to combine per-task predictions based on task similarity, it is ultimately more eﬀective to gather new observations Pi,new, since these allow to reﬁne the task similarity estimates with every new observation"))

