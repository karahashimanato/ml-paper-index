<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Calibrate Before Use: Improving Few-Shot Performance of Language Models

- カード: [`arxiv-2102.09690`](../../papers/arxiv-2102.09690.yaml)
- 著者: Tony Z. Zhao, Eric Wallace, Shi Feng, Dan Klein, Sameer Singh
- 年・掲載: 2021 ICML 2021
- 原論文: [PDF](https://arxiv.org/pdf/2102.09690v2)(arXiv v2、カード作成時に読んだ版)
- タグ: in-context-learning, large-language-models, llm-evaluation, natural-language-understanding
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Instability of few-shot in-context learning: with GPT-3 2.7B on 4-shot SST-2 and a fixed format, varying only the permutation of the training examples changed accuracy from near chance (54.3%) to near state-of-the-art (93.4%); the authors state permutation can be as important as, or more important than, which examples are chosen, and that the variance persists with more examples (up to 16) and larger models.([Section 3, p.3](https://arxiv.org/pdf/2102.09690v2#page=3 "varying the permutation of the train-
ing examples can cause accuracy to go from near chance
(54.3%) to near state-of-the-art (93.4%)."))
- **c2** Majority label bias: GPT-3 is biased toward answers that are frequent in the prompt (with unbalanced prompts it heavily predicts the majority class), and the authors attribute the frequently observed drop from 0-shot to 1-shot to the model repeating the class of the single training example; on 4-shot LAMA with GPT-3 2.7B, 50.2% of predictions repeat one of the four training answers versus a correct repeat rate of 24.7%.([Section 4, p.4](https://arxiv.org/pdf/2102.09690v2#page=4 "On the
validation set for 4-shot LAMA with GPT-3 2.7B, 50.2%
of the model predictions are a repeat of one of the four train-
ing answers (the correct repeat rate is 24.7%)."))
- **c3** Recency bias: the model tends to repeat answers that appear toward the end of the prompt, which aggravates the majority label bias and can outweigh it (a 'P P P N' SST-2 prompt led to nearly 90% Negative predictions); the authors say it helps explain why the permutation of training examples matters, and it also affects generation (LAMA answers closer to the end are more likely to be repeated).([Section 4, p.4](https://arxiv.org/pdf/2102.09690v2#page=4 "The model’s majority label bias is aggravated
by its recency bias: the tendency to repeat answers that ap-
pear towards the end of the prompt."))
- **c4** Common token bias: GPT-3 is biased toward tokens common in its pre-training distribution, which is 'likely suboptimal' for the downstream answer distribution; e.g. on DBPedia (balanced, 14-way) it predicts 'book' 11 times more often than 'artist', and the frequency of a label name (Google Ngrams) and the rate GPT-3 predicts its class (0-shot, validation set) correlate moderately (r = 0.67). The authors say this helps explain why the choice of label names matters.([Section 4, p.5](https://arxiv.org/pdf/2102.09690v2#page=5 "In fact, there is a moderate correlation (r = 0.67) between
the frequency of a DBPedia label name and the rate at which
GPT-3 predicts its class."))
- **c5** Contextual calibration: the output probabilities (label-name probabilities renormalized to one for classification; first-token probabilities for generation) are transformed by an affine map restricted to a diagonal W (vector scaling); W = diag(p_cf)^-1 and b = 0, where p_cf is the prediction for a content-free input, averaged over 'N/A', '[MASK]' and the empty string. It is applied to probabilities rather than logits because the OpenAI API only returned output probabilities, and only the first output token is calibrated for generation tasks.([Section 5, p.5](https://arxiv.org/pdf/2102.09690v2#page=5 "The key idea is that the model’s bias towards
certain answers can be estimated by feeding in a content-
free input such as the string “N/A”."))
- **c6** Protocol: GPT-3 at 2.7B, 13B and 175B parameters accessed through the OpenAI API, plus GPT-2 1.5B; for the main results a fixed prompt format with five random sets of training examples in arbitrary order, labels not artificially balanced, the same sets for baseline and calibration; 0 to 8 shots because more shots made API queries prohibitively expensive.([Section 5.1, p.6](https://arxiv.org/pdf/2102.09690v2#page=6 "We
use labeling budgets of 0–8 examples; using more than 8-
shots causes the cost of querying the OpenAI API to become
prohibitively expensive."))
- **c7** On prompt engineering, the authors state contextual calibration does not eliminate the need to engineer prompts but mitigates it, making the accuracy of the best, average and worst-case prompts more similar (and higher).([Section 6, p.7](https://arxiv.org/pdf/2102.09690v2#page=7 "Contextual
calibration does not eliminate the need to engineer prompts,
however, it does mitigate it: contextual calibration makes the
accuracy of the best, average, and worst-case prompts more
similar (and higher)."))
- **c8** Consequence for probing: since prompt completion is also used to probe LMs' factual or commonsense knowledge, the authors suggest such probing methods may underestimate model accuracy and recommend that future work take advantage of contextual calibration.([Section 7, p.8](https://arxiv.org/pdf/2102.09690v2#page=8 "Our results suggest that these probing methods
may underestimate model accuracy, and we recommend that
future work take advantage of contextual calibration."))

