import pandas as pd
from roman_urdu_pragmatics.metrics import summarize_predictions


def test_summary_has_expected_accuracy_and_count():
    frame = pd.DataFrame({"setting": ["with_context", "with_context"], "language": ["English", "English"], "gold_intent": ["PRAISE", "CRITICISM"], "predicted_intent": ["PRAISE", "PRAISE"]})
    result = summarize_predictions(frame)
    assert result.loc[0, "accuracy"] == 0.5
    assert result.loc[0, "n"] == 2
