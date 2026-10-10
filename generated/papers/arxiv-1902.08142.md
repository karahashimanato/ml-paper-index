<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Evaluating the Search Phase of Neural Architecture Search

- カード: [`arxiv-1902.08142`](../../papers/arxiv-1902.08142.yaml)
- 著者: Kaicheng Yu, Christian Sciuto, Martin Jaggi, Claudiu Musat, Mathieu Salzmann
- 年・掲載: 2019
- 原論文: [PDF](https://arxiv.org/pdf/1902.08142v3)(arXiv v3、カード作成時に読んだ版)
- タグ: deep-learning, image-classification, language-modeling, neural-architecture-search
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Main finding: on average the evaluated state-of-the-art NAS algorithms perform similarly to the random policy, and weight sharing degrades the ranking of NAS candidates to the point of not reflecting their true performance, reducing the effectiveness of the search.([Abstract, p.1](https://arxiv.org/pdf/1902.08142v3#page=1 "On average, the state-of-the-art NAS algorithms perform similarly to the random policy;"))
- **c2** Protocol: the random policy uniformly samples an architecture from the same search space as the NAS algorithms and trains it with the same hyperparameters as the NAS solutions; to reduce randomness, the search with each policy is repeated with different random seeds.([Introduction, p.2](https://arxiv.org/pdf/1902.08142v3#page=2 "To reduce randomness, the search using each policy, i.e., random and NAS ones, is repeated several times, with different random seeds."))
- **c3** Standard-space setup: DARTS, NAO, ENAS and BayesNAS were compared with random sampling in the DARTS RNN (12-node) and CNN (7-node) spaces, 10 runs each with different initializations, using the authors-provided hyperparameters and code in the search phase; the chosen architectures were trained from scratch for 1000 epochs (RNN) and 600 (CNN).([Section 4.1, p.5](https://arxiv.org/pdf/1902.08142v3#page=5 "During the search phase, we used the authors-provided hyper-parameters and code for each policy."))
- **c4** Earlier comparisons to random search are described as not giving the random policy a fair chance: Pham et al. (2018) reported a single random architecture, and Liu et al. (2018b) one selected among 8 random architectures after only 300 epochs of training.([Section 2, p.3](https://arxiv.org/pdf/1902.08142v3#page=3 "While some works have provided partial comparisons to random search, these comparisons unfortunately did not give a fair chance to the random policy."))
- **c5** Interpretation caveat: not significantly outperforming random sampling does not necessarily mean the algorithms perform poorly; rather the search space has been sufficiently constrained that even a random architecture performs well. The authors therefore also test reduced spaces that can be evaluated exhaustively.([Introduction, p.2](https://arxiv.org/pdf/1902.08142v3#page=2 "Note that this does not necessarily mean that these algorithms perform poorly, but rather that the search space has been sufﬁciently constrained so that even a random architecture in this space provides good results."))
- **c6** In the NASBench-101 7-node space (10 runs per method), the best test accuracy found by DARTS, NAO or ENAS is 93.33 (NAO), much lower than the ground-truth best of 95.06; ENAS and DARTS are stated to have only 7% and 24% chance to surpass the random policy.([Section 4.2, p.7](https://arxiv.org/pdf/1902.08142v3#page=7 "The best test accuracy found by these methods is 93.33, by NAO, which remains much lower than the ground-truth best of 95.06."))
- **c7** Weight-sharing ranking: in the reduced spaces, the architecture rankings obtained with and without weight sharing are uncorrelated in the RNN space (Kendall tau -0.004 over 10 runs) and have little correlation in the CNN space (0.195 over 10 runs); since such rankings serve as training data for the NAS sampler, this further explains the small margin over random search.([Introduction, p.2](https://arxiv.org/pdf/1902.08142v3#page=2 "the architecture rankings obtained with and without weight sharing are entirely uncorrelated in RNN space"))
- **c8** Scope of the weight-sharing analysis: weight-sharing rankings were obtained with uniform per-minibatch architecture sampling (described as equivalent to Single Path One Shot), and DARTS was not included because it has no discrete solutions during the search, so solution ranking does not apply.([Section 4.3, p.7](https://arxiv.org/pdf/1902.08142v3#page=7 "As DARTS does not have discrete representations of the solutions during the search, the idea of solution ranking does not apply."))
- **c9** When NAO and ENAS are trained without weight sharing in NASBench, performance is on average 1% higher than with it, and the probability to surpass random search increases from 0.62 to 0.92 for NAO and from 0.07 to 0.90 for ENAS.([Section 4.3, p.8](https://arxiv.org/pdf/1902.08142v3#page=8 "Furthermore, the probability to surpass random search increases from 0.62 to 0.92 for NAO and from 0.07 to 0.90 for ENAS."))

