<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# An Empirical Study of Training Self-Supervised Vision Transformers

- カード: [`arxiv-2104.02057`](../../papers/arxiv-2104.02057.yaml)
- 著者: Xinlei Chen, Saining Xie, Kaiming He
- 年・掲載: 2021 ICCV 2021
- 原論文: [PDF](https://arxiv.org/pdf/2104.02057v4)(arXiv v4、カード作成時に読んだ版)
- タグ: image-classification, joint-embedding, representation-learning, self-supervised
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Unstable self-supervised ViT training may not fail catastrophically (e.g. diverge) but can cause mild accuracy degradation (e.g. 1-3%), which may not be noticeable without a more stable counterpart for comparison.([Introduction, p.1](https://arxiv.org/pdf/2104.02057v4#page=1 "Interestingly, we observe that unstable ViT training may not result in catastrophic failure (e.g., divergence); instead, it can cause mild degradation in accuracy (e.g., 1∼3%)."))
- **c2** MoCo v3 design: keys that co-exist in the same batch are used as negatives and the memory queue is abandoned because its gain diminishes for sufficiently large batches (e.g. 4096); the loss is symmetrized, the query encoder has a projection and a prediction head, and the key encoder is a moving average of the query encoder excluding the prediction head.([Section 3, p.3](https://arxiv.org/pdf/2104.02057v4#page=3 "We abandon the memory queue [20], which we ﬁnd has diminishing gain if the batch is sufﬁciently large (e.g., 4096)."))
- **c3** Batch size: 1k and 2k batches give reasonably smooth training curves and the larger batch improves accuracy thanks to more negatives; a 4k batch becomes noticeably unstable and a 6k batch shows worse failure patterns, yet still gives an apparently decent result.([Section 4.1, p.3](https://arxiv.org/pdf/2104.02057v4#page=3 "In this regime, the larger batch improves accuracy thanks to more negative samples [20, 10]."))
- **c4** Hidden degradation is hard to notice: repeating the same configuration usually differs by only 0.1-0.3%, so mild instability does not show up as large run-to-run variation.([Section 4.1, p.3](https://arxiv.org/pdf/2104.02057v4#page=3 "In many of our ablations, running the same conﬁguration for a second trial often results in a small difference of 0.1∼0.3%."))
- **c5** Stability trick: gradient spikes appear earlier in the first layer (patch projection) than in the last layers, so the authors freeze the patch projection as a fixed random layer (stop-gradient after it); it stabilized training and improved accuracy in MoCo v3, SimCLR, BYOL and SwAV in their experiments.([Section 4.2, p.4](https://arxiv.org/pdf/2104.02057v4#page=4 "In other words, we use a ﬁxed random patch projection layer to embed the patches, which is not learned."))
- **c6** Limitation of the trick: it alleviates but does not solve the instability (the model can still be unstable if lr is too large); the authors think the issue concerns all layers and is an optimization problem, and hope for a more fundamental solution.([Section 4.2, p.5](https://arxiv.org/pdf/2104.02057v4#page=5 "The trick alleviates the issue, but does not solve it."))
- **c7** Evaluation protocol: after pre-training on the ImageNet training set, the MLP heads are removed and a linear classifier is trained on frozen features for 90 epochs on the ImageNet training set (random resized crop and flip only; SGD, batch 4096, wd 0, lr swept per case), reporting single-crop top-1 on the validation set. Pre-training lr and wd are searched on 100-epoch results. The data used to select the swept probe lr is not stated (searched for sweep, search, validation).([Section 5, p.5](https://arxiv.org/pdf/2104.02057v4#page=5 "We use the SGD optimizer, with a batch size of 4096, wd of 0, and sweep lr for each case."))
- **c8** Framework comparison: MoCo v3, SimCLR, BYOL and SwAV with ViT are all run by the authors with the random-projection trick, two 224x224 crops, and lr and wd swept per framework; R-50 results of the other frameworks are taken from an improved implementation in [13] (Chen and He, an earlier paper by two of the authors).([Section 6.1, p.6](https://arxiv.org/pdf/2104.02057v4#page=6 "We sweep lr and wd for each individual framework for fair comparisons."))
- **c9** Momentum encoder ablation (ViT-B, 300 epochs): m = 0, analogous to SimCLR plus the prediction head and stop-gradient on keys, gives accuracy similar to SimCLR, and using the momentum encoder leads to a 2.2% increase. Removing the prediction head still gives a decent result: MoCo as a contrastive method does not need the predictor, unlike negative-free methods.([Section 6.2, p.7](https://arxiv.org/pdf/2104.02057v4#page=7 "The usage of the momentum encoder leads to 2.2% increase."))

