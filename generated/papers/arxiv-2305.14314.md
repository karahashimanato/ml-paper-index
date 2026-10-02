<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# QLoRA: Efficient Finetuning of Quantized LLMs

- カード: [`arxiv-2305.14314`](../../papers/arxiv-2305.14314.yaml)
- 著者: Tim Dettmers, Artidoro Pagnoni, Ari Holtzman, Luke Zettlemoyer
- 年・掲載: 2023
- 原論文: [PDF](https://arxiv.org/pdf/2305.14314v1)(arXiv v1、カード作成時に読んだ版)
- タグ: deep-learning, large-language-models, model-compression, quantization, supervised
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** QLoRA finetunes by backpropagating through a frozen 4-bit quantized pretrained model into LoRA adapters (the base weights are not updated).([Abstract, p.1](https://arxiv.org/pdf/2305.14314v1#page=1 "QLORA backpropagates gradients through a frozen, 4-bit quantized pretrained language model into Low Rank Adapters (LoRA)."))
- **c2** Assumption behind NF4: the data type is information-theoretically optimal for normally distributed weights.([Abstract, p.1](https://arxiv.org/pdf/2305.14314v1#page=1 "(a) 4-bit NormalFloat (NF4), a new data type that is information theoretically optimal for normally distributed weights"))
- **c3** Summary claim (GLUE / Super-NaturalInstructions and 5-shot MMLU experiments): 4-bit QLoRA with NF4 matches 16-bit full finetuning and 16-bit LoRA finetuning performance on academic benchmarks with well-established evaluation setups.([QLoRA vs. Standard Finetuning (Summary), p.7](https://arxiv.org/pdf/2305.14314v1#page=7 "Our results consistently show that 4-bit QLORA with NF4 data type matches 16-bit full finetuning and 16-bit LoRA finetuning performance on academic benchmarks with well-established evaluation setups."))
- **c4** Evaluation practice: GPT-4 and human (Elo tournament) evaluations largely agree on model ranking but show instances of strong disagreement, so model-based evaluation has uncertainties.([Introduction, p.2](https://arxiv.org/pdf/2305.14314v1#page=2 "We find that GPT-4 and human evaluations largely agree on the rank of model performance in the tournaments, but we also find there are instances of strong disagreement."))
- **c5** The authors find that current chatbot benchmarks are not trustworthy for accurately evaluating chatbot performance levels.([Abstract, p.1](https://arxiv.org/pdf/2305.14314v1#page=1 "Furthermore, we find that current chatbot benchmarks are not trustworthy to accurately evaluate the performance levels of chatbots."))
- **c6** Limitation: the paper did not establish that QLoRA matches full 16-bit finetuning at 33B and 65B scales.([Limitations and Discussion, p.15](https://arxiv.org/pdf/2305.14314v1#page=15 "Despite this evidence, we did not establish that QLORA can match full 16-bit finetuning performance at 33B and 65B scales."))
- **c7** Limitation: other bit-precisions (e.g. 3-bit base models) and other adapter methods were not evaluated; responsible-AI (bias) evaluation is also described as limited.([Limitations and Discussion, p.16](https://arxiv.org/pdf/2305.14314v1#page=16 "An additional limitation is that we did not evaluate different bit-precisions, such as using 3-bit base models, or different adapter methods."))

