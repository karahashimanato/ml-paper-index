<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# A JEPA Recipe for Tabular Foundation Models

- カード: [`arxiv-2609.25541`](../../papers/arxiv-2609.25541.yaml)
- 著者: Mingyu Jeon, Suwan Cho, Jae Young Suh
- 年・掲載: 2026
- 原論文: [PDF](https://arxiv.org/pdf/2609.25541v1)(arXiv v1、カード作成時に読んだ版)
- タグ: in-context-learning, self-supervised, tabular-classification, tabular-foundation-model, tabular-regression
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** A recipe lets the JEPA latent term survive to convergence beside the value objective: the value head reads the encoder field and the target is an EMA difference.([Abstract, p.1](https://arxiv.org/pdf/2609.25541v1#page=1 "We report a recipe under which the latent term survives to convergence beside the value objective: the value head reads the encoder field rather than the predictor, and the target is an exponential moving average (EMA) difference."))
- **c2** The JEPA recipe does not beat the value-only arm at convergence, and the authors do not claim it does.([Introduction, p.2](https://arxiv.org/pdf/2609.25541v1#page=2 "The recipe does not beat the value-only arm at convergence, and we do not claim that it does (§4.3)."))
- **c3** Evaluation suite: classification and regression datasets drawn from OpenML-CC18, the Grinsztajn benchmark and TabArena.([Experimental setup, p.4](https://arxiv.org/pdf/2609.25541v1#page=4 "The real-data suite holds 115 classification and 32 regression datasets from OpenML-CC18, the Grinsztajn benchmark and TabArena (Bischl et al., 2021; Grinsztajn et al., 2022; Erickson et al., 2025)."))
- **c4** Each model gets a capped context and feature budget (features chosen by an F-test before the split) and is scored on 3 random halves with a capped test size.([Appendix, p.12](https://arxiv.org/pdf/2609.25541v1#page=12 "give each model at most 1,024 rows of context and 64 features picked by an F-test ahead of the split, average 3 random halves scoring no more than 512 test rows in each"))
- **c5** Neither foundation-model arm beats gradient-boosted trees (HistGB) on the suite.([Results, p.7](https://arxiv.org/pdf/2609.25541v1#page=7 "Neither arm beats gradient-boosted trees, with ds at 28:84 on classification and 4:28 on regression and jepa at 27:87 and 3:29 (Figure 4)."))
- **c6** Limitation: one seed per arm is the sharpest limit on every claim.([Limitations, p.8](https://arxiv.org/pdf/2609.25541v1#page=8 "One seed per arm is the sharpest limit on every claim, because the sign test spans datasets rather than seeds and the noise floor comes from a second run of the same seed, which a second seed would be expected to widen (§4.1)."))

