"""Load and validate YAML experiment configuration."""

from __future__ import annotations

from pathlib import Path
import yaml


def load_config(path: str | Path) -> dict:
    with Path(path).open(encoding="utf-8") as handle:
        config = yaml.safe_load(handle)
    if not isinstance(config, dict):
        raise ValueError("Experiment config must contain a YAML mapping")
    for section in ("data", "model", "task", "outputs"):
        if section not in config:
            raise ValueError(f"Experiment config is missing section: {section}")
    return config
