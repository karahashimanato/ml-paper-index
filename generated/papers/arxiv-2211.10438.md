<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# SmoothQuant: Accurate and Efficient Post-Training Quantization for Large Language Models

- カード: [`arxiv-2211.10438`](../../papers/arxiv-2211.10438.yaml)
- 著者: Guangxuan Xiao, Ji Lin, Mickael Seznec, Hao Wu, Julien Demouth, Song Han
- 年・掲載: 2022
- 原論文: [PDF](https://arxiv.org/pdf/2211.10438v7)(arXiv v7、カード作成時に読んだ版)
- タグ: deep-learning, large-language-models, model-compression, post-hoc, post-training-quantization, quantization
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Proposes SmoothQuant, a training-free PTQ method for 8-bit weight and 8-bit activation (W8A8) quantization of LLMs.([Abstract, p.1](https://arxiv.org/pdf/2211.10438v7#page=1 "We propose SmoothQuant, a training-free, accuracy-preserving, and general-purpose post-training quantization (PTQ) solution to enable 8-bit weight, 8-bit activation (W8A8) quantization for LLMs."))
- **c2** Mechanism: activation outliers are smoothed by offline migrating quantization difficulty from activations to weights via a mathematically equivalent transformation.([Abstract, p.1](https://arxiv.org/pdf/2211.10438v7#page=1 "SmoothQuant smooths the activation outliers by offline migrating the quantization difficulty from activations to weights with a mathematically equivalent transformation."))
- **c3** Motivation, stated with citations to prior work (Dettmers et al. 2022; Wei et al. 2022; Bondarenko et al. 2021) rather than as a new finding: LLMs are notoriously difficult to quantize due to outliers in the activations.([Review of Quantization Difficulty, p.3](https://arxiv.org/pdf/2211.10438v7#page=3 "LLMs are notoriously difficult to quantize due to the outliers in the activations (Dettmers et al., 2022; Wei et al., 2022; Bondarenko et al., 2021)."))
- **c4** Calibration: smoothing factors and static quantization step sizes are calibrated once with 512 random sentences from the Pile and the same model is used for all downstream tasks.([Experimental setup (Activation smoothing), p.5](https://arxiv.org/pdf/2211.10438v7#page=5 "To get the statistics of activations, we calibrate the smoothing factors and the static quantization step sizes once with 512 random sentences from the pre-training dataset Pile, and apply the same smoothed and quantized model for all downstream tasks."))
- **c5** Hyperparameter selection: the migration strength alpha is chosen by a quick grid search on a subset of the Pile validation set (the paper reports alpha = 0.5 for OPT/BLOOM and 0.75 for GLM-130B).([Experimental setup (Activation smoothing), p.5](https://arxiv.org/pdf/2211.10438v7#page=5 "We get a suitable α by running a quick grid search on a subset of the Pile (Gao et al., 2020) validation set."))
- **c6** Metrics for the OPT-175B comparison (Table 3): average accuracy over 7 zero-shot benchmarks plus 1 language-modeling benchmark (perplexity).([Results (Table 3 caption), p.6](https://arxiv.org/pdf/2211.10438v7#page=6 "We extensively benchmark the performance on 7 zero-shot benchmarks (by reporting the average accuracy) and 1 language modeling benchmark (perplexity)."))
- **c7** The authors state that they focus on the relative performance change before and after quantization, not on absolute values.([Experimental setup (Models and datasets), p.5](https://arxiv.org/pdf/2211.10438v7#page=5 "Note that we focus on the relative performance change before and after quantization but not the absolute value."))
- **c8** Smoothing transformation (Eq. 3): Y = (X diag(s)^-1)(diag(s) W) = X_hat W_hat, dividing input activations by a per-channel factor s and scaling the weights in the reverse direction; s can be fused offline into the previous layer's parameters.([Migrate the quantization difficulty from activations to weights, p.4](https://arxiv.org/pdf/2211.10438v7#page=4 "Considering input X is usually produced from previous linear operations (e.g., linear layers, layer norms, etc.), we can easily fuse the smoothing factor into previous layers’ parameters offline, which doe not incur kernel call overhead from an extra scaling."))
- **c9** Extremes of the smoothing factor: s_j = max(|X_j|) gives all activation channels the same maximum (easy to quantize) but pushes all difficulty to the weights, and s_j = 1/max(|W_j|) pushes it all to the activations; the authors state both lead to poor accuracy.([Migrate the quantization difficulty from activations to weights, p.4](https://arxiv.org/pdf/2211.10438v7#page=4 "This choice ensures that after the division, all the activation channels will have the same maximum value, which is easy to quantize."))
- **c10** Migration strength (Eq. 4): s_j = max(|X_j|)^alpha / max(|W_j|)^(1 - alpha), with the hyperparameter alpha controlling how much difficulty is migrated from activations to weights.([Migrate the quantization difficulty from activations to weights, p.4](https://arxiv.org/pdf/2211.10438v7#page=4 "Here we introduce a hyper-parameter, migration strength α, to control how much difficulty we want to migrate from activation to weights, using the following equation:"))

