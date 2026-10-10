<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Mixture-of-Experts with Expert Choice Routing

- カード: [`arxiv-2202.09368`](../../papers/arxiv-2202.09368.yaml)
- 著者: Yanqi Zhou, Tao Lei, Hanxiao Liu, Nan Du, Yanping Huang, Vincent Zhao, Andrew Dai, Zhifeng Chen, Quoc Le, James Laudon
- 年・掲載: 2022 NeurIPS 2022
- 原論文: [PDF](https://arxiv.org/pdf/2202.09368v2)(arXiv v2、カード作成時に読んだ版)
- タグ: deep-learning, language-modeling, large-language-models, mixture-of-experts, self-supervised, supervised
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Method: instead of tokens choosing top-k experts, each expert independently selects its top-k tokens, where k = n c / e (n tokens in the batch, capacity factor c = average number of experts per token, e experts); this achieves perfect load balancing by design and lets tokens be received by a variable number of experts.([Section 3.2, p.3](https://arxiv.org/pdf/2202.09368v2#page=3 "Despite its simplicity, expert choice achieves perfect load balancing by design."))
- **c2** Pitfall of token-choice routing: the auxiliary balancing loss does not guarantee a balanced load, especially early in training; the authors empirically observe that the over-capacity ratio can reach 20%-40% for some experts, so a significant portion of tokens routed to them will be dropped. Load imbalance can also hurt step latency since it is determined by the most loaded expert.([Section 3.1, p.3](https://arxiv.org/pdf/2202.09368v2#page=3 "Indeed, we empirically observe that the over-capacity ratio can reach 20%–40% for some experts in token choice routing, indicating that a signiﬁcant portion of the tokens routed to these experts will be dropped."))
- **c3** Setup: MoE replaces the FFN in every other Transformer layer; training follows GLaM (1.6T-token GLaM dataset, sequence length 1024, Adafactor, 256K SentencePiece vocabulary, dropout 0), the largest 8B/64E model on 512 TPU v4 chips, and no auxiliary load-balancing loss is used.([Section 4.1, p.6](https://arxiv.org/pdf/2202.09368v2#page=6 "Unlike most related works, we do not impose any auxiliary loss for load balance, such as described in Switch Transformer [10] and GShard [21]."))
- **c4** Budget-matched comparison: expert choice with capacity factor 2 (EC-CF2) matches the per-token activated size and computation of GShard top-2 gating; run for a fixed number of steps, EC-CF2 reaches the same perplexity in less than half the steps, and each GShard top-2 step is 20% slower, which the authors attribute to load imbalance.([Section 4.2, p.6](https://arxiv.org/pdf/2202.09368v2#page=6 "More speciﬁcally, EC-CF2 reaches the same perplexity as GShard top-2 in less than half the steps, and with each GShard top-2 step being 20% slower than our method."))
- **c5** Perplexity vs downstream: on 11 GLUE/SuperGLUE fine-tuning tasks, the 100M/32E setting worked best for both GShard top-2 and EC-CF2 even though 64 and 128 experts give larger capacity, which the authors take to indicate that good training perplexity does not always translate to better downstream performance.([Section 4.4, p.7](https://arxiv.org/pdf/2202.09368v2#page=7 "This result indicates that a good training perplexity does not always translate to better performance of downstream tasks."))
- **c6** Heterogeneity ablation: capping each token at 2 experts (EC-CAP2) decreases average fine-tuning accuracy by 0.8 points, while a cap of 3 is on par with uncapped expert choice; the authors conclude that allowing a variable number of experts per token is indeed helpful.([Section 4.5, p.8](https://arxiv.org/pdf/2202.09368v2#page=8 "This decreases the ﬁne-tuning accuracy by 0.8 points on average."))
- **c7** Limitation: expert choice might not immediately apply to auto-regressive text generation, because the current implementation uses past and future tokens for the top-k selection; it also does not immediately apply when the batch size is very small at serving/inference time. Possible fixes are left to future work.([Section 6, p.9](https://arxiv.org/pdf/2202.09368v2#page=9 "The expert choice method might not immediately apply to auto-regressive text generation as our current implementation takes in the past and future tokens to perform the top-k selection."))
- **c8** Limitation: MoE keeps a large memory footprint since total parameters grow linearly or sub-linearly with the number of experts and require reserving many devices; dynamic (used) power is saved but static (reserved) power is not.([Section 6, p.9](https://arxiv.org/pdf/2202.09368v2#page=9 "Therefore, dynamic (used) power is saved while static (reserved) power is not."))

