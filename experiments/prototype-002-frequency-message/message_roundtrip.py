"""Prototype 002: encode and decode bit strings as frequency messages."""

from __future__ import annotations

from pathlib import Path
from wave_compute_lab import decode_bit_message, encode_bit_message, print_csv, write_csv

MESSAGES = ["1011001", "11001010", "111100001111", "100110011001"]
NOISE_LEVELS = [0.00, 0.02, 0.05, 0.10, 0.20]
RESULT_PATH = Path("results/prototype-002/message_roundtrip.csv")


def run_message_roundtrip() -> list[dict[str, float | int | str]]:
    rows: list[dict[str, float | int | str]] = []
    for message in MESSAGES:
        for noise_amplitude in NOISE_LEVELS:
            signal = encode_bit_message(
                message,
                zero_hz=100,
                one_hz=200,
                sample_rate=4000,
                bit_duration_s=0.05,
                noise_amplitude=noise_amplitude,
                seed=42,
            )
            decoded = decode_bit_message(
                signal,
                bit_count=len(message),
                zero_hz=100,
                one_hz=200,
                bit_duration_s=0.05,
            )
            correct_bits = sum(1 for expected, actual in zip(message, decoded) if expected == actual)
            rows.append(
                {
                    "message": message,
                    "noise_amplitude": noise_amplitude,
                    "decoded": decoded,
                    "bit_count": len(message),
                    "correct_bits": correct_bits,
                    "bit_accuracy": round(correct_bits / len(message), 4),
                    "success": int(decoded == message),
                }
            )
    return rows


if __name__ == "__main__":
    experiment_rows = run_message_roundtrip()
    write_csv(RESULT_PATH, experiment_rows)
    print_csv(experiment_rows)
