<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# SelectiveNet: A Deep Neural Network with an Integrated Reject Option

- カード: [`arxiv-1901.09192`](../../papers/arxiv-1901.09192.yaml)
- 著者: Yonatan Geifman, Ran El-Yaniv
- 年・掲載: 2019
- 原論文: [PDF](https://arxiv.org/pdf/1901.09192v4)(arXiv v4、カード作成時に読んだ版)
- タグ: deep-learning, image-classification, selective-prediction, supervised, tabular-regression
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Contribution: unlike rejection mechanisms that threshold the confidence of a pre-trained network, SelectiveNet optimizes prediction (classification or regression) and rejection jointly, end-to-end, for a target coverage.([Abstract, p.1](https://arxiv.org/pdf/1901.09192v4#page=1 "In contrast, SelectiveNet is trained to optimize both classiﬁcation (or regression) and rejection simultaneously"))
- **c2** Selection signal: a learned selection head whose final layer is a single sigmoid neuron; at inference the network predicts only if g(x) is at least 0.5 and abstains otherwise.([SelectiveNet Architecture, p.3](https://arxiv.org/pdf/1901.09192v4#page=3 "At inference time, a sample x is fed to SelectiveNet, which predicts f(x) if and only if g(x) ≥0.5; otherwise, SelectiveNet abstains from predicting the label of x."))
- **c3** Coverage is not guaranteed by training: on CIFAR-10 both SR (threshold chosen on the training set) and SelectiveNet (trained with target coverage c) miss the target coverage on the test set in all cases (in Table 1 SR falls below the target, SelectiveNet lands above it), with a smaller average violation for SelectiveNet.([Coverage Accuracy, p.4](https://arxiv.org/pdf/1901.09192v4#page=4 "Clearly, both SR and SelectiveNet violate the target coverage rate in all cases."))
- **c4** Guarantee and its assumptions: a post-training calibration sets the threshold tau at the 100(1-c) percentile of g over an independent unlabeled validation set of n samples; treating each event g(x_i) >= tau as a Bernoulli variable, a Hoeffding bound gives, with probability at least 1 - delta, coverage in [c - epsilon, c + epsilon] with epsilon = sqrt(ln(2/delta)/(2n)). (The Hoeffding step presumes independent draws from the distribution the coverage refers to; shift is not discussed.) This is a coverage guarantee only, not a risk guarantee; Section 2 states such a model can be converted into a risk-controlling one with the technique of Geifman & El-Yaniv (2017b).([Coverage Accuracy, p.4](https://arxiv.org/pdf/1901.09192v4#page=4 "This goal can be achieved easily using the following simple post-training coverage calibration technique, which relies on an independent unlabeled validation set Vn containing n samples."))
- **c5** Evaluation protocol: datasets SVHN, CIFAR-10, Cats vs. Dogs (image classification) and UCI Concrete Compressive Strength (regression); baselines are SR and MC-dropout, rejection mechanisms composed over a standard network trained for full coverage (MC-dropout as recommended by its creators: p = 0.5 and 100 passes in classification, p = 0.05 and 200 passes in regression); SR is not applied to regression because there is no softmax layer.([Baseline Methods, p.4](https://arxiv.org/pdf/1901.09192v4#page=4 "We compare the proposed method with two baselines: SR and MC-dropout, which are described below."))
- **c6** Hyperparameters: alpha (weight between selective and auxiliary loss) was 0.5 in all experiments (Section 4.2 adds: without any hyperparameter optimization); lambda was set to 32, a value found large enough to preserve the coverage constraint through training.([Architectures and Hyperparameters, p.5](https://arxiv.org/pdf/1901.09192v4#page=5 "The value of α (the convex combination between the selective loss and the auxiliary loss) was set to 0.5 for all experiments, and λ was set to 32"))
- **c7** Stated limitations / future work: the capacity (architecture) of the selection head was not optimized, and the authors anticipate that different datasets and perhaps different coverage rates may require different selection-head architectures; whether ensembling improves SelectiveNet is left open.([Concluding Remarks, p.8](https://arxiv.org/pdf/1901.09192v4#page=8 "Here, we have not tried to optimize this choice, but we anticipate that different datasets and perhaps different coverage rates may require different architectures also for the selection head."))

