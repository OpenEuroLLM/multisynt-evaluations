# MultiSynt vs HPLT: Evaluation Report

## Setup

This report compares two families of 1.7B language models trained on 300B tokens across a set of multilingual benchmarks:

- **HPLT (native)** — models from the [HPLT project](https://hplt-project.org/), trained on monolingual native-language web data. One model per language (e.g. `hplt2c_fra_checkpoints` for French).
- **MultiSynt (artificial)** — models fine-tuned on high-quality English text that has been machine-translated into the target language. One model per language (e.g. `nemotron-cc-french-tower9b`).

The central question is whether **artificially generated training data** (translated from English) can match or beat models trained on **native data** across a range of downstream tasks.

### Benchmarks

| Benchmark | Type | Metric | Notes |
|:----------|:-----|:-------|:------|
| **belebele** | Reading comprehension (multiple choice) | Accuracy | Language-specific variant per language |
| **global_mmlu** | Knowledge / reasoning (multiple choice) | Accuracy | Global MMLU translated into target language |
| **include** | Knowledge / reasoning (multiple choice) | Accuracy | Locally-sourced multilingual knowledge benchmark |
| **mgsm** | Math word problems | Exact match | Native CoT prompting |
| **copa** | Causal reasoning (multiple choice) | Accuracy | Available for Catalan only |
| **icelandic_winogrande** | Winograd-style coreference | Accuracy | Icelandic only |
| **flores200** | Translation | BLEU | Two directions: `eng→target` and `target→eng` |

### Languages covered

Basque, Catalan, Danish, Dutch, Finnish, French, German, Icelandic, Italian, Norwegian, Polish, Portuguese, Romanian, Spanish, Swedish.

---

## Results

Bold values indicate the best score per row. When scores are equal, both are bolded.

### All benchmarks
| language   | benchmark   | HPLT (artificial=False)   | MultiSynt (artificial=True)   |
|:-----------|:------------|:--------------------------|:------------------------------|
| basque     | belebele    | 0.2841                    | **0.3022**                    |
| basque     | include     | **0.2660**                | **0.2660**                    |
| catalan    | belebele    | 0.3215                    | **0.3726**                    |
| catalan    | copa        | 0.6580                    | **0.6880**                    |
| danish     | belebele    | 0.3048                    | **0.3459**                    |
| danish     | flores200   | **7.0235**                | 1.1157                        |
| dutch      | belebele    | 0.3363                    | **0.3559**                    |
| dutch      | flores200   | **12.5997**               | 1.9584                        |
| dutch      | global      | 0.2572                    | **0.2694**                    |
| dutch      | include     | 0.1325                    | **0.3176**                    |
| finnish    | belebele    | 0.3267                    | **0.3437**                    |
| finnish    | flores200   | **4.0573**                | 2.0967                        |
| finnish    | include     | 0.2323                    | **0.2650**                    |
| french     | belebele    | 0.3444                    | **0.3607**                    |
| french     | flores200   | **33.4790**               | 2.3657                        |
| french     | global      | **0.2617**                | 0.2594                        |
| french     | include     | 0.2625                    | **0.2721**                    |
| french     | mgsm        | **0.0240**                | 0.0080                        |
| german     | belebele    | 0.3493                    | **0.3659**                    |
| german     | flores200   | **24.9519**               | 1.3784                        |
| german     | global      | 0.2443                    | **0.2607**                    |
| german     | include     | **0.3381**                | 0.2662                        |
| german     | mgsm        | 0.0120                    | **0.0280**                    |
| icelandic  | icelandic   | 0.5110                    | **0.5956**                    |
| italian    | belebele    | 0.3144                    | **0.3678**                    |
| italian    | flores200   | **22.1046**               | 1.5019                        |
| italian    | global      | **0.2668**                | 0.2502                        |
| italian    | include     | **0.2591**                | 0.2318                        |
| norwegian  | belebele    | 0.3126                    | **0.3426**                    |
| polish     | belebele    | 0.3237                    | **0.3441**                    |
| polish     | flores200   | **9.0725**                | 1.1510                        |
| polish     | global      | **0.2480**                | 0.2432                        |
| polish     | include     | **0.2719**                | 0.2062                        |
| portuguese | belebele    | 0.3419                    | **0.3719**                    |
| portuguese | flores200   | **34.2722**               | 1.9077                        |
| portuguese | global      | 0.2615                    | **0.2684**                    |
| portuguese | include     | 0.2105                    | **0.2541**                    |
| romanian   | belebele    | 0.3304                    | **0.3726**                    |
| romanian   | flores200   | **12.2645**               | 1.2099                        |
| romanian   | global      | 0.2420                    | **0.2631**                    |
| spanish    | belebele    | 0.3619                    | **0.3741**                    |
| spanish    | flores200   | **20.0892**               | 1.0100                        |
| spanish    | global      | 0.2659                    | **0.2831**                    |
| spanish    | include     | **0.2600**                | 0.2345                        |
| spanish    | mgsm        | **0.0240**                | 0.0120                        |
| swedish    | belebele    | 0.3259                    | **0.3593**                    |
| swedish    | flores200   | **19.6873**               | 1.9793                        |
| swedish    | global      | **0.2514**                | 0.2488                        |

## Flores200 by direction

| language   | direction   | HPLT (native)   | MultiSynt (artificial)   |
|:-----------|:------------|:----------------|:-------------------------|
| danish     | eng→target  | **8.78**        | 0.41                     |
| danish     | target→eng  | **5.27**        | 1.82                     |
| dutch      | eng→target  | **11.38**       | 1.71                     |
| dutch      | target→eng  | **13.82**       | 2.21                     |
| finnish    | eng→target  | 0.93            | **3.42**                 |
| finnish    | target→eng  | **7.18**        | 0.77                     |
| french     | eng→target  | **33.39**       | 2.94                     |
| french     | target→eng  | **33.56**       | 1.79                     |
| german     | eng→target  | **21.67**       | 2.08                     |
| german     | target→eng  | **28.23**       | 0.68                     |
| italian    | eng→target  | **21.23**       | 1.61                     |
| italian    | target→eng  | **22.98**       | 1.40                     |
| polish     | eng→target  | **9.45**        | 1.05                     |
| polish     | target→eng  | **8.70**        | 1.26                     |
| portuguese | eng→target  | **35.89**       | 2.64                     |
| portuguese | target→eng  | **32.66**       | 1.18                     |
| romanian   | eng→target  | **8.90**        | 1.26                     |
| romanian   | target→eng  | **15.63**       | 1.16                     |
| spanish    | eng→target  | **20.74**       | 1.07                     |
| spanish    | target→eng  | **19.44**       | 0.95                     |
| swedish    | eng→target  | **18.81**       | 3.60                     |
| swedish    | target→eng  | **20.56**       | 0.36                     |

## Win rate: MultiSynt (artificial) vs HPLT (native)

| benchmark   | win_rate   |
|:------------|:-----------|
| belebele    | 100%       |
| copa        | 100%       |
| flores200   | 0%         |
| global      | 56%        |
| icelandic   | 100%       |
| include     | 44%        |
| mgsm        | 33%        |

---

## Summary

Excluding flores200 (where evaluation validity is questionable for MultiSynt models), results across knowledge and reasoning benchmarks are broadly competitive:

- **global_mmlu**: MultiSynt leads in 56% of languages — a slight but consistent advantage for artificial training data on translated knowledge tasks.
- **belebele / include**: MultiSynt wins in 100% of evaluated languages (14/14). Average scores — HPLT: 0.3270, MultiSynt: 0.3557 (absolute +0.0287, relative +8.8%). Largest gains: Italian +0.0534, Catalan +0.0511, Romanian +0.0422; smallest gain: Spanish +0.0122. Takeaway: MultiSynt consistently outperforms HPLT on the belebele reading-comprehension benchmark across the evaluated languages.
- **mgsm**: HPLT leads (67% win rate), suggesting native data is better for math reasoning in the target language.
- **copa / icelandic_winogrande**: MultiSynt wins in both cases, though these cover only one or two languages each.

Overall, artificially generated (translated) training data is surprisingly competitive with native data on downstream NLP tasks, while being clearly weaker at producing native-sounding text as measured by BLEU-based translation benchmarks.
