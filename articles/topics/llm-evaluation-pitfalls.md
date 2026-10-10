---
title: 大規模言語モデルの評価の落とし穴 — 汚染、プロンプトへの敏感さ、LLM による採点、ベンチマークの誤り、再現性
kind: topic
tags: [llm-evaluation]
depends_on: [arxiv-2308.08493, arxiv-2310.17623, arxiv-2311.09783, arxiv-2405.00332, arxiv-2102.09690, arxiv-2310.11324, arxiv-2309.03882, arxiv-2306.05685, arxiv-2305.17926, arxiv-2403.04132, arxiv-2009.03300, arxiv-2406.04127, arxiv-2211.09110, arxiv-2405.14782, arxiv-2206.07682, arxiv-2304.15004]
written_at: 2026-10-11
written_by: claude-opus-5-5 via Claude Code
---

# 大規模言語モデルの評価の落とし穴 — 汚染、プロンプトへの敏感さ、LLM による採点、ベンチマークの誤り、再現性

<!-- generated:stale -->
> 未反映のカードはありません。
<!-- /generated:stale -->

## この記事の読み方

大規模言語モデル(LLM)の性能は、ベンチマークの点数で比べられることが多い。しかしその点数は、モデルの能力だけでなく、評価のやり方によって大きく変わりうる。
この記事は14本の新しいカードと既存の2本のカードから、次の5つの落とし穴を整理する。

1. **汚染**:評価データが学習データに含まれている
2. **プロンプトと形式への敏感さ**:問い方を少し変えるだけで点数や順位が変わる
3. **LLM による採点の偏り**と、人の好みによる比較
4. **ベンチマーク自体の誤り**と、指標の選び方
5. **評価の再現性**

性能の数値は書かない。各論文のページの結果表を参照のこと(カードは結果表を記録せず、主張だけを記録している)。
混合エキスパートや状態空間モデルの比較でも、問題の書き方で差が大きく変わる例があった([混合エキスパートと状態空間モデル](../methods/moe-and-state-space-models.md) の4節)。

## 1. 汚染:評価データを学習していないか

LLM は大量のウェブのデータで学習されるので、公開されたベンチマークの問題が学習データに入っている可能性がある。これを**汚染**という。学習データが公開されていない場合、確かめることは難しい。HELM の著者らも、学習データにアクセスできず開示もされていなければ、評価データで学習されたかどうかは検証できないと述べている [arxiv-2211.09110#c8](https://arxiv.org/pdf/2211.09110v2#page=45 "We encourage more proactive documentation/disclosure of model contamination, as well as the use of canaries or other methods for minimizing contamination, for future work on language model development to maintain the health of the evaluation ecosystem.")。

### 汚染を検出する方法

| 方法 | 必要なもの | 考え方 | 限界 |
|---|---|---|---|
| 誘導した指示(Golchin と Surdeanu)| モデルの出力だけ | データセット名と問題の冒頭を与えて続きを書かせ、元の問題とほぼ一致するかを見る [arxiv-2308.08493#c1](https://arxiv.org/pdf/2308.08493v3#page=1 "An instance is ﬂagged as contaminated if the LLM’s output either exactly or nearly matches the latter segment of the reference.") | 汚染していても完全な複製が出るとは限らない [arxiv-2308.08493#c2](https://arxiv.org/pdf/2308.08493v3#page=3 "Note that, due to the inherent probabilistic behavior of LLMs, achieving perfect replicas is not always possible even when contamination is certain.") |
| 順序の交換可能性の検定(Oren ら)| 系列の対数確率 | データの正規の順序が、並べ替えた順序より出やすいかを統計的に検定する [arxiv-2310.17623#c1](https://arxiv.org/pdf/2310.17623v2#page=3 "In our setting, the only method we have to study θ is through a log probability query log pθ(s) for a sequence s (i.e. no access to dataset or parameters).") [arxiv-2310.17623#c3](https://arxiv.org/pdf/2310.17623v2#page=5 "Run a one-sided t-test for E[si] > 0, returning the associated p-value of the test as p.") | データが交換可能であることを仮定し [arxiv-2310.17623#c2](https://arxiv.org/pdf/2310.17623v2#page=3 "Notably, this assumption would hold under the standard assumption that the dataset is a collection of i.i.d examples.")、問題がそのまま含まれる汚染しか扱えない [arxiv-2310.17623#c9](https://arxiv.org/pdf/2310.17623v2#page=11 "Verbatim memorization of a test set is not the only form of contamination, and our test cannot rule out the possibility of more complex forms of partial contamination.") |
| 検索(Deng ら)| 学習コーパス | ベンチマークの問題を、学習コーパスから BM25 で検索する [arxiv-2311.09783#c1](https://arxiv.org/pdf/2311.09783v2#page=4 "Our system employs the BM25 indexing method, widely used for ranking functions in information retrieval and text search systems.") | コーパス全体が必要で時間がかかる [arxiv-2311.09783#c8](https://arxiv.org/pdf/2311.09783v2#page=9 "TS-Guessing, while suitable for a broad range of benchmarks, including those requiring advanced reasoning, is considered less reliable since it relies on inferred knowledge rather than direct retrieval.") |
| 隠した選択肢の推測(Deng ら)| モデルの出力だけ | 誤りの選択肢の1つを隠し、モデルがそれを正確に言い当てられるかを見る [arxiv-2311.09783#c3](https://arxiv.org/pdf/2311.09783v2#page=5 "We intentionally avoid masking the correct option to prevent the model from directly providing the correct answer, instead compelling it to guess an incorrect answer from a vast set of erroneous possibilities.") | 検索より信頼性が低い [arxiv-2311.09783#c8](https://arxiv.org/pdf/2311.09783v2#page=9 "TS-Guessing, while suitable for a broad range of benchmarks, including those requiring advanced reasoning, is considered less reliable since it relies on inferred knowledge rather than direct retrieval.") |

Oren らの検定は、学習データ中で同じ問題が何度も繰り返されていれば検出できるが、1回しか含まれない場合は検出できなかった [arxiv-2310.17623#c6](https://arxiv.org/pdf/2310.17623v2#page=7 "We find that we cannot reliably detect duplication rates of 1, but that at counts of 2 and 4 we begin to detect some test sets (gray points below the dashed line) and that the detection threshold is around a duplication rate of 4.")。

### 新しく作った問題で確かめる(GSM1k)

Zhang らは、算数の問題集 GSM8k と同じような問題を、LLM を一切使わずに人が新しく作り(GSM1k)、両方での成績を比べた [arxiv-2405.00332#c1](https://arxiv.org/pdf/2405.00332v4#page=4 "No language models were used to construct this dataset.")。

- いくつかのモデルの系列は、GSM8k で GSM1k より系統的に成績が良く、**過学習**の兆候を示した [arxiv-2405.00332#c6](https://arxiv.org/pdf/2405.00332v4#page=7 "Several families of models, including the Phi and Mistral families of models, show systematic tendencies to perform stronger on GSM8k compared to GSM1k for almost every release and scale of models.")。
- 一方、最先端に近いモデルは、両方でほぼ同じ成績だった [arxiv-2405.00332#c7](https://arxiv.org/pdf/2405.00332v4#page=8 "Since the hypothesis that Mistral took unique care in ensuring that only their largest model was free from data contamination seems unlikely, we lean instead towards the hypothesis that sufficiently strong LLMs also learn elementary reasoning ability during training.")。
- モデルが GSM8k の問題を生成する確率と、2つの成績の差には、正の相関があった [arxiv-2405.00332#c8](https://arxiv.org/pdf/2405.00332v4#page=8 "This result suggests that some of the reason for overfitting is due to partial memorization of the test set.")。ただし、外れ値もあり、汚染だけでは説明しきれない [arxiv-2405.00332#c9](https://arxiv.org/pdf/2405.00332v4#page=9 "Conversely, the reverse is also true: small amounts of data contamination do not necessarily lead to overfitting.")。
- 著者ら自身、2つのデータセットは「よく似ているが、同じ分布ではない」と注意している [arxiv-2405.00332#c2](https://arxiv.org/pdf/2405.00332v4#page=4 "We would recommend reading all results with the understanding that GSM8k and GSM1k are only highly similar, but not identically distributed despite all our efforts below.")。著者は全員、このデータセットを作った Scale AI の所属である(カードの notes 参照)。

MMLU の原論文も、暗記していれば問題の生成確率が高く正答率も高いはずだと考え、その関係がないことを間接的な確認として示していた [arxiv-2009.03300#c7](https://arxiv.org/pdf/2009.03300v3#page=14 "This suggests that our exact questions were not memorized.")。

## 2. プロンプトと形式への敏感さ

### 例の並べ方だけで変わる

Zhao らは、少数の例を与えるプロンプト(few-shot)で、例の**並べ方**を変えるだけで、正答率が偶然と同程度から最先端に近い水準まで変わることを示した [arxiv-2102.09690#c1](https://arxiv.org/pdf/2102.09690v2#page=3 "varying the permutation of the train-
ing examples can cause accuracy to go from near chance
(54.3%) to near state-of-the-art (93.4%).")。原因として、次の3つの偏りを挙げている。

- **多数派のラベルの偏り**:プロンプトに多く出てくる答えを選びやすい [arxiv-2102.09690#c2](https://arxiv.org/pdf/2102.09690v2#page=4 "On the
validation set for 4-shot LAMA with GPT-3 2.7B, 50.2%
of the model predictions are a repeat of one of the four train-
ing answers (the correct repeat rate is 24.7%).")。
- **直近の偏り**:プロンプトの終わりのほうに出てくる答えを繰り返しやすい [arxiv-2102.09690#c3](https://arxiv.org/pdf/2102.09690v2#page=4 "The model’s majority label bias is aggravated
by its recency bias: the tendency to repeat answers that ap-
pear towards the end of the prompt.")。
- **よく出る単語の偏り**:事前学習でよく出る単語を答えにしやすい [arxiv-2102.09690#c4](https://arxiv.org/pdf/2102.09690v2#page=5 "In fact, there is a moderate correlation (r = 0.67) between
the frequency of a DBPedia label name and the rate at which
GPT-3 predicts its class.")。

対策として、「N/A」のような内容のない入力に対するモデルの出力で、確率を補正する方法を提案した [arxiv-2102.09690#c5](https://arxiv.org/pdf/2102.09690v2#page=5 "The key idea is that the model’s bias towards
certain answers can be estimated by feeding in a content-
free input such as the string “N/A”.")。ただし、プロンプトの工夫が不要になるわけではなく、その影響を小さくするものだと述べている [arxiv-2102.09690#c7](https://arxiv.org/pdf/2102.09690v2#page=7 "Contextual
calibration does not eliminate the need to engineer prompts,
however, it does mitigate it: contextual calibration makes the
accuracy of the best, average, and worst-case prompts more
similar (and higher).")。

### 書式の細部で変わる

Sclar らは、区切り記号や空白、大文字小文字のように、意味を変えない書式の違いだけで、LLM の正答率が大きく変わることを示した [arxiv-2310.11324#c1](https://arxiv.org/pdf/2310.11324v2#page=1 "Sensitivity remains
even when increasing model size, the number of few-shot examples, or perform-
ing instruction tuning.")。

- 1か所の小さな変更(区切り記号1つなど)でも、大きく変わることが多い [arxiv-2310.11324#c7](https://arxiv.org/pdf/2310.11324v2#page=6 "For example, 24% of atomic changes
have an associated accuracy change of at least 5 points when using exact prefix matching as scoring
criteria (11% when using probability ranking).")。
- ある書式でモデル A がモデル B を上回っていても、別の書式では逆転することがある [arxiv-2310.11324#c6](https://arxiv.org/pdf/2310.11324v2#page=5 "Comparison trends between models are often reversed just by choosing different formats.")。
- 著者らは、1つの書式での点数ではなく、もっともらしい書式の範囲での**点数の幅**を報告することを勧めている [arxiv-2310.11324#c8](https://arxiv.org/pdf/2310.11324v2#page=9 "Thus, we recommend that work evaluating LLMs with prompting-based methods would
benefit from reporting a range of performance across plausible formats.")。

HELM の著者らも、最良のプロンプトの書式はモデルによって違うと報告している [arxiv-2211.09110#c6](https://arxiv.org/pdf/2211.09110v2#page=57 "The clear finding is that the best prompt formatting is not consistent across models")。

### 選択肢の記号への偏り

Zheng らは、多肢選択の問題で、LLM が特定の選択肢の記号(A、B など)を選びやすい**選択の偏り**を持つことを示した [arxiv-2309.03882#c2](https://arxiv.org/pdf/2309.03882v4#page=3 "In our study, selection bias is defined as the model’s behavioral bias to select specific option IDs as
answers.")。正解をいつも同じ位置に動かすだけで、正答率が大きく変動する [arxiv-2309.03882#c1](https://arxiv.org/pdf/2309.03882v4#page=1 "For instance, moving the golden answers
to position D degrades the accuracy of gpt-3.5-turbo by 6.3 (from 67.2 to 60.9).")。
主な原因は、記号そのものへの偏り(トークンの偏り)だった [arxiv-2309.03882#c5](https://arxiv.org/pdf/2309.03882v4#page=4 "These results confirm
that the model’s token bias is one primary intrinsic cause of selection bias.")。偏りを打ち消すように指示したり、段階的に考えさせたりしても、あまり改善しなかった [arxiv-2309.03882#c6](https://arxiv.org/pdf/2309.03882v4#page=5 "It suggests that selection bias is an inherent behavioral
bias of LLMs that cannot be addressed by simple prompt engineering.")。

### 多肢選択の問い方そのもの

HELM の著者らは、選択肢を1つのプロンプトにまとめて記号を答えさせる方法と、各選択肢を別々に採点する方法とで、同じモデルの正答率が大きく変わることを報告している [arxiv-2211.09110#c5](https://arxiv.org/pdf/2211.09110v2#page=58 "This choice can be very consequential for the model accuracy: for OPT (175B), the accuracies are 79.1%, 54.8%, and 30.2% respectively.")。
lm-eval-harness の開発者らも、MMLU 式の問い方ではほぼ偶然の水準なのに、別の問い方では高い点数を出すモデルの例を挙げ、これを測定の人工物としている [arxiv-2405.14782#c6](https://arxiv.org/pdf/2405.14782v3#page=9 "An even more extreme example is from ARC-Easy: using the “cloze” evaluation setup, GPT-NeoX achieves an accuracy of 72.4 ± 1.80% but using the MMLU-style setup it scores 26.5 ± 1.78%.")。

## 3. LLM による採点と人の好み

自由に答える問題では、正解と照合するだけでは採点できない。そこで、強い LLM に採点させる方法(LLM-as-a-judge)が使われる。

### 採点者としての LLM の偏り

Zheng らは、LLM による採点の偏りを3つ挙げた。

- **位置の偏り**:2つの答えを比べるとき、特定の位置の答えを好む [arxiv-2306.05685#c3](https://arxiv.org/pdf/2306.05685v4#page=5 "Only GPT-4 outputs consistent results in more than 60% of cases.")。2つのモデルの性能が近いほど目立ち、大きく違えばほぼ消える [arxiv-2306.05685#c4](https://arxiv.org/pdf/2306.05685v4#page=25 "the position bias is more noticeable for models with close performance and can almost disappear when the performance of the two models differs a lot.")。
- **長さの偏り**:長く冗長な答えを、明確さや正確さに関係なく好む [arxiv-2306.05685#c5](https://arxiv.org/pdf/2306.05685v4#page=5 "Table 3 shows the failure rate of LLM judges under this attack, demonstrating that all LLMs may be prone to verbosity bias though GPT-4 defends significantly better than others.")。
- **自己優遇の偏り**:自分の答えを好む。ただし、偏りがあるかどうかは断定できないとしている [arxiv-2306.05685#c6](https://arxiv.org/pdf/2306.05685v4#page=5 "Due to limited data and small differences, our study cannot determine whether the models exhibit a self-enhancement bias.")。

Wang らも、同じ採点の雛形で、GPT-4 は1番目の答えを、ChatGPT は2番目の答えを好むことを示した [arxiv-2305.17926#c1](https://arxiv.org/pdf/2305.17926v2#page=3 "Based on the same evaluation template T in Table 1, GPT-4 tends to favor the response in the first position, while ChatGPT shows a preference for the response in the second position.")。答えの順序を入れ替えて結果が変わる割合(矛盾率)を定義し [arxiv-2305.17926#c2](https://arxiv.org/pdf/2305.17926v2#page=3 "These findings indicate that LLMs can be self-conflicting due to the sensitivity of the response order in the template, with stronger models being less influenced by the placement of responses.")、順序を入れ替えて両方を平均する補正などを提案した [arxiv-2305.17926#c5](https://arxiv.org/pdf/2305.17926v2#page=5 "and we regard the response with the higher average score as the better response.")。

対策として、Zheng らは順序を入れ替えて2回採点し、両方で勝ったときだけ勝ちとする保守的な方法を使っている [arxiv-2306.05685#c8](https://arxiv.org/pdf/2306.05685v4#page=6 "However, high consistency may not imply high accuracy and we are not sure whether the few-shot examples will introduce new biases.")。数学の問題では、採点者も答えと同じ間違いをしやすいので、参照の答えを与える方法が有効だった [arxiv-2306.05685#c7](https://arxiv.org/pdf/2306.05685v4#page=6 "In Table 4, we see a significant improvement in failure rate (from 70% to 15%) over the default prompt.")。
これらの対策をとったうえで、GPT-4 による採点は人の専門家とよく一致したと報告している [arxiv-2306.05685#c9](https://arxiv.org/pdf/2306.05685v4#page=7 "The agreement under setup S2 (w/o tie) between GPT-4 and humans reaches 85%, which is even higher than the agreement among humans (81%).")。ただし、評価対象には著者ら自身のモデル(Vicuna)が含まれる [arxiv-2306.05685#c2](https://arxiv.org/pdf/2306.05685v4#page=2 "Vicuna-13B, our fine-tuned model from LLaMA-13B on high-quality conversations")。

### 人の好みによる比較(Chatbot Arena)

Chatbot Arena は、利用者が自分で入力した質問に対する2つの匿名のモデルの答えを比べ、良いほうに投票する仕組みである [arxiv-2403.04132#c2](https://arxiv.org/pdf/2403.04132v1#page=3 "Hence, we adopt a pairwise comparison mechanism where users only need to compare two model responses and vote for the better one, instead of requiring users to provide an absolute score.")。固定のベンチマークは時間とともに汚染されうる、という問題意識がある [arxiv-2403.04132#c1](https://arxiv.org/pdf/2403.04132v1#page=1 "Secondly, the test sets in these benchmarks are static, meaning they can become contaminated over time, which undermines the reliability of the evaluation results (Yang et al., 2023).")。
投票から Bradley-Terry モデルで強さを推定し [arxiv-2403.04132#c4](https://arxiv.org/pdf/2403.04132v1#page=4 "show that maximum likelihood estimators are still asymptotically normal even when these assumptions do not hold, so long as the so-called “sandwich” covariance matrix is used")、信頼区間に基づいて順位を付ける [arxiv-2403.04132#c5](https://arxiv.org/pdf/2403.04132v1#page=5 "i.e., with high probability, no model’s performance is understated.")。

著者らは、利用者が主に LLM の愛好家や研究者に偏っていると考えられること、質問がオンラインのチャットから来ていて実際の利用を反映しないかもしれないことを、限界として挙げている [arxiv-2403.04132#c9](https://arxiv.org/pdf/2403.04132v1#page=8 "This source might not accurately reflect the real-world usage of LLMs in production environments or specialized domains, potentially leading to a skewed prompt distribution.")。運営者自身が自分たちのプラットフォームを評価している点にも注意が要る(カードの notes 参照)。

## 4. ベンチマーク自体の誤りと指標の選び方

### 正解ラベルの誤り

MMLU は、学生が公開の資料から集めた57分野の多肢選択問題である [arxiv-2009.03300#c1](https://arxiv.org/pdf/2009.03300v3#page=3 "The questions in the dataset were manually collected by graduate and undergraduate students from freely available sources online.")。Gema らは、MMLU の問題を分野ごとに標本抽出して調べ、無視できない割合の問題に誤り(問題文の不明確さや正解の誤り)があることを見つけた [arxiv-2406.04127#c3](https://arxiv.org/pdf/2406.04127v3#page=4 "we estimate that 6.49% of the questions in the complete MMLU dataset contain errors")。誤りのある問題を除くと、いくつかの分野でモデルの順位が入れ替わった [arxiv-2406.04127#c6](https://arxiv.org/pdf/2406.04127v3#page=5 "For example, in the Virology subset, Llama 3.1 Instruct Turbo (405B) ranked 16th when considering all Virology instances, but ranked first when only correct instances were used.")。LLM に誤りを自動で見つけさせる方法は、まだ不十分だった [arxiv-2406.04127#c7](https://arxiv.org/pdf/2406.04127v3#page=9 "although Claude 3 Opus seems to produce the most accurate results on this task (41.9% F2 score when using retrieval-augmented generation), it is still insufficient to produce a high-quality dataset.")。

### 「創発」は指標の産物か

Wei らは、小さいモデルにはなく大きいモデルで現れる能力を**創発能力**と定義し、多くの例を報告した [arxiv-2206.07682#c1](https://arxiv.org/pdf/2206.07682v2#page=1 "We consider an ability to be emergent if it is not present in smaller models but is present in larger models.")。
これに対し Schaeffer らは、同じモデルの出力でも、非線形な指標(完全一致など)を連続的な指標に変えると、急な変化が消えることを示し、創発の多くは研究者の指標の選び方によるものだという別の説明を示した [arxiv-2304.15004#c1](https://arxiv.org/pdf/2304.15004v2#page=1 "Here, we present an alternative explanation for emergent abilities: that for a particular task and model family, when analyzing ﬁxed model outputs, emergent abilities appear due the researcher’s choice of metric rather than due to fundamental changes in model behavior with scale.") [arxiv-2304.15004#c4](https://arxiv.org/pdf/2304.15004v2#page=5 "To test these predictions, we collected outputs from the InstructGPT/GPT-3 family on two tasks: 2-shot multiplication between two 2-digit integers and 2-shot addition between two 4-digit integers.")。ただし、LLM が創発能力を持ちえないと主張しているわけではない [arxiv-2304.15004#c7](https://arxiv.org/pdf/2304.15004v2#page=9 "We emphasize that nothing in this paper should be interpreted as claiming that large language models cannot display emergent abilities; rather, our message is that previously claimed emergent abilities in [3, 8, 28, 33] might likely be a mirage induced by researcher analyses.")。Wei らの論文自身も、長い答えの完全一致が段階的な改善を創発のように見せうることを認めている [arxiv-2206.07682#c6](https://arxiv.org/pdf/2206.07682v2#page=7 "using evaluation metrics that do not give partial credit are at best an incomplete explanation, because emergent abilities are still observed on many classiﬁcation tasks (e.g., the tasks in Figure 2D–H)")。

## 5. 評価の再現性

### 細部が結果を変える

lm-eval-harness を開発してきた著者らは、評価の再現が難しい理由を整理している [arxiv-2405.14782#c1](https://arxiv.org/pdf/2405.14782v3#page=1 "In this paper we draw on three years of experience in evaluating large language models (LMs) as developers of the popular Language Model Evaluation Harness (lm-eval) (Gao et al., 2023) framework to provide guidance and lessons for the field moving forward.")。

- 意味は同じでも書き方の違う答えを、正しいと自動で判定することは難しい(「鍵となる問題」)[arxiv-2405.14782#c2](https://arxiv.org/pdf/2405.14782v3#page=2 "However, our best automated tools for determining whether two sentences are semantically equivalent are the very models we are seeking to evaluate.")。
- 空白まで含めたプロンプトの文字列や、例の選び方が結果を大きく変える [arxiv-2405.14782#c3](https://arxiv.org/pdf/2405.14782v3#page=5 "Thus, the selection of prompt affects the model rankings and research conclusions produced in addition to numeric scores themselves (Alzahrani et al., 2024).")。
- MMLU の平均を、問題ごとに取るか分野ごとに取るかで、結果が数ポイント変わる [arxiv-2405.14782#c4](https://arxiv.org/pdf/2405.14782v3#page=6 "the choice of which affects results by several percentage points")。
- 自由回答から正規表現などで答えを取り出す方法は、多くの場合不完全である [arxiv-2405.14782#c5](https://arxiv.org/pdf/2405.14782v3#page=28 "Without knowledge of the extent to what extraction code is used, how it may be tailored to a model, or without access to model outputs, it is difficult to separate models’ compliance with the evaluation format from their answer correctness.")。
- 標準誤差の推定は、問題の標本のばらつきを表すもので、実行ごとのばらつきとは別物である [arxiv-2405.14782#c7](https://arxiv.org/pdf/2405.14782v3#page=10 "We report bootstrapped standard error metrics by default, making reporting of confidence intervals (as we have done in this paper) nearly as simple as copy-pasting an additional number into one’s paper.")。

HELM は、多くのモデルを同じ条件で評価することで、それまでモデルごとにばらばらだった評価をそろえようとした [arxiv-2211.09110#c3](https://arxiv.org/pdf/2211.09110v2#page=5 "Previously, on average models were evaluated on 17.9% of our core scenarios, even after compiling evaluations dispersed across different prior works.")。それでも著者らは、費用のため少数の乱数シードしか使えず、測定の信頼性を一様に示す証拠はないと認めている [arxiv-2211.09110#c9](https://arxiv.org/pdf/2211.09110v2#page=82 "That is, both of these settings for our evaluation may render some of our claims statistically insignificant; we encourage future work to consider how to better address significance given the scale of this evaluation.")。

### 推奨されていること

lm-eval-harness の著者らは、プロンプトと評価のコードを共有すること、特定のモデルのためにプロンプトを最適化せず、プロンプトの工夫の量を開示すること、同じ条件でない限り他の論文の結果をそのまま写さないことを勧めている [arxiv-2405.14782#c8](https://arxiv.org/pdf/2405.14782v3#page=31 "Results should not be copied or reported from other papers (Marie, 2022) whenever possible, unless one can verify that the same code has been used to run the experiments in those papers.")。

## 示唆(本記事の整理)

- **汚染を疑う。** 公開から時間のたったベンチマークでは、新しく作った問題での成績と比べる [arxiv-2405.00332#c6](https://arxiv.org/pdf/2405.00332v4#page=7 "Several families of models, including the Phi and Mistral families of models, show systematic tendencies to perform stronger on GSM8k compared to GSM1k for almost every release and scale of models.")。検出の方法には、それぞれ仮定と限界がある(1節の表)。
- **1つのプロンプトの点数で比べない。** もっともらしい書式の範囲で点数の幅を見る [arxiv-2310.11324#c8](https://arxiv.org/pdf/2310.11324v2#page=9 "Thus, we recommend that work evaluating LLMs with prompting-based methods would
benefit from reporting a range of performance across plausible formats.")。順位の入れ替わりにも注意する [arxiv-2310.11324#c6](https://arxiv.org/pdf/2310.11324v2#page=5 "Comparison trends between models are often reversed just by choosing different formats.")。
- **多肢選択では、選択肢の位置や記号を入れ替えて確かめる** [arxiv-2309.03882#c1](https://arxiv.org/pdf/2309.03882v4#page=1 "For instance, moving the golden answers
to position D degrades the accuracy of gpt-3.5-turbo by 6.3 (from 67.2 to 60.9).")。
- **LLM に採点させるときは、順序を入れ替えて2回採点する** [arxiv-2306.05685#c8](https://arxiv.org/pdf/2306.05685v4#page=6 "However, high consistency may not imply high accuracy and we are not sure whether the few-shot examples will introduce new biases.") [arxiv-2305.17926#c5](https://arxiv.org/pdf/2305.17926v2#page=5 "and we regard the response with the higher average score as the better response.")。採点者と評価対象の関係(自社のモデルかどうか)も確認する。
- **ベンチマークの正解ラベルを疑う** [arxiv-2406.04127#c3](https://arxiv.org/pdf/2406.04127v3#page=4 "we estimate that 6.49% of the questions in the complete MMLU dataset contain errors")。創発のような急な変化は、指標を変えても残るかを確かめる [arxiv-2304.15004#c1](https://arxiv.org/pdf/2304.15004v2#page=1 "Here, we present an alternative explanation for emergent abilities: that for a particular task and model family, when analyzing ﬁxed model outputs, emergent abilities appear due the researcher’s choice of metric rather than due to fundamental changes in model behavior with scale.")。
- **評価のコードとプロンプトを公開する** [arxiv-2405.14782#c8](https://arxiv.org/pdf/2405.14782v3#page=31 "Results should not be copied or reported from other papers (Marie, 2022) whenever possible, unless one can verify that the same code has been used to run the experiments in those papers.")。

## わかっていないこと

- 学習データが公開されていないモデルについて、汚染を確実に否定する方法はない [arxiv-2211.09110#c8](https://arxiv.org/pdf/2211.09110v2#page=45 "We encourage more proactive documentation/disclosure of model contamination, as well as the use of canaries or other methods for minimizing contamination, for future work on language model development to maintain the health of the evaluation ecosystem.") [arxiv-2310.17623#c8](https://arxiv.org/pdf/2310.17623v2#page=10 "We strongly encourage future dataset creators to apply a random shuffle to their datasets (and to publicize this fact), which would allow our tests to be applied.")。
- 成績の差が汚染によるものか、似た問題への過学習によるものかを、完全に切り分ける方法は示されていない [arxiv-2405.00332#c9](https://arxiv.org/pdf/2405.00332v4#page=9 "Conversely, the reverse is also true: small amounts of data contamination do not necessarily lead to overfitting.")。
- LLM による採点の偏りのうち、自己優遇が本当にあるかは断定されていない [arxiv-2306.05685#c6](https://arxiv.org/pdf/2306.05685v4#page=5 "Due to limited data and small differences, our study cannot determine whether the models exhibit a self-enhancement bias.")。

## 参照カード

- [arxiv-2308.08493](../../papers/arxiv-2308.08493.yaml) Golchin & Surdeanu, "Time Travel in LLMs: Tracing Data Contamination in Large Language Models"
- [arxiv-2310.17623](../../papers/arxiv-2310.17623.yaml) Oren et al., "Proving Test Set Contamination in Black Box Language Models"
- [arxiv-2311.09783](../../papers/arxiv-2311.09783.yaml) Deng et al., "Investigating Data Contamination in Modern Benchmarks for Large Language Models"
- [arxiv-2405.00332](../../papers/arxiv-2405.00332.yaml) Zhang et al., "A Careful Examination of Large Language Model Performance on Grade School Arithmetic"
- [arxiv-2102.09690](../../papers/arxiv-2102.09690.yaml) Zhao et al., "Calibrate Before Use: Improving Few-Shot Performance of Language Models"
- [arxiv-2310.11324](../../papers/arxiv-2310.11324.yaml) Sclar et al., "Quantifying Language Models' Sensitivity to Spurious Features in Prompt Design"
- [arxiv-2309.03882](../../papers/arxiv-2309.03882.yaml) Zheng et al., "Large Language Models Are Not Robust Multiple Choice Selectors"
- [arxiv-2306.05685](../../papers/arxiv-2306.05685.yaml) Zheng et al., "Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena"
- [arxiv-2305.17926](../../papers/arxiv-2305.17926.yaml) Wang et al., "Large Language Models are not Fair Evaluators"
- [arxiv-2403.04132](../../papers/arxiv-2403.04132.yaml) Chiang et al., "Chatbot Arena: An Open Platform for Evaluating LLMs by Human Preference"
- [arxiv-2009.03300](../../papers/arxiv-2009.03300.yaml) Hendrycks et al., "Measuring Massive Multitask Language Understanding"
- [arxiv-2406.04127](../../papers/arxiv-2406.04127.yaml) Gema et al., "Are We Done with MMLU?"
- [arxiv-2211.09110](../../papers/arxiv-2211.09110.yaml) Liang et al., "Holistic Evaluation of Language Models"
- [arxiv-2405.14782](../../papers/arxiv-2405.14782.yaml) Biderman et al., "Lessons from the Trenches on Reproducible Evaluation of Language Models"
- [arxiv-2206.07682](../../papers/arxiv-2206.07682.yaml) Wei et al., "Emergent Abilities of Large Language Models"
- [arxiv-2304.15004](../../papers/arxiv-2304.15004.yaml) Schaeffer, Miranda & Koyejo, "Are Emergent Abilities of Large Language Models a Mirage?"
