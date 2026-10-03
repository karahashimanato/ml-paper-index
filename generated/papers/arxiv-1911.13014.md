<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# SOSD: A Benchmark for Learned Indexes

- カード: [`arxiv-1911.13014`](../../papers/arxiv-1911.13014.yaml)
- 著者: Andreas Kipf, Ryan Marcus, Alexander van Renen, Mihail Stoian, Alfons Kemper, Tim Kraska, Thomas Neumann
- 年・掲載: 2019
- 原論文: [PDF](https://arxiv.org/pdf/1911.13014v1)(arXiv v1、カード作成時に読んだ版)
- タグ: efficiency-evaluation, learned-indexes, linear-models
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Critique of earlier evaluation (attributed): the original learned index paper lacked an open-source implementation, which left many in the community skeptical that learned models could beat optimized in-memory data structures.([Introduction, p.1](https://arxiv.org/pdf/1911.13014v1#page=1 "However, [14] lacked an open-source implementation and thus left many in the community skeptical that learned models could outperform optimized in-memory data structures [11, 15]."))
- **c2** Proposal: SOSD, a framework for comparing new (learned) index structures on both synthetic and real-world datasets, released as open-source code with highly optimized baselines; the authors state it includes the first performant public RMI implementation (a new implementation, not the one used in the original paper).([Introduction, p.1](https://arxiv.org/pdf/1911.13014v1#page=1 "Thus, we introduce the Search On Sorted Data Benchmark (SOSD), a framework that allows researchers to compare their new (learned) index structures on both synthetic and real-world datasets."))
- **c3** Datasets: eight datasets of 200M 64-bit unsigned integer keys; amzn (book sale popularity), face (upsampled Facebook user IDs), osmc (OpenStreetMap locations as S2 CellIds) and wiki (edit timestamps) are real-derived, while logn, norm, uden (dense) and uspr (uniform sparse) are synthetic; 32-bit versions exist for all except osmc and wiki.([Search on Sorted Data Benchmark, p.3](https://arxiv.org/pdf/1911.13014v1#page=3 "SOSD currently includes eight different datasets."))
- **c4** Query protocol: 10M equality lookups with keys drawn uniformly from the stored keys, hashing excluded to support range-based (lower bound) lookups, at most 100 matches per key, executed one at a time in a single thread on an AWS c5.4xlarge machine.([Search on Sorted Data Benchmark, p.3](https://arxiv.org/pdf/1911.13014v1#page=3 "Lookups are performed one-at-a-time in a single thread."))
- **c5** Main empirical claim (preliminary, on SOSD's tested datasets): the CDF approximators RMI and RadixSpline both have very low lookup latencies, which the authors attribute to fitting a model to the data distribution; B-tree, binary search and FAST are hardly affected by the data distribution while interpolation search is heavily affected by skew.([Results, p.3](https://arxiv.org/pdf/1911.13014v1#page=3 "The CDF approximators RMI and RadixSpline both have very low lookup latencies, highlighting the beneﬁt learned index structures receive from ﬁtting a model to the data distribution."))
- **c6** Tuning caveat: both RMI and RadixSpline require dataset-specific tuning, and the authors recommend them only if users can afford this step (if users cannot afford the training time, they recommend ART or FAST for 32-bit keys and ART or RBS for 64-bit keys).([Takeaways, p.4](https://arxiv.org/pdf/1911.13014v1#page=4 "Otherwise, the optimal search strategy depends on whether a user can afford to manually tune and ﬁt a CDF model, as both RMI and RS require dataset-speciﬁc tuning."))
- **c7** Limitation: learned indexes currently lack support for efficient updates; the authors note that several benchmarked non-learned methods (e.g. RBS, FAST) also lack efficient updates, and SOSD does not yet measure updates or multi-threaded lookups.([Takeaways, p.4](https://arxiv.org/pdf/1911.13014v1#page=4 "A current drawback of learned indexes is the lack of support for efﬁcient updates, an arguably important feature for index structures."))

