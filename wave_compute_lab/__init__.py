"""Wave Compute Lab simulation primitives."""

from .core import (
    WaveSignal,
    add_uniform_noise,
    average_power,
    combine_waves,
    correlation,
    decode_frequency,
    encode_bit,
    generate_sine,
    interference_gate,
    interference_gate_from_signals,
    peak_amplitude,
    resonance_detector,
)

__all__ = [
    "WaveSignal",
    "add_uniform_noise",
    "average_power",
    "combine_waves",
    "correlation",
    "decode_frequency",
    "encode_bit",
    "generate_sine",
    "interference_gate",
    "interference_gate_from_signals",
    "peak_amplitude",
    "resonance_detector",
]
