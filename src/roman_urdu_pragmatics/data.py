"""Dataset validation for the controlled pilot corpus."""

from pathlib import Path
import pandas as pd

REQUIRED_COLUMNS = {"id", "pair_id", "language", "category", "text", "context", "gold_intent"}


def load_evaluation_data(path: str | Path) -> pd.DataFrame:
    """Load and validate the pilot evaluation table without changing its labels."""
    frame = pd.read_csv(path)
    missing = REQUIRED_COLUMNS.difference(frame.columns)
    if missing:
        raise ValueError(f"Dataset is missing columns: {sorted(missing)}")
    if frame["id"].duplicated().any():
        raise ValueError("Dataset contains duplicate item IDs")
    if frame["text"].isna().any() or frame["gold_intent"].isna().any():
        raise ValueError("Text and gold_intent must not contain missing values")
    return frame
