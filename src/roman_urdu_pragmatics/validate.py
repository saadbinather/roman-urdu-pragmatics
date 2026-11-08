"""Structural and design checks for evaluation datasets."""

from __future__ import annotations

import pandas as pd

from .data import load_evaluation_data


def validate_design(frame: pd.DataFrame) -> list[str]:
    """Return human-readable warnings/errors without silently repairing data."""
    findings: list[str] = []
    if frame["pair_id"].nunique() < 2:
        findings.append("fewer than two scenario families")
    if frame.groupby("pair_id")["language"].nunique().min() < 2:
        findings.append("at least one pair has fewer than two language variants")
    if frame.groupby("pair_id")["gold_intent"].nunique().gt(1).any():
        findings.append("gold intent differs within a matched scenario family")
    if frame["language"].value_counts().min() < 2:
        findings.append("at least one language has fewer than two items")
    return findings


def validate_path(path: str) -> list[str]:
    frame = load_evaluation_data(path)
    return validate_design(frame)
