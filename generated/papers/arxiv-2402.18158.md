<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Evaluating Quantized Large Language Models

- カード: [`arxiv-2402.18158`](../../papers/arxiv-2402.18158.yaml)
- 著者: Shiyao Li, Xuefei Ning, Luning Wang, Tengxuan Liu, Xiangsheng Shi, Shengen Yan, Guohao Dai, Huazhong Yang, Yu Wang
- 年・掲載: 2024
- 原論文: [PDF](https://arxiv.org/pdf/2402.18158v2)(arXiv v2、カード作成時に読んだ版)
- タグ: large-language-models, model-compression, post-hoc, post-training-quantization, quantization
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Scope: PTQ of weights, activations and KV cache on 11 model families from 125M to 180B parameters, evaluated on basic NLP, emergent ability, trustworthiness, dialogue and long-context tasks.([Abstract, p.1](https://arxiv.org/pdf/2402.18158v2#page=1 "The evaluation encompasses five types of tasks: basic NLP, emergent ability, trustworthiness, dialogue, and long-context tasks."))
- **c2** Quantization format: uniform quantization; weight-only uses asymmetric group-wise quantization, weight-activation uses group-wise weights with symmetric per-token activations, and KV cache uses asymmetric group-wise quantization of keys and values.([Preliminaries, p.3](https://arxiv.org/pdf/2402.18158v2#page=3 "For Weight-only Quantization, we apply asymmetric group-wise quantization as shown in Figure 1 (b)."))
- **c3** Tensor-type finding: in most cases larger models tolerate weight-only and KV cache quantization better but tolerate activation quantization worse, which the authors relate to activation kurtosis (outliers) increasing with model size.([Results (basic NLP tasks), p.4](https://arxiv.org/pdf/2402.18158v2#page=4 "Notably, the Kurtosis of the Activation increases significantly with the size of the model, which means more outliers in the Activation tensors of larger LLMs."))
- **c4** Task-dependent degradation: in the Ethics benchmark, a W3-quantized model stops refusing some ethical questions and gives informative answers, so the measured accuracy increases after quantization; the paper notes this kind of effect appears only in small models (< 7B), while for larger models lower bit-width means lower performance.([Results (trustworthiness), p.7](https://arxiv.org/pdf/2402.18158v2#page=7 "The FP16 LLM refrains from answering some ethical questions, but for W3, the model breaks this limitation and begins to provide informative answers."))
- **c5** Dialogue is scored by GPT-4 (MT-bench single-answer grading); most families can be quantized to W8, W8A8 and KV4 without significant loss of GPT-4 score, while lower bit-widths lead to sentence-level and then token-level repetition.([Results (dialogue), p.8](https://arxiv.org/pdf/2402.18158v2#page=8 "Most LLM families can be quantized to W8, W8A8, and KV4 without significant loss of GPT-4 score (< 2%), as shown in Table 1."))
- **c6** Long-context tasks are more sensitive to KV cache quantization than to weight-only or weight-activation quantization for most LLMs.([Results (long-context), p.9](https://arxiv.org/pdf/2402.18158v2#page=9 "For long-context tasks (≥4k), most LLMs are more sensitive to KV Cache Quantization than Weight-only and Weight-Activation Quantization."))
- **c7** SOTA methods: AWQ improves weight-only quantized LLMs but cannot restore W2 models, and SmoothQuant only partially recovers W4A4.([Appendix (SOTA quantization methods), p.21](https://arxiv.org/pdf/2402.18158v2#page=21 "However, in the case of W2 quantization, where quantized LLMs lose their abilities entirely, AWQ cannot restore the corrupted performances."))
- **c8** Limitations: only PTQ (no QAT), no ablation of group size, not all small LLMs evaluated, and bit-width recommendations may not transfer to new tasks or LLMs.([Limitations, p.9](https://arxiv.org/pdf/2402.18158v2#page=9 "In this paper, we focused solely on Post-training Quantization (PTQ) and did not consider Quantization-Aware Training (QAT)."))

