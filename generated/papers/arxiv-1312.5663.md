<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# k-Sparse Autoencoders

- カード: [`arxiv-1312.5663`](../../papers/arxiv-1312.5663.yaml)
- 著者: Alireza Makhzani, Brendan Frey
- 年・掲載: 2013
- 原論文: [PDF](https://arxiv.org/pdf/1312.5663v2)(arXiv v2、カード作成時に読んだ版)
- タグ: autoencoders, image-classification, representation-learning, unsupervised
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Motivation: sparse autoencoders usually combine activation functions, sampling steps and penalties and are sometimes not guaranteed to give sparse representations for each input; e.g. a 'lifetime sparsity' KL penalty (citing Lee et al. 2007; Nair & Hinton 2009) makes hidden units sparse across training points but not each input's code.([Introduction, p.1](https://arxiv.org/pdf/1312.5663v2#page=1 "This results in sparse activation of hidden units across training points, but does not guarantee that each input has a sparse representation."))
- **c2** Contribution claim: relying solely on sparsity as the regularizer and as the only nonlinearity, the authors report much better results than the other methods compared, including RBMs, denoising autoencoders and dropout.([Introduction, p.2](https://arxiv.org/pdf/1312.5663v2#page=2 "by solely relying on sparsity as the regularizer and as the only nonlinearity"))
- **c3** Mechanism: once the k largest activities are selected the network is linear, so the only nonlinearity is the selection, which acts as a regularizer preventing the use of too many hidden units in the reconstruction.([Section 2.2, p.2](https://arxiv.org/pdf/1312.5663v2#page=2 "This selection step acts as a regularizer that prevents the use of an overly large number of hidden units when reconstructing the input."))
- **c4** Encoding differs from training: features for classification use the alpha*k largest hidden units, with alpha >= 1 selected using validation data, which the authors observed to give slightly better performance (citing Coates & Ng 2011 for mismatched training/encoding stages).([Section 2.2, p.2](https://arxiv.org/pdf/1312.5663v2#page=2 "we have observed that slightly better performance is obtained by using the αk largest hidden units where α ≥1 is selected using validation data."))
- **c5** Theory: the k-sparse autoencoder is derived as an approximation of a sparse coding algorithm that uses ITI for sparse recovery; Theorem 3.1 shows the first ITI step recovers the support if the dictionary is incoherent enough, and the authors argue that the learnt dictionary must be sufficiently incoherent when training converges.([Section 3.2, p.3](https://arxiv.org/pdf/1312.5663v2#page=3 "In summary, we can view k-sparse autoencoders as the approximation of a sparse coding algorithm which uses ITI in the sparse recovery stage."))
- **c6** Training failure mode: with low k, the first epochs greedily assign hidden units to groups of examples (similar to k-means) and other units become 'dead'; the authors address this by starting from a large k and linearly decreasing it over the first half of the epochs.([Section 4.2.1, p.5](https://arxiv.org/pdf/1312.5663v2#page=5 "That is, too much sparsity can prevent gradient back-propagation from adjusting the weights of these other ‘dead’ hidden units."))
- **c7** Effect of sparsity level (qualitative, from filter visualizations): large k gives very local features too primitive for a linear classifier (but usable for pre-training deep nets), smaller k gives more global features, and too much sparsity gives features that are too global and do not factor the input into parts.([Section 4.3, p.5](https://arxiv.org/pdf/1312.5663v2#page=5 "Nevertheless, forcing too much sparsity (e.g., k = 10 on MNIST), results in features that are too global and do not factor the input into parts, as depicted Figure 1d and 2c."))
- **c8** Evaluation protocol: MNIST training set split into 50,000 training and 10,000 validation, small NORB training set into 20,000 and 4,300; momentum, learning rate and initialization differ per task and dataset and are selected on validation; unsupervised features are evaluated by training logistic regression on fixed features, and baseline feature choices (all hidden units for dropout AE, uncorrupted input for denoising AE) are described as 'this worked best'.([Section 4.2.2, p.5](https://arxiv.org/pdf/1312.5663v2#page=5 "We use diﬀerent momentum values, learning rates and initializations based on the task and the dataset, and validation is used to select hyperparameters."))

