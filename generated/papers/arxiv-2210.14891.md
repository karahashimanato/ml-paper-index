<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Broken Neural Scaling Laws

- カード: [`arxiv-2210.14891`](../../papers/arxiv-2210.14891.yaml)
- 著者: Ethan Caballero, Kshitij Gupta, Irina Rish, David Krueger
- 年・掲載: 2022
- 原論文: [PDF](https://arxiv.org/pdf/2210.14891v17)(arXiv v17、カード作成時に読んだ版)
- タグ: deep-learning, scaling-laws
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Contribution: a smoothly broken power-law functional form (BNSL) that the authors say accurately models and extrapolates how evaluation metrics vary with compute, parameters, dataset size, input size, training steps or upstream performance.([Abstract, p.1](https://arxiv.org/pdf/2210.14891v17#page=1 "We present a smoothly broken power law functional form (referred to by us as a broken neural scaling law (BNSL)) that accurately models and extrapolates the scaling behaviors of deep neural networks"))
- **c2** Evaluation protocol: the functional form is fit to smaller-x points and evaluated on held-out larger-x points for extrapolation; tabulated extrapolation errors are RMSLE.([Empirical results: fits & extrapolations of functional forms, p.5](https://arxiv.org/pdf/2210.14891v17#page=5 "black points are points used for fitting a functional form, green (gray if color blind) points are held-out points used for evaluating extrapolation of functional form fit to the black points, & a red line is BNSL that has been fit to black points."))
- **c3** Baseline provenance: the percentages of tasks won by the competing functional forms M1-M4 in the benchmark comparison were obtained via correspondence with the authors of Alabdulmohsin et al. (2022), not recomputed in this paper.([Empirical results (Table 2 caption), p.5](https://arxiv.org/pdf/2210.14891v17#page=5 "Numbers for M1, M2, M3, and M4 were obtained via correspondence with authors of Alabdulmohsin et al. (2022)."))
- **c4** Data provenance: much of the scaling data is taken from other papers; e.g. the compute-on-x-axis vision experiment uses data from Figure 2 of Zhai et al. (2021) and compares BNSL with M3, the form proposed there.([Appendix A.9, p.15](https://arxiv.org/pdf/2210.14891v17#page=15 "The experimental scaling data was obtained from Figure 2 of Zhai et al. (2021), and as a result in Table 6 we compare extrapolation of BNSL to the extrapolation of M3 (which was proposed in Zhai et al. (2021))"))
- **c5** Emergence framing: the authors define the 'emergent' / 'breakthrough' / 'phase transition' behaviors advertised in recent papers as any scaling behavior with more than zero breaks in BNSL.([The limit of the predictability of scaling behavior, p.10](https://arxiv.org/pdf/2210.14891v17#page=10 "We define all these quoted phrases as any scaling behaviors with greater than 0 breaks"))
- **c6** Limit of predictability: if a sufficiently sharp break occurs at a scale sufficiently larger than the largest fitted point, there is currently no way to extrapolate past that break.([The limit of the predictability of scaling behavior, p.11](https://arxiv.org/pdf/2210.14891v17#page=11 "2) If an additional break of sufficient sharpness happens at a scale that is sufficiently larger than the maximum (along the x-axis) of the points used for fitting, there does not (currently) exist a way to extrapolate the scaling behavior after that additional break."))
- **c7** Stated limitation: a small number of (x, y) samples sometimes may not suffice to fit and extrapolate BNSL, and collecting many samples can be costly; the authors suggest entities with more compute may get more accurate extrapolations.([Ethics statement, p.11](https://arxiv.org/pdf/2210.14891v17#page=11 "A small number of samples sometimes may not be sufficient to accurately fit and extrapolate the BNSL functional form, and obtaining a large number of such samples can sometimes be costly."))

