"""Small, inspectable report generator for prediction CSVs."""

from __future__ import annotations

from pathlib import Path

import pandas as pd

from .evaluate import add_correctness, language_gap
from .metrics import summarize_predictions


def _markdown_table(frame: pd.DataFrame) -> str:
    """Render a compact Markdown table without requiring the tabulate package."""
    if frame.empty:
        return ""
    columns = [str(column) for column in frame.columns]
    lines = ["| " + " | ".join(columns) + " |", "| " + " | ".join("---" for _ in columns) + " |"]
    for values in frame.itertuples(index=False, name=None):
        lines.append("| " + " | ".join(str(value) for value in values) + " |")
    return "\n".join(lines)


def render_report(predictions: pd.DataFrame) -> str:
    scored = add_correctness(predictions)
    metrics = summarize_predictions(scored)
    gaps = language_gap(scored)
    lines = ["# Pilot evaluation report", "", "This report describes model-level performance on the supplied evaluation items.", ""]
    lines.append("## Stratified metrics\n")
    lines.append(_markdown_table(metrics) if not metrics.empty else "No stratified metrics available.")
    lines.append("\n## Matched language gaps\n")
    lines.append(_markdown_table(gaps) if not gaps.empty else "No matched language comparison available.")
    lines.append("\n## Interpretation\n")
    lines.append("These descriptive estimates are specific to this model, prompt, dataset, and run. They do not establish population-level differences between languages or speakers.")
    return "\n".join(lines) + "\n"


def write_report(predictions_path: str | Path, output_path: str | Path) -> None:
    predictions = pd.read_csv(predictions_path)
    destination = Path(output_path)
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(render_report(predictions), encoding="utf-8")
