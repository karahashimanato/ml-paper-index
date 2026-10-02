<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# GPTQ: Accurate Post-Training Quantization for Generative Pre-trained Transformers

- カード: [`arxiv-2210.17323`](../../papers/arxiv-2210.17323.yaml)
- 著者: Elias Frantar, Saleh Ashkboos, Torsten Hoefler, Dan Alistarh
- 年・掲載: 2022
- 原論文: [PDF](https://arxiv.org/pdf/2210.17323v2)(arXiv v2、カード作成時に読んだ版)
- タグ: deep-learning, large-language-models, model-compression, post-hoc, post-training-quantization, quantization
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Proposes GPTQ, a one-shot weight quantization method using approximate second-order information.([Abstract, p.1](https://arxiv.org/pdf/2210.17323v2#page=1 "we address this challenge, and propose GPTQ, a new one-shot weight quantization method based on approximate second-order information, that is both highly-accurate and highly-efficient."))
- **c2** Calibration data: 128 random 2048-token segments from C4 (generic web text); the authors say GPTQ sees no task-specific data.([Experimental validation (Setup), p.6](https://arxiv.org/pdf/2210.17323v2#page=6 "Our entire GPTQ calibration data consists of 128 random 2048 token segments from the C4 dataset (Raffel et al., 2020), i.e., excerpts from randomly crawled websites, which represents generic text data."))
- **c3** Granularity: standard uniform per-row asymmetric quantization on the min-max grid (weights only).([Experimental validation (Setup), p.6](https://arxiv.org/pdf/2210.17323v2#page=6 "We perform standard uniform per-row asymmetric quantization on the min-max grid, similar to Dettmers et al. (2022)."))
- **c4** Metric choice: the main evaluation uses perplexity-based language generation tasks (WikiText2, PTB, C4) because they are known to be sensitive to quantization; zero-shot tasks are a complement.([Experimental validation (Language Generation), p.7](https://arxiv.org/pdf/2210.17323v2#page=7 "We focus on these perplexity-based tasks, as they are known to be particularly sensitive to model quantization (Yao et al., 2022)."))
- **c5** Evaluation caveat stated by the authors: since calibration data is sampled from the C4 training set, the C4 perplexity evaluation is not fully zero-shot.([Appendix (Tables 11-12 captions), p.14](https://arxiv.org/pdf/2210.17323v2#page=14 "We note that the calibration data used by GPTQ is sampled from the C4 training set, this task is thus not fully zero-shot."))
- **c6** Limitation: speedups come from reduced memory movement, not from computational reductions; the study also does not consider activation quantization.([Summary and limitations, p.9](https://arxiv.org/pdf/2210.17323v2#page=9 "our method obtains speedups from reduced memory movement, and does not lead to computational reductions."))
- **c7** The authors note that the study focused on standard 'leading accuracy' metrics such as perplexity, and that a thorough study of compression's impact on secondary measures, in particular bias effects, is warranted.([Ethics statement, p.10](https://arxiv.org/pdf/2210.17323v2#page=10 "We believe a thorough study of the impact of compression upon secondary measures, and in particular bias effects (Bender et al., 2021) is warranted, and may be rendered easier through our work."))

