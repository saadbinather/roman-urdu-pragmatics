"""Versioned prompt construction and strict output parsing."""

from __future__ import annotations

import re

LABELS = ("PRAISE", "CRITICISM", "DISAGREEMENT", "UNCERTAINTY", "REASSURANCE", "COMMITMENT", "CONCERN")


def build_prompt(text: str, context: str | None, labels: tuple[str, ...] = LABELS) -> str:
    context_block = f"Context: {context}\n" if context else ""
    label_block = ", ".join(labels)
    return (
        "Classify the communicative intent using exactly one label. "
        f"Allowed labels: {label_block}.\n{context_block}Message: {text}\nLabel:"
    )


def parse_label(raw_output: str, labels: tuple[str, ...] = LABELS) -> str:
    """Extract one allowed label; return INVALID for unparseable output."""
    upper = raw_output.upper()
    matches = [label for label in labels if re.search(rf"\b{re.escape(label)}\b", upper)]
    return matches[0] if len(matches) == 1 else "INVALID"
