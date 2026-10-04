<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Autoencoders

- カード: [`arxiv-2003.05991`](../../papers/arxiv-2003.05991.yaml)
- 著者: Dor Bank, Noam Koenigstein, Raja Giryes
- 年・掲載: 2020
- 原論文: [PDF](https://arxiv.org/pdf/2003.05991v2)(arXiv v2、カード作成時に読んだ版)
- タグ: anomaly-detection, autoencoders, generative-modeling, reconstruction-based-detectors, representation-learning, unsupervised, variational-autoencoders
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** When the hidden layer is at least as large as the input, there is a risk that the encoder learns the identity function; regularization is described as a way to prevent this without a bottleneck.([Section 2, p.3](https://arxiv.org/pdf/2003.05991v2#page=3 "In cases where the size of the hidden layer is equal or greater than the size of the input, there is a risk that the encoder will simply learn the identity function."))
- **c2** A bottleneck alone is not sufficient: even with a bottleneck of a single node, overfitting is still possible if encoder and decoder have enough capacity to encode each sample to an index.([Section 2, p.3](https://arxiv.org/pdf/2003.05991v2#page=3 "overﬁtting is still possible if the capacity of the encoder and the decoder is large enough to encode each sample to an index."))
- **c3** Citing [38], a linear autoencoder achieves the same latent representation as PCA; the authors therefore describe an autoencoder as a generalization of PCA that can learn a non-linear manifold.([Section 1, p.2](https://arxiv.org/pdf/2003.05991v2#page=2 "Therefore, an autoencoder is in fact a generalization of PCA, where instead of ﬁnding a low dimensional hyperplane in which the data lies, it is able to learn a non-linear manifold."))
- **c4** Anomaly detection use: the objective is to learn a normal profile from normal data only, assuming a trained autoencoder learns the latent subspace of normal samples and thus gives low reconstruction error for normal samples and high error for anomalies (citing [21, 18, 62, 61]). No discussion of how the anomaly threshold is set, or of failure modes such as anomalies being reconstructed well, was found in the text (searched for threshold, anomal, outlier, novelty, limitation, weakness).([Section 4.4, p.11](https://arxiv.org/pdf/2003.05991v2#page=11 "The use of autoencoders for this tasks, follows the assumption that a trained autoencoder would learn the latent subspace of normal samples."))
- **c5** Clustering use: the main disadvantage of vanilla autoencoders for clustering is that the embeddings are trained solely for reconstruction, not for clustering; modifications add a cluster-distance term or a prior on the embeddings.([Section 4.3, p.10](https://arxiv.org/pdf/2003.05991v2#page=10 "The main disadvantage of using vanilla autoencoders for clustering is that the embeddings are trained solely for reconstruction and not for the clustering application."))
- **c6** Limitation of reconstruction losses: autoencoder reconstructions of images are usually blurry, which the authors attribute to a loss that does not take into account how realistic the results are; combinations with GANs are presented as addressing this.([Section 5, p.14](https://arxiv.org/pdf/2003.05991v2#page=14 "On the other hand, by looking at the reconstruction quality of autoencoders for images, one of its major weaknesses becomes clear, as the resulting images are usually blurry."))
- **c7** Dimensionality reduction: PCA is optimal as a linear projection, while non-linear methods such as autoencoders 'may and often do' achieve superior results (stated without supporting experiments in the chapter).([Section 4.6, p.13](https://arxiv.org/pdf/2003.05991v2#page=13 "However, non-linear methods such as autoencoders, may and often do achieve superior results."))
- **c8** Open problem: for generative modelling, choosing the size and distribution of the hidden state is still done by experimentation (reconstruction error and varying the hidden state after training), and the authors call for research to set these parameters better.([Section 6, p.19](https://arxiv.org/pdf/2003.05991v2#page=19 "As for modeling generative processes, despite the success of variational and disentangled autoencoders, the way to choose the size and distribution of the hidden state is still based on experimentation, by considering the reconstruction error, and by varying the hidden state at post training."))

