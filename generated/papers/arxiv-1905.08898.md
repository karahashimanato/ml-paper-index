<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# ALEX: An Updatable Adaptive Learned Index

- カード: [`arxiv-1905.08898`](../../papers/arxiv-1905.08898.yaml)
- 著者: Jialin Ding, Umar Farooq Minhas, Jia Yu, Chi Wang, Jaeyoung Do, Yinan Li, Hantian Zhang, Badrish Chandramouli, Johannes Gehrke, Donald Kossmann, David Lomet, Tim Kraska
- 年・掲載: 2019
- 原論文: [PDF](https://arxiv.org/pdf/1905.08898v2)(arXiv v2、カード作成時に読んだ版)
- タグ: learned-indexes, linear-models
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Relation to B+Trees: like a B+Tree, ALEX builds a tree, but lets different nodes grow and shrink at different rates; data nodes use a Gapped Array so that gaps absorb inserts and records can be placed near their predicted positions.([Introduction, p.1](https://arxiv.org/pdf/1905.08898v2#page=1 "Similar to a B+Tree, ALEX builds a tree, but allows diﬀerent nodes to grow and shrink at diﬀerent rates."))
- **c2** Critique of prior work (attributed): the authors characterize the original Learned Index of Kraska et al. as limited to static, read-only workloads.([Abstract, p.1](https://arxiv.org/pdf/1905.08898v2#page=1 "However, it is limited to static, read-only workloads."))
- **c3** Main empirical claim (abstract, for the authors' evaluated datasets and workloads): across the spectrum of read-write workloads ALEX beats B+Trees by up to 4.1x while never performing worse, with up to 2000x smaller index size.([Abstract, p.1](https://arxiv.org/pdf/1905.08898v2#page=1 "Across the spectrum of read-write workloads, ALEX beats B+Trees by up to 4.1× while never performing worse, with up to 2000× smaller index size."))
- **c4** Guarantee and its scope: Theorem 5.1 bounds RMI depth by the density of the densest subregion of the key space (B+Trees bound depth by the number of keys) (m = max node size, p = minimum number of equal-width partitions each holding at most m*d_u keys), and maximal depth can be maintained under inserts; the authors add that this analysis gives intuition about RMI depth but does not reflect worst-case guarantees in practice.([Bound on RMI depth, p.8](https://arxiv.org/pdf/1905.08898v2#page=8 "We can construct an RMI that satisﬁes the max node size and upper density limit constraints whose depth is no larger than ⌈logmp⌉—we call this the maximal depth."))
- **c5** Baseline tuning: for each dataset and workload, grid search tunes the page size of B+Tree and Model B+Tree and the number of models of the Learned Index for best throughput, whereas ALEX itself is not tuned (unless users add constraints). The B+Tree is the STX B+Tree and the Learned Index is the authors' best-effort reimplementation (two-level RMI, linear models, binary search).([Experimental Setup, p.9](https://arxiv.org/pdf/1905.08898v2#page=9 "For each dataset and workload, we use grid search to tune the page size for B+Tree and Model B+Tree and the number of models for Learned Index to achieve the best throughput."))
- **c6** Reimplementation detail (attributed): in private communication the authors of the original Learned Index told the ALEX authors that a neural-net root model usually does not justify its added complexity given minor performance gains, which the ALEX authors say they verified independently.([Experimental Setup, p.9](https://arxiv.org/pdf/1905.08898v2#page=9 "Inprivatecommunicationwiththeauthorsof[19], welearnedthattheadded complexity of using a neural net for the root model usually is not justiﬁed by theresultingminorperformancegains, whichwealsoindependentlyveriﬁed."))
- **c7** Limitations / future work stated: open theoretical problems about ALEX performance, support for secondary storage for larger-than-memory datasets, and concurrency control tailored to ALEX.([Conclusion, p.14](https://arxiv.org/pdf/1905.08898v2#page=14 "We intend to pursue open theoretical problems about ALEX performance, supporting secondary storage for larger than memory datasets, and new concurrency control techniques tailored to the ALEX design."))

