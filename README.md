# Roman Urdu Pragmatics Pilot

This repository contains a small research-engineering pilot on pragmatic intent classification across English, Roman Urdu, and code-switched messages.

The work was completed for the **Fatima Institute Fellowship Task** as an initial study design and reproducibility exercise. It shows how a research question can be translated into a documented, testable computational workflow.

## Overview

The pilot asks whether an instruction-tuned language model interprets context-dependent communicative intent differently across matched language variants.

The current evaluation uses researcher-authored examples with contextual conditions and the following intent labels:

`PRAISE`, `CRITICISM`, `DISAGREEMENT`, `UNCERTAINTY`, `REASSURANCE`, `COMMITMENT`, and `CONCERN`.

The initial model configuration uses Qwen2.5-3B-Instruct. Existing pilot artifacts include 12 scenario families and 72 context-conditioned items.

## Scope and status

This is a pilot instrument, not a population-representative benchmark. The current labels require independent human review, and the existing results should be interpreted as model- and dataset-specific observations. They should not be read as evidence about the ability of Roman Urdu speakers or about language communities generally.

The repository is structured so that annotation, model comparison, preregistration, and larger-scale evaluation can be added without rewriting the core workflow.

## Repository structure

```text
configs/       Versioned experiment configuration
data/          Data documentation and annotation template
docs/          Study protocol, data statement, and research roadmap
src/           Reusable validation, inference, evaluation, and reporting code
tests/         Deterministic unit tests and mock-model tests
roman_urdu_research_final (1)/
               Original notebook export and pilot artifacts
```

## Reproducible workflow

Install the analysis and development dependencies:

```bash
python -m pip install -e '.[dev]'
```

Validate the evaluation data:

```bash
validate-ru-pragmatics validate --data 'roman_urdu_research_final (1)/data/evaluation_dataset.csv'
```

Generate a report from saved predictions:

```bash
validate-ru-pragmatics report --predictions results/generated/predictions.csv --output results/generated/report.md
```

Inference is opt-in. To load the configured model, install the inference dependencies and provide an explicit run ID:

```bash
python -m pip install -e '.[inference]'
validate-ru-pragmatics infer --config configs/pilot.yaml --run-id pilot-001
```

Every run is designed to retain its raw model outputs, parsed labels, model identifier, prompt version, seed, and run manifest. Inference can resume from an existing prediction file by item ID.

## Research safeguards

- Matched scenario families are treated as the comparison unit.
- Invalid or ambiguous model outputs are retained rather than silently coerced.
- New examples require provenance and an annotation status.
- Synthetic augmentation, if added, will remain separate from confirmatory estimates.
- Future publication should include independent annotation, agreement statistics, a preregistered analysis, and comparisons across multiple models and prompts.

## Development status

The project is an active pilot scaffold. The original notebook and exported results are retained for provenance; the modular implementation under `src/` is the basis for future runs.
