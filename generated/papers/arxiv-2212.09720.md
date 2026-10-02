<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# The case for 4-bit precision: k-bit Inference Scaling Laws

- カード: [`arxiv-2212.09720`](../../papers/arxiv-2212.09720.yaml)
- 著者: Tim Dettmers, Luke Zettlemoyer
- 年・掲載: 2022
- 原論文: [PDF](https://arxiv.org/pdf/2212.09720v2)(arXiv v2、カード作成時に読んだ版)
- タグ: deep-learning, large-language-models, model-compression, post-hoc, post-training-quantization, quantization
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Study design: more than 35,000 experiments with 16-bit inputs and k-bit (3 to 8-bit) parameters, 19M to 176B parameters, across BLOOM, OPT, NeoX/Pythia and GPT-2.([Abstract, p.1](https://arxiv.org/pdf/2212.09720v2#page=1 "We run more than 35,000 experiments with 16-bit inputs and k-bit parameters to examine which zero-shot quantization methods improve scaling for 3 to 8-bit precision at scales of 19M to 176B parameters across the LLM families BLOOM, OPT, NeoX/Pythia, and GPT-2."))
- **c2** Main finding: 4-bit precision is almost universally optimal for the trade-off between total model bits and zero-shot accuracy.([Abstract, p.1](https://arxiv.org/pdf/2212.09720v2#page=1 "Overall, our findings show that 4-bit precision is almost universally optimal for total model bits and zero-shot accuracy."))
- **c3** Metrics: perplexity on the CommonCrawl subset of the Pile and mean zero-shot performance from the EleutherAI LM Evaluation harness.([Experimental setup, p.4](https://arxiv.org/pdf/2212.09720v2#page=4 "To measure inference performance for k-bit quantization methods, we use perplexity on the CommonCrawl subset of The Pile (Gao et al., 2020) and mean zero-shot performance on the EleutherAI LM Evaluation harness (Gao et al., 2021)."))
- **c4** Metric sensitivity: when zero-shot accuracy is used instead of perplexity, the float data type is sometimes better (whereas quantile quantization is best by perplexity), which the authors attribute to zero-shot accuracy being noisier.([Experimental setup, p.4](https://arxiv.org/pdf/2212.09720v2#page=4 "Still, when we use zero-shot accuracy as an evaluation metric, the float data type is sometimes better because zero-shot accuracy is noisier."))
- **c5** Failure mode: Pythia and OPT are unstable at 3-bit, with performance close to random for the largest models.([Results & Analysis, p.4](https://arxiv.org/pdf/2212.09720v2#page=4 "Pythia and OPT are unstable for 3-bit inference where performance is close to random (35%) for the largest Pythia/OPT models."))
- **c6** Contrast with prior work: outlier-dependent quantization (citing Dettmers et al. 2022a and Xiao et al. 2022) improves predictive performance but is shown not to be effective for bit-level scaling.([Introduction, p.2](https://arxiv.org/pdf/2212.09720v2#page=2 "While earlier work has shown that it is possible to significantly improve the predictive performance of quantized models by using outlier-dependent quantization (Dettmers et al., 2022a; Xiao et al., 2022), we show that this is not effective for bit-level scaling."))
- **c7** Limitation: certain classes of quantization methods (e.g. data types optimized with additional input data) were not considered; optimized GPU implementations are also lacking.([Discussion & Limitations, p.8](https://arxiv.org/pdf/2212.09720v2#page=8 "While we ran more than 35,000 experiments, a main limitation is that we did not consider certain classes of quantization methods."))

