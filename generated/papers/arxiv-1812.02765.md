<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Improving Reconstruction Autoencoder Out-of-distribution Detection with Mahalanobis Distance

- カード: [`arxiv-1812.02765`](../../papers/arxiv-1812.02765.yaml)
- 著者: Taylor Denouden, Rick Salay, Krzysztof Czarnecki, Vahdat Abdelzad, Buu Phan, Sachin Vernekar
- 年・掲載: 2018
- 原論文: [PDF](https://arxiv.org/pdf/1812.02765v1)(arXiv v1、カード作成時に読んだ版)
- タグ: anomaly-detection, autoencoders, reconstruction-based-detectors, unsupervised
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Thesis: the authors suggest that reconstruction-based approaches fail to capture anomalies that lie far from known inliers in latent space but near the latent manifold defined by the model, and propose adding the latent Mahalanobis distance; the abstract says this 'often' improves over the baseline.([Abstract, p.1](https://arxiv.org/pdf/1812.02765v1#page=1 "Here we suggest that reconstruction-based approaches fail to capture particular anomalies that lie far from known inlier samples in latent space but near the latent dimension manifold deﬁned by the parameters of the model."))
- **c2** Observed failure: autoencoders sometimes reconstruct OOD samples with less error than many inlier samples, so no threshold can classify those OOD samples correctly while keeping all inliers correct; the authors report observing this for dense and convolutional autoencoders of different depths and hidden-layer sizes, often with OOD samples visibly distinct to humans.([Problem and approach, p.2](https://arxiv.org/pdf/1812.02765v1#page=2 "Experimentally, we have found that autoencoders will sometimes reconstruct OOD samples with less error than many inlier samples."))
- **c3** Why not enlarge the bottleneck: increasing the latent dimensionality increases model power, and a bottleneck equal to or larger than the input can potentially learn the identity and reconstruct any input; the authors instead add a distance in the latent space.([Problem and approach, p.3](https://arxiv.org/pdf/1812.02765v1#page=3 "An autoencoder with a bottleneck layer dimensionality equal to or greater than the original input can potentially learn the identity function and reconstruct any given input, diminishing its ability to distinguish between inlier and OOD data."))
- **c4** Score weighting without OOD data: the mixing parameters are set from an inlier-only validation set (alpha = 1/std of the latent Mahalanobis distance, beta = 1/std of the reconstruction error); the authors say tuning this combination may give further improvements in future work.([Experiments and results, p.4](https://arxiv.org/pdf/1812.02765v1#page=4 "α and β are mixing parameters that were determined using a validation set of inliers samples."))
- **c5** Evaluation setup: for each of ten bottleneck sizes (2 to 798, stated as the original input size), a separate autoencoder is trained on a single MNIST digit class, which is the inlier class for that model; metrics are FPR at 95% TPR, AUROC, AUPR (in) and AUPR (out). MNIST is the only dataset.([Experiments and results, p.3](https://arxiv.org/pdf/1812.02765v1#page=3 "For each of the different architectures, a separate autoencoder was trained using only images from a single digit class from MNIST."))
- **c6** Result statement (hedged): incorporating the latent distance improved performance over reconstruction error alone 'in most cases'; the conclusion says the hybrid 'often' improves performance.([Experiments and results, p.4](https://arxiv.org/pdf/1812.02765v1#page=4 "Our results show that incorporating the latent distance improved performance over using only the reconstruction error in most cases."))
- **c7** Model selection for the summary table: Table 1 compares methods at the architecture that gave the best available result for the baseline (reconstruction error); the caption does not say on which data split this best result was determined.([Table 1 caption, p.5](https://arxiv.org/pdf/1812.02765v1#page=5 "Architecture chosen was for the best available result for the baseline method."))
- **c8** Stated limitations / future work: extend to more complex naturalistic image datasets, optimize how latent distance and reconstruction error are combined, and model multiple inlier classes with a single autoencoder.([Conclusion and future work, p.4](https://arxiv.org/pdf/1812.02765v1#page=4 "In the future, we would like to extend our work to more complex naturalistic image datasets"))

