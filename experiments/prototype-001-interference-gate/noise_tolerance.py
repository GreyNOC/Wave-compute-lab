"""Run deterministic noise tolerance checks for Prototype 001."""

from __future__ import annotations

import math
from wave_compute_lab import interference_gate


def classify_trials(*, phase_radians: float, expected: str, noise_amplitude: float, trials: int = 100) -> float:
    correct = 0
    for seed in range(trials):
        result = interference_gate(
            phase_difference_radians=phase_radians,
            noise_amplitude=noise_amplitude,
            seed=seed,
        )
        if result["decision"] == expected:
            correct += 1
    return correct / trials


def run_noise_tolerance() -> list[dict[str, float | str]]:
    rows: list[dict[str, float | str]] = []
    for noise in [0.0, 0.02, 0.05, 0.10, 0.20, 0.40]:
        high_accuracy = classify_trials(phase_radians=0.0, expected="HIGH", noise_amplitude=noise)
        low_accuracy = classify_trials(phase_radians=math.pi, expected="LOW", noise_amplitude=noise)
        rows.append(
            {
                "noise_amplitude": noise,
                "in_phase_high_accuracy": high_accuracy,
                "opposite_phase_low_accuracy": low_accuracy,
                "combined_accuracy": (high_accuracy + low_accuracy) / 2.0,
            }
        )
    return rows


def print_csv(rows: list[dict[str, float | str]]) -> None:
    print("noise_amplitude,in_phase_high_accuracy,opposite_phase_low_accuracy,combined_accuracy")
    for row in rows:
        print(
            f"{row['noise_amplitude']:.2f},{row['in_phase_high_accuracy']:.2f},"
            f"{row['opposite_phase_low_accuracy']:.2f},{row['combined_accuracy']:.2f}"
        )


if __name__ == "__main__":
    print_csv(run_noise_tolerance())
