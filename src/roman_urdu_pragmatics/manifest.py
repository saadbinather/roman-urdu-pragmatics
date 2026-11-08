"""Run manifest creation for provenance and auditability."""

from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
import json

from .runner import RunSettings


def write_manifest(settings: RunSettings, path: str | Path, *, data_path: str, decoding: dict) -> None:
    payload = {
        "run_id": settings.run_id,
        "created_at": datetime.now(timezone.utc).isoformat(),
        "model_id": settings.model_id,
        "prompt_version": settings.prompt_version,
        "seed": settings.seed,
        "data_path": data_path,
        "decoding": decoding,
    }
    destination = Path(path)
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
