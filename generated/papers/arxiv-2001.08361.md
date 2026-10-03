<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Scaling Laws for Neural Language Models

- カード: [`arxiv-2001.08361`](../../papers/arxiv-2001.08361.yaml)
- 著者: Jared Kaplan, Sam McCandlish, Tom Henighan, Tom B. Brown, Benjamin Chess, Rewon Child, Scott Gray, Alec Radford, Jeffrey Wu, Dario Amodei
- 年・掲載: 2020
- 原論文: [PDF](https://arxiv.org/pdf/2001.08361v1)(arXiv v1、カード作成時に読んだ版)
- タグ: deep-learning, efficiency-evaluation, language-modeling, large-language-models, scaling-laws, self-supervised
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Main claim: language-model cross-entropy loss scales as a power law with model size, dataset size and training compute, with some trends spanning more than seven orders of magnitude.([Abstract, p.1](https://arxiv.org/pdf/2001.08361v1#page=1 "The loss scales as a power-law with model size, dataset size, and the amount of compute used for training, with some trends spanning more than seven orders of magnitude."))
- **c2** Experimental range: the relations are stated to hold across eight orders of magnitude in minimum compute, six in model size and over two in dataset size; the fitted numerical values are tied to the WebText2 training set (next sentence).([Summary of Scaling Laws, p.5](https://arxiv.org/pdf/2001.08361v1#page=5 "These relations hold across eight orders of magnitude in Cmin, six orders of magnitude in N, and over two orders of magnitude in D."))
- **c3** Compute counting: training compute is estimated as about 6N floating point operations per training token (forward pass about 2N, backward about twice that), excluding embedding parameters and context-dependent terms.([Parameter and Compute Scaling of Transformers, p.7](https://arxiv.org/pdf/2001.08361v1#page=7 "Accounting for the backwards pass (approximately twice the compute as the forwards pass), we then deﬁne the estimated non-embedding compute as C ≈6N ﬂoating point operators per training token."))
- **c4** Compute-optimal allocation: as the compute budget increases it should be spent primarily on larger models, without dramatic increases in training time or dataset size (a conclusion drawn from the paper's power-law fits on WebText2 Transformer LMs within the studied range).([Summary of Scaling Laws, p.5](https://arxiv.org/pdf/2001.08361v1#page=5 "As the computational budget C increases, it should be spent primarily on larger models, without dramatic increases in training time or dataset size (see Figure 3)."))
- **c5** Training protocol: unless otherwise noted, all training runs used a learning-rate schedule with a 3000-step linear warmup followed by cosine decay to zero (models were trained for a fixed number of steps unless otherwise noted).([Training Procedures, p.7](https://arxiv.org/pdf/2001.08361v1#page=7 "Unless otherwise noted, all training runs included in our data used a learning rate schedule with a 3000 step linear warmup followed by a cosine decay to zero."))
- **c6** Stated limit: far beyond the studied scales, the L(Cmin) and L(D) trends contradict each other, so the authors say the scaling laws must break down before that point (they conjecture the intersection marks maximal Transformer LM performance; values are highly uncertain).([Contradictions and a Conjecture, p.17](https://arxiv.org/pdf/2001.08361v1#page=17 "This implies that our scaling laws must break down before this point, but we conjecture that the intersection point has a deeper meaning: it provides an estimate of the point at which Transformer language models reach maximal performance."))
- **c7** Disagreement with prior work: the paper states that Hestness et al. ([HNA+17]) found super-linear scaling of dataset size with model size (i.e. data growing faster than model size), whereas this paper finds sub-linear scaling (data growing more slowly than model size; in Section 4 this is the dataset size needed to avoid overfitting as model size grows).([Related Work, p.18](https://arxiv.org/pdf/2001.08361v1#page=18 "Note, however, that [HNA+17] found super-linear scaling of dataset size with model size, whereas we ﬁnd a sub-linear scaling."))

