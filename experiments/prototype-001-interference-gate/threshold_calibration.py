"""Compare HIGH/LOW threshold choices for Prototype 001."""

from __future__ import annotations

import math
from pathlib import Path
from wave_compute_lab import interference_gate, print_csv, write_csv

PHASES_DEGREES = [0, 30, 60, 75, 85, 90, 95, 100, 105, 110, 120, 150, 180]
NOISE_LEVELS = [0.00, 0.05, 0.10, 0.20]
THRESHOLDS = [1.00, 1.10, 1.20, 1.25, 1.30, 1.40, 1.50]
TRIALS = 50
RESULT_PATH = Path("results/prototype-001/threshold_calibration.csv")


def expected_label(phase_degrees: int) -> str:
    """Use the clean 90/105 boundary as the target label model."""

    return "HIGH" if phase_degrees <= 90 else "LOW"


def run_threshold_calibration() -> list[dict[str, float | int]]:
    rows: list[dict[str, float | int]] = []
    total_cases = len(PHASES_DEGREES) * len(NOISE_LEVELS) * TRIALS
    for threshold in THRESHOLDS:
        correct = 0
        high_false_positive = 0
        low_false_negative = 0
        for phase_degrees in PHASES_DEGREES:
            target = expected_label(phase_degrees)
            for noise_amplitude in NOISE_LEVELS:
                for seed in range(TRIALS):
                    result = interference_gate(
                        phase_difference_radians=math.radians(phase_degrees),
                        noise_amplitude=noise_amplitude,
                        high_threshold=threshold,
                        seed=seed,
                    )
                    decision = str(result["decision"])
                    if decision == target:
                        correct += 1
                    elif decision == "HIGH" and target == "LOW":
                        high_false_positive += 1
                    elif decision == "LOW" and target == "HIGH":
                        low_false_negative += 1
        rows.append(
            {
                "threshold": threshold,
                "accuracy": round(correct / total_cases, 4),
                "high_false_positive_rate": round(high_false_positive / total_cases, 4),
                "low_false_negative_rate": round(low_false_negative / total_cases, 4),
            }
        )
    return rows


if __name__ == "__main__":
    experiment_rows = run_threshold_calibration()
    write_csv(RESULT_PATH, experiment_rows)
    print_csv(experiment_rows)
