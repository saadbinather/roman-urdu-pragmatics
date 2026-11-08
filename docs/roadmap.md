# Research-engineering roadmap

## Completed

- Versioned project scaffold and configuration
- Reusable data checks, prompt construction, parsing, and evaluation
- Paired comparison logic and CI test workflow
- Draft protocol and data statement

## Next batches

1. Add a command-line inference workflow that wires the Transformers adapter to the runner and manifest writer.
2. Convert the notebook's expanded dataset generation into a reviewed data-construction module.
3. Add bootstrap confidence intervals and paired permutation tests after preregistering the estimands.
4. Add annotation agreement reports and an adjudication workflow.
5. Add model-card and dataset-card generation from run artifacts.
6. Add a clean release layout for the legacy notebook and pilot outputs, preserving provenance.

## Data expansion rule

“More data” means more documented, independently reviewed scenario families—not duplicated paraphrases or synthetic rows counted as human evidence. Synthetic augmentation may be used for stress testing, but it must remain separately labeled and excluded from confirmatory estimates.
