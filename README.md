# Roman Urdu Pragmatics Pilot

Research-engineering repository for a controlled pilot study of pragmatic intent classification in English, Roman Urdu, and code-switched text.

## Research question

Do instruction-tuned language models interpret context-dependent pragmatic intent differently across English, Roman Urdu, and code-switched messages?

This repository is an **analysis scaffold**, not a claim of population-level language disparity. The current dataset is researcher-authored and requires human validation before publication.

## Current pilot

- Model: Qwen2.5-3B-Instruct
- Task: context-conditioned intent classification
- Languages: English, Roman Urdu, code-switching
- Intents: praise, criticism, disagreement, uncertainty, reassurance, commitment, concern
- Existing pilot artifacts: 12 scenario families and 72 context-conditioned items

The original notebook and exported results are retained in the existing `roman_urdu_research_final (1)/` export. They are useful provenance, but the canonical implementation will live under `src/`.

## Repository layout

```text
configs/       Versioned experiment configuration
data/          Dataset documentation and local data drop-in point
docs/          Study protocol, annotation plan, and analysis notes
legacy/        Original notebook and exported pilot artifacts
src/           Reusable package code
tests/         Small deterministic tests for data and metrics
```

## Suggested project name

Use **`roman-urdu-pragmatics-pilot`** for the GitHub repository. It is specific enough for discovery, broad enough to support later model comparisons, and accurately signals that this is a pilot rather than a definitive benchmark.

## Planned commands

```bash
python -m pip install -e '.[dev]'
validate-ru-pragmatics validate --data 'roman_urdu_research_final (1)/data/evaluation_dataset.csv'
validate-ru-pragmatics report --predictions results/generated/predictions.csv --output results/generated/report.md
validate-ru-pragmatics infer --config configs/pilot.yaml --run-id pilot-001
```

No inference is run by the repository bootstrap step.

The Transformers adapter is opt-in and requires the `inference` extra. The `infer` command downloads/loads model weights only when explicitly invoked. Report generation works from saved prediction CSVs and does not load model weights.

## Engineering principles

- Every prediction must retain the raw model output, parsed label, prompt version, model identifier, and run seed.
- Paired scenario families are the comparison unit; item counts alone are not evidence of independent replication.
- Invalid or ambiguous model outputs are retained and reported, never silently coerced.
- New examples must carry provenance and annotation status (`draft`, `reviewed`, or `adjudicated`).
- Inference is resumable by stable item ID and preserves raw model output for audit.
