from pathlib import Path

import pytest

from roman_urdu_pragmatics.config import load_config


def test_project_config_loads():
    config = load_config(Path(__file__).parents[1] / "configs" / "pilot.yaml")
    assert config["model"]["id"] == "Qwen/Qwen2.5-3B-Instruct"


def test_invalid_config_is_rejected(tmp_path):
    path = tmp_path / "bad.yaml"
    path.write_text("model: {}\n", encoding="utf-8")
    with pytest.raises(ValueError, match="missing section"):
        load_config(path)
