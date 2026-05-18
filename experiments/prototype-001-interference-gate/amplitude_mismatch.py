"""Measure destructive-interference behavior when source amplitudes do not match."""

from __future__ import annotations

import math
from pathlib import Path
from wave_compute_lab import interference_gate_custom, print_csv, write_csv

AMPLITUDE_B_VALUES = [1.00, 0.90, 0.75, 0.50, 0.25]
NOISE_LEVELS = [0.00, 0.05, 0.10, 0.20]
TRIALS = 100
RESULT_PATH = Path("results/prototype-001/amplitude_mismatch.csv")


def run_amplitude_mismatch() -> list[dict[str, float]]:
    rows: list[dict[str, float]] = []
    for amplitude_b in AMPLITUDE_B_VALUES:
        for noise_amplitude in NOISE_LEVELS:
            low_count = 0
            strengths: list[float] = []
            for seed in range(TRIALS):
                result = interference_gate_custom(
                    phase_difference_radians=math.pi,
                    amplitude_a=1.0,
                    amplitude_b=amplitude_b,
                    noise_amplitude=noise_amplitude,
                    seed=seed,
                )
                low_count += int(result["decision"] == "LOW")
                strengths.append(float(result["strength"]))
            rows.append(
                {
                    "amplitude_a": 1.0,
                    "amplitude_b": amplitude_b,
                    "noise_amplitude": noise_amplitude,
                    "low_rate": round(low_count / TRIALS, 4),
                    "average_strength": round(sum(strengths) / TRIALS, 6),
                }
            )
    return rows


if __name__ == "__main__":
    experiment_rows = run_amplitude_mismatch()
    write_csv(RESULT_PATH, experiment_rows)
    print_csv(experiment_rows)
