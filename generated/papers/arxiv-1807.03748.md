<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Representation Learning with Contrastive Predictive Coding

- カード: [`arxiv-1807.03748`](../../papers/arxiv-1807.03748.yaml)
- 著者: Aaron van den Oord, Yazhe Li, Oriol Vinyals
- 年・掲載: 2018
- 原論文: [PDF](https://arxiv.org/pdf/1807.03748v2)(arXiv v2、カード作成時に読んだ版)
- タグ: image-classification, joint-embedding, representation-learning, self-supervised, unsupervised
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Motivation: unimodal losses are not very useful for predicting high-dimensional data and generative models that reconstruct every detail are computationally intense; since high-level latent variables carry far less information than the data, the authors suggest that modelling p(x|c) directly may not be optimal for extracting the information shared between x and c.([Motivation and Intuitions, p.2](https://arxiv.org/pdf/1807.03748v2#page=2 "This suggests that modeling p(x/c) directly may not be optimal for the purpose of extracting shared information between x and c."))
- **c2** InfoNCE: the encoder and autoregressive model are trained jointly on a loss based on NCE; given a set of N samples containing one positive from p(x_{t+k}|c_t) and N - 1 negatives from the proposal distribution p(x_{t+k}), the loss is the categorical cross-entropy of identifying the positive.([Section 2.3, p.3](https://arxiv.org/pdf/1807.03748v2#page=3 "Both the encoder and autoregressive model are trained to jointly optimize a loss based on NCE, which we will call InfoNCE."))
- **c3** The optimal score f(x_{t+k}, c_t) for this loss is proportional to the density ratio p(x_{t+k}|c_t)/p(x_{t+k}), and this optimum does not depend on the number of negative samples.([Section 2.3, p.4](https://arxiv.org/pdf/1807.03748v2#page=4 "is independent of the the choice of the number of negative samples N −1"))
- **c4** Link to mutual information: I(x_{t+k}, c_t) >= log(N) - L_N, which becomes tighter as N grows, so minimizing the InfoNCE loss maximizes a lower bound on mutual information (the authors note the MI evaluation is not required for training).([Section 2.3, p.4](https://arxiv.org/pdf/1807.03748v2#page=4 "Also observe that minimizing the InfoNCE loss LN maximizes a lower bound on mutual information."))
- **c5** The appendix derivation of the bound contains an approximation step (replacing the sum over negatives by N - 1 times an expectation); the authors state that it quickly becomes more accurate as N increases and that log(N) - L_N also increases, so large N is useful.([Appendix A.1, p.13](https://arxiv.org/pdf/1807.03748v2#page=13 "Equation 8 quickly becomes more accurate as N increases."))
- **c6** InfoNCE is related to the MINE estimator (maximizing a lower bound on it, up to a constant); using MINE directly gave identical performance when the task was non-trivial but became very unstable when the target was easy to predict from the context (e.g. one-step prediction overlapping the context).([Appendix A.1, p.13](https://arxiv.org/pdf/1807.03748v2#page=13 "We found that using MINE directly gave identical performance when the task was non-trivial, but became very unstable if the target was easy to predict from the context"))
- **c7** ImageNet evaluation protocol: CPC with a ResNet-v2-101 encoder (not pretrained, no BatchNorm) on a 7x7 grid of 64x64 crops with simple augmentation; a linear classifier (SGD, fixed learning-rate schedule) is trained on the spatially mean-pooled 1024-d features. The authors note that the prior work they follow uses a 3x3x1024 representation without pooling, giving the linear mapping more parameters, which could be advantageous; previous results in Table 4 are taken from that work.([Vision, p.7](https://arxiv.org/pdf/1807.03748v2#page=7 "This is slightly different from [36] which uses a 3x3x1024 representation without pooling, and thus has more parameters in the supervised linear mapping (which could be advantageous)."))
- **c8** Caveat on the NLP transfer benchmark (BookCorpus pre-training, logistic regression on five classification tasks with the L2 weight chosen by (nested) cross-validation): models that learned better relationships in the source books did not necessarily perform better on the very different target tasks.([Natural Language, p.8](https://arxiv.org/pdf/1807.03748v2#page=8 "Although this is a standard transfer learning benchmark, we found that models that learn better relationships in the childeren books did not necessarily perform better on the target tasks"))

