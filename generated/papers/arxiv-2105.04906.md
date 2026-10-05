<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# VICReg: Variance-Invariance-Covariance Regularization for Self-Supervised Learning

- カード: [`arxiv-2105.04906`](../../papers/arxiv-2105.04906.yaml)
- 著者: Adrien Bardes, Jean Ponce, Yann LeCun
- 年・掲載: 2021 ICLR 2022
- 原論文: [PDF](https://arxiv.org/pdf/2105.04906v3)(arXiv v3、カード作成時に読んだ版)
- タグ: image-classification, joint-embedding, representation-learning, self-supervised
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Claim of the method: the variance and covariance terms explicitly avoid collapse, so VICReg does not require weight sharing, batch or feature-wise normalization, quantization, stop-gradient or memory banks.([Abstract, p.1](https://arxiv.org/pdf/2105.04906v3#page=1 "Unlike most other approaches to the same problem, VICReg does not require techniques such as: weight sharing between the branches, batch normalization, feature-wise normalization, output quantization, stop gradient, memory banks, etc."))
- **c2** Using the standard deviation rather than the variance in the hinge is crucial: with the variance, the gradient vanishes near the mean and the embeddings collapse.([Method, p.5](https://arxiv.org/pdf/2105.04906v3#page=5 "Using the standard deviation and not directly the variance is crucial."))
- **c3** Coefficient ablation: without the variance term the representations immediately collapse to a single vector, and the covariance term, which has no repulsive effect, has no impact; the invariance term is necessary; variance and covariance are complementary.([Appendix D.4, p.18](https://arxiv.org/pdf/2105.04906v3#page=18 "Without variance regularization the representations immediately collapse to a single vector and the covariance term, which has no repulsive effect preventing collapse, has no impact."))
- **c4** Combining components (Table 4, 100 epochs): with variance regularization, adding a predictor makes no significant difference (redundant); without it, the representations collapse and both stop-gradient and predictor are necessary.([Analysis (Asymmetric networks), p.8](https://arxiv.org/pdf/2105.04906v3#page=8 "In comparison, without VR, the representations collapse, and both stop-gradient (SG) and PR are necessary."))
- **c5** Adding variance regularization to stop-gradient or momentum-encoder setups gives small gains, which the authors suggest might be because those tricks do not perfectly maintain the variance, i.e. very slow collapse is happening.([Analysis (Asymmetric networks), p.9](https://arxiv.org/pdf/2105.04906v3#page=9 "which might be explained by the fact that these architectural tricks that prevent collapse are not perfectly maintaining the variance of the representations, i.e. very slow collapse is happening with these methods."))
- **c6** Batch size (128 to 4096, base learning rate grid-searched per size): small drops at 256 and 128, which the authors call comparable to the batch-size robustness of Barlow Twins and SimSiam.([Appendix D.7, p.21](https://arxiv.org/pdf/2105.04906v3#page=21 "We observe a 0.7% and 1.2% drop in accuracy with small batch size of 256 and 128 which is comparable with the robustness to batch size of Barlow Twins Zbontar et al. (2021) and SimSiam Chen & He (2020)"))
- **c7** Selection of the loss coefficients: the final values were the ones that worked best (by a small margin) on ImageNet; the authors add that they could have tuned them by cross-validation on validation sets of smaller datasets (MNIST, CIFAR), where the same values also worked well.([Appendix D.4, p.19](https://arxiv.org/pdf/2105.04906v3#page=19 "that setting lambda = mu = 25 and nu = 1 works best (by a small margin) for Imagenet"))
- **c8** Non-shared weights: going from shared to different weights, performance drops by 2.1% for VICReg and 4.5% for Barlow Twins; the authors conclude VICReg is more robust in these scenarios.([Analysis (Weight sharing), p.9](https://arxiv.org/pdf/2105.04906v3#page=9 "The performance drops by 2.1% with VICReg and 4.5% with Barlow Twins, between the shared weights scenario (SW) and the different weight scenario (DW)."))

