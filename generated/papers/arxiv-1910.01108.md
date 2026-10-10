<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# DistilBERT, a distilled version of BERT: smaller, faster, cheaper and lighter

- カード: [`arxiv-1910.01108`](../../papers/arxiv-1910.01108.yaml)
- 著者: Victor Sanh, Lysandre Debut, Julien Chaumond, Thomas Wolf
- 年・掲載: 2019 EMC^2 Workshop at NeurIPS 2019
- 原論文: [PDF](https://arxiv.org/pdf/1910.01108v4)(arXiv v4、カード作成時に読んだ版)
- タグ: deep-learning, knowledge-distillation, model-compression, natural-language-understanding, self-supervised
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Training loss: the student is trained with L_ce = sum_i t_i log(s_i) over the teacher's soft probabilities, using a softmax temperature (following Hinton et al., 2015) applied to both student and teacher during training and set to 1 at inference; the final objective is a linear combination of L_ce with the masked language modeling loss L_mlm, plus a cosine embedding loss L_cos aligning hidden-state directions. The temperature value and the combination weights were not found in the text (searched for temperature, weight, alpha).([Section 2, p.2](https://arxiv.org/pdf/1910.01108v4#page=2 "We found it beneﬁcial to add a cosine embedding loss (Lcos) which will tend to align the directions of the student and teacher hidden states vectors."))
- **c2** Student architecture: same general architecture as BERT with the token-type embeddings and pooler removed and the number of layers reduced by a factor of 2; the authors justify reducing depth rather than hidden size by their investigations that changes in the hidden size have a smaller impact on computational efficiency (for a fixed parameter budget) than other factors like the number of layers.([Section 3, p.2](https://arxiv.org/pdf/1910.01108v4#page=2 "Thus we focus on reducing the number of layers."))
- **c3** Student initialization, described as an important element for the sub-network to converge: exploiting the common dimensionality, the student is initialized from the teacher by taking one layer out of two.([Section 3, p.2](https://arxiv.org/pdf/1910.01108v4#page=2 "we initialize the student from the teacher by taking one layer out of two."))
- **c4** Distillation setup: following RoBERTa best practices, very large batches (up to 4K examples with gradient accumulation), dynamic masking and no next-sentence-prediction objective; same corpus as BERT (English Wikipedia and Toronto Book Corpus); trained on 8 16GB V100 GPUs for approximately 90 hours, compared with RoBERTa's 1 day on 1024 32GB V100s.([Section 3, p.3](https://arxiv.org/pdf/1910.01108v4#page=3 "DistilBERT was trained on 8 16GB V100 GPUs for approximately 90 hours."))
- **c5** GLUE evaluation: scores are reported on the development sets of the 9 GLUE tasks, fine-tuning without ensembling or multi-tasking, against the GLUE authors' ELMo + two BiLSTMs baseline; BERT and DistilBERT results are medians of 5 runs with different seeds (Table 1 caption). The authors state DistilBERT retains 97% of BERT's performance with 40% fewer parameters.([Section 4, p.3](https://arxiv.org/pdf/1910.01108v4#page=3 "DistilBERT also compares surprisingly well to BERT, retaining 97% of the performance with 40% fewer parameters."))
- **c6** Size and speed: measured as the time for a full pass over the STS-B development set on CPU (Intel Xeon E5-2690 v3) with batch size 1, DistilBERT has 40% fewer parameters and is 60% faster than BERT; in an iPhone 7 Plus question-answering app it is 71% faster than BERT excluding tokenization, and the model weighs 207 MB.([Section 4.1, p.4](https://arxiv.org/pdf/1910.01108v4#page=4 "DistilBERT has 40% fewer parameters than BERT and is 60% faster than BERT."))
- **c7** Ablation on GLUE macro-score: removing the masked language modeling loss has little impact while the two distillation losses account for a large portion of the performance; in Related work the authors add that, as shown by the ablation, leveraging the teacher's knowledge with initialization and additional losses leads to substantial gains.([Section 4.2, p.4](https://arxiv.org/pdf/1910.01108v4#page=4 "Table 4 presents the deltas with the full triple loss: removing the Masked Language Modeling loss has little impact while the two distillation losses account for a large portion of the performance."))
- **c8** Conflict of interest: the authors (Hugging Face) release the trained weights and training code in the Transformers library from Hugging Face (Wolf et al., 2019, on which all four authors are co-authors).([Section 1, p.2](https://arxiv.org/pdf/1910.01108v4#page=2 "We have made the trained weights available along with the training code in the Transformers2"))

