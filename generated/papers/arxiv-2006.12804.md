<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Benchmarking Learned Indexes

- カード: [`arxiv-2006.12804`](../../papers/arxiv-2006.12804.yaml)
- 著者: Ryan Marcus, Andreas Kipf, Alexander van Renen, Mihail Stoian, Sanchit Misra, Alfons Kemper, Thomas Neumann, Tim Kraska
- 年・掲載: 2020
- 原論文: [PDF](https://arxiv.org/pdf/2006.12804v2)(arXiv v2、カード作成時に読んだ版)
- タグ: efficiency-evaluation, learned-indexes, linear-models
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Critique of earlier evaluations: the authors summarize criticisms of learned indexes as stemming from the lack of an efficient open-source implementation, inadequate datasets, and no standardized benchmark for fair comparison.([Introduction, p.1](https://arxiv.org/pdf/2006.12804v2#page=1 "The main reasons for these criticisms were the lack of an eﬃcient open-source implementation of the learned index structure, inadequate data-sets, and the lack of a standardized benchmark suite to ensure a fair comparison between the diﬀerent approaches."))
- **c2** Weak-baseline risk: because researchers had to re-implement the original learned index (or use back-of-the-envelope calculations), the authors say it is easy to leave baselines unoptimized or make unrealistic assumptions, potentially voiding the main takeaways.([Introduction, p.1](https://arxiv.org/pdf/2006.12804v2#page=1 "While not a bad thing per se, it is easy to leave the baseline unoptimized, or make other unrealistic assumptions, even with the best of intentions, potentially rendering the main takeaways void."))
- **c3** Synthetic-data critique: learned structures have an 'unfair' advantage on synthetic datasets because these are often surprisingly easy to learn; the benchmark therefore uses only four real-world datasets (amzn, face, osm, wiki; 200M 64-bit keys each).([Introduction, p.1](https://arxiv.org/pdf/2006.12804v2#page=1 "Further complicating matters, learned structures have an “unfair” advantage on synthetic datasets, as synthetic datasets are often surprisingly easy to learn."))
- **c4** Re-evaluation of the PGM-index paper: contrary to that paper's claim that the PGM-index dominates RMI, the authors found PGM significantly slower than RMI on 3 of the 4 datasets and slightly slower on osm.([Pareto analysis, p.6](https://arxiv.org/pdf/2006.12804v2#page=6 "Indeed, in our experimental evaluation we found that the PGM index performs signiﬁcantly worse than RMI on 3 out of the 4 datasets and slightly worse on osm."))
- **c5** Stated cause of the disagreement: after contacting the PGM authors, they report the PGM paper's RMI implementation used only linear models instead of tuning model types and omitted some optimizations for linear-only RMIs; they stress theirs is the first comparison of RMI and PGM implementations each tuned by their own authors.([Pareto analysis, p.6](https://arxiv.org/pdf/2006.12804v2#page=6 "After contacting the authors of [13], we found that their RMI implementation was missing several key optimizations: their RMI only used linear models rather than tuning diﬀerent type of models as proposed in [19,22], and omitted some optimizations for RMIs with only linear models."))
- **c6** Tuning protocol: implementations tuned by each structure's original authors are used; RMIs are tuned with the CDFShop optimizer, RS and PGM by varying the model error tolerance, and tree structures' size/accuracy trade-off is varied by inserting a subset of keys (a simple technique the authors note may not be ideal for each tree).([Setup, p.5](https://arxiv.org/pdf/2006.12804v2#page=5 "We use implementations tuned by each structure’s original authors."))
- **c7** Limitations: only read-only workloads were studied and each index was tested in isolation in a lookup loop rather than inside a broader application.([Introduction, p.2](https://arxiv.org/pdf/2006.12804v2#page=2 "We focused only on read-only workloads, and we tested each index structure in isolation (e.g., a lookup loop, not with integration into any broader application)."))

