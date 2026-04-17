import csv

MULTISYNT_MODELS = [
    "MultiSynt/nemotron-cc-basque-opus",
    "MultiSynt/nemotron-cc-catalan-opus",
    "MultiSynt/nemotron-cc-danish-tower9b",
    "MultiSynt/nemotron-cc-dutch-tower9b",
    "MultiSynt/nemotron-cc-finnish-tower72b",
    "MultiSynt/nemotron-cc-french-tower9b",
    "MultiSynt/nemotron-cc-german-tower72b",
    "MultiSynt/nemotron-cc-icelandic-tower9b",
    "MultiSynt/nemotron-cc-italian-tower72b",
    "MultiSynt/nemotron-cc-norwegian-tower9b",
    "MultiSynt/nemotron-cc-polish-tower9b",
    "MultiSynt/nemotron-cc-portuguese-opus",
    "MultiSynt/nemotron-cc-romanian-tower9b",
    "MultiSynt/nemotron-cc-spanish-tower72b",
    "MultiSynt/nemotron-cc-swedish-tower72b",
]

HPLT_MODELS = [
    "HPLT/hplt2c_eus_checkpoints",
    "HPLT/hplt2c_cat_checkpoints",
    "HPLT/hplt2c_dan_checkpoints",
    "HPLT/hplt2c_nld_checkpoints",
    "HPLT/hplt2c_fin_checkpoints",
    "HPLT/hplt2c_fra_checkpoints",
    "HPLT/hplt2c_deu_checkpoints",
    "HPLT/hplt2c_isl_checkpoints",
    "HPLT/hplt2c_ita_checkpoints",
    "HPLT/hplt2c_nob_checkpoints",
    "HPLT/hplt2c_pol_checkpoints",
    "HPLT/hplt2c_por_checkpoints",
    "HPLT/hplt2c_ron_checkpoints",
    "HPLT/hplt2c_spa_checkpoints",
    "HPLT/hplt2c_swe_checkpoints",
]

# ISO 639-3 code → language name (for HPLT models)
HPLT_LANG_CODE_MAP = {
    "eus": "basque",
    "cat": "catalan",
    "dan": "danish",
    "nld": "dutch",
    "fin": "finnish",
    "fra": "french",
    "deu": "german",
    "isl": "icelandic",
    "ita": "italian",
    "nob": "norwegian",
    "pol": "polish",
    "por": "portuguese",
    "ron": "romanian",
    "spa": "spanish",
    "swe": "swedish",
}

# Language-specific tasks as individual (task_path, n_shot, eval_suite) tuples.
# Edit this dict to add/remove tasks per language.
LANGUAGE_TASKS: dict[str, list[tuple[str, int, str]]] = {
    "basque": [
        ("include_base_44_basque", 0, "lm-eval-harness"),
        ("belebele_eus_Latn", 5, "lm-eval-harness"),
        ("belebele_eus_Latn_cf", 5, "lighteval"),
    ],
    "catalan": [
        ("belebele_cat_Latn", 5, "lm-eval-harness"),
        ("copa_ca", 0, "lm-eval-harness"),
        ("belebele_cat_Latn_cf", 5, "lighteval"),
    ],
    "danish": [
        ("belebele_dan_Latn", 5, "lm-eval-harness"),
        ("flores200:dan_Latn-eng_Latn", 0, "lighteval"),
        ("flores200:eng_Latn-dan_Latn", 0, "lighteval"),
        ("belebele_dan_Latn_cf", 5, "lighteval"),
    ],
    "dutch": [
        ("belebele_nld_Latn", 5, "lm-eval-harness"),
        ("flores200:nld_Latn-eng_Latn", 0, "lighteval"),
        ("flores200:eng_Latn-nld_Latn", 0, "lighteval"),
        ("global_mmlu_full_nl", 5, "lm-eval-harness"),
        ("include_base_44_dutch", 0, "lm-eval-harness"),
        ("belebele_nld_Latn_cf", 5, "lighteval"),
    ],
    "finnish": [
        ("belebele_fin_Latn", 5, "lm-eval-harness"),
        ("flores200:fin_Latn-eng_Latn", 0, "lighteval"),
        ("flores200:eng_Latn-fin_Latn", 0, "lighteval"),
        ("include_base_44_finnish", 0, "lm-eval-harness"),
        ("belebele_fin_Latn_cf", 5, "lighteval"),
    ],
    "french": [
        ("belebele_fra_Latn", 5, "lm-eval-harness"),
        ("flores200:fra_Latn-eng_Latn", 0, "lighteval"),
        ("flores200:eng_Latn-fra_Latn", 0, "lighteval"),
        ("global_mmlu_full_fr", 5, "lm-eval-harness"),
        ("mgsm_native_cot_fr", 5, "lm-eval-harness"),
        ("include_base_44_french", 0, "lm-eval-harness"),
        ("belebele_fra_Latn_cf", 5, "lighteval"),
    ],
    "german": [
        ("belebele_deu_Latn", 5, "lm-eval-harness"),
        ("flores200:deu_Latn-eng_Latn", 0, "lighteval"),
        ("flores200:eng_Latn-deu_Latn", 0, "lighteval"),
        ("global_mmlu_full_de", 5, "lm-eval-harness"),
        ("mgsm_native_cot_de", 5, "lm-eval-harness"),
        ("include_base_44_german", 0, "lm-eval-harness"),
        ("belebele_deu_Latn_cf", 5, "lighteval"),
    ],
    "icelandic": [
        ("icelandic_winogrande", 0, "lm-eval-harness"),
    ],
    "italian": [
        ("belebele_ita_Latn", 5, "lm-eval-harness"),
        ("flores200:ita_Latn-eng_Latn", 0, "lighteval"),
        ("flores200:eng_Latn-ita_Latn", 0, "lighteval"),
        ("global_mmlu_full_it", 5, "lm-eval-harness"),
        ("include_base_44_italian", 0, "lm-eval-harness"),
        ("belebele_ita_Latn_cf", 5, "lighteval"),
    ],
    "norwegian": [
        ("belebele_nob_Latn", 5, "lm-eval-harness"),
        ("belebele_nob_Latn_cf", 5, "lighteval"),
    ],
    "polish": [
        ("belebele_pol_Latn", 5, "lm-eval-harness"),
        ("flores200:pol_Latn-eng_Latn", 0, "lighteval"),
        ("flores200:eng_Latn-pol_Latn", 0, "lighteval"),
        ("global_mmlu_full_pl", 5, "lm-eval-harness"),
        ("include_base_44_polish", 0, "lm-eval-harness"),
        ("belebele_pol_Latn_cf", 5, "lighteval"),
    ],
    "portuguese": [
        ("belebele_por_Latn", 5, "lm-eval-harness"),
        ("flores200:por_Latn-eng_Latn", 0, "lighteval"),
        ("flores200:eng_Latn-por_Latn", 0, "lighteval"),
        ("global_mmlu_full_pt", 5, "lm-eval-harness"),
        ("include_base_44_portuguese", 0, "lm-eval-harness"),
        ("belebele_por_Latn_cf", 5, "lighteval"),
    ],
    "romanian": [
        ("belebele_ron_Latn", 5, "lm-eval-harness"),
        ("flores200:ron_Latn-eng_Latn", 0, "lighteval"),
        ("flores200:eng_Latn-ron_Latn", 0, "lighteval"),
        ("global_mmlu_full_ro", 5, "lm-eval-harness"),
        ("belebele_ron_Latn_cf", 5, "lighteval"),
    ],
    "spanish": [
        ("belebele_spa_Latn", 5, "lm-eval-harness"),
        ("flores200:spa_Latn-eng_Latn", 0, "lighteval"),
        ("flores200:eng_Latn-spa_Latn", 0, "lighteval"),
        ("global_mmlu_full_es", 5, "lm-eval-harness"),
        ("mgsm_native_cot_es", 5, "lm-eval-harness"),
        ("include_base_44_spanish", 0, "lm-eval-harness"),
        ("belebele_spa_Latn_cf", 5, "lighteval"),
    ],
    "swedish": [
        ("belebele_swe_Latn", 5, "lm-eval-harness"),
        ("flores200:swe_Latn-eng_Latn", 0, "lighteval"),
        ("flores200:eng_Latn-swe_Latn", 0, "lighteval"),
        ("global_mmlu_full_sv", 5, "lm-eval-harness"),
        ("belebele_swe_Latn_cf", 5, "lighteval"),
    ],
}

# Tasks run for every model regardless of language
COMMON_TASKS: list[tuple[str, int, str]] = []


def get_language_multisynt(model: str) -> str:
    # e.g. MultiSynt/nemotron-cc-danish-tower9b → danish
    name = model.split("/")[1]  # nemotron-cc-danish-tower9b
    parts = name.split("-")     # ['nemotron', 'cc', 'danish', 'tower9b']
    return parts[2]


def get_language_hplt(model: str) -> str:
    # e.g. HPLT/hplt2c_dan_checkpoints → danish
    name = model.split("/")[1]          # hplt2c_dan_checkpoints
    code = name.split("_")[1]           # dan
    return HPLT_LANG_CODE_MAP[code]


def generate_rows(models: list[str], get_language) -> list[dict]:
    rows = []
    for model in models:
        language = get_language(model)
        tasks = COMMON_TASKS + LANGUAGE_TASKS.get(language, [])
        for task_path, n_shot, eval_suite in tasks:
            rows.append({
                "model_path": model,
                "task_path": task_path,
                "n_shot": n_shot,
                "eval_suite": eval_suite,
            })
    return rows


def main():
    rows = (
        generate_rows(MULTISYNT_MODELS, get_language_multisynt)
        + generate_rows(HPLT_MODELS, get_language_hplt)
    )

    output_path = "multisynt_evals.csv"
    with open(output_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["model_path", "task_path", "n_shot", "eval_suite"])
        writer.writeheader()
        writer.writerows(rows)

    print(f"Wrote {len(rows)} rows to {output_path}")


if __name__ == "__main__":
    main()
