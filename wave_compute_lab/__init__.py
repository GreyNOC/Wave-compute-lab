"""Wave Compute Lab simulation primitives."""

from .core import (
    WaveSignal,
    add_uniform_noise,
    average_power,
    combine_waves,
    concatenate_signals,
    correlation,
    decode_bit_message,
    decode_frequency,
    encode_bit,
    encode_bit_message,
    generate_sine,
    interference_gate,
    interference_gate_custom,
    interference_gate_from_signals,
    peak_amplitude,
    resonance_detector,
    slice_signal,
)
from .experiment_io import print_csv, write_csv

__all__ = [
    "WaveSignal",
    "add_uniform_noise",
    "average_power",
    "combine_waves",
    "concatenate_signals",
    "correlation",
    "decode_bit_message",
    "decode_frequency",
    "encode_bit",
    "encode_bit_message",
    "generate_sine",
    "interference_gate",
    "interference_gate_custom",
    "interference_gate_from_signals",
    "peak_amplitude",
    "print_csv",
    "resonance_detector",
    "slice_signal",
    "write_csv",
]
