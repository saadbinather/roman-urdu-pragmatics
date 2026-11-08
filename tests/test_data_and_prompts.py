import pandas as pd

from roman_urdu_pragmatics.prompts import build_prompt, parse_label
from roman_urdu_pragmatics.validate import validate_design


def test_prompt_parser_rejects_ambiguous_output():
    assert parse_label("PRAISE") == "PRAISE"
    assert parse_label("PRAISE or CRITICISM") == "INVALID"
    assert parse_label("not a label") == "INVALID"


def test_design_check_detects_inconsistent_matched_labels():
    frame = pd.DataFrame({"pair_id": [1, 1], "language": ["English", "Roman_Urdu"], "gold_intent": ["PRAISE", "CRITICISM"]})
    assert "gold intent differs within a matched scenario family" in validate_design(frame)


def test_prompt_includes_context():
    assert "Context: A friend responds" in build_prompt("Tum bohat achay ho", "A friend responds")
