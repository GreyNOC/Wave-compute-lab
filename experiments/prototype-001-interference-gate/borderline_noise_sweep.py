"""Measure Prototype 001 near the phase decision boundary under noise."""

from __future__ import annotations

import math
from pathlib import Path
from wave_compute_lab import interference_gate, print_csv, write_csv

PHASES_DEGREES = [75, 85, 90, 95, 100, 105, 110, 115, 120]
NOISE_LEVELS = [0.00, 0.02, 0.05, 0.10, 0.20, 0.40]
TRIALS = 100
RESULT_PATH = Path("results/prototype-001/borderline_noise_sweep.csv")


def run_borderline_noise_sweep() -> list[dict[str, float | int]]:
    rows: list[dict[str, float | int]] = []
    for phase_degrees in PHASES_DEGREES:
        phase_radians = math.radians(phase_degrees)
        for noise_amplitude in NOISE_LEVELS:
            high_count = 0
            strengths: list[float] = []
            correlations: list[float] = []
            for seed in range(TRIALS):
                result = interference_gate(
                    phase_difference_radians=phase_radians,
                    noise_amplitude=noise_amplitude,
                    seed=seed,
                )
                high_count += int(result["decision"] == "HIGH")
                strengths.append(float(result["strength"]))
                correlations.append(float(result["correlation"]))
            high_rate = high_count / TRIALS
            rows.append(
                {
                    "phase_degrees": phase_degrees,
                    "noise_amplitude": noise_amplitude,
                    "high_rate": round(high_rate, 4),
                    "low_rate": round(1.0 - high_rate, 4),
                    "average_strength": round(sum(strengths) / TRIALS, 6),
                    "average_correlation": round(sum(correlations) / TRIALS, 6),
                }
            )
    return rows


if __name__ == "__main__":
    experiment_rows = run_borderline_noise_sweep()
    write_csv(RESULT_PATH, experiment_rows)
    print_csv(experiment_rows)
