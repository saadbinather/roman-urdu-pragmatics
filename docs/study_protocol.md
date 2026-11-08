# Study protocol (draft)

## Objective

Estimate whether a fixed instruction-tuned language model's pragmatic-intent classification differs across matched English, Roman Urdu, and code-switched messages under controlled context conditions.

## Design

Use scenario families as the unit of matched comparison. Each family should contain semantically aligned language variants and explicit context conditions. Report item-level results, paired language contrasts, uncertainty intervals, and the number of independent scenario families.

## Primary outcome

Macro-F1 and accuracy for context-conditioned intent classification, stratified by language. The primary contrast is Roman Urdu versus English within matched scenario families.

## Safeguards against overclaiming

The pilot is researcher-authored, small, and model-specific. Results must be described as evidence about this model and this instrument. Do not describe them as evidence about speakers, communities, or language ability without a separately designed human study.

## Required next steps

1. Pre-register labels, exclusions, primary contrasts, and uncertainty estimation.
2. Obtain independent annotation from at least two annotators fluent in the relevant varieties.
3. Record agreement and adjudication before model predictions are inspected.
4. Add calibration, invalid-output handling, and repeated-seed sensitivity checks.
5. Compare multiple model families and prompt templates.
6. Release a data statement, model card, and exact environment lockfile.
