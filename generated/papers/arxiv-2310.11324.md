<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Quantifying Language Models' Sensitivity to Spurious Features in Prompt Design or: How I learned to start worrying about prompt formatting

- カード: [`arxiv-2310.11324`](../../papers/arxiv-2310.11324.yaml)
- 著者: Melanie Sclar, Yejin Choi, Yulia Tsvetkov, Alane Suhr
- 年・掲載: 2023 ICLR 2024
- 原論文: [PDF](https://arxiv.org/pdf/2310.11324v2)(arXiv v2、カード作成時に読んだ版)
- タグ: in-context-learning, large-language-models, llm-evaluation, natural-language-understanding
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Several widely used open-source LLMs are reported to be extremely sensitive to subtle, meaning-preserving prompt formatting changes in few-shot settings (up to 76 accuracy points for LLaMA-2-13B), and the sensitivity remains when increasing model size, the number of few-shot examples, or performing instruction tuning.([Abstract, p.1](https://arxiv.org/pdf/2310.11324v2#page=1 "Sensitivity remains
even when increasing model size, the number of few-shot examples, or perform-
ing instruction tuning."))
- **c2** Format space and equivalence: the grammar of formats is constructed manually (rather than induced from data) for precision, and was tested by checking it can generate the formatting of 100+ Super-NaturalInstructions tasks; only the casing of descriptors is modified, to guarantee semantic equivalence (paraphrasing descriptors is mentioned as a possible extension). Sensitivity is measured only within the space of formats equivalent to a task's original format.([Section 3.1, p.3](https://arxiv.org/pdf/2310.11324v2#page=3 "The grammar is manually constructed, as opposed to automatically induced
from data, to guarantee a higher level of precision when defining the set of equivalent formats."))
- **c3** Metric and search: for formats p_1..p_n, dataset D and metric m, the performance interval is [min_i m(p_i, D), max_i m(p_i, D)] and the spread is its width; estimated task accuracy is the metric used, on classification tasks. The search is cast as a multi-arm bandit with mini-batch rewards: half of an evaluation budget E searches for the best format and half for the worst, with Thompson sampling (Beta priors) in FormatSpread, compared against UCB and naive sampling.([Section 3.2, p.4](https://arxiv.org/pdf/2310.11324v2#page=4 "Higher spread indicates more sensitivity
to variance within the space of plausible, semantically-equivalent formats."))
- **c4** Protocol: 53 Super-NaturalInstructions tasks (19 multiple-choice, 34 classification); few-shot examples and their order are fixed per task and number of shots to remove that confounder, and are not used for evaluation; datasets are assumed to be of size 1,000. Models: LLaMA-2-7B/13B/70B, Falcon-7B, Falcon-7B-Instruct and GPT-3.5-Turbo (no dated API version was found in the text). Accuracy is measured by probability ranking unless stated otherwise, or by exact prefix matching after normalization.([Experimental Setup, p.5](https://arxiv.org/pdf/2310.11324v2#page=5 "To remove this confounder, we
fix the exact choice and ordering of examples for each task and for a given number of shots n."))
- **c5** With 10 randomly sampled formats per task, the median spread across model and n-shot choices was 7.5 accuracy points, and 20% of tasks consistently had a spread of at least 15 points for all LLaMA-2 settings; the authors note that, because only 10 formats were sampled, this is a lower bound of the true spreads.([Section 4.2, p.5](https://arxiv.org/pdf/2310.11324v2#page=5 "Because this analysis
uses only 10 randomly sampled formats, it represents a lower bound of the true spreads for each
task."))
- **c6** Model comparisons can flip with the format: given M beats M' by at least d under format p, the probability that M' beats M by at least d under another format p' was 0.141 for LLaMA-2-13B vs -70B and 0.140 for LLaMA-2-7B vs Falcon-7B (d = 0.02); often both comparisons were significant under one-sided McNemar tests on 1000 samples. The authors infer that formats may not be inherently good or bad.([Section 4.2, p.5](https://arxiv.org/pdf/2310.11324v2#page=5 "Comparison trends between models are often reversed just by choosing different formats."))
- **c7** Single atomic changes (e.g. one separator, space or casing) are often associated with large accuracy changes: 24% of atomic changes changed accuracy by at least 5 points with exact prefix matching (11% with probability ranking). In sampled triples of successive atomic changes, 32.4% and 33.6% were monotonic (vs 33.3% under random shuffling), which the authors say suggests local search such as simulated annealing may not be effective.([Section 4.3, p.6](https://arxiv.org/pdf/2310.11324v2#page=6 "For example, 24% of atomic changes
have an associated accuracy change of at least 5 points when using exact prefix matching as scoring
criteria (11% when using probability ranking)."))
- **c8** Recommendation: the authors recommend that work evaluating LLMs with prompting-based methods would benefit from reporting a range of performance across plausible formats, because spread may influence conclusions especially when comparing models on benchmarks; they add that single-format evaluation may still be sufficient for many use cases (e.g. a system built on an LLM), and encourage computing FormatSpread when comparing systems to out-of-the-box models.([Discussion, p.9](https://arxiv.org/pdf/2310.11324v2#page=9 "Thus, we recommend that work evaluating LLMs with prompting-based methods would
benefit from reporting a range of performance across plausible formats."))

