<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Decoding Compressed Trust: Scrutinizing the Trustworthiness of Efficient LLMs Under Compression

- カード: [`arxiv-2403.15447`](../../papers/arxiv-2403.15447.yaml)
- 著者: Junyuan Hong, Jinhao Duan, Chenhui Zhang, Zhangheng Li, Chulin Xie, Kelsey Lieberman, James Diffenderfer, Brian Bartoldson, Ajay Jaiswal, Kaidi Xu, Bhavya Kailkhura, Dan Hendrycks, Dawn Song, Zhangyang Wang, Bo Li
- 年・掲載: 2024
- 原論文: [PDF](https://arxiv.org/pdf/2403.15447v3)(arXiv v3、カード作成時に読んだ版)
- タグ: large-language-models, model-compression, post-hoc, post-training-quantization, pruning, quantization
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Main claim: quantization is currently more effective than pruning for obtaining efficiency and trustworthiness together (the abstract's example: 4-bit quantization keeps the original's trustworthiness while pruning degrades it even at 50% sparsity).([Abstract, p.1](https://arxiv.org/pdf/2403.15447v3#page=1 "We find that quantization is currently a more effective approach than pruning in achieving efficiency and trustworthiness simultaneously."))
- **c2** What is compressed: weights only, with GPTQ and AWQ at 3, 4 and 8 bits (post-training, calibration set of 128 samples), compared with 2:4 semi-structured pruning; models are LLAMA2 13b, LLAMA2 13b Chat and Vicuna 13b Chat.([Experimental setup, p.4](https://arxiv.org/pdf/2403.15447v3#page=4 "In this paper, we study three pre-trained models: LLAMA2 13b, LLAMA2 13b Chat (Touvron et al., 2023b), and Vicuna 13b Chat (Chiang et al., 2023)."))
- **c3** Evaluation metrics: benign performance by MMLU average accuracy, trustworthiness by DecodingTrust's eight dimensions (stereotype, privacy, toxicity, fairness, AdvGLUE++, OOD robustness, adversarial demonstrations, ethics), and additionally refusal rates.([Experimental setup, p.4](https://arxiv.org/pdf/2403.15447v3#page=4 "The benchmark includes 8 trustworthy dimensions: Stereotype, Privacy, Toxicity, Fairness, Adversarial Robustness (AdvGLUE++), Out-Of-Distribution (OOD) Robustness, Robustness to Adversarial Demonstrations (AdvDemo), and Ethics."))
- **c4** Extreme quantization (3 bits) tends to reduce trustworthiness significantly, and this risk is not visible from benign performance alone, so the authors call for comprehensive trustworthiness evaluation in practice.([Abstract, p.1](https://arxiv.org/pdf/2403.15447v3#page=1 "This increased risk cannot be uncovered by looking at benign performance alone, in turn, mandating comprehensive trustworthiness evaluation in practice."))
- **c5** Moderate-bit quantization may unexpectedly improve some trust dimensions such as ethics and fairness.([Abstract, p.1](https://arxiv.org/pdf/2403.15447v3#page=1 "Moreover, employing quantization within a moderate bit range could unexpectedly improve certain trustworthiness dimensions such as ethics and fairness."))
- **c6** Calibration-set randomness matters: GPTQ at 4 bits can vary by over 5 points in fairness, ethics and adversarial demonstrations depending on the randomly sampled calibration set, and this variance is not predictable from MMLU.([Bag of tricks (discussion), p.8](https://arxiv.org/pdf/2403.15447v3#page=8 "Note that such variance is not predictable from the standard MMLU benchmark."))
- **c7** The authors modified the DecodingTrust benchmark (to mitigate score variance caused by high refusal rates) and release it with the compressed models.([Conclusion, p.9](https://arxiv.org/pdf/2403.15447v3#page=9 "To benefit the reproducibility of our experiments, we release all models tested in the benchmark and the modified DecodingTrust benchmark to mitigate the large score variances caused by the large refusal rates."))

