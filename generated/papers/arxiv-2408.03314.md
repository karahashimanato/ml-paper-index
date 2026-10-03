<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters

- カード: [`arxiv-2408.03314`](../../papers/arxiv-2408.03314.yaml)
- 著者: Charlie Snell, Jaehoon Lee, Kelvin Xu, Aviral Kumar
- 年・掲載: 2024
- 原論文: [PDF](https://arxiv.org/pdf/2408.03314v1)(arXiv v1、カード作成時に読んだ版)
- タグ: efficiency-evaluation, large-language-models, scaling-laws
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Main claim (abstract wording), for PaLM 2-S* on MATH only: allocating test-time compute adaptively per prompt (by difficulty bin) improves the efficiency of test-time compute scaling by more than 4x compared to a best-of-N baseline. The body states 'up to 4x less test-time compute' (for PRM search it only 'nearly' outperforms best-of-N; with predicted rather than oracle bins some benefits diminish at higher budgets), and the Discussion states 2-4x.([Abstract, p.1](https://arxiv.org/pdf/2408.03314v1#page=1 "Using this compute-optimal strategy, we can improve the efficiency of test-time compute scaling by more than 4× compared to a best-of-N baseline."))
- **c2** FLOPs-matched claim (PaLM 2-S* on MATH): on problems where the smaller base model has somewhat non-trivial success rates, test-time compute can outperform a ~14x larger pretrained model (greedy decoding, parameters scaled with fixed data); per Section 7 this depends on difficulty bin and the inference/pretraining token ratio R (see c5).([Abstract, p.1](https://arxiv.org/pdf/2408.03314v1#page=1 "Additionally, in a FLOPs-matched evaluation, we find that on problems where a smaller base model attains somewhat non-trivial success rates, test-time compute can be used to outperform a 14× larger model."))
- **c3** Experimental range: a single base model, PaLM 2-S* (Codey), fine-tuned for revisions or used with a PRM verifier, evaluated only on MATH with the 12k train / 500 test split of Lightman et al.; the authors say they believe the model is representative and think the findings likely transfer to similar models (not tested).([Experimental Setup, p.6](https://arxiv.org/pdf/2408.03314v1#page=6 "We conduct our analysis using the PaLM 2-S* [3] (Codey) base model."))
- **c4** Compute counting: pretraining FLOPs approximated as 6 N D_pretrain and inference FLOPs as 2 N D_inference; the exchange depends on R = D_inference / D_pretrain, compared at R = 0.16, 0.79 and 22.([Exchanging Pretraining and Test-Time Compute, p.14](https://arxiv.org/pdf/2408.03314v1#page=14 "To determine pretraining FLOPs, use use the common approximation 𝑋= 6𝑁𝐷pretrain [14], and for inference FLOPs, we use 𝑌= 2𝑁𝐷inference [29]."))
- **c5** Not 1-to-1 exchangeable (FLOPs-matched comparison with PaLM 2-S* on MATH, oracle difficulty bins, R = 0.16/0.79/22): on easy/medium questions or with small inference requirements test-time compute can cover for additional pretraining, but on challenging questions outside the base model's capabilities or under higher inference load, pretraining is likely more effective.([Exchanging Pretraining and Test-Time Compute (takeaways), p.15](https://arxiv.org/pdf/2408.03314v1#page=15 "However, on challenging questions which are outside a given base model’s capabilities or under higher inference requirement, pretraining is likely more effective for improving performance."))
- **c6** Cost not counted: estimating question difficulty itself costs inference compute, and the experiments do not account for this cost, for simplicity.([How to Scale Test-Time Computation Optimally, p.6](https://arxiv.org/pdf/2408.03314v1#page=6 "This is a crucial avenue for future work (see Section 8) and our experiments do not account for this cost largely for simplicity, since our goal is to present some of the first results of what is in fact possible by effectively allocating test-time compute."))
- **c7** Oracle difficulty in the FLOPs-matched figure: the pretraining-vs-test-time comparison (Figure 9) plots the compute-optimal policy within oracle difficulty bins, i.e. bins computed from ground-truth correctness of 2048 samples per question (the paper also defines model-predicted bins from verifier scores and uses them in e.g. Figures 4 and 8, but Figure 9 shows only the oracle-bin policy, which assumes ground-truth access unavailable at deployment).([Exchanging Pretraining and Test-Time Compute (Figure 9), p.15](https://arxiv.org/pdf/2408.03314v1#page=15 "Each line represents the performance of scaling test-time compute with our compute-optimal policy in each oracle difficulty bin."))

