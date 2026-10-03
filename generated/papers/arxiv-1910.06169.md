<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# The PGM-index: a multicriteria, compressed and learned approach to data indexing

- カード: [`arxiv-1910.06169`](../../papers/arxiv-1910.06169.yaml)
- 著者: Paolo Ferragina, Giorgio Vinciguerra
- 年・掲載: 2019
- 原論文: [PDF](https://arxiv.org/pdf/1910.06169v1)(arXiv v1、カード作成時に読んだ版)
- タグ: learned-indexes, linear-models
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Critique of prior learned indexes (attributed to these authors): they describe earlier learned indexes as heuristic and lacking guarantees on time and space.([Abstract, p.1](https://arxiv.org/pdf/1910.06169v1#page=1 "However, these novel approaches are based on heuristics, thus they lack any guarantees both in their time and space requirements."))
- **c2** Relation to binary search: the epsilon-approximate positions from the optimal piecewise linear model are turned into exact positions by binary search within +-epsilon keys, so this step costs time logarithmic in epsilon rather than in the array size.([The PGM-index, p.3](https://arxiv.org/pdf/1910.06169v1#page=3 "can be turned into exact positions via a binary search within a range of ±ε keys in A, thus taking time logarithmic in the parameter ε, not in the size of A."))
- **c3** Guarantee: citing a known external-memory lower bound for predecessor search, the authors state the PGM-index solves the fully indexable dictionary problem I/O-optimally (Theorem 1: Theta(m) space, O(log m) time and O((log_c m) log(epsilon/B)) I/Os, for fixed integer epsilon >= 1, fan-out c >= 2epsilon and block size B of the External Memory model, m = minimum number of epsilon-approximate segments); they also state it cannot be asymptotically worse in space and time than a 2epsilon-way tree such as a FITing-tree, B+-tree or CSS-tree. These are theoretical bounds, separate from the experiments.([The PGM-index, p.6](https://arxiv.org/pdf/1910.06169v1#page=6 "According to the lower bound proved by [30], we can state that the PGM-index solves I/O-optimally the fully indexable dictionary problem with predecessor search, meaning that it can potentially replace any existing index with virtually no performance degradation."))
- **c4** Main empirical claim: the PGM-index improves the space of the FITing-tree (described as the best known learned index) by 63.3% and of the B-tree by more than four orders of magnitude, with the same or better query time (the abstract's continuation).([Abstract, p.1](https://arxiv.org/pdf/1910.06169v1#page=1 "We show experimentally that the PGM-index improves the space of the best known learned index, i.e. FITing-tree, by 63.3% and of the B-tree by more than four orders of magnitude"))
- **c5** Evaluation protocol: three real datasets (Web logs, about 715M timestamps; Longitude, about 166M OpenStreetMap points; IoT, about 26M timestamps) plus synthetic uniform, Zipf and lognormal datasets; query experiments use the Web logs dataset with 8-byte keys and 128-byte payloads and 10M randomly generated queries. CSS-tree is the authors' own implementation and the B+-tree a well-known library.([Experiments, p.8](https://arxiv.org/pdf/1910.06169v1#page=8 "We used the following three standard datasets, each having diﬀerent data distributions, regularities and patterns:"))
- **c6** Comparison with RMI (Kraska et al.): the authors report that the PGM-index dominates a 2-stage RMI (which they describe as using a combination of linear and other models) and argue it has better latency guarantees; the text does not say whose RMI implementation was used or how it was tuned beyond varying second-stage sizes (searched 'RMI' and 'implementation').([Query performance of the PGM-index, p.10](https://arxiv.org/pdf/1910.06169v1#page=10 "Figure 6 shows that the PGM-index dominates RMI, it has indeed better latency guarantees"))
- **c7** Limitation: insertions and deletions are not evaluated in this version; the authors list experimenting with insertion and deletion performance as a research direction.([Conclusions and future work, p.12](https://arxiv.org/pdf/1910.06169v1#page=12 "A possible research direction is to experiment with the performance of insertion and deletion of keys in a PGM-index."))

