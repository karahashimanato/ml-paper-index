<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Deep Compression: Compressing Deep Neural Networks with Pruning, Trained Quantization and Huffman Coding

- カード: [`arxiv-1510.00149`](../../papers/arxiv-1510.00149.yaml)
- 著者: Song Han, Huizi Mao, William J. Dally
- 年・掲載: 2015 ICLR 2016
- 原論文: [PDF](https://arxiv.org/pdf/1510.00149v5)(arXiv v5、カード作成時に読んだ版)
- タグ: deep-learning, image-classification, model-compression, pruning, quantization, supervised
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Abstract: pruning, trained quantization and Huffman coding together reduce the storage of neural networks by 35x to 49x without affecting accuracy; AlexNet goes from 240MB to 6.9MB (35x) and VGG-16 from 552MB to 11.3MB (49x); pruning cuts connections by 9x to 13x and quantization reduces bits per connection from 32 to 5.([Abstract, p.1](https://arxiv.org/pdf/1510.00149v5#page=1 "On the ImageNet dataset, our method reduced the storage required by AlexNet by 35×, from 240MB to 6.9MB, without loss of accuracy."))
- **c2** The pruning stage builds on Han et al. (2015) (the authors' own earlier work, arxiv-1506.02626): train, remove connections with weights below a threshold, and retrain; the sparse structure is stored in CSR/CSC with index differences encoded in 8 bits for conv layers and 5 bits for fc layers.([Section 2, p.2](https://arxiv.org/pdf/1510.00149v5#page=2 "We build on top of that approach."))
- **c3** Weight sharing: per layer (not across layers), k-means clustering on the trained weights minimizes the within-cluster sum of squares, so each connection stores only a log2(k)-bit index into a codebook; unlike HashedNets, sharing is determined after the network is fully trained.([Section 3.1, p.4](https://arxiv.org/pdf/1510.00149v5#page=4 "We use k-means clustering to identify the shared weights for each layer of a trained network, so that all the weights that fall into the same cluster will share the same weight."))
- **c4** Trained quantization: the shared weights (centroids) are fine-tuned, with the gradient of each centroid being the sum of the gradients of the weights assigned to it.([Section 3.3, p.5](https://arxiv.org/pdf/1510.00149v5#page=5 "During back-propagation, the gradient for each shared weight is calculated and used to update the shared weight."))
- **c5** Among Forgy (random), density-based and linear centroid initialization, linear initialization gives better accuracy in all cases except at 3 bits; the authors explain this by linear initialization keeping large centroids, citing their earlier pruning work for the claim that large weights matter more.([Section 6.2, p.8](https://arxiv.org/pdf/1510.00149v5#page=8 "Linear initialization outperforms the density initialization and random initialization in all cases except at 3 bits."))
- **c6** Huffman coding the biased distributions of quantized weights and sparse index differences saves 20% to 30% of network storage; it requires no training and is applied offline after fine-tuning.([Section 4, p.5](https://arxiv.org/pdf/1510.00149v5#page=5 "Experiments show that Huffman coding these non-uniformly distributed values saves 20%"))
- **c7** Individually, pruned or quantized AlexNet loses accuracy significantly when compressed below 8% of its original size, but combined the network can be compressed to 3% with no loss of accuracy; the authors explain that quantization works well on the pruned network because fewer weights (6.7 million vs 60 million) are quantized with the same number of centroids.([Section 6.1, p.7](https://arxiv.org/pdf/1510.00149v5#page=7 "But when combined, as shown in the red line, the network can be compressed to 3% of original size with no loss of accuracy."))
- **c8** Speed/energy benchmarks cover only the FC layers of the pruned (not quantized) model at batch size 1, because current BLAS libraries do not support indirect look-up and relative indexing; pruned layers give 3x to 4x speedup over dense on average, but with batching (matrix-matrix multiplication) the pruned network no longer shows its advantage.([Section 6.3, p.10](https://arxiv.org/pdf/1510.00149v5#page=10 "In this scenario, pruned network no longer shows its advantage."))

