<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Scaling Laws for Precision

- カード: [`arxiv-2411.04330`](../../papers/arxiv-2411.04330.yaml)
- 著者: Tanishq Kumar, Zachary Ankner, Benjamin F. Spector, Blake Bordelon, Niklas Muennighoff, Mansheej Paul, Cengiz Pehlevan, Christopher Ré, Aditi Raghunathan
- 年・掲載: 2024
- 原論文: [PDF](https://arxiv.org/pdf/2411.04330v2)(arXiv v2、カード作成時に読んだ版)
- タグ: language-modeling, large-language-models, model-compression, post-training-quantization, quantization, quantization-aware-training, scaling-laws
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Main claim: PTQ degradation increases as models are trained on more data, eventually making additional pretraining data harmful; the authors propose that training in lower precision reduces the effective parameter count.([Abstract, p.1](https://arxiv.org/pdf/2411.04330v2#page=1 "For inference, we find that the degradation introduced by post-training quantization increases as models are trained on more data, eventually making additional pretraining data actively harmful."))
- **c2** Setup: OLMo-style models on Dolma V1.7 with 30-220M non-embedding parameters and 1.5-26B tokens, sweeping 8 precisions each for weights, activations and attention (KV); over 465 pretraining runs, with predictions validated up to 1.7B parameters.([Setup, p.4](https://arxiv.org/pdf/2411.04330v2#page=4 "Our experiments consist of a sweep of language model pretraining runs over N ∈[30, 60, 110, 220] million parameters (non-embedding) and D ∈[1.5, 3, 6, 13, 26] billion tokens."))
- **c3** PTQ setting: BF16-trained models are weight-quantized after training with GPTQ, with findings replicated with AWQ and round-to-nearest in the appendix.([Scaling laws for post-train quantization, p.4](https://arxiv.org/pdf/2411.04330v2#page=4 "In this section, we consider models trained in BF16 and use GPTQ [Frantar et al., 2022] to post-train quantize them, replicating our findings with two other methods in Appendix F."))
- **c4** Within a model size, degradation from PTQ grows with training data, while for a fixed dataset size larger models degrade less; degradation grows exponentially as the post-training precision is lowered.([Scaling laws for post-train quantization, p.5](https://arxiv.org/pdf/2411.04330v2#page=5 "We find that the degradation δPTQ increases in training data size across all model sizes, but that for a fixed dataset size larger models incur a smaller degradation."))
- **c5** For training, the fitted laws suggest that training larger models in lower precision may be compute optimal (under the paper's cost model).([Abstract, p.1](https://arxiv.org/pdf/2411.04330v2#page=1 "For training, our scaling laws allow us to predict the loss of a model with different parts in different precisions, and suggest that training larger models in lower precision may be compute optimal."))
- **c6** The authors stress that the contribution is the trends and functional forms rather than the fitted numerical constants, which can vary with small implementation differences.([Background, p.4](https://arxiv.org/pdf/2411.04330v2#page=4 "For this reason, we emphasize our contribution is not the numerical values we fit, but the trends and functional forms we identify."))
- **c7** Limitations: a fixed architecture, compute gains from halving precision usually below 2x due to systems overhead, and only loss scaling without downstream evaluations; trends are meant to be suggestive.([Conclusion and limitations, p.12](https://arxiv.org/pdf/2411.04330v2#page=12 "Third, we only consider loss scaling without downstream model evaluations."))

