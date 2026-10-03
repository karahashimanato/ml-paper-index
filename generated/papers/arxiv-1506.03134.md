<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Pointer Networks

- カード: [`arxiv-1506.03134`](../../papers/arxiv-1506.03134.yaml)
- 著者: Oriol Vinyals, Meire Fortunato, Navdeep Jaitly
- 年・掲載: 2015
- 原論文: [PDF](https://arxiv.org/pdf/1506.03134v2)(arXiv v2、カード作成時に読んだ版)
- タグ: algorithm-learning, deep-learning, supervised
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Contribution: instead of using attention to blend encoder states into a context vector, Ptr-Net uses the attention distribution itself as a pointer that selects an input element as the output, so outputs are positions in the input (e.g. permutations or subsets of the input).([Abstract, p.1](https://arxiv.org/pdf/1506.03134v2#page=1 "It differs from the previous attention attempts in that, instead of using attention to blend hidden units of an encoder to a context vector at each decoder step, it uses attention as a pointer to select a member of the input sequence as the output."))
- **c2** Motivation: problems whose output dictionary size depends on the input length, such as sorting variable-sized sequences and various combinatorial optimization problems, cannot be trivially handled by sequence-to-sequence models or Neural Turing Machines.([Abstract, p.1](https://arxiv.org/pdf/1506.03134v2#page=1 "Problems such as sorting variable sized sequences, and various combinatorial optimization problems belong to this class."))
- **c3** Sorting is not among the evaluated tasks: the paper lists applying Ptr-Net to sorting as future work.([Conclusions, p.8](https://arxiv.org/pdf/1506.03134v2#page=8 "Future work will try and show its applicability to other problems such as sorting where the outputs are chosen from the inputs."))
- **c4** Evaluated tasks: learning approximate solutions, from input-output examples alone, to planar convex hull, Delaunay triangulation and planar symmetric TSP.([Abstract, p.1](https://arxiv.org/pdf/1506.03134v2#page=1 "We show Ptr-Nets can be used to learn approximate solutions to three challenging geometric problems – ﬁnding planar convex hulls, computing Delaunay triangulations, and the planar Travelling Salesman Problem – using training examples alone."))
- **c5** Length generalization (convex hull): a single model trained on lengths 5 to 50 extrapolates to lengths never seen in training (tested up to n = 500), whereas the LSTM baselines must be retrained for each n.([Empirical Results (Convex Hull), p.6](https://arxiv.org/pdf/1506.03134v2#page=6 "More impressive is the fact that the model does extrapolate to lengths that it has never seen during training."))
- **c6** Limitation of length generalization (TSP): trained on optimal tours with 5 to 20 cities, the model is near perfect at n = 25 and good at n = 30 but appears to break at 40 and beyond; the authors contrast this with the factor-of-10 generalization on convex hull and suggest that the underlying algorithms being of far greater complexity than O(n log n) could explain it.([Empirical Results (Travelling Salesman Problem), p.8](https://arxiv.org/pdf/1506.03134v2#page=8 "The results are virtually perfect for n = 25, and good for n = 30, but it seems to break for 40 and beyond (still, the results are far better than chance)."))
- **c7** Evaluation protocol: no extensive architecture or hyperparameter search was done for Ptr-Net; virtually the same architecture was used for all experiments and datasets.([Empirical Results (Architecture and Hyperparameters), p.6](https://arxiv.org/pdf/1506.03134v2#page=6 "No extensive architecture or hyperparameter search of the Ptr-Net was done in the work presented here, and we used virtually the same architecture throughout all the experiments and datasets."))

