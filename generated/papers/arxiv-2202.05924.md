<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Compute Trends Across Three Eras of Machine Learning

- カード: [`arxiv-2202.05924`](../../papers/arxiv-2202.05924.yaml)
- 著者: Jaime Sevilla, Lennart Heim, Anson Ho, Tamay Besiroglu, Marius Hobbhahn, Pablo Villalobos
- 年・掲載: 2022
- 原論文: [PDF](https://arxiv.org/pdf/2202.05924v2)(arXiv v2、カード作成時に読んだ版)
- タグ: deep-learning, efficiency-evaluation
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Main claim: training compute doubled roughly every 20 months before 2010 (in line with Moore's law) and accelerated to roughly every 6 months since the advent of Deep Learning in the early 2010s; a separate large-scale trend emerged in late 2015.([Abstract, p.1](https://arxiv.org/pdf/2202.05924v2#page=1 "Since the advent of Deep Learning in the early 2010s, the scaling of training compute has accelerated, doubling approximately every 6 months."))
- **c2** Data: the analysis is based on a curated dataset of 123 milestone ML systems (selected by necessary and notability criteria, with a subjective selection for models from 2020 onward) annotated with training compute.([Introduction, p.1](https://arxiv.org/pdf/2202.05924v2#page=1 "We curate a dataset of 123 milestone Machine Learning systems, annotated with the compute it took to train them."))
- **c3** Estimation method: when a paper does not report training compute, it is estimated with the AI and Compute appendix techniques (from forward-pass compute or from GPU time), with the reasoning annotated per dataset cell.([Appendix A (Methods), p.16](https://arxiv.org/pdf/2202.05924v2#page=16 "When the training compute is not shared in the paper, we follow the techniques in AI and Compute’s appendix to estimate the training compute of our models (Amodei & Hernandez, 2018)."))
- **c4** Scope: only the final training run is counted; hyperparameter-search runs are not, as they are often unreported.([Appendix A (Methods), p.16](https://arxiv.org/pdf/2202.05924v2#page=16 "Our dataset only annotates the compute used for the ﬁnal training run."))
- **c5** Uncertainty: the authors expect most compute estimates to be accurate within about a factor of two (based on comparing estimation methods) and add noise when bootstrapping to account for it.([Appendix H (Limitations), p.24](https://arxiv.org/pdf/2202.05924v2#page=24 "We expect most of the compute estimates to be accurate within a factor of about two based on some comparisons we did between different estimation methods (Sevilla et al., 2022)."))
- **c6** Caveat: assignment of systems to the large-scale trend was an intuitive decision, justified post hoc with a Z-value threshold, and the authors state there is room for alternative interpretations.([Trends in the Large-Scale era, p.5](https://arxiv.org/pdf/2202.05924v2#page=5 "Note that we made an intuitive decision in deciding which systems belong to this new large-scale trend."))
- **c7** Disagreement with prior work: the results contrast with Amodei & Hernandez (3.4-month doubling, 2012-2018) and Lyzhov (>2-year doubling, 2018-2020); the authors attribute this to small samples and single-trend assumptions in those analyses.([Trends in the Large-Scale era, p.5](https://arxiv.org/pdf/2202.05924v2#page=5 "Our results contrast with Amodei & Hernandez (2018), who ﬁnd a much faster doubling period of 3.4 months between 2012 and 2018, and with Lyzhov (2021), who ﬁnds a much longer doubling period of >2 years between 2018 and 2020."))

