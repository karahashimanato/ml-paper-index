<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity

- カード: [`arxiv-2101.03961`](../../papers/arxiv-2101.03961.yaml)
- 著者: William Fedus, Barret Zoph, Noam Shazeer
- 年・掲載: 2021
- 原論文: [PDF](https://arxiv.org/pdf/2101.03961v3)(arXiv v3、カード作成時に読んだ版)
- タグ: deep-learning, efficiency-evaluation, language-modeling, large-language-models, mixture-of-experts, scaling-laws, self-supervised
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Motivation/method: MoE models select different parameters per example, giving a sparsely-activated model with very many parameters but constant computational cost; Switch Transformer simplifies MoE routing to reduce complexity, communication cost and instability.([Abstract, p.1](https://arxiv.org/pdf/2101.03961v3#page=1 "The result is a sparsely-activated model—with an outrageous number of parameters—but a constant computational cost."))
- **c2** Main claim: models built from T5-Base and T5-Large obtain up to 7x increases in pre-training speed with the same computational resources; pre-training up to trillion-parameter models on C4 achieves a 4x speedup over T5-XXL (the Table 9 caption specifies the 1.6T Switch-C as 4x faster to a fixed perplexity with the same compute budget; footnote 10 says the T5-XXL quality gap is a lower bound because T5-XXL was pretrained on an easier C4 version). The contributions list phrases the 7x+ speedup as using the same FLOPS per token.([Abstract, p.1](https://arxiv.org/pdf/2101.03961v3#page=1 "We design models based oﬀT5-Base and T5-Large (Raﬀel et al., 2019) to obtain up to 7x increases in pre-training speed with the same computational resources."))
- **c3** Scaling regime: following Kaplan et al., the scaling study considers a regime not bottlenecked by compute or data, using C4 with over 180B target tokens and training until diminishing returns.([Scaling Properties, p.11](https://arxiv.org/pdf/2101.03961v3#page=11 "To avoid the data bottleneck, we use the large C4 corpus with over 180B target tokens (Raﬀel et al., 2019) and we train until diminishing returns are observed."))
- **c4** Step-basis vs wall-clock: since Switch models have roughly the same FLOPs per token as the baseline but add cross-device communication and routing computation, the authors caution that higher sample efficiency per step does not necessarily translate to better quality per wall-clock time, and therefore also compare on a time basis.([Scaling Results on a Time-Basis, p.13](https://arxiv.org/pdf/2101.03961v3#page=13 "Therefore, the increased sample eﬃciency observed on a step-basis doesn’t necessarily translate to a better model quality as measured by wall-clock."))
- **c5** Time-basis protocol: in the time comparison all models are trained on 32 TPUv3 cores with equal FLOPs per example, and, for a fixed amount of computation and training time, the 64-expert Switch-Base reaches the same quality as T5-Base in one-seventh of the time.([Scaling Results on a Time-Basis (Figure 5), p.13](https://arxiv.org/pdf/2101.03961v3#page=13 "All models trained on 32 TPUv3 cores with equal FLOPs per example."))
- **c6** Versus a larger dense model: Switch-Base (64 experts) is compared to T5-Large, which applies 3.5x more FLOPs per token, and on a wall-clock basis Switch-Base is still faster (2.5x speedup).([Scaling Versus a Larger Dense Model (Figure 6), p.14](https://arxiv.org/pdf/2101.03961v3#page=14 "Right Plot: As before, on a wall-clock basis, we ﬁnd that Switch-Base is still faster, and yields a 2.5x speedup over T5-Large."))
- **c7** Limitation: despite similar C4 perplexities, the 1.6T-parameter Switch-C scores lower on SQuAD than the smaller Switch-XXL, which uses about 10x the FLOPs per token; the authors say this suggests a poorly understood dependence between fine-tuning quality, FLOPs per token and parameter count (they also report Switch-XXL training instability as unsolved).([Future Work, p.26](https://arxiv.org/pdf/2101.03961v3#page=26 "This suggests a poorly understood dependence between ﬁne-tuning quality, FLOPS per token and number of parameters."))

