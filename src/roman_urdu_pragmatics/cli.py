"""Small command-line entry points for validation and reporting."""

from __future__ import annotations

import argparse

from .validate import validate_path


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", required=True)
    args = parser.parse_args()
    findings = validate_path(args.data)
    if findings:
        for finding in findings:
            print(f"WARNING: {finding}")
    else:
        print("Dataset passed structural design checks.")


if __name__ == "__main__":
    main()
