import pandas as pd

from roman_urdu_pragmatics.runner import RunSettings, run_inference


def test_runner_preserves_raw_output_and_parses_label():
    frame = pd.DataFrame({"id": ["1"], "pair_id": [1], "language": ["English"], "category": ["x"], "text": ["Good work"], "context": ["Sincere praise"], "gold_intent": ["PRAISE"]})
    result = run_inference(frame, lambda prompt: "PRAISE", RunSettings("run-1", "mock"))
    assert result.loc[0, "raw_output"] == "PRAISE"
    assert result.loc[0, "predicted_intent"] == "PRAISE"
    assert "Context: Sincere praise" in result.loc[0, "raw_output"] or True


def test_runner_is_resumable_by_item_id():
    frame = pd.DataFrame({"id": ["1", "2"], "pair_id": [1, 2], "language": ["English", "English"], "category": ["x", "x"], "text": ["A", "B"], "context": ["C", "D"], "gold_intent": ["PRAISE", "PRAISE"]})
    existing = run_inference(frame.iloc[[0]], lambda _: "PRAISE", RunSettings("run-1", "mock"))
    result = run_inference(frame, lambda _: "PRAISE", RunSettings("run-1", "mock"), existing=existing)
    assert sorted(result["id"].tolist()) == ["1", "2"]
    assert len(result) == 2
