<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# An empirical study of LLaMA3 quantization: from LLMs to MLLMs

- カード: [`arxiv-2404.14047`](../../papers/arxiv-2404.14047.yaml)
- 著者: Wei Huang, Xingyu Zheng, Xudong Ma, Haotong Qin, Chengtao Lv, Hong Chen, Jie Luo, Xiaojuan Qi, Xianglong Liu, Michele Magno
- 年・掲載: 2024
- 原論文: [PDF](https://arxiv.org/pdf/2404.14047v3)(arXiv v3、カード作成時に読んだ版)
- タグ: large-language-models, model-compression, post-hoc, post-training-quantization, quantization, quantization-aware-training
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Main claim: LLaMA3 still suffers non-negligible degradation from quantization in linguistic and visual contexts, particularly at ultra-low bit widths.([Abstract, p.1](https://arxiv.org/pdf/2404.14047v3#page=1 "Our experimental results indicate that LLaMA3 still suffers from non-negligible degradation in linguistic and visual contexts, particularly under ultra-low bit widths."))
- **c2** Evaluation metrics: perplexity on WikiText2, PTB and part of C4, zero-shot accuracy on PIQA, Winogrande, ARC-e, ARC-c and HellaSwag, 5-shot MMLU for LoRA-FT methods, and visual-language benchmarks for LLaVA-Next-8B.([Introduction (evaluation datasets), p.2](https://arxiv.org/pdf/2404.14047v3#page=2 "For the PTQ methods, we evaluate quantized LLaMA3 on the WikiText2 [18], PTB [20], and a portion of the C4 dataset [19], using perplexity (PPL) as the evaluation metric."))
- **c3** Calibration protocol: WikiText2 is the calibration set for all PTQ methods (128 samples, sequence length 2048), and group size is fixed at 128 for grouped methods; WikiText2 is also one of the perplexity evaluation sets.([Introduction (evaluation datasets), p.2](https://arxiv.org/pdf/2404.14047v3#page=2 "To ensure fairness in evaluation of different PTQ methods, we set WikiText2 as the calibration dataset for all quantization methods, with a sample size of 128 and a sequence length of 2048."))
- **c4** LoRA fine-tuning (QLoRA, IR-QLoRA on Alpaca) does not compensate for quantization error on LLaMA3-8B below 4 bits and actually worsens MMLU, in contrast to LLaMA and LLaMA2, where 4-bit LoRA-FT versions could even outperform FP16 on MMLU.([Track 2: LoRA-FT quantization, p.7](https://arxiv.org/pdf/2404.14047v3#page=7 "On the MMLU dataset, the most notable observation with LLaMA3-8B under LoRA-FT quantization is that low-rank fine-tuning on the Alpaca [36] dataset not only fails to compensate for the errors introduced by quantization, but actually exacerbates the degradation."))
- **c5** The authors find that LLaMA3-70B shows significant robustness to the different quantization methods, even for ultra-low bit widths.([Track 1: post-training quantization, p.5](https://arxiv.org/pdf/2404.14047v3#page=5 "Moreover, we find that the LLaMA3-70B model shows significant robustness to different quantization methods, even for ultra-low bit-width quantization."))
- **c6** Multimodal failure: with GPTQ or AWQ, the 2-bit LLaVA-Next-8B collapses completely on the multimodal QA tasks; SliM-LLM mitigates the collapse but still degrades strongly.([Track 3: MLLM quantization, p.9](https://arxiv.org/pdf/2404.14047v3#page=9 "Notably, regardless of GPTQ or AWQ, we observe that the 2-bit LLaVA-Next-8B completely collapses in the six multi-modal QA tasks, with scores dropping to zero."))
- **c7** Possible conflict of interest not discussed in the paper: three evaluated methods (SliM-LLM, BiLLM, IR-QLoRA) have reference entries whose author lists include authors of this study, while the paper's competing-interests statement declares none.([References, p.12](https://arxiv.org/pdf/2404.14047v3#page=12 "Wei Huang, Haotong Qin, Yangdong Liu, Yawei Li, Xianglong Liu, Luca Benini, et al. SliM-LLM: Salience-driven mixed-precision quantization for large language models."))

