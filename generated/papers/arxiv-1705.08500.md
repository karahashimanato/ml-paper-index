<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Selective Classification for Deep Neural Networks

- カード: [`arxiv-1705.08500`](../../papers/arxiv-1705.08500.yaml)
- 著者: Yonatan Geifman, Ran El-Yaniv
- 年・掲載: 2017
- 原論文: [PDF](https://arxiv.org/pdf/1705.08500v2)(arXiv v2、カード作成時に読んだ版)
- タグ: deep-learning, image-classification, post-hoc, selective-prediction
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Contribution: a method to construct a selective classifier from a trained neural network in which the user sets a desired risk level and, at test time, instances are rejected as needed to grant that risk with high probability.([Abstract, p.1](https://arxiv.org/pdf/1705.08500v2#page=1 "At test time, the classiﬁer rejects instances as needed, to grant the desired risk (with high probability)."))
- **c2** Selection mechanism: the classifier f is fixed; a rejection function is learned by choosing a threshold over one of two known confidence-rate functions, softmax response (SR, the maximal softmax output) or MC-dropout (minus the variance of the most probable class's response over dropout passes).([Introduction, p.2](https://arxiv.org/pdf/1705.08500v2#page=2 "To this end, we consider the above two known techniques for rejection (SR and MC-dropout), and devise a learning method that chooses an appropriate threshold that ensures the desired risk."))
- **c3** Guarantee and its assumptions (Theorem 3.2): if the labeled set S_m used by SGR is sampled i.i.d. from P, then with probability at least 1 - delta over the draw of S_m, every selective classifier computed in the k = ceil(log2 m) SGR iterations has true selective risk (w.r.t. P restricted to its accepted region) no larger than its computed bound (Lemma 3.1 applied with delta/k, plus a union bound). The guarantee is for the 0/1 loss and for test data from the same P; nothing is assumed about the confidence-rate function beyond using it to rank inputs (Section 3).([Selection with Guaranteed Risk Control, p.5](https://arxiv.org/pdf/1705.08500v2#page=5 "Theorem 3.2 (SGR) Let Sm be a given labeled set, sampled i.i.d. from P, and consider an application of the SGR procedure."))
- **c4** Caveat on the confidence function: the theorem always holds, but if the confidence-rate function is severely skewed (far from ideal), the bound of the resulting selective classifier can be far from the target risk.([Confidence-Rate Functions for Neural Networks (footnote), p.6](https://arxiv.org/pdf/1705.08500v2#page=6 "While Theorem 3.2 always holds, we note that if κf is severely skewed (far from ideal), the bound of the resulting selective classiﬁer can be far from the target risk."))
- **c5** Choice of signal: risk-coverage curves computed on validation data show SR and MC-dropout nearly identical on CIFAR-10/100, while on ImageNet SR is significantly better on both top-1 and top-5, so the remaining experiments use SR only.([Empirical Results, p.7](https://arxiv.org/pdf/1705.08500v2#page=7 "see that SR is signiﬁcantly better than MC-dropout on both tasks."))
- **c6** Evaluation protocol: for CIFAR-10 the standard validation set is randomly split into two equal halves, one used as the SGR training set and the other reserved for testing the bounds (the paper states CIFAR-100 and ImageNet repeat the same experimental design); the test half is thus a random split of the same validation data (no shifted test data), and all SGR runs use delta = 0.001.([Selective Guaranteed Risk for CIFAR-10, p.8](https://arxiv.org/pdf/1705.08500v2#page=8 "The other half, which was not consumed by SGR for training, was reserved for testing the resulting bounds."))
- **c7** Stated limitations / open questions: only the 0/1 loss is studied (extension to other losses and regression, and control of false-positive/false-negative rates, is left open), and the classifier and selection function are not trained jointly.([Concluding Remarks, p.11](https://arxiv.org/pdf/1705.08500v2#page=11 "In this paper we only studied selective classiﬁcation under the 0/1 loss."))

