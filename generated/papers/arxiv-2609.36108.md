<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# LoopICL: Looping a single transformer block to solve tabular tasks

- カード: [`arxiv-2609.36108`](../../papers/arxiv-2609.36108.yaml)
- 著者: Amir Rezaei Balef, Katharina Eggensperger
- 年・掲載: 2026
- 原論文: [PDF](https://arxiv.org/pdf/2609.36108v1)(arXiv v1、カード作成時に読んだ版)
- タグ: in-context-learning, tabular-attention, tabular-classification, tabular-foundation-model
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** LoopICL is a looped transformer whose design decouples parameter count from computational depth.([Abstract, p.1](https://arxiv.org/pdf/2609.36108v1#page=1 "We introduce LoopICL, a looped transformer whose core design decouples parameter count from computational depth."))
- **c2** In its standard setting, LoopICL performs competitively with TabICLv2 on TabArena and TALENT at the same FLOPs while using far fewer parameters.([Abstract, p.1](https://arxiv.org/pdf/2609.36108v1#page=1 "In its standard setting, LoopICL performs competitively with TabICLv2 on TabArena and TALENT at the same computational cost (FLOPs), while using nearly 90% fewer parameters."))
- **c3** Ablations use intermediate checkpoints evaluated on synthetic prior tasks and on 10 folds of the 54-dataset development set used by TabICLv2 and TabPFNv2, without ensembling.([Experiments, p.6](https://arxiv.org/pdf/2609.36108v1#page=6 "We study classification performance averaged across 1,000 synthetic tasks sampled from the prior and across 10 folds of the 54 development set used in TabICLv2 and TabPFNv2 (Hollmann et al., 2025) , without any ensembling."))
- **c4** The final comparison is on TabArena and TALENT, with LoopICL evaluated as an ensemble of 8 members.([Experiments, p.8](https://arxiv.org/pdf/2609.36108v1#page=8 "We evaluate LoopICL using an ensemble of 8 members."))
- **c5** On TALENT all models are run on an A100 under identical conditions; on TabArena competitor runtimes are taken from the published benchmark and should not be used for direct runtime comparison.([Experiments (Figure 7 caption), p.9](https://arxiv.org/pdf/2609.36108v1#page=9 "For TabArena, competitor runtimes are taken from the published benchmark and may reflect different hardware; these results should not be used for direct runtime comparisons of LoopICL with other baselines."))
- **c6** The current model supports classification only; regression is left for future work.([Limitations, p.10](https://arxiv.org/pdf/2609.36108v1#page=10 "The current model supports classification tasks; extending it to regression tasks is left for future work."))

