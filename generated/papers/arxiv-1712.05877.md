<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Quantization and Training of Neural Networks for Efficient Integer-Arithmetic-Only Inference

- カード: [`arxiv-1712.05877`](../../papers/arxiv-1712.05877.yaml)
- 著者: Benoit Jacob, Skirmantas Kligys, Bo Chen, Menglong Zhu, Matthew Tang, Andrew Howard, Hartwig Adam, Dmitry Kalenichenko
- 年・掲載: 2017
- 原論文: [PDF](https://arxiv.org/pdf/1712.05877v1)(arXiv v1、カード作成時に読んだ版)
- タグ: deep-learning, model-compression, quantization, quantization-aware-training, supervised
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Proposes a quantization scheme that lets inference run with integer-only arithmetic, plus a co-designed training procedure to preserve accuracy after quantization.([Abstract, p.1](https://arxiv.org/pdf/1712.05877v1#page=1 "We propose a quantization scheme that allows inference to be carried out using integer-only arithmetic, which can be implemented more efficiently than floating point inference on commonly available integer-only hardware."))
- **c2** Granularity: one set of quantization parameters (scale and zero-point) per activations array and per weights array (per-tensor), with separate parameters for separate arrays.([Quantized Inference, p.3](https://arxiv.org/pdf/1712.05877v1#page=3 "Our quantization scheme uses a single set of quantization parameters for all values within each activations array and within each weights array; separate arrays use separate quantization parameters."))
- **c3** The training procedure simulates quantization in the forward pass while backpropagation and weight storage stay in floating point (quantization-aware training).([Training with simulated quantization, p.5](https://arxiv.org/pdf/1712.05877v1#page=5 "We propose an approach that simulates quantization effects in the forward pass of training."))
- **c4** Failure mode: the authors found that training in float and then quantizing works sufficiently well for large models but leads to significant accuracy drops for small models; the common failure modes they list for simple post-training quantization are large differences in weight ranges across output channels and outlier weight values.([Training with simulated quantization, p.5](https://arxiv.org/pdf/1712.05877v1#page=5 "We found that this approach works sufficiently well for large models with considerable representational capacity, but leads to significant accuracy drops for small models."))
- **c5** Speed was evaluated on real hardware: MobileNets with varying depth multipliers and resolutions on ImageNet were benchmarked on three types of Qualcomm (Snapdragon) cores.([Experiments, p.7](https://arxiv.org/pdf/1712.05877v1#page=7 "We benchmarked the MobileNet architecture with varying depth-multipliers (DM) and resolutions on ImageNet on three types of Qualcomm cores"))
- **c6** Evaluation-practice position: rather than only minimizing accuracy loss for a fixed architecture, the authors advocate the latency-vs-accuracy tradeoff as a better measure.([Experiments, p.7](https://arxiv.org/pdf/1712.05877v1#page=7 "While most of the quantization literature focuses on minimizing accuracy loss for a given architecture, we advocate for a more comprehensive latency-vs-accuracy tradeoff as a better measure."))
- **c7** Affiliation/product disclosure: the authors are at Google, and the described scheme is the one adopted in TensorFlow Lite.([Quantized Inference (footnote), p.2](https://arxiv.org/pdf/1712.05877v1#page=2 "The quantization scheme described here is the one adopted in TensorFlow Lite [5] and we will refer to specific parts of its code to illustrate aspects discussed below."))

