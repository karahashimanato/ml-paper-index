<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Compressing LLMs: The Truth is Rarely Pure and Never Simple

- カード: [`arxiv-2310.01382`](../../papers/arxiv-2310.01382.yaml)
- 著者: Ajay Jaiswal, Zhe Gan, Xianzhi Du, Bowen Zhang, Zhangyang Wang, Yinfei Yang
- 年・掲載: 2023
- 原論文: [PDF](https://arxiv.org/pdf/2310.01382v2)(arXiv v2、カード作成時に読んだ版)
- タグ: large-language-models, model-compression, post-hoc, post-training-quantization, pruning, quantization
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Critique of evaluation practice: state-of-the-art LLM compression methods are evaluated mostly with perplexity, a metric that is widely questioned even for dense LLMs; the paper re-evaluates them with LLM-KICK.([Abstract, p.1](https://arxiv.org/pdf/2310.01382v2#page=1 "As recent research efforts are focused on developing increasingly sophisticated compression methods, our work takes a step back and re-evaluates the effectiveness of existing SoTA compression methods, which rely on a fairly simple and widely questioned metric, perplexity (even for dense LLMs)."))
- **c2** Setup: compression methods are SparseGPT, Wanda and one-shot magnitude pruning (unstructured and N:M sparsity) plus GPTQ quantization, applied to Vicuna models without fine-tuning.([LLM-KICK setup, p.4](https://arxiv.org/pdf/2310.01382v2#page=4 "our work primarily focuses on the top-2 existing training-free and data-free LLM pruning techniques (i.e., SparseGPT (Frantar & Alistarh, 2023) and Wanda (Sun et al., 2023)), along with the baseline of One-shot Magnitude-based Pruning (Han et al., 2016), plus a popular quantization technique (GPTQ)"))
- **c3** Evaluation metric definition: a compressed LLM is called 'matching' if its task performance drops by at most 5% relative to the dense model, a tolerance the authors deliberately relaxed from prior work, which used the dense performance itself or a 1% margin as the matching threshold.([LLM-KICK setup, p.4](https://arxiv.org/pdf/2310.01382v2#page=4 "In this work, we consider ϵ0 to be ≤5% of the performance of f(x; θ, T)."))
- **c4** Tasks: factoid QA (FreebaseQA), multiple-choice reasoning QA (MMLU), in-context retrieval-augmented QA, in-context summarization (CNN/DailyMail, judged by GPT-4 against GPT-3.5 summaries) and instruction following.([LLM-KICK tasks, p.7](https://arxiv.org/pdf/2310.01382v2#page=7 "For evaluation, similar to Zheng et al. (2023), we propose to use GPT-4 as a judge, which compares the compressed LLM generated summaries wrt. GPT-3.5 (text-davinci-003) generated summaries."))
- **c5** Main findings: pruning methods fail for N:M sparsity on knowledge-intensive tasks; current quantization methods are more successful than pruning; pruned LLMs at 50% or more sparsity remain robust in-context retrieval and summarization systems.([Abstract, p.1](https://arxiv.org/pdf/2310.01382v2#page=1 "and fail for N:M sparsity in knowledge-intensive tasks; current quantization methods are more successful than pruning; yet, pruned LLMs even at ≥50% sparsity are robust in-context retrieval and summarization systems"))
- **c6** Even non-aggressive 8-bit GPTQ quantization shows a roughly 8-10% drop on factoid QA, so the authors argue 8-bit quantization is not yet solved.([Results (factoid QA), p.5](https://arxiv.org/pdf/2310.01382v2#page=5 "3 ∼8-10% drop in performance for non-aggressive 8-bit quantization indicates that along with chasing for aggressive quantization levels (1-2 bits), it is also important to focus on yet unsolved 8-bit quantization."))
- **c7** Limitation: the evaluation is restricted mainly to Vicuna (decoder-only) models.([Conclusion and limitations, p.9](https://arxiv.org/pdf/2310.01382v2#page=9 "We primarily restrict our evaluation to Vicuna (decoder-only architecture) due to its open-source license, high performance, and instruction-following ability."))

