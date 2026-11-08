import pandas as pd

from roman_urdu_pragmatics.report import render_report


def test_report_contains_metrics_and_caution():
    frame = pd.DataFrame({"setting": ["with_context", "with_context"], "language": ["English", "Roman_Urdu"], "pair_id": [1, 1], "gold_intent": ["PRAISE", "PRAISE"], "predicted_intent": ["PRAISE", "CRITICISM"]})
    report = render_report(frame)
    assert "Pilot evaluation report" in report
    assert "population-level" in report
    assert "accuracy" in report
