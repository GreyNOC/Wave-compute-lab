"""Wave Compute Lab simulation primitives."""

from .core import (
    WaveSignal,
    average_power,
    combine_waves,
    correlation,
    decode_frequency,
    encode_bit,
    generate_sine,
    interference_gate,
    peak_amplitude,
    resonance_detector,
)

__all__ = [
    "WaveSignal",
    "average_power",
    "combine_waves",
    "correlation",
    "decode_frequency",
    "encode_bit",
    "generate_sine",
    "interference_gate",
    "peak_amplitude",
    "resonance_detector",
]
