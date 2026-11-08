"""Metric functions kept independent from model inference."""

from __future__ import annotations

import pandas as pd
from sklearn.metrics import accuracy_score, f1_score


def summarize_predictions(frame: pd.DataFrame, *, gold: str = "gold_intent", predicted: str = "predicted_intent", group_columns: tuple[str, ...] = ("setting", "language")) -> pd.DataFrame:
    """Return accuracy, macro-F1, and sample size for each analysis stratum."""
    required = {*group_columns, gold, predicted}
    missing = required.difference(frame.columns)
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")
    rows = []
    for keys, group in frame.groupby(list(group_columns), dropna=False):
        if not isinstance(keys, tuple):
            keys = (keys,)
        row = dict(zip(group_columns, keys))
        row.update(accuracy=accuracy_score(group[gold], group[predicted]), macro_f1=f1_score(group[gold], group[predicted], average="macro", zero_division=0), n=len(group))
        rows.append(row)
    return pd.DataFrame(rows)
