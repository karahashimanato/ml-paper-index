<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# AWQ: Activation-aware Weight Quantization for LLM Compression and Acceleration

- カード: [`arxiv-2306.00978`](../../papers/arxiv-2306.00978.yaml)
- 著者: Ji Lin, Jiaming Tang, Haotian Tang, Shang Yang, Wei-Ming Chen, Wei-Chen Wang, Guangxuan Xiao, Xingyu Dang, Chuang Gan, Song Han
- 年・掲載: 2023
- 原論文: [PDF](https://arxiv.org/pdf/2306.00978v6)(arXiv v6、カード作成時に読んだ版)
- タグ: deep-learning, large-language-models, model-compression, post-hoc, post-training-quantization, quantization
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Proposes AWQ, a hardware-friendly method for low-bit weight-only quantization of LLMs.([Abstract, p.1](https://arxiv.org/pdf/2306.00978v6#page=1 "We propose Activation-aware Weight Quantization (AWQ), a hardware-friendly approach for LLM low-bit weight-only quantization."))
- **c2** Key assumption: salient weight channels should be identified from the activation distribution rather than from the weights.([Abstract, p.1](https://arxiv.org/pdf/2306.00978v6#page=1 "To identify salient weight channels, we should refer to the activation distribution, not weights."))
- **c3** Granularity: grouped weight-only quantization with group size 128 throughout unless otherwise specified (INT4/INT3 focus).([Experiments (Settings), p.7](https://arxiv.org/pdf/2306.00978v6#page=7 "We used a group size of 128 throughout the work, except otherwise specified."))
- **c4** Calibration: a small calibration set from the Pile, chosen to avoid overfitting to a specific downstream domain.([Experiments (Settings), p.7](https://arxiv.org/pdf/2306.00978v6#page=7 "For AWQ, we used a small calibration set from the Pile (Gao et al., 2020) dataset in order not to overfit to a specific downstream domain."))
- **c5** Critique of GPTQ stated by the AWQ authors in related work: GPTQ's reconstruction process overfits the calibration set and may not preserve the generalist abilities of LLMs for other modalities and domains.([Related work, p.2](https://arxiv.org/pdf/2306.00978v6#page=2 "However, the reconstruction process of GPTQ leads to an over-fitting issue to the calibration set and may not preserve the generalist abilities of LLMs for other modalities and domains."))
- **c6** Evaluation of instruction-tuned models uses an LLM judge: GPT-4 scores the quantized Vicuna against its FP16 counterpart on 80 sample questions, comparing both response orders because the authors found GPT-4 tends to increase the rating of the first input.([Experiments (instruction-tuned models), p.8](https://arxiv.org/pdf/2306.00978v6#page=8 "We used the GPT-4 score to evaluate the quantized models' performance against the FP16 counterpart on 80 sample questions (Chiang et al., 2023)."))
- **c7** Speed measurement: TinyChat benchmarking on RTX 4090 and Jetson Orin following the exllama protocol.([Speedup Evaluation, p.10](https://arxiv.org/pdf/2306.00978v6#page=10 "We conduct benchmarking experiments on RTX 4090 and Jetson Orin following the protocol described in exllama"))

