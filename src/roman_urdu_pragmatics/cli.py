"""Small command-line entry points for validation and reporting."""

from __future__ import annotations

import argparse

from .report import write_report
from .validate import validate_path


def main() -> None:
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command", required=True)
    validate = subparsers.add_parser("validate")
    validate.add_argument("--data", required=True)
    report = subparsers.add_parser("report")
    report.add_argument("--predictions", required=True)
    report.add_argument("--output", required=True)
    args = parser.parse_args()
    if args.command == "validate":
        findings = validate_path(args.data)
        if findings:
            for finding in findings:
                print(f"WARNING: {finding}")
        else:
            print("Dataset passed structural design checks.")
    else:
        write_report(args.predictions, args.output)
        print(f"Wrote report to {args.output}")


if __name__ == "__main__":
    main()
