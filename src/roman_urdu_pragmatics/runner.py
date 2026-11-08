"""Resumable inference orchestration.

The runner depends on a small predictor interface, so model loading stays separate
from experiment bookkeeping and can be replaced by a mock in tests.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Protocol

import pandas as pd

from .prompts import LABELS, build_prompt, parse_label


class Predictor(Protocol):
    def __call__(self, prompt: str) -> str: ...


@dataclass(frozen=True)
class RunSettings:
    run_id: str
    model_id: str
    prompt_version: str = "intent-v1"
    seed: int = 42


def _input_for_row(row: pd.Series, setting: str) -> str:
    context = row["context"] if setting == "with_context" else None
    return build_prompt(str(row["text"]), context, LABELS)


def run_inference(
    frame: pd.DataFrame,
    predictor: Predictor,
    settings: RunSettings,
    *,
    setting: str = "with_context",
    existing: pd.DataFrame | None = None,
) -> pd.DataFrame:
    """Generate predictions, skipping IDs already present in an existing run."""
    if setting not in {"with_context", "without_context"}:
        raise ValueError("setting must be with_context or without_context")
    completed = set() if existing is None else set(existing["id"].astype(str))
    rows = [] if existing is None else existing.to_dict("records")
    for _, row in frame.iterrows():
        item_id = str(row["id"])
        if item_id in completed:
            continue
        prompt = _input_for_row(row, setting)
        raw_output = predictor(prompt)
        predicted = parse_label(raw_output, LABELS)
        rows.append(
            {
                "id": item_id,
                "pair_id": row["pair_id"],
                "language": row["language"],
                "category": row["category"],
                "setting": setting,
                "gold_intent": row["gold_intent"],
                "raw_output": raw_output,
                "predicted_intent": predicted,
                "run_id": settings.run_id,
                "model_id": settings.model_id,
                "prompt_version": settings.prompt_version,
                "seed": settings.seed,
            }
        )
    return pd.DataFrame(rows)


def save_predictions(predictions: pd.DataFrame, path: str | Path) -> None:
    """Write predictions atomically enough for ordinary interrupted local runs."""
    destination = Path(path)
    destination.parent.mkdir(parents=True, exist_ok=True)
    temporary = destination.with_suffix(destination.suffix + ".tmp")
    predictions.to_csv(temporary, index=False)
    temporary.replace(destination)
