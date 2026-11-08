"""Small command-line entry points for validation and reporting."""

from __future__ import annotations

import argparse

from .report import write_report
from .config import load_config
from .data import load_evaluation_data
from .manifest import write_manifest
from .model import TransformersPredictor
from .runner import RunSettings, run_inference, save_predictions
from .validate import validate_path


def main() -> None:
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command", required=True)
    validate = subparsers.add_parser("validate")
    validate.add_argument("--data", required=True)
    report = subparsers.add_parser("report")
    report.add_argument("--predictions", required=True)
    report.add_argument("--output", required=True)
    infer = subparsers.add_parser("infer")
    infer.add_argument("--config", required=True)
    infer.add_argument("--run-id", required=True)
    infer.add_argument("--setting", choices=["with_context", "without_context"], default="with_context")
    infer.add_argument("--resume", default=None, help="Existing predictions CSV to resume")
    args = parser.parse_args()
    if args.command == "validate":
        findings = validate_path(args.data)
        if findings:
            for finding in findings:
                print(f"WARNING: {finding}")
        else:
            print("Dataset passed structural design checks.")
    elif args.command == "report":
        write_report(args.predictions, args.output)
        print(f"Wrote report to {args.output}")
    else:
        config = load_config(args.config)
        data_path = config["data"]["evaluation"]
        frame = load_evaluation_data(data_path)
        settings = RunSettings(args.run_id, config["model"]["id"], seed=config.get("seed", 42))
        predictor = TransformersPredictor(config["model"]["id"], max_new_tokens=config["model"].get("max_new_tokens", 32), temperature=config["model"].get("temperature", 0.0))
        existing = None
        if args.resume:
            import pandas as pd
            existing = pd.read_csv(args.resume)
        predictions = run_inference(frame, predictor, settings, setting=args.setting, existing=existing)
        output_dir = config["outputs"]["directory"]
        output_path = f"{output_dir}/{args.run_id}_{args.setting}_predictions.csv"
        save_predictions(predictions, output_path)
        write_manifest(settings, f"{output_dir}/{args.run_id}_manifest.json", data_path=data_path, decoding=config["model"])
        print(f"Wrote predictions to {output_path}")


if __name__ == "__main__":
    main()
