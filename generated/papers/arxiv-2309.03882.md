<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Large Language Models Are Not Robust Multiple Choice Selectors

- カード: [`arxiv-2309.03882`](../../papers/arxiv-2309.03882.yaml)
- 著者: Chujie Zheng, Hao Zhou, Fandong Meng, Jie Zhou, Minlie Huang
- 年・掲載: 2023 ICLR 2024
- 原論文: [PDF](https://arxiv.org/pdf/2309.03882v4)(arXiv v4、カード作成時に読んだ版)
- タグ: in-context-learning, large-language-models, llm-evaluation, natural-language-understanding
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Answer-moving attack: in 0-shot MMLU, always moving the golden answers to one option position causes large performance fluctuations; e.g. moving them to D lowers gpt-3.5-turbo accuracy by 6.3 (67.2 to 60.9), while moving them to A raises llama-30B by 15.2 so that it surpasses gpt-3.5-turbo (68.2 vs 65.3), contrasting with their original 53.1 vs 67.2.([Introduction, p.1](https://arxiv.org/pdf/2309.03882v4#page=1 "For instance, moving the golden answers
to position D degrades the accuracy of gpt-3.5-turbo by 6.3 (from 67.2 to 60.9)."))
- **c2** Definition and metric: selection bias is the model's behavioral bias to select specific option IDs as answers; instead of counting predictions (susceptible to label imbalance) it is measured by the standard deviation of the recalls of the option IDs (RStd). This presumes golden answers are randomly placed, which the authors support by showing (Appendix C) that random shuffling of options does not obviously change selection bias.([Measurement of selection bias, p.3](https://arxiv.org/pdf/2309.03882v4#page=3 "In our study, selection bias is defined as the model’s behavioral bias to select specific option IDs as
answers."))
- **c3** Protocol: 20 decoder-only LLMs (llama-7/13/30/65B, llama-2(-chat)-7/13/70B, vicuna-v1.3-7/13/33B, vicuna-v1.5-7/13B, falcon(-inst)-7/40B, gpt-3.5-turbo-0613) on MMLU, ARC-Challenge and CommonsenseQA; for open models the prediction is the option-ID token (A-E) with maximal probability, while for the API model gpt-3.5-turbo (no output probabilities) the first generated token at temperature 0 is compared with the golden answer; mainly 0-shot, with 5-shot experiments using development-set examples.([Section 2.1, p.3](https://arxiv.org/pdf/2309.03882v4#page=3 "For
gpt-3.5-turbo, we compare the golden answer with the first generated token, with the decoding
temperature set to 0."))
- **c4** Observations: selection bias is prevalent and varies with model families and sizes without a consistent pattern within a family trained on the same data, so the authors speculate it arises from complex interactions of training data composition and ordering, model capacity and other factors; within a model it shows moderate similarity across domains; in-context examples can reduce but may also alter it.([Section 2.3, p.3](https://arxiv.org/pdf/2309.03882v4#page=3 "We speculate that selection bias arises as a product of
complex interactions between training data composition and ordering, model capacity (number of
parameters), and other factors like hyperparameters."))
- **c5** Cause: to separate token bias (prior mass on specific ID tokens) from position bias (favoring options at specific positions), the authors shuffle option IDs (leaving only token bias) and remove option IDs (scoring length-normalized option likelihoods). Removing IDs notably reduces RStd, in most cases across models, benchmarks and 2-5 options, while shuffling IDs changes it little, and alternative ID symbols (a/b/c/d, 1/2/3/4, (A)) give no remarkable reduction; the remaining position bias is described as somewhat present but quite irregular, depending on models and tasks.([Section 2.4, p.4](https://arxiv.org/pdf/2309.03882v4#page=4 "These results confirm
that the model’s token bias is one primary intrinsic cause of selection bias."))
- **c6** Simple prompting strategies applied to gpt-3.5-turbo, an explicit debiasing instruction in the system message and Chain-of-Thought ('Let's think step by step'), could not mitigate selection bias well; the authors suggest it is an inherent behavioral bias that cannot be addressed by simple prompt engineering. Removing option IDs reduces bias but usually degrades performance, so they also suggest it is not a practical mitigation.([Section 2.6, p.5](https://arxiv.org/pdf/2309.03882v4#page=5 "It suggests that selection bias is an inherent behavioral
bias of LLMs that cannot be addressed by simple prompt engineering."))
- **c7** PriDe assumptions: the observed distribution over option IDs is decomposed into a prior over IDs (covering both token and position bias) times a debiased distribution over option contents (a conditional independence assumption); the debiased part is assumed invariant to option order and the prior is assumed to depend only on the question. The per-sample prior is obtained label-free from permuted inputs (Eq. 7), averaged over K test samples into a global prior, which is divided out for the remaining samples (Eq. 8), relying on the observed cross-domain similarity of selection bias.([Section 3.3, p.6](https://arxiv.org/pdf/2309.03882v4#page=6 "Recall our observation in §2.3 that selection bias within the same model displays a moderate cross-
domain similarity."))
- **c8** Caveats of PriDe: priors estimated on one domain showed reasonable debiasing transfer to others, but there may be a slight performance degradation when the domain gap is large (e.g. STEM/Humanities to ARC); PriDe is not designed to improve performance, and the authors suggest updating the prior with new samples under predictable domain shifts. In the main experiments, gpt-3.5-turbo's distribution is approximated by 100 sampled answers and PriDe results are averaged over 5 runs.([Section 4.2, p.8](https://arxiv.org/pdf/2309.03882v4#page=8 "we suggest updating the estimated prior using new
samples when there are predictable domain shifts in test samples"))

