"""Sweep Prototype 001 across phase angles and print CSV results."""

from __future__ import annotations

import math
from wave_compute_lab import interference_gate


def run_phase_sweep(step_degrees: int = 15) -> list[dict[str, float | str]]:
    rows: list[dict[str, float | str]] = []
    for degrees in range(0, 181, step_degrees):
        result = interference_gate(phase_difference_radians=math.radians(degrees))
        rows.append(
            {
                "phase_degrees": degrees,
                "strength": round(float(result["strength"]), 6),
                "power": round(float(result["power"]), 6),
                "correlation": round(float(result["correlation"]), 6),
                "decision": str(result["decision"]),
            }
        )
    return rows


def print_csv(rows: list[dict[str, float | str]]) -> None:
    print("phase_degrees,strength,power,correlation,decision")
    for row in rows:
        print(
            f"{row['phase_degrees']},{row['strength']:.6f},{row['power']:.6f},"
            f"{row['correlation']:.6f},{row['decision']}"
        )


if __name__ == "__main__":
    print_csv(run_phase_sweep())
