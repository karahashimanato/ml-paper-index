<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# What Do Compressed Deep Neural Networks Forget?

- カード: [`arxiv-1911.05248`](../../papers/arxiv-1911.05248.yaml)
- 著者: Sara Hooker, Aaron Courville, Gregory Clark, Yann Dauphin, Andrea Frome
- 年・掲載: 2019
- 原論文: [PDF](https://arxiv.org/pdf/1911.05248v3)(arXiv v3、カード作成時に読んだ版)
- タグ: deep-learning, model-compression, post-hoc, post-training-quantization, pruning, quantization, supervised
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Main claim: top-line accuracy hides that compressed models with very different weight counts diverge on a narrow subset of the data, which the authors call Pruning Identified Exemplars (PIEs).([Abstract, p.1](https://arxiv.org/pdf/1911.05248v3#page=1 "We ﬁnd that models with radically different numbers of weights have comparable top-line performance metrics but diverge considerably in behavior on a narrow subset of the dataset."))
- **c2** Compression methods: magnitude pruning during training at 30-90% sparsity, and three post-training quantization variants (float16, hybrid dynamic-range int8 weights, and fixed-point int8 using a small representative dataset).([Experimental framework, p.5](https://arxiv.org/pdf/1911.05248v3#page=5 "All quantization methods we evaluate are implemented post-training, in contrast to the pruning which is applied progressively over the course of training."))
- **c3** Evaluation protocol: a population of independently trained models per compression method, dataset and model (30 per pruning level); for each class a two-tailed Welch's t-test on mean-shifted class accuracy decides (p <= 0.05) whether compression impacts that class disproportionately; tasks are CIFAR-10 (wide ResNet), ImageNet (ResNet-50) and CelebA (ResNet-18).([Methodology, p.3](https://arxiv.org/pdf/1911.05248v3#page=3 "If the p-value <= 0.05, we reject the null hypothesis and consider the class to be disparately impacted by t level of compression relative to the baseline."))
- **c4** PIEs are more difficult for models and humans: a human study finds they are more often mislabelled, lower quality, multi-object or fine-grained, and compression impairs prediction on the long tail of less frequent instances.([Introduction (contributions), p.2](https://arxiv.org/pdf/1911.05248v3#page=2 "Compression impairs the model’s ability to predict accurately on the long-tail of less frequent instances."))
- **c5** Quantization versus pruning: all evaluated techniques have non-uniform impact, but quantization appears to introduce less disparate harm than (high levels of) pruning.([Results, p.6](https://arxiv.org/pdf/1911.05248v3#page=6 "While all the techniques we benchmark evidence disparate class level impact, we note that quantization appears to introduce less disparate harm."))
- **c6** Pruned networks are more sensitive to distribution shift (ImageNet-C corruptions and ImageNet-A natural adversarial images), increasingly so at higher sparsity.([Introduction (contributions), p.2](https://arxiv.org/pdf/1911.05248v3#page=2 "Pruned networks are more sensitive to natural adversarial images and corruptions."))
- **c7** Limitations: implications for fairness remain open, and other domains such as language and audio were not evaluated.([Limitations, p.10](https://arxiv.org/pdf/1911.05248v3#page=10 "Underserved areas worthy of future consideration include evaluating the impact of compression on additional domains such as language and audio, and leveraging these insights to explicitly optimize for compressed models that also minimize the disparate impact on underrepresented data attributes."))

