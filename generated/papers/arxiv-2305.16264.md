<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Scaling Data-Constrained Language Models

- カード: [`arxiv-2305.16264`](../../papers/arxiv-2305.16264.yaml)
- 著者: Niklas Muennighoff, Alexander M. Rush, Boaz Barak, Teven Le Scao, Aleksandra Piktus, Nouamane Tazi, Sampo Pyysalo, Thomas Wolf, Colin Raffel
- 年・掲載: 2023
- 原論文: [PDF](https://arxiv.org/pdf/2305.16264v5)(arXiv v5、カード作成時に読んだ版)
- タグ: deep-learning, language-modeling, large-language-models, scaling-laws, self-supervised
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Proposal: a scaling law for compute optimality that accounts for the decreasing value of repeated tokens and of excess parameters, which the authors propose and empirically validate.([Abstract, p.1](https://arxiv.org/pdf/2305.16264v5#page=1 "We propose and empirically validate a scaling law for compute optimality that accounts for the decreasing value of repeated tokens and excess parameters."))
- **c2** Main empirical claim (in experiments the abstract describes as ranging up to 900 billion training tokens and 9 billion parameter models): with constrained data and a fixed compute budget, training for up to 4 epochs of repeated data gives negligible changes in loss compared with unique data; with more repetition the value of added compute eventually decays to zero.([Abstract, p.1](https://arxiv.org/pdf/2305.16264v5#page=1 "We find that with constrained data for a fixed compute budget, training with up to 4 epochs of repeated data yields negligible changes to loss compared to having unique data."))
- **c3** Experimental range and setup: GPT-2 architecture and tokenizer, models up to 8.7B parameters trained for up to 900B total tokens on subsets of C4, cosine schedules decaying 10x following Chinchilla, no early stopping, other hyperparameters from prior work; loss is reported on a held-out test set unless otherwise specified (unlike the training loss used by Chinchilla).([Experimental Setup, p.5](https://arxiv.org/pdf/2305.16264v5#page=5 "Models have up to 8.7 billion parameters and are trained for up to 900 billion total tokens."))
- **c4** Compute counting: the paper uses Kaplan et al.'s approximation FLOPs(N, D) ≈ 6ND, with D the number of tokens processed.([Background (footnote), p.3](https://arxiv.org/pdf/2305.16264v5#page=3 "In this work we use [46]’s approximation for the compute cost: FLOPs(N, D) ≈6ND, where N denotes the number of model parameters and D denotes the number of tokens processed."))
- **c5** Disagreement with Chinchilla, as stated by this paper: when data are repeated, its fit suggests allocating most additional compute to more epochs rather than more parameters, which contrasts with the Chinchilla scaling laws' equal scaling; the paper notes that Chinchilla does not repeat the entire training data and its parametric fit assumes single-epoch training, so there is no guarantee its predictions hold for repeated data.([Results: Resource Allocation for Data-Constrained Scaling, p.6](https://arxiv.org/pdf/2305.16264v5#page=6 "However, note that they do not repeat the entire training data and their parametric fit explicitly relies on the assumption that models are trained for a single epoch only."))
- **c6** Model limitation: the paper states that adding parameters and epochs causes loss to decrease and eventually increase again (suggesting too much compute can hurt), but the proposed formula and its predicted isoLoss contours do not model the possibility that excess epochs or parameters hurt performance (the authors expect appropriate regularization could prevent this).([Results: Resource Allocation for Data-Constrained Scaling, p.7](https://arxiv.org/pdf/2305.16264v5#page=7 "Thus, our formula presented in §3 and its predicted isoLoss contours in Figure 3 do not model the possibility that excess epochs or parameters could hurt performance."))
- **c7** Stated limitation: the returns from additional epochs may depend heavily on hyperparameters such as learning rate, dropout or optimizer; most hyperparameters were fixed to commonly used values.([Appendix Q (Limitations and Future Work), p.41](https://arxiv.org/pdf/2305.16264v5#page=41 "The returns from additional epochs may heavily depend on hyperparameters such as learning rate, dropout, or the optimizer choice."))

