<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Soft-DTW: a Differentiable Loss Function for Time-Series

- カード: [`arxiv-1703.01541`](../../papers/arxiv-1703.01541.yaml)
- 著者: Marco Cuturi, Mathieu Blondel
- 年・掲載: 2017
- 原論文: [PDF](https://arxiv.org/pdf/1703.01541v2)(arXiv v2、カード作成時に読んだ版)
- タグ: deep-learning, dynamic-programming, supervised, time-series-classification, time-series-forecasting, unsupervised
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Contribution: a differentiable loss between time series built on DTW, using a smoothed formulation (soft-DTW) that takes the soft-minimum over the costs of all alignments rather than the minimum.([Abstract, p.1](https://arxiv.org/pdf/1703.01541v2#page=1 "Our work takes advantage of a smoothed formulation of DTW, called soft-DTW, that computes the soft-minimum of all alignment costs."))
- **c2** Relation to the DP: soft-DTW is computed by a minor modification of Bellman's recursion for DTW (all (min, +) operations replaced by (+, x); the authors attribute such smoothed modifications of Bellman's recursion to prior work on smoothed DP distances and kernels), even though it considers all alignments instead of only the optimal one; setting gamma = 0 recovers the original DTW.([Introduction, p.2](https://arxiv.org/pdf/1703.01541v2#page=2 "Despite considering all alignments and not just the optimal one, soft-DTW can be computed with a minor modification of Bellman’s recursion, in which all (min, +) operations are replaced with (+, ×)."))
- **c3** Complexity: value and gradient of soft-DTW are computed in quadratic time and space; the authors contrast this with DTW's quadratic time but linear space (the gradient's backward pass needs the full matrix of intermediate costs, while the naive recursion for the expected alignment would be quartic).([Abstract, p.1](https://arxiv.org/pdf/1703.01541v2#page=1 "We show in this paper that soft-DTW is a differentiable loss function, and that both its value and gradient can be computed with quadratic time/space complexity (DTW has quadratic time but linear space complexity)."))
- **c4** What hard DTW lacks: the gradient of hard DTW (the optimal alignment) is defined almost everywhere for continuous data but is discontinuous where a small change switches the optimal alignment, which the authors say is likely to hamper gradient descent.([The DTW and soft-DTW loss functions, p.3](https://arxiv.org/pdf/1703.01541v2#page=3 "However, that gradient, when it exists, will be discontinuous around those values x where a small change in x causes a change in A⋆, which is likely to hamper the performance of gradient descent methods."))
- **c5** No optimality guarantee: the soft-DTW barycenter objective is non-convex (a soft minimum of convex functions for squared Euclidean cost), so the authors state that barycenter computations come with no way of ensuring optimality; they argue informally that smoothing gives a better (though slightly different from DTW) optimization landscape.([Learning with the soft-DTW loss, p.5](https://arxiv.org/pdf/1703.01541v2#page=5 "all of the computations involving barycenters should be taken with a grain of salt, since we have no way of ensuring optimality when approximating Eq. (4)."))
- **c6** Protocol: experiments use a 79-dataset subset of the UCR time series classification archive; barycenters (10 series of a random class, 10 repetitions, at most 100 iterations, L-BFGS) and k-means are compared with DBA and a subgradient method in terms of the hard DTW loss; nearest-centroid classification uses a 50/25/25 train/validation/test split with gamma chosen from 15 log-spaced values; multistep-ahead prediction uses an MLP with one hidden layer predicting the last 40% of each series.([Experimental results, p.6](https://arxiv.org/pdf/1703.01541v2#page=6 "We use a subset containing 79 datasets encompassing a wide variety of fields (astronomy, geology, medical imaging) and lengths."))
- **c7** Trade-off of the training loss: in the prediction experiment, training with soft-DTW gives lower DTW loss and training with the Euclidean loss gives lower Euclidean loss; the authors argue that DTW-robust errors may be the more judicious choice for many applications.([Experimental results, p.8](https://arxiv.org/pdf/1703.01541v2#page=8 "Unsurprisingly, we achieve lower DTW loss when training with the soft-DTW loss, and lower Euclidean loss when training with the Euclidean loss."))

