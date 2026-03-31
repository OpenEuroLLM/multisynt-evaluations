#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = ["pandas", "tabulate"]
# ///

from pathlib import Path

import pandas as pd
import re

HPLT_LANG_CODE_MAP = {
    "cat": "catalan",
    "dan": "danish",
    "deu": "german",
    "eus": "basque",
    "fin": "finnish",
    "fra": "french",
    "isl": "icelandic",
    "ita": "italian",
    "nld": "dutch",
    "nob": "norwegian",
    "pol": "polish",
    "por": "portuguese",
    "ron": "romanian",
    "spa": "spanish",
    "swe": "swedish",
}


def extract_language(model_name: str) -> str:
    # MultiSynt/nemotron-cc-{language}-tower... or nemotron-cc-{language}-opus
    m = re.search(r"nemotron-cc-([a-z]+)-", model_name)
    if m:
        return m.group(1)

    # HPLT/hplt2c_{lang_code}_checkpoints
    m = re.search(r"hplt2c_([a-z]+)_", model_name)
    if m:
        code = m.group(1)
        return HPLT_LANG_CODE_MAP.get(code, code)

    return "unknown"


df = pd.read_csv(Path(__file__).parent / "results.csv")

def abbreviate_benchmark(task: str) -> str:
    return task.split("_")[0].split(":")[0]


df["language"] = df["model_name"].apply(extract_language)
df["artificial"] = df["model_name"].str.contains("MultiSynt", case=False)
df["benchmark"] = df["task"].apply(abbreviate_benchmark)

table = df.pivot_table(
    index=["language", "benchmark"],
    columns="artificial",
    values="performance",
    aggfunc="mean",
)
table.columns = ["HPLT (artificial=False)", "MultiSynt (artificial=True)"]
table = table.reset_index()

perf_cols = ["HPLT (artificial=False)", "MultiSynt (artificial=True)"]


def bold_max(row):
    best = row[perf_cols].max()
    return [
        f"**{v:.4f}**" if (col in perf_cols and v == best) else (f"{v:.4f}" if col in perf_cols else v)
        for col, v in zip(row.index, row)
    ]


str_table = table.apply(bold_max, axis=1, result_type="expand")
str_table.columns = table.columns

pd.set_option("display.max_rows", None)
print(str_table.to_markdown(index=False))

# Flores200 by direction
print("\n## Flores200 by direction\n")
flores = df[df["benchmark"] == "flores200"].copy()
flores["direction"] = flores["task"].apply(
    lambda t: "eng→target" if t.startswith("flores200:eng") else "target→eng"
)
flores_table = flores.pivot_table(
    index=["language", "direction"],
    columns="artificial",
    values="performance",
    aggfunc="mean",
).reset_index()
flores_table.columns = ["language", "direction", "HPLT (native)", "MultiSynt (artificial)"]

def bold_max_flores(row):
    perf = ["HPLT (native)", "MultiSynt (artificial)"]
    best = row[perf].max()
    return [
        f"**{v:.2f}**" if (col in perf and v == best) else (f"{v:.2f}" if col in perf else v)
        for col, v in zip(row.index, row)
    ]

flores_str = flores_table.apply(bold_max_flores, axis=1, result_type="expand")
flores_str.columns = flores_table.columns
print(flores_str.to_markdown(index=False))

# Win rate: artificial beats native, per benchmark
print("\n## Win rate: MultiSynt (artificial) vs HPLT (native)\n")
hplt_col, ms_col = "HPLT (artificial=False)", "MultiSynt (artificial=True)"
wins = table.dropna(subset=[hplt_col, ms_col])
winrate = (
    wins.groupby("benchmark")
    .apply(lambda g: (g[ms_col] > g[hplt_col]).mean(), include_groups=False)
    .rename("win_rate")
    .reset_index()
)
winrate["win_rate"] = winrate["win_rate"].map("{:.0%}".format)
print(winrate.to_markdown(index=False))
