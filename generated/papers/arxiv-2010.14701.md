<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Scaling Laws for Autoregressive Generative Modeling

- カード: [`arxiv-2010.14701`](../../papers/arxiv-2010.14701.yaml)
- 著者: Tom Henighan, Jared Kaplan, Mor Katz, Mark Chen, Christopher Hesse, Jacob Jackson, Heewoo Jun, Tom B. Brown, Prafulla Dhariwal, Scott Gray, Chris Hallacy, Benjamin Mann, Alec Radford, Aditya Ramesh, Nick Ryder, Daniel M. Ziegler, John Schulman, Dario Amodei, Sam McCandlish
- 年・掲載: 2020
- 原論文: [PDF](https://arxiv.org/pdf/2010.14701v2)(arXiv v2、カード作成時に読んだ版)
- タグ: deep-learning, image-classification, scaling-laws, self-supervised
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Main claim: in four domains (generative image modeling, video, multimodal image-text, math problem solving) autoregressive Transformers improve smoothly with model size and compute, following a power-law plus constant scaling law.([Abstract, p.1](https://arxiv.org/pdf/2010.14701v2#page=1 "In all cases autoregressive Transformers smoothly improve in performance as model size and compute budgets increase, following a power-law plus constant scaling law."))
- **c2** Compute-optimal model size: the optimal model size depends on the compute budget through a power law whose exponents are nearly universal across data domains.([Abstract, p.1](https://arxiv.org/pdf/2010.14701v2#page=1 "The optimal model size also depends on the compute budget through a power-law, with exponents that are nearly universal across all data domains."))
- **c3** Compute counting: C is defined theoretically as 6NE, with N the non-embedding parameter count and E the total tokens processed in training (a footnote explains the factor 6 as 2 for add-multiply times 3 for forward and backward passes); the critical-batch-size adjustment used in Kaplan et al. was not made here.([Compute Scaling and Optimal Model Sizes, p.9](https://arxiv.org/pdf/2010.14701v2#page=9 "We deﬁne C theoretically rather than empirically, and approximate7 it as C ≡6NE where N is the non-embedding parameter count (model size) and E = SB is the total number of tokens processed during training"))
- **c4** Caveat on convergence: L(N) uses the loss at (or as close as feasible to) convergence, but the largest models did not fully converge, so the authors warn against over-interpreting the irreducible loss as entropy and the reducible loss as KL divergence.([Model Size Scaling and Aspect Ratios, p.9](https://arxiv.org/pdf/2010.14701v2#page=9 "Thus caution is warranted when interpreting L(N) trends according to equation (1.2) and identifying the irreducible loss as an entropy, and the reducible loss as a KL divergence."))
- **c5** Caveat on extrapolation: the sub-linear data-vs-model-size conclusion for compute-optimal training is stated together with the caution that no models were trained in a regime where compute-optimal training actually implies D much smaller than N.([Compute Scaling and Optimal Model Sizes, p.10](https://arxiv.org/pdf/2010.14701v2#page=10 "As a word of caution, we have yet to train models in a regime where compute optimal training actually implies D ≪N numerically."))
- **c6** Attribution: the language-modeling compute scaling results are taken from GPT-3 ([BMR+20]) and the language Nopt(C) from Kaplan et al. ([KMH+20]), not from new experiments in this paper.([Summary of scaling laws (Table 1 caption), p.7](https://arxiv.org/pdf/2010.14701v2#page=7 "The compute scaling results and data for language are from [BMR+20], while Nopt(C) comes from [KMH+20]."))
- **c7** Downstream: when generative image models are finetuned for ImageNet classification, classification loss follows a power law in model size even beyond where generative loss approaches its irreducible value; the authors conclude that approaching the irreducible loss does not necessarily indicate diminishing returns for representation quality.([Summary of Results, p.6](https://arxiv.org/pdf/2010.14701v2#page=6 "We conclude that the approach to the irreducible loss does not necessarily indicate diminishing returns for representation quality or semantic content."))

