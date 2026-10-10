<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Learning both Weights and Connections for Efficient Neural Networks

- カード: [`arxiv-1506.02626`](../../papers/arxiv-1506.02626.yaml)
- 著者: Song Han, Jeff Pool, John Tran, William J. Dally
- 年・掲載: 2015 NIPS 2015
- 原論文: [PDF](https://arxiv.org/pdf/1506.02626v3)(arXiv v3、カード作成時に読んだ版)
- タグ: deep-learning, image-classification, model-compression, pruning, supervised
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Abstract: a train / prune / retrain method reduces the parameters of AlexNet on ImageNet by 9x (61 million to 6.7 million) without accuracy loss, and of VGG-16 by 13x (138 million to 10.3 million) with no loss of accuracy.([Abstract, p.1](https://arxiv.org/pdf/1506.02626v3#page=1 "On the ImageNet dataset, our method reduced the number of parameters of AlexNet by a factor of 9×, from 61 million to 6.7 million, without incurring accuracy loss."))
- **c2** Method: connectivity is first learned by normal training, then all connections with weights below a threshold are removed (dense to sparse), and the network is retrained to learn the final weights of the remaining connections. The authors call retraining critical: without it, accuracy is significantly impacted.([Section 3, p.3](https://arxiv.org/pdf/1506.02626v3#page=3 "If the pruned network is used without retraining, accuracy is signiﬁcantly impacted."))
- **c3** Regularization: L1 regularization pushes more parameters near zero and gives better accuracy after pruning but before retraining, whereas L2 gives higher accuracy after retraining; overall L2 gives the best pruning results.([Section 3.1, p.3](https://arxiv.org/pdf/1506.02626v3#page=3 "Overall, L2 regularization gives the best pruning results."))
- **c4** During retraining, the surviving weights from the initial training should be kept rather than re-initializing pruned layers (citing fragile co-adapted features); to limit vanishing-gradient effects, CONV parameters are fixed while FC layers are retrained after pruning FC layers, and vice versa.([Section 3.3, p.3](https://arxiv.org/pdf/1506.02626v3#page=3 "So when we retrain the pruned layers, we should keep the surviving parameters instead of re-initializing them."))
- **c5** Iterative pruning (pruning followed by retraining, repeated) increases the pruning rate on AlexNet from 5x to 9x without loss of accuracy compared with single-step aggressive pruning; probabilistic pruning based on absolute value gave worse results.([Section 3.4, p.4](https://arxiv.org/pdf/1506.02626v3#page=4 "Without loss of accuracy, this method can boost pruning rate from 5× to 9× on AlexNet compared with single-step aggressive pruning."))
- **c6** Criterion and implementation: pruning is implemented in Caffe with a mask per weight tensor, and the per-layer threshold is a quality parameter multiplied by the standard deviation of that layer's weights.([Section 4, p.4](https://arxiv.org/pdf/1506.02626v3#page=4 "The pruning threshold is chosen as a quality parameter multiplied by the standard deviation of a layer’s weights."))
- **c7** Cost: the original AlexNet took 75 hours to train on an NVIDIA Titan X, and retraining the pruned AlexNet (at 1/100 of the original initial learning rate) took 173 hours; the authors argue this is less of a concern because pruning is used for model reduction when the model is ready for deployment.([Section 4.2, p.5](https://arxiv.org/pdf/1506.02626v3#page=5 "It took 173 hours to retrain the pruned AlexNet."))
- **c8** Hardware caveat: the authors target fixed-function hardware specialized for sparse DNNs, citing the limitation of general-purpose hardware on sparse computation; they note that after pruning AlexNet and VGGNet are small enough to store all weights on chip.([Section 5, p.8](https://arxiv.org/pdf/1506.02626v3#page=8 "We are targeting our pruning method for ﬁxed-function hardware specialized for sparse DNN, given the limitation of general purpose hardware on sparse computation."))

