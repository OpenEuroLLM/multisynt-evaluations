# MultiSynt Nemotron-CC Models by Language

Models follow the naming convention `MultiSynt/nemotron-cc-{language}-{translation-model}`.

| Language   | tower9b | tower72b | opus | include | belebele | flores |
|------------|:-------:|:--------:|:----:|:-------:|:--------:|:------:|
| Basque     | ✗       | ✗        | ✓    | ✓       | ✗        | ✗      |
| Catalan    | ✗       | ✗        | ✓    | ✗       | ✗        | ✗      |
| Danish     | ✓       | ✗        | ✓    | ✗       | ✓        | ✓      |
| Dutch      | ✓       | ✗        | ✓    | ✓       | ✓        | ✓      |
| Finnish    | ✓       | ✓        | ✓    | ✓       | ✓        | ✓      |
| French     | ✓       | ✗        | ✓    | ✓       | ✓        | ✓      |
| German     | ✓       | ✓        | ✓    | ✓       | ✓        | ✓      |
| Icelandic  | ✓       | ✗        | ✓    | ✗       | ✗        | ✗      |
| Italian    | ✓       | ✓        | ✓    | ✓       | ✓        | ✓      |
| Norwegian  | ✓       | ✗        | ✗    | ✗       | ✗        | ✗      |
| Polish     | ✓       | ✗        | ✓    | ✓       | ✓        | ✓      |
| Portuguese | ✗       | ✗        | ✓    | ✓       | ✓        | ✓      |
| Romanian   | ✓       | ✗        | ✓    | ✗       | ✓        | ✓      |
| Spanish    | ✓       | ✓        | ✓    | ✓       | ✓        | ✓      |
| Swedish    | ✓       | ✓        | ✓    | ✗       | ✓        | ✓      |

## Analysis

Unlike HPLT2 monolingual models, no model has intermediate checkpoints available.

### Model coverage
- **Full coverage** (all 3 models): Finnish, German, Italian, Spanish, Swedish
- **Missing tower72b only**: Danish, Dutch, French, Icelandic, Polish, Romanian
- **Missing tower9b + tower72b**: Basque, Catalan, Portuguese
- **Missing opus only**: Norwegian
- Norwegian is the only language missing opus while having tower9b.

### Benchmark coverage
- **include**: Basque, Dutch, Finnish, French, German, Italian, Polish, Portuguese, Spanish (9/15 languages)
- **belebele**: Danish, Dutch, Finnish, French, German, Italian, Polish, Portuguese, Romanian, Spanish, Swedish (11/15 languages)
- **flores**: Danish, Dutch, Finnish, French, German, Italian, Polish, Portuguese, Romanian, Spanish, Swedish (11/15 languages)
- **No benchmark coverage**: Catalan, Icelandic, Norwegian
- **Only include (not belebele/flores)**: Basque
- **belebele and flores but not include**: Danish, Romanian, Swedish



Steps:
* evaluate multisynt models with tower72b > tower9B > opus on all languages
* evaluate hplt models on all languages
* add missing evaluation noreval etc in oellm-cli

## Generate Evaluations

### 1. Generate the evaluation list

The script [`generate_eval_list.py`](generate_eval_list.py) produces `multisynt_evals.csv`, a flat CSV with one row per `(model, task)` pair, ready to be passed to [oellm-cli](https://github.com/OpenEuroLLM/oellm-cli).

The core of the script is `LANGUAGE_TASKS`, a dictionary mapping each language to its list of individual evaluation tasks with their n-shot settings and eval suite. The tasks are chosen based on the benchmark coverage table above — for example, languages present in belebele get `belebele_{lang}_Latn`, languages in flores get the corresponding `flores200:` tasks, and so on. Languages with no benchmark coverage (Catalan, Icelandic, Norwegian) have an empty task list. For each model, the best available translation model is selected following the priority `tower72b > tower9b > opus`.

To regenerate the CSV:

```bash
uv run generate_eval_list.py
```

This writes `multisynt_evals.csv` with columns: `model_path`, `task_path`, `n_shot`, `eval_suite`.

### 2. Schedule evaluations on a cluster

Copy the CSV to the cluster (e.g. LUMI):

```bash
scp multisynt_evals.csv lumi:
```

Then on the cluster, schedule all evaluations with [oellm-cli](https://github.com/OpenEuroLLM/oellm-cli):

```bash
oellm schedule-eval --eval_csv_path multisynt_evals.csv
```