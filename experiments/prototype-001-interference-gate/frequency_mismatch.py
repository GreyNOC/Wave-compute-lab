"""Measure interference behavior when the two wave sources drift in frequency."""

from __future__ import annotations

import math
from pathlib import Path
from wave_compute_lab import interference_gate_custom, print_csv, write_csv

FREQUENCY_B_VALUES = [10.00, 10.05, 10.10, 10.25, 10.50, 11.00, 12.00]
PHASES = {"in_phase": 0.0, "opposite_phase": math.pi}
TRIALS = 50
RESULT_PATH = Path("results/prototype-001/frequency_mismatch.csv")


def run_frequency_mismatch() -> list[dict[str, float | str]]:
    rows: list[dict[str, float | str]] = []
    for phase_label, phase_radians in PHASES.items():
        expected = "HIGH" if phase_label == "in_phase" else "LOW"
        for frequency_b in FREQUENCY_B_VALUES:
            correct = 0
            strengths: list[float] = []
            correlations: list[float] = []
            for _ in range(TRIALS):
                result = interference_gate_custom(
                    phase_difference_radians=phase_radians,
                    frequency_a_hz=10.0,
                    frequency_b_hz=frequency_b,
                )
                correct += int(result["decision"] == expected)
                strengths.append(float(result["strength"]))
                correlations.append(float(result["correlation"]))
            rows.append(
                {
                    "phase_case": phase_label,
                    "frequency_a_hz": 10.0,
                    "frequency_b_hz": frequency_b,
                    "frequency_delta_hz": round(frequency_b - 10.0, 4),
                    "expected": expected,
                    "accuracy": round(correct / TRIALS, 4),
                    "average_strength": round(sum(strengths) / TRIALS, 6),
                    "average_correlation": round(sum(correlations) / TRIALS, 6),
                }
            )
    return rows


if __name__ == "__main__":
    experiment_rows = run_frequency_mismatch()
    write_csv(RESULT_PATH, experiment_rows)
    print_csv(experiment_rows)
