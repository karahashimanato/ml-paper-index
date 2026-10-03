<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Fast Differentiable Sorting and Ranking

- カード: [`arxiv-2002.08871`](../../papers/arxiv-2002.08871.yaml)
- 著者: Mathieu Blondel, Olivier Teboul, Quentin Berthet, Josip Djolonga
- 年・掲載: 2020
- 原論文: [PDF](https://arxiv.org/pdf/2002.08871v2)(arXiv v2、カード作成時に読んだ版)
- タグ: deep-learning, differentiable-sorting, image-classification, linear-models, supervised, tabular-regression
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Problem statement: sorting is piecewise linear (differentiable almost everywhere but with many kinks), while ranking is piecewise constant, so its derivatives are null or undefined and block backpropagation.([Introduction, p.1](https://arxiv.org/pdf/2002.08871v2#page=1 "As piecewise constant functions, ranks are unfortunately much more problematic than sorting: their derivatives are null or undeﬁned, preventing gradient backpropagation."))
- **c2** Contribution and stated complexity: the paper claims the first differentiable sorting and ranking operators with O(n log n) time and O(n) space complexity, and says prior differentiable proxies do not achieve O(n log n).([Abstract, p.1](https://arxiv.org/pdf/2002.08871v2#page=1 "In this paper, we propose the ﬁrst differentiable sorting and ranking operators with O(n log n) time and O(n) space complexity."))
- **c3** Relaxation used: sorting and ranking are written as linear programs over the permutahedron (convex hull of permutations); adding strongly convex regularization turns them into projections, which reduce to isotonic optimization.([Abstract, p.1](https://arxiv.org/pdf/2002.08871v2#page=1 "We achieve this feat by constructing differentiable operators as projections onto the permutahedron, the convex hull of permutations, and using a reduction to isotonic optimization."))
- **c4** Exactness and where the O(n log n) comes from: the isotonic subproblems are solved exactly by pool adjacent violators in O(n) time, so no iteration count or precision level must be chosen (unlike Sinkhorn); the overall O(n log n) is due to first sorting the input vector, which the projection requires.([Fast computation and differentiation, p.5](https://arxiv.org/pdf/2002.08871v2#page=5 "This means that we do not need to choose a number of iterations or a level of precision, unlike with Sinkhorn."))
- **c5** Comparison with prior relaxations as stated by this paper: Taylor et al. take O(n^3), Qin et al. O(n^2) (refined by Grover et al. with unimodal row-stochastic matrices), and Cuturi et al.'s optimal transport method differentiates through Sinkhorn iterates at O(Tmn) cost, where T is the number of Sinkhorn iterations and m a hyperparameter trading cost for precision (Blondel et al. state that convergence to hard sort/ranks is only guaranteed if m = n).([Introduction, p.1](https://arxiv.org/pdf/2002.08871v2#page=1 "Their method is based on differentiating through the iterates of the Sinkhorn algorithm (Sinkhorn & Knopp, 1967) and costs O(Tmn) time, where T is the number of Sinkhorn iterations"))
- **c6** Top-k classification (reproducing Cuturi et al.'s CIFAR-10/CIFAR-100 experiment with the same vanilla CNN, Adam step 1e-4, k = 1, 12 runs): the proposed soft ranks reach accuracy comparable to the OT formulation while being significantly faster.([Experiments (Top-k classification loss function), p.6](https://arxiv.org/pdf/2002.08871v2#page=6 "On both CIFAR-10 and CIFAR-100, our soft rank formulations achieve comparable accuracy to the OT formulation, though signiﬁcantly faster, as we elaborate below."))
- **c7** Caveat on runtime: in the 600-epoch CIFAR-100 training, the proposed operators were faster than OT but slower than the O(n^2) All-pairs baseline, which the authors attribute to All-pairs being efficient on GPU at n = 100 while their PAV implementation runs on CPU.([Experiments (Top-k classification loss function), p.7](https://arxiv.org/pdf/2002.08871v2#page=7 "While our soft operators are several hours faster than OT, they are slower than All-pairs, despite its O(n2) complexity."))

