<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Beyond neural scaling laws: beating power law scaling via data pruning

- カード: [`arxiv-2206.14486`](../../papers/arxiv-2206.14486.yaml)
- 著者: Ben Sorscher, Robert Geirhos, Shashank Shekhar, Surya Ganguli, Ari S. Morcos
- 年・掲載: 2022
- 原論文: [PDF](https://arxiv.org/pdf/2206.14486v6)(arXiv v6、カード作成時に読んだ版)
- タグ: deep-learning, image-classification, scaling-laws, supervised
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Theory claim (perceptron student-teacher setting): exponential scaling of error with pruned dataset size is possible if the pruning fraction is chosen Pareto-optimally, pruning more aggressively as the initial dataset grows.([Introduction (contributions), p.3](https://arxiv.org/pdf/2206.14486v6#page=3 "(b) Exponential scaling is possible with respect to pruned dataset size provided one chooses an increasing Pareto optimal pruning fraction as a function of initial dataset size."))
- **c2** Theory prediction (perceptron student-teacher setting): the optimal pruning strategy depends on the amount of initial data; with abundant data keep only hard examples, with scarce data keep easy examples. The paper's next contribution states that both theoretical predictions also hold in practice in more general settings (ResNets, ViT fine-tuning).([Introduction (contributions), p.3](https://arxiv.org/pdf/2206.14486v6#page=3 "(a) The optimal pruning strategy changes depending on the amount of initial data; with abundant (scarce) initial data, one should retain only hard (easy) examples."))
- **c3** Empirical claim: better than power law scaling with pruned dataset size is observed for ResNets trained on CIFAR-10, SVHN and ImageNet (the paper's contribution list also mentions ViTs fine-tuned on CIFAR-10).([Abstract, p.1](https://arxiv.org/pdf/2206.14486v6#page=1 "We then test this improved scaling prediction with pruned dataset size empirically, and indeed observe better than power law scaling in practice on ResNets trained on CIFAR-10, SVHN, and ImageNet."))
- **c4** Benchmark of ten pruning metrics on ImageNet: most existing high-performing metrics scale poorly to ImageNet and the best are computationally intensive and need labels; the proposed self-supervised metric is reported comparable to the best supervised metrics.([Abstract, p.1](https://arxiv.org/pdf/2206.14486v6#page=1 "We ﬁnd most existing high performing metrics scale poorly to ImageNet, while the best are computationally intensive and require labels for every image."))
- **c5** Compute accounting (preliminary): for ResNets, compute is measured as FLOPs in a fixed-epoch setting, so a model on 60% of the data uses 60% of the iterations and compute (previous work fixed iterations); for the perceptron, compute is clock time to convergence on a CPU. The authors describe the ResNet evidence as preliminary.([Appendix C (Breaking compute scaling laws via data pruning), p.33](https://arxiv.org/pdf/2206.14486v6#page=33 "While previous works have ﬁxed the number of iterations [10], here we ﬁx the number of epochs, so that the model trained on 60% of the full dataset is trained for only 60% the iterations of the model trained on the full dataset, using only 60% the compute."))
- **c6** Main stated limitation: exponential scaling requires a high-quality pruning metric; the authors note that most metrics developed for smaller datasets scale poorly to ImageNet.([Discussion (Limitations), p.10](https://arxiv.org/pdf/2206.14486v6#page=10 "The most notable limitation is that achieving exponential scaling requires a high quality data pruning metric."))
- **c7** Accuracy vs. training-time trade-off: performance often increased when training on pruned data for the same number of iterations as the full data (more epochs), with gains saturating before matching full training time; the authors say this trade-off must be considered when evaluating gains from pruning, and also found class balancing essential.([Discussion (Limitations), p.10](https://arxiv.org/pdf/2206.14486v6#page=10 "Overall this tradeoff between accuracy and training time on pruned data is important to consider in evaluating potential gains due to data pruning."))

