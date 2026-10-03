<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Modern graph neural networks do worse than classical greedy algorithms in solving combinatorial optimization problems like maximum independent set

- カード: [`arxiv-2206.13211`](../../papers/arxiv-2206.13211.yaml)
- 著者: Maria Chiara Angelini, Federico Ricci-Tersenghi
- 年・掲載: 2022
- 原論文: [PDF](https://arxiv.org/pdf/2206.13211v2)(arXiv v2、カード作成時に読んだ版)
- タグ: combinatorial-optimization, graph-neural-networks, greedy-methods, unsupervised
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Paper evaluated: the comment targets the physics-inspired unsupervised GNN of Schuetz, Brubaker and Katzgraber ('Combinatorial Optimization with Physics-Inspired Graph Neural Networks', Nat Mach Intell 2022), which was tested on maximum cut and MIS on sparse graphs.([Introduction, p.1](https://arxiv.org/pdf/2206.13211v2#page=1 "The recent work “Combinatorial Optimization with Physics-Inspired Graph Neural Networks” [Nat Mach Intell 4 (2022) 367] introduces a physics-inspired unsupervised Graph Neural Network (GNN) to solve combinatorial optimization problems on sparse graphs."))
- **c2** Main claim (instance setting: MIS on random regular graphs of fixed degree d, with d = 3 and 5 in Fig. 1): a simple greedy algorithm running in almost linear time finds MIS solutions of much better quality than the Schuetz et al. GNN in a much shorter time; the GNN numbers are taken from the original paper, not re-run.([Introduction, p.1](https://arxiv.org/pdf/2206.13211v2#page=1 "In this comment, we show that a simple greedy algorithm, running in almost linear time, can ﬁnd solutions for the MIS problem of much better quality than the GNN in a much shorter time."))
- **c3** Instance setting: the comparison is on d-regular random graphs with d = 3 and 5; the greedy baseline (DGA) repeatedly picks a node of smallest degree in the residual graph; quality is reported as approximation ratio to the current best theoretical upper bounds, which the authors note are likely not strict.([Comparison with simple greedy algorithms, p.2](https://arxiv.org/pdf/2206.13211v2#page=2 "In Fig. 1 we compare the performances of the GNN of Ref. [4] (empty symbols) and DGA (full symbols) in ﬁnding MIS on d-RRG with d = 3, 5."))
- **c4** Critique of the original baselines: according to the comment, Schuetz et al. compared only against the Boppana-Halldorsson approximation algorithm, while many faster MIS algorithms exist.([Introduction, p.2](https://arxiv.org/pdf/2206.13211v2#page=2 "The authors of Ref. [4] consider only the Boppana-Halldorsson (BH) approximated algorithm [8]"))
- **c5** Run-time comparison caveat: DGA times were measured on a 2.3 GHz MacBook Pro, while GNN times were extracted from Fig. 5 of the original paper and include post-processing, since the original authors give no per-step timing; the commenters argue the post-processing (checking the output is an IS) should be linear in n, so most of that time should be GNN computation.([Comparison with simple greedy algorithms, p.2](https://arxiv.org/pdf/2206.13211v2#page=2 "The latter correspond to the aggregated run-time that includes the post-processing, because the authors furnish no additional information on the time needed for the diﬀerent steps of the computation."))
- **c6** Recommendation: such a simple greedy algorithm should be considered a minimal benchmark that any new algorithm must beat to be taken seriously.([Discussion, p.3](https://arxiv.org/pdf/2206.13211v2#page=3 "We have reported in detail the performances of DGA because we believe that such a simple greedy algorithm should be considered as a minimal benchmark and any new algorithm must perform at least better than DGA to be taken into serious consideration."))
- **c7** Benchmark hardness: the authors argue MIS on d-regular random graphs (d-RRG) with d < 16 is likely easy (citing a statistical-physics study of the independent-set space) and propose d > 16 as a harder benchmark, starting from results in their earlier work for d = 20 and d = 100.([Discussion, p.3](https://arxiv.org/pdf/2206.13211v2#page=3 "So, a possible answer to the fundamental question above is to study MIS on d-RRG with d > 16."))

