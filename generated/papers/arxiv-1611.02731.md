<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Variational Lossy Autoencoder

- カード: [`arxiv-1611.02731`](../../papers/arxiv-1611.02731.yaml)
- 著者: Xi Chen, Diederik P. Kingma, Tim Salimans, Yan Duan, Prafulla Dhariwal, John Schulman, Ilya Sutskever, Pieter Abbeel
- 年・掲載: 2016 ICLR 2017
- 原論文: [PDF](https://arxiv.org/pdf/1611.02731v2)(arXiv v2、カード作成時に読んだ版)
- タグ: generative-modeling, representation-learning, unsupervised, variational-autoencoders
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Thesis: VAEs are often interpreted as regularized autoencoders, but they do not always autoencode; the paper explains why earlier sequence VAEs did not use the latent code unless the decoder was weakened.([VAEs do not autoencode in general, p.2](https://arxiv.org/pdf/1611.02731v2#page=2 "In this section, we discuss the often-neglected fact that VAEs do not always autoencode"))
- **c2** Argument from bits-back coding: ignoring the latent code is not only an optimization problem; even with exact optimization, the code should be ignored at the optimum for most practical VAEs with intractable true posteriors and sufficiently powerful decoders.([Section 2.2, p.3](https://arxiv.org/pdf/1611.02731v2#page=3 "the latent code should still be ignored at optimum for most practical instances of VAE that have intractable true posterior distributions and sufﬁciently powerful decoders."))
- **c3** Information preference: information that the decoder can model locally without the latent code will be modelled by the decoder, and only the remainder is put into the code.([Section 2.2, p.4](https://arxiv.org/pdf/1611.02731v2#page=4 "information that can be modeled locally by decoding distribution p(x/z) without access to z will be encoded locally and only the remainder will be encoded in z."))
- **c4** Factorized decoders: because the required independence structure rarely exists in images, common VAEs with factorized decoders autoencode almost exactly.([Section 2.2, p.4](https://arxiv.org/pdf/1611.02731v2#page=4 "This kind of independence structure rarely exists in images so common VAEs that have factorized decoder autoencode almost exactly."))
- **c5** The information-preference argument is asymptotic (it holds only when the bound can be optimized well); the authors still use free bits and KL annealing to smooth optimization in their experiments.([Lossy code via explicit information placement, p.5](https://arxiv.org/pdf/1611.02731v2#page=5 "We want to additionally emphasize the information preference property is an asymptotic view in a sense that it only holds when the variational lowerbound can be optimized well."))
- **c6** Limitation: the lossy code does not always capture the global information one cares about; on OMNIGLOT, decompressions sometimes did not preserve semantics, so the decoder constraint has to be designed for the statistics that matter in each task and dataset.([Lossy compression, p.7](https://arxiv.org/pdf/1611.02731v2#page=7 "However, we remark that the lossy code z doesn’t always capture the kind of global information that we care about and it’s dependent on the type of constraint we put on the decoder."))
- **c7** Evaluation protocol for density estimation: one VLAE architecture with hyperparameters chosen manually on statically binarized MNIST is applied to dynamically binarized MNIST, OMNIGLOT and Caltech-101 Silhouettes; marginal NLL is estimated with importance sampling (4096 samples). The authors note that per-dataset tuning gives better results and report a fine-tuned VLAE on OMNIGLOT separately.([Density estimation, p.8](https://arxiv.org/pdf/1611.02731v2#page=8 "We choose hyperparameters manually on statically binarized MNIST and use the same hyperparameters to evaluate on dynamically binarized MNIST, OMNIGLOT and Caltech-101 Silhouettes."))

