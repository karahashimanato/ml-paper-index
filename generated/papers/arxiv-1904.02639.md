<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Memorizing Normality to Detect Anomaly: Memory-augmented Deep Autoencoder for Unsupervised Anomaly Detection

- カード: [`arxiv-1904.02639`](../../papers/arxiv-1904.02639.yaml)
- 著者: Dong Gong, Lingqiao Liu, Vuong Le, Budhaditya Saha, Moussa Reda Mansour, Svetha Venkatesh, Anton van den Hengel
- 年・掲載: 2019 ICCV 2019
- 原論文: [PDF](https://arxiv.org/pdf/1904.02639v2)(arXiv v2、カード作成時に読んだ版)
- タグ: anomaly-detection, autoencoders, reconstruction-based-detectors, unsupervised
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Motivation (failure mode of AE detectors): the assumption that anomalies get higher reconstruction error may not always hold; sometimes the AE 'generalizes' so well that it also reconstructs anomalous inputs well, an observation the authors attribute to existing literature ([47, Figure 1]) and to their own Figures 4 and 6.([Introduction, p.1](https://arxiv.org/pdf/1904.02639v2#page=1 "However, this assumption may not always hold, and sometimes the AE can “generalize” so well that it can also reconstruct the abnormal inputs well."))
- **c2** Proposed explanation: since there are no anomalous training samples, reconstruction behaviour on anomalies should be unpredictable; if anomalies share compositional patterns with normal data (e.g. local edges in images) or the decoder is 'too strong', the AE is very likely to reconstruct them well.([Introduction, p.2](https://arxiv.org/pdf/1904.02639v2#page=2 "AE is very likely to reconstruct the anomalies well."))
- **c3** Anomaly score: at test time the anomaly criterion is the l2-norm based mean squared reconstruction error between the input and its reconstruction.([Section 3.2, p.3](https://arxiv.org/pdf/1904.02639v2#page=3 "to measure of the reconstruction quality, which is used as the criterion for anomaly detection."))
- **c4** Sparse addressing is motivated by a remaining failure mode: some anomalies might still be reconstructed well by a complex combination of memory items through dense addressing weights, so a hard shrinkage operator (threshold lambda, suggested in [1/N, 3/N]) is applied to the weights.([Section 3.3.3, p.4](https://arxiv.org/pdf/1904.02639v2#page=4 "To alleviate this issue, we apply a hard shrinkage operation to promote the sparsity of w:"))
- **c5** Image protocol (MNIST, CIFAR-10, one class as normal): the training set contains only normal samples and does not overlap the test set; anomalies from other classes make up around 30% of the test data; performance is reported as AUC over a varying threshold, so no operating threshold is selected.([Section 4.1, p.5](https://arxiv.org/pdf/1904.02639v2#page=5 "Following the setting used in [42, 47], the training set only consists of normal samples and has no overlapping with the testing set."))
- **c6** Observed AE failure: in the MNIST visualization, the AE without memory tends to learn more local representations, so an abnormal sample may also be reconstructed well, whereas MemAE reconstructs a normal-class digit.([Section 4.1, p.6](https://arxiv.org/pdf/1904.02639v2#page=6 "Thus an abnormal sample may also be reconstructed well."))
- **c7** Video protocol (UCSD-Ped2, CUHK Avenue, ShanghaiTech), following [9, 24]: the frame normality score is the reconstruction error min-max normalized to [0, 1] using the minimum and maximum error over the frames of the same video episode; frame-level AUC is reported.([Section 4.2, p.7](https://arxiv.org/pdf/1904.02639v2#page=7 "where eu denotes the reconstruction error the u-th frame in a video episode."))
- **c8** Cybersecurity protocol (KDDCUP99 10 percent, following [47]): 80% of the samples labelled 'attack' in the original dataset are treated as normal, half of the data is randomly sampled for training, and only normal-class samples are used for training; precision, recall and F1 are averaged over 20 runs. How the decision threshold for these metrics is set was not found in the text (searched for 'threshold'); the paper refers to the standard protocol of [47].([Section 4.3, p.8](https://arxiv.org/pdf/1904.02639v2#page=8 "Only data samples from normal class are used for training."))

