<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# LLM.int8(): 8-bit Matrix Multiplication for Transformers at Scale

- カード: [`arxiv-2208.07339`](../../papers/arxiv-2208.07339.yaml)
- 著者: Tim Dettmers, Mike Lewis, Younes Belkada, Luke Zettlemoyer
- 年・掲載: 2022
- 原論文: [PDF](https://arxiv.org/pdf/2208.07339v2)(arXiv v2、カード作成時に読んだ版)
- タグ: large-language-models, model-compression, post-hoc, post-training-quantization, quantization
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Method: Int8 matrix multiplication for feed-forward and attention projection layers, combining vector-wise quantization with a mixed-precision decomposition that isolates outlier feature dimensions into 16-bit multiplication while more than 99.9% of values are multiplied in 8-bit.([Abstract, p.1](https://arxiv.org/pdf/2208.07339v2#page=1 "However, for the emergent outliers, we also include a new mixed-precision decomposition scheme, which isolates the outlier feature dimensions into a 16-bit matrix multiplication while still more than 99.9% of values are multiplied in 8-bit."))
- **c2** Post-training use without retraining: a 16/32-bit checkpoint can be converted to Int8 and used immediately; the paper claims no performance degradation up to 175B parameters.([Abstract, p.1](https://arxiv.org/pdf/2208.07339v2#page=1 "With our method, a 175B parameter 16/32-bit checkpoint can be loaded, converted to Int8, and used immediately without performance degradation."))
- **c3** Failure mode of regular 8-bit quantization: systematic large-magnitude outlier features emerge in all transformer layers from about 6.7B parameters, and regular quantization methods fail from that scale (shown with C4 perplexity and OPT zero-shot accuracy).([Introduction, p.2](https://arxiv.org/pdf/2208.07339v2#page=2 "the need to explicitly represent the sparse but systematic large magnitude outlier features that ruin quantization precision once they emerge in all transformer layers starting at scales of 6.7B parameters"))
- **c4** Evaluation metrics: C4 validation perplexity on fairseq-pretrained models (125M-13B) to compare quantization baselines, and zero-shot accuracy on OPT models (up to 175B) via the EleutherAI evaluation harness compared only against a 16-bit baseline.([Section 3.3, p.5](https://arxiv.org/pdf/2208.07339v2#page=5 "Additionally, we evaluate zeroshot accuracy degradation on OPT models for a range of different end tasks, where we compare our methods with a 16-bit baseline."))
- **c5** Speed: the main focus is memory; quantization overhead can slow inference for models below 6.7B parameters relative to FP16, while large matrix multiplications equivalent to 175B models run about two times faster (appendix benchmarks).([Section 3.4, p.6](https://arxiv.org/pdf/2208.07339v2#page=6 "The quantization overhead can slow inference for models with less than 6.7B parameters, as compared to a FP16 baseline."))
- **c6** End-to-end BLOOM-176B inference in Hugging Face with Int8 is slightly slower but close to 16-bit per-token latency.([Appendix D.2, p.18](https://arxiv.org/pdf/2208.07339v2#page=18 "Overall Int8 inference is slightly slower but close to the millisecond latency per token compared to 16-bit inference."))
- **c7** Limitations: only the Int8 data type (no FP8), only models up to 175B, no Int8 for the attention function, and only inference (not training or fine-tuning).([Discussion and limitations, p.10](https://arxiv.org/pdf/2208.07339v2#page=10 "The main limitation of our work is that our analysis is solely on the Int8 data type, and we do not study 8-bit ﬂoating-point (FP8) data types."))
- **c8** Absmax quantization: X_i8 = round(127 X_f16 / max_ij |X_f16,ij|), i.e. scaling into [-127, 127] by 127 divided by the absolute maximum (infinity norm) of the entire tensor.([Section 2.1, p.3](https://arxiv.org/pdf/2208.07339v2#page=3 "Absmax quantization scales inputs into the 8-bit range [−127, 127] by multiplying with sxf16 which is 127 divided by the absolute maximum of the entire tensor."))

