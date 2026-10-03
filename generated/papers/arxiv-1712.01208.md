<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# The Case for Learned Index Structures

- カード: [`arxiv-1712.01208`](../../papers/arxiv-1712.01208.yaml)
- 著者: Tim Kraska, Alex Beutel, Ed H. Chi, Jeffrey Dean, Neoklis Polyzotis
- 年・掲載: 2017
- 原論文: [PDF](https://arxiv.org/pdf/1712.01208v3)(arXiv v3、カード作成時に読んだ版)
- タグ: deep-learning, learned-indexes, linear-models, supervised
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Relation to classical structures: the paper frames existing indexes as models; a B-Tree maps a key to the position of a record in a sorted array, a hash index maps a key to a position in an unsorted array, and a bitmap index indicates whether a record exists.([Abstract, p.1](https://arxiv.org/pdf/1712.01208v3#page=1 "Indexes are models: a B-Tree-Index can be seen as a model to map a key to the position of a record within a sorted array, a Hash-Index as a model to map a key to a position of a record within an unsorted array, and a BitMap-Index as a model to indicate if a data record exists or not."))
- **c2** Main empirical claim (initial results): using neural nets the authors outperform cache-optimized B-Trees by up to 70% in speed while saving an order of magnitude in memory over several real-world data sets.([Abstract, p.1](https://arxiv.org/pdf/1712.01208v3#page=1 "Our initial results show, that by using neural nets we are able to outperform cache-optimized B-Trees by up to 70% in speed while saving an order-of-magnitude in memory over several real-world data sets."))
- **c3** Evaluation protocol (integer datasets): two real-world datasets (Weblogs request timestamps, Maps longitudes) and one synthetic dataset (Lognormal, mu=0, sigma=2) were used; the paragraph describes Weblogs as almost a worst case for learned indexes and all B-Tree experiments use 64-bit keys and 64-bit payloads.([Integer Datasets, p.11](https://arxiv.org/pdf/1712.01208v3#page=11 "For the data we used 2 real-world datasets, (1) Weblogs and (2) Maps [56], and (3) a synthetic dataset, Lognormal."))
- **c4** Baseline implementation and tuning: the B-Tree baseline is a production-quality implementation similar to stx::btree with further cache-line optimization and dense pages; in the same paragraph the 2-stage learned indexes are tuned by simple grid search over neural nets with zero to two hidden layers and widths 4 to 32. B-Tree page size 128 is used as the fixed reference point because it gave the best B-Tree lookup performance.([Integer Datasets, p.11](https://arxiv.org/pdf/1712.01208v3#page=11 "As our baseline, we used a production quality B-Tree implementation which is similar to the stx::btree but with further cache-line optimization, dense pages (i.e., ﬁll factor of 100%), and very competitive performance."))
- **c5** Guarantee (hybrid indexes): replacing last-stage models whose absolute min/max error exceeds a threshold by B-Trees lets the authors bound the worst-case performance of learned indexes to that of B-Trees; for an extremely hard-to-learn distribution the index would become virtually an entire B-Tree.([Hybrid Indexes, p.9](https://arxiv.org/pdf/1712.01208v3#page=9 "Note, that hybrid indexes allow us to bound the worst case performance of learned indexes to the performance of B-Trees."))
- **c6** Theoretical scaling (assumes N i.i.d. keys from a known distribution F): the average error in predicted positions of a constant-sized model grows as O(sqrt(N)), which the authors contrast with the linear scaling of a constant-sized B-Tree; they describe this as preliminary understanding.([Theoretical Analysis of Scaling Learned Range Indexes, p.26](https://arxiv.org/pdf/1712.01208v3#page=26 "Note that this sub-linear scaling in error for a constant-sized model is an improvement over the linear scaling achieved by a constant-sized B-Tree."))
- **c7** Limitations: the evaluation covers read-only analytical workloads, and the authors state that open challenges remain, such as handling write-heavy workloads.([Introduction, p.2](https://arxiv.org/pdf/1712.01208v3#page=2 "However, many open challenges still remain, such as how to handle write-heavy workloads, and we outline many possible directions for future work."))

