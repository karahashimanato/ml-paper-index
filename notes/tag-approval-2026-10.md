# タグ追加の承認記録(2026-10)

`registry/tags.yaml` に 23 個のタグが、CLAUDE.md の「新しいタグはユーザーに提案してから使う」に反して、提案なしで追加された
(コミット ffebbf9、承認済み候補のカード化と解釈可能性・量子化の記事の作成時)。
2026-10-03 にユーザーへ経緯と影響を報告し、23 個すべての採用が承認された。

保留: `large-language-models` は手法の系統として広く、`post-hoc` は `model-explanation`・`feature-attribution` と付くカードが重なる可能性がある。
統合するかは未決定(重なりはまだ数えていない)。

| 種類 | タグ | 親 | 承認時のカード数 |
|---|---|---|---|
| tasks | change-point-detection | drift-detection | 2 |
| tasks | stream-classification | | 4 |
| tasks | time-series-classification | | 2 |
| tasks | tabular-data-generation | | 4 |
| tasks | tabular-imputation | | 1 |
| tasks | model-explanation | | 15 |
| tasks | model-compression | | 20 |
| method_families | feature-attribution | | 17 |
| method_families | saliency-maps | feature-attribution | 5 |
| method_families | attention-explanations | | 2 |
| method_families | interpretable-models | | 4 |
| method_families | quantization | | 17 |
| method_families | post-training-quantization | quantization | 14 |
| method_families | quantization-aware-training | quantization | 4 |
| method_families | pruning | | 5 |
| method_families | knowledge-distillation | | 2 |
| method_families | large-language-models | | 30 |
| method_families | gaussian-processes | | 4 |
| method_families | kernel-methods | | 9 |
| method_families | graph-neural-networks | | 7 |
| method_families | imbalance-resampling | | 2 |
| paradigms | self-supervised | | 14 |
| paradigms | post-hoc | | 27 |

`spectral-data`(RamanPFN、arxiv-2608.02157 用)は未決定で、まだ追加していない。
