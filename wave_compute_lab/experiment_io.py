"""Small CSV helpers for repeatable Wave Compute Lab experiments."""

from __future__ import annotations

import csv
from pathlib import Path
from typing import Any, Iterable


def write_csv(path: str | Path, rows: Iterable[dict[str, Any]]) -> Path:
    """Write a sequence of dictionaries to CSV and return the output path.

    The field order is taken from the first row.  Parent directories are created
    automatically so experiment scripts can write into results/prototype-001.
    """

    output_path = Path(path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    row_list = list(rows)
    if not row_list:
        raise ValueError("rows must contain at least one row")

    with output_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(row_list[0].keys()))
        writer.writeheader()
        writer.writerows(row_list)
    return output_path


def print_csv(rows: Iterable[dict[str, Any]]) -> None:
    """Print dictionaries as CSV to stdout."""

    row_list = list(rows)
    if not row_list:
        return
    writer = csv.DictWriter(__import__("sys").stdout, fieldnames=list(row_list[0].keys()))
    writer.writeheader()
    writer.writerows(row_list)
