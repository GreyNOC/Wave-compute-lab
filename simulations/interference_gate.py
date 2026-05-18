"""Run Prototype 001: an interference-based wave decision gate."""

from __future__ import annotations

import math
from wave_compute_lab import interference_gate


def run_demo() -> None:
    scenarios = {
        "in_phase": 0.0,
        "quarter_phase": math.pi / 2.0,
        "opposite_phase": math.pi,
    }
    print("Prototype 001 - Interference Gate")
    for name, phase in scenarios.items():
        result = interference_gate(phase_difference_radians=phase)
        print(
            f"{name:15s} phase={phase:.3f} "
            f"strength={result['strength']:.3f} "
            f"power={result['power']:.3f} "
            f"corr={result['correlation']:.3f} "
            f"decision={result['decision']}"
        )


if __name__ == "__main__":
    run_demo()
