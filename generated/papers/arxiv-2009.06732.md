<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Efficient Transformers: A Survey

- カード: [`arxiv-2009.06732`](../../papers/arxiv-2009.06732.yaml)
- 著者: Yi Tay, Mostafa Dehghani, Dara Bahri, Donald Metzler
- 年・掲載: 2020
- 原論文: [PDF](https://arxiv.org/pdf/2009.06732v3)(arXiv v3、カード作成時に読んだ版)
- タグ: deep-learning, efficiency-evaluation, efficient-attention, mixture-of-experts
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Scope: the survey characterizes a selection of efficiency-oriented "X-former" Transformer variants (e.g. Reformer, Linformer, Performer, Longformer), many of which target computational and memory efficiency, across multiple domains.([Abstract, p.1](https://arxiv.org/pdf/2009.06732v3#page=1 "With the aim of helping the avid researcher navigate this ﬂurry, this paper characterizes a large and thoughtful selection of recent eﬃciency-ﬂavored “X-former” models, providing an organized and comprehensive overview of existing work and models across multiple domains."))
- **c2** Contribution: the paper proposes a taxonomy of efficient Transformer models organized by technical innovation and primary use case.([Introduction, p.2](https://arxiv.org/pdf/2009.06732v3#page=2 "We propose a taxonomy of eﬃcient Transformer models, characterizing them by their technical innovation and primary use case."))
- **c3** Definition of efficiency used: the survey says efficiency can mean memory footprint (relevant when accelerator memory is limited) or computational cost such as FLOPs in training and inference, and it uses both senses, with particular interest in large inputs.([Introduction, p.2](https://arxiv.org/pdf/2009.06732v3#page=2 "Throughout this survey, we refer to the eﬃciency of Transformers both in terms of memory and computation."))
- **c4** Cost composition: the survey notes that self-attention is only part of a Transformer's compute; the survey states that the two-layer feed-forward layers account for approximately half the compute time and/or FLOPs and notes that much recent work (citing Lepikhin et al., 2020; Fedus et al., 2021) has explored sparsity to scale up the FFN without incurring compute costs; it calls efficiency and computational cost a complicated affair and refers readers to Dehghani et al. (2021).([Background on Transformers, p.5](https://arxiv.org/pdf/2009.06732v3#page=5 "A non-trivial amount of compute still stems from the two layer feed-forward layers at every Transformer block (approximately half the compute time and/or FLOPs)."))
- **c5** Evaluation caveat: there is no easy way to compare efficient Transformers side by side; papers choose their own benchmarks and differ in model sizes and configurations (and some conflate with pretraining), making it difficult to attribute performance gains.([Discussion (On Evaluation), p.25](https://arxiv.org/pdf/2009.06732v3#page=25 "This is also coupled with diﬀerent hyperparameter set-tings like model sizes and conﬁgurations which can make it diﬃcult to correctly attribute the reason for the performance gains."))
- **c6** Benchmark caveat: the survey notes that Long Range Arena (an attempt to unify evaluation that benchmarked 10 xformer variants) was designed for encoder-only mode and does not cover autoregressive tasks that need causal masking.([Discussion (On Evaluation), p.26](https://arxiv.org/pdf/2009.06732v3#page=26 "It is good to note that LRA was designed for evalu-ating Transformers in encoder-only mode and do not consider generative (or autoregressive tasks) that require causal masking."))
- **c7** 'Efficiency misnomer' caveat: in the retrospective of the updated version (Section 4.4), the authors state that efficient attention models do not always make the Transformer fast; many may make the model much slower, many linear attention models observe no speed or memory gain at all when the sequence length is short, and many have painful requirements for causal masking (or TPU packing) (citing Choromanski et al., 2020b; Peng et al., 2021; Wang et al., 2020c), often substantially trading off throughput for linear complexity. They refer to Dehghani et al. (2021) for more on this efficiency misnomer.([Retrospective (Discussion), p.30](https://arxiv.org/pdf/2009.06732v3#page=30 "Moreover, many linear attention models do not observe any speed or memory gain at all if the sequence length is short."))

