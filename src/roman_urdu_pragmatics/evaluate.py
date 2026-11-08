"""Evaluation and paired language comparisons."""

from __future__ import annotations

import pandas as pd

from .metrics import summarize_predictions


def add_correctness(frame: pd.DataFrame) -> pd.DataFrame:
    result = frame.copy()
    result["correct"] = result["gold_intent"].eq(result["predicted_intent"])
    return result


def language_gap(frame: pd.DataFrame, reference: str = "English", comparison: str = "Roman_Urdu") -> pd.DataFrame:
    """Compute descriptive paired gaps; inferential statistics belong in preregistered analysis."""
    scored = add_correctness(frame)
    rows = []
    for setting, group in scored.groupby("setting"):
        paired = group.pivot_table(index="pair_id", columns="language", values="correct", aggfunc="mean")
        if reference not in paired or comparison not in paired:
            continue
        paired = paired[[reference, comparison]].dropna()
        rows.append({"setting": setting, "reference": reference, "comparison": comparison, "n_pairs": len(paired), "reference_accuracy": paired[reference].mean(), "comparison_accuracy": paired[comparison].mean(), "gap_pp": 100 * (paired[reference].mean() - paired[comparison].mean())})
    return pd.DataFrame(rows)


__all__ = ["add_correctness", "language_gap", "summarize_predictions"]
