<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# FrugalGPT: How to Use Large Language Models While Reducing Cost and Improving Performance

- カード: [`arxiv-2305.05176`](../../papers/arxiv-2305.05176.yaml)
- 著者: Lingjiao Chen, Matei Zaharia, James Zou
- 年・掲載: 2023
- 原論文: [PDF](https://arxiv.org/pdf/2305.05176v1)(arXiv v1、カード作成時に読んだ版)
- タグ: large-language-models, model-cascades, model-selection, post-hoc, supervised
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Switching signal: the cascade decides whether to accept an API's answer or call the next API using a generation scoring function g(query, answer) in [0,1]; the authors state it can be obtained by training a simple regression model that predicts whether a generation is correct from the query and the generated answer (i.e. the score is computed after the cheaper model has answered).([LLM cascade, p.5](https://arxiv.org/pdf/2305.05176v1#page=5 "The scoring function can be obtained by training a simple regression model that learns whether a generation is correct from the query and a generated answer."))
- **c2** Thresholds and budget: the API list and the per-position threshold vector are learned jointly by maximizing expected reward subject to an average-cost budget b; because this is a mixed-integer problem, the authors use a specialized optimizer that prunes API lists with small answer disagreement and approximates the objective by interpolation over a few samples.([LLM cascade, p.6](https://arxiv.org/pdf/2305.05176v1#page=6 "To address this issue, we develop a specialized optimizer that (i) prunes the search space of L by ignoring any list of LLMs with small answer disagreement, and (ii) approximates the objective by interpolating it within a few samples."))
- **c3** Evaluation setup (models and cost): 12 commercial LLM APIs from OpenAI, AI21, CoHere, Textsynth and ForeFrontAI; cost is computed from the providers' per-token input/output prices and per-request fees (Table 1, prices retrieved March 2023).([Experiments, p.6](https://arxiv.org/pdf/2305.05176v1#page=6 "We have selected 12 LLM APIs from 5 mainstream providers, namely, OpenAI [Ope], AI21 [AI2], CoHere [CoH], Textsynth [Tex], and ForeFrontAI [FFA]."))
- **c4** Evaluation protocol: three datasets (HEADLINES financial news, OVERRULING legal sentences, COQA reading comprehension adapted to direct query answering), cascade length fixed at 3, and each dataset randomly split into a training set used to learn the cascade (its components being the scoring function and the API list with thresholds) and a test set. Thresholds are thus set on the training split; no separate validation split for threshold setting or scorer tuning was found in the text, and no shifted or out-of-distribution test set is used (random split only).([Experiments, p.6](https://arxiv.org/pdf/2305.05176v1#page=6 "Each dataset is randomly split into a training set to learn the LLM cascade and a test set for evaluation."))
- **c5** Main empirical claim (abstract): FrugalGPT can match the best individual LLM (e.g. GPT-4) with up to 98% cost reduction, or improve accuracy over GPT-4 by 4% at the same cost.([Abstract, p.1](https://arxiv.org/pdf/2305.05176v1#page=1 "Our experiments show that FrugalGPT can match the performance of the best individual LLM (e.g. GPT-4) with up to 98% cost reduction or improve the accuracy over GPT-4 by 4% with the same cost."))
- **c6** Failure mode of the switching mechanism: in an example where all LLMs in the chain give the same answer, FrugalGPT is unsure whether the first LLMs are correct and queries every LLM in the chain; the authors call avoiding such cases an open problem.([Experiments, p.10](https://arxiv.org/pdf/2305.05176v1#page=10 "However, FrugalGPT is unsure if the ﬁrst LLMs are correct, resulting in the need to query all LLMs in the chain."))
- **c7** Stated limitations: training the cascade needs labeled examples, and for the cascade to work well the training examples should come from the same or a similar distribution as the test examples; learning the cascade is an upfront cost that pays off when the final query set is larger than the training data.([Discussions, Limitations and Future Prospects, p.10](https://arxiv.org/pdf/2305.05176v1#page=10 "And in order for the cascade to work well, the training examples should be from the same or similar distribution as the test examples."))

