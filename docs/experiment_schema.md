# Experiment record schema

Every inference run should write a machine-readable manifest alongside predictions:

```yaml
study_id: ru_pragmatics_pilot_v1
run_id: 2026-01-01T000000Z_example
model_id: Qwen/Qwen2.5-3B-Instruct
prompt_version: intent-v1
seed: 42
decoding:
  do_sample: false
  temperature: 0.0
data_commit: <git-sha>
```

Prediction rows should retain `id`, `pair_id`, `language`, `setting`, `gold_intent`, `raw_output`, `predicted_intent`, `correct`, and the manifest `run_id`. This makes later audits possible without rerunning the model.
