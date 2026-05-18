"""Phase 2 measurement suite for GreyNOC Wave Compute Lab.

Runs repeatable noise-tolerance trials against Prototype 001 and prints a compact
Markdown table suitable for experiment notes.
"""

from __future__ import annotations

import math
from dataclasses import dataclass

import numpy as np

from wave_compute_lab import accuracy, interference_gate


@dataclass(frozen=True)
class TrialSummary:
    noise_std: float
    high_accuracy: float
    low_accuracy: float
    combined_accuracy: float
    avg_high_strength: float
    avg_low_strength: float


def run_trials(*, noise_levels: list[float], trials_per_level: int = 200, seed: int = 42) -> list[TrialSummary]:
    rng = np.random.default_rng(seed)
    summaries: list[TrialSummary] = []

    for noise_std in noise_levels:
        expected_high: list[str] = []
        observed_high: list[str] = []
        high_strengths: list[float] = []

        expected_low: list[str] = []
        observed_low: list[str] = []
        low_strengths: list[float] = []

        for _ in range(trials_per_level):
            high = interference_gate(
                phase_difference_radians=0.0,
                noise_std=noise_std,
                decision_threshold=1.0,
                rng=rng,
            )
            low = interference_gate(
                phase_difference_radians=math.pi,
                noise_std=noise_std,
                decision_threshold=1.0,
                rng=rng,
            )

            expected_high.append("HIGH")
            observed_high.append(str(high["decision"]))
            high_strengths.append(float(high["strength"]))

            expected_low.append("LOW")
            observed_low.append(str(low["decision"]))
            low_strengths.append(float(low["strength"]))

        expected = expected_high + expected_low
        observed = observed_high + observed_low
        summaries.append(
            TrialSummary(
                noise_std=noise_std,
                high_accuracy=accuracy(expected_high, observed_high),
                low_accuracy=accuracy(expected_low, observed_low),
                combined_accuracy=accuracy(expected, observed),
                avg_high_strength=float(np.mean(high_strengths)),
                avg_low_strength=float(np.mean(low_strengths)),
            )
        )

    return summaries


def print_markdown_table(summaries: list[TrialSummary]) -> None:
    print("| noise_std | high_acc | low_acc | combined_acc | avg_high_strength | avg_low_strength |")
    print("|---:|---:|---:|---:|---:|---:|")
    for row in summaries:
        print(
            f"| {row.noise_std:.2f} | {row.high_accuracy:.3f} | {row.low_accuracy:.3f} | "
            f"{row.combined_accuracy:.3f} | {row.avg_high_strength:.3f} | {row.avg_low_strength:.3f} |"
        )


def main() -> None:
    summaries = run_trials(noise_levels=[0.00, 0.05, 0.10, 0.20, 0.35, 0.50])
    print("Phase 2 - Interference Gate Noise Tolerance")
    print_markdown_table(summaries)


if __name__ == "__main__":
    main()
