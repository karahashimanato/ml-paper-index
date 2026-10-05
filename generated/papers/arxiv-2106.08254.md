<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# BEiT: BERT Pre-Training of Image Transformers

- カード: [`arxiv-2106.08254`](../../papers/arxiv-2106.08254.yaml)
- 著者: Hangbo Bao, Li Dong, Songhao Piao, Furu Wei
- 年・掲載: 2021
- 原論文: [PDF](https://arxiv.org/pdf/2106.08254v2)(arXiv v2、カード作成時に読んだ版)
- タグ: autoencoders, image-classification, masked-image-modeling, representation-learning, self-supervised
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Target: the image is first tokenized into discrete visual tokens with the publicly available DALL-E dVAE tokenizer (vocabulary 8192, 14x14 tokens per image); masked patches are fed to the Transformer and the objective is to recover the original visual tokens.([Abstract, p.1](https://arxiv.org/pdf/2106.08254v2#page=1 "The pre-training objective is to recover the original visual tokens based on the corrupted image patches."))
- **c2** Motivation for tokens rather than pixels: citing [RPG+21], the authors state that pixel-level recovery tends to waste modelling capacity on short-range dependencies and high-frequency details.([Introduction, p.1](https://arxiv.org/pdf/2106.08254v2#page=1 "However, such pixel-level recovery task tends to waste modeling capability on pre-training short-range dependencies and high-frequency details [RPG+21]."))
- **c3** Pre-training setup: ViT-Base, ImageNet-1K training set without labels, augmentations random resized cropping, horizontal flipping and color jittering; at most 75 patches masked (roughly 40%) with blockwise masking; about 500k steps (800 epochs) with 2k batch size, taking about five days on 16 V100 32GB GPUs.([Pre-Training Setup, p.5](https://arxiv.org/pdf/2106.08254v2#page=5 "The 500k training steps take about ﬁve days using 16 Nvidia Telsa V100 32GB GPU cards."))
- **c4** Ablation (300-epoch pre-training, fine-tuned on ImageNet and ADE20K): predicting raw pixels instead of visual tokens is clearly worse, even worse than training from scratch; blockwise masking helps, especially for segmentation and for pixel regression; recovering all visual tokens hurts.([Section 3.3, p.8](https://arxiv.org/pdf/2106.08254v2#page=8 "Our proposed masked image modeling task signiﬁcantly outperforms naive pixel-level auto-encoding."))
- **c5** Tokenizer data: a tokenizer re-trained on ImageNet-1K without labels gives comparable reconstruction loss and ImageNet fine-tuning accuracy to the off-the-shelf DALL-E tokenizer (ablation setup of Section 3.3).([Appendix C, p.15](https://arxiv.org/pdf/2106.08254v2#page=15 "Table 8 shows that our reimplemented tokenizer obtains comparable reconstruction loss and ImageNet ﬁne-tuning performance compared with the off-the-shelf DALL-E tokenizer."))
- **c6** Main evaluation is end-to-end fine-tuning: a linear classifier on average-pooled patch representations is fine-tuned together with BEiT, mostly following DeiT hyperparameters (fewer epochs, larger learning rate with layer-wise decay); intermediate fine-tuning on labeled ImageNet is also used.([Image Classification, p.6](https://arxiv.org/pdf/2106.08254v2#page=6 "We directly follow the most of hyperparameters of DeiT [TCD+20] in our ﬁne-tuning experiments for a fair comparison."))
- **c7** Linear probes (appendix): the authors state that discriminative methods (contrastive, self-distillation) learn to aggregate image-level features into a global vector, which suits linear probing, while generative methods such as iGPT and BEiT do not, which tends to make linear probes difficult. Following iGPT, they average-pool patch states and probe an intermediate layer (best at the 9th layer for BEiT-B and 14th for BEiT-L), training with AdamW for 50 epochs with DINO's augmentations.([Appendix D, p.15](https://arxiv.org/pdf/2106.08254v2#page=15 "In contrast, the second strand of methods, such as iGPT [CRC+20] and ours, usually do not pretrain such global feature aggregation, which tends to make linear probes difﬁcult."))
- **c8** Overall, discriminative methods perform better than generative pre-training on linear probing; the authors attribute this to pre-trained global aggregation in DINO and MoCo v3 and state that full fine-tuning eliminates the gap.([Appendix D, p.16](https://arxiv.org/pdf/2106.08254v2#page=16 "So the pre-training of global aggregation of image-level features is beneﬁcial to linear probing in DINO and MoCo v3, although full ﬁne-tuning eliminates the gap."))

