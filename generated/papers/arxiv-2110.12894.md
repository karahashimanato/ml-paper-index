<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# The Efficiency Misnomer

- カード: [`arxiv-2110.12894`](../../papers/arxiv-2110.12894.yaml)
- 著者: Mostafa Dehghani, Anurag Arnab, Lucas Beyer, Ashish Vaswani, Yi Tay
- 年・掲載: 2021
- 原論文: [PDF](https://arxiv.org/pdf/2110.12894v2)(arXiv v2、カード作成時に読んだ版)
- タグ: deep-learning, efficiency-evaluation, image-classification, mixture-of-experts
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Main claim: cost indicators (parameter count, FLOPs, throughput/speed) can contradict each other, and incomplete reporting of them can lead to partial conclusions about model efficiency.([Abstract, p.1](https://arxiv.org/pdf/2110.12894v2#page=1 "We demonstrate how incomplete reporting of cost indicators can lead to partial conclusions and a blurred or incomplete picture of the practical considerations of different models."))
- **c2** Measurement caveat: reported FLOPs are usually theoretical values that ignore practical factors such as which parts of the model can be parallelized.([A Primer on Cost Indicators, p.3](https://arxiv.org/pdf/2110.12894v2#page=3 "Note that theoretical FLOPs ignores practical factors, like which parts of the model can be parallelized."))
- **c3** Experimental setup: in controlled ViT experiments (Scenic, 64 TPU-V3) scaling depth vs width, all other hyperparameters were kept fixed at the default values from the referenced papers; which architecture looks better depends on the cost indicator.([Potential disagreement between cost indicators, p.6](https://arxiv.org/pdf/2110.12894v2#page=6 "Note that when changing depth or width of the model (see Table 2 in Appendix A for the exact conﬁgurations) all other hyper-parameters are kept ﬁxed based on the default values given by the referenced papers."))
- **c4** Measurement source for the ImageNet model comparison: accuracies and cost values are taken from Steiner et al. and Liu et al., with cost indicators from PyTorch implementations and throughput measured on a V100 GPU with timm.([Discussion (Figure 5 caption), p.7](https://arxiv.org/pdf/2110.12894v2#page=7 "Cost indicators are based on PyTorch implementation of the included models and the throughput is measured on a V100 GPU, using timm (Wightman, 2019)."))
- **c5** Training time as a metric: the authors warn that training time is prone to Goodhart's law and depends on the whole training recipe; they state that a claim that one method performs almost as well as another with dramatically reduced training cost is not valid, because a method not optimized for training cost may be re-tuned with that in mind (e.g. learning rate, weight decay).([Training or inference cost?, p.4](https://arxiv.org/pdf/2110.12894v2#page=4 "Whilst “training time” can be a great cost indicator, it is also prone to Goodhart’s Law: When used as the main metric, it can and will be gamed and lose its meaning."))
- **c6** Sparse models / MoE: the authors argue that parameter-matched comparisons do not make sense for sparse models and unnecessarily downplay their strengths.([The issues with parameter matched comparisons, p.8](https://arxiv.org/pdf/2110.12894v2#page=8 "Hence, parameter matched comparisons do not make sense for sparse models and parameter-matching sparse models can be seen as an unfair method of unnecessarily downplaying the strengths of sparse models."))
- **c7** Recommendation: always report and plot curves with all available cost indicators, avoid highlighting a single one, and narrow efficiency claims to the exact evaluated setup.([Suggestions and Conclusion, p.9](https://arxiv.org/pdf/2110.12894v2#page=9 "Since each indicator stands for something different and comes with its own pros and cons, we suggest always reporting and plotting curves using all available cost indicators, and refraining from highlighting results using just a single one."))

