"""Core simulation helpers for GreyNOC Wave Compute Lab.

The functions in this module keep the project grounded in measurable outputs:
strength, power, correlation, signal-to-noise ratio, and classification accuracy.
"""

from __future__ import annotations

import math
from typing import Iterable

import numpy as np


def time_axis(sample_rate: int = 4_000, duration_seconds: float = 1.0) -> np.ndarray:
    """Return a stable time axis for repeatable signal simulations."""
    if sample_rate <= 0:
        raise ValueError("sample_rate must be positive")
    if duration_seconds <= 0:
        raise ValueError("duration_seconds must be positive")
    return np.linspace(0.0, duration_seconds, int(sample_rate * duration_seconds), endpoint=False)


def sine_wave(
    frequency_hz: float,
    *,
    phase_radians: float = 0.0,
    amplitude: float = 1.0,
    sample_rate: int = 4_000,
    duration_seconds: float = 1.0,
) -> np.ndarray:
    """Generate a sine wave using frequency, phase, and amplitude."""
    if frequency_hz <= 0:
        raise ValueError("frequency_hz must be positive")
    t = time_axis(sample_rate=sample_rate, duration_seconds=duration_seconds)
    return amplitude * np.sin((2.0 * np.pi * frequency_hz * t) + phase_radians)


def add_noise(signal: np.ndarray, noise_std: float, *, rng: np.random.Generator | None = None) -> np.ndarray:
    """Add Gaussian noise to a signal."""
    if noise_std < 0:
        raise ValueError("noise_std must be non-negative")
    generator = rng or np.random.default_rng()
    return signal + generator.normal(0.0, noise_std, size=signal.shape)


def rms(signal: np.ndarray) -> float:
    """Root-mean-square amplitude."""
    return float(np.sqrt(np.mean(np.square(signal))))


def peak_strength(signal: np.ndarray) -> float:
    """Peak absolute amplitude."""
    return float(np.max(np.abs(signal)))


def signal_power(signal: np.ndarray) -> float:
    """Mean signal power."""
    return float(np.mean(np.square(signal)))


def normalized_correlation(a: np.ndarray, b: np.ndarray) -> float:
    """Return correlation in the range [-1, 1] for two same-length signals."""
    if a.shape != b.shape:
        raise ValueError("signals must have the same shape")
    denom = np.linalg.norm(a) * np.linalg.norm(b)
    if denom == 0:
        return 0.0
    return float(np.dot(a, b) / denom)


def estimate_snr_db(clean_signal: np.ndarray, observed_signal: np.ndarray) -> float:
    """Estimate signal-to-noise ratio in decibels."""
    noise = observed_signal - clean_signal
    noise_power = signal_power(noise)
    if noise_power == 0:
        return math.inf
    return float(10.0 * np.log10(signal_power(clean_signal) / noise_power))


def interference_gate(
    *,
    frequency_hz: float = 10.0,
    phase_difference_radians: float = 0.0,
    sample_rate: int = 4_000,
    duration_seconds: float = 1.0,
    noise_std: float = 0.0,
    decision_threshold: float = 1.0,
    rng: np.random.Generator | None = None,
) -> dict[str, float | str]:
    """Simulate a two-wave interference gate and classify HIGH/LOW output.

    HIGH means the combined signal has enough peak strength to act as a detectable
    constructive-interference event. LOW means cancellation or noise pushed the
    output below the selected decision threshold.
    """
    generator = rng or np.random.default_rng()
    wave_a = sine_wave(
        frequency_hz,
        sample_rate=sample_rate,
        duration_seconds=duration_seconds,
    )
    wave_b = sine_wave(
        frequency_hz,
        phase_radians=phase_difference_radians,
        sample_rate=sample_rate,
        duration_seconds=duration_seconds,
    )
    clean_combined = wave_a + wave_b
    observed = add_noise(clean_combined, noise_std, rng=generator) if noise_std else clean_combined
    strength = peak_strength(observed)
    return {
        "strength": strength,
        "rms": rms(observed),
        "power": signal_power(observed),
        "correlation": normalized_correlation(wave_a, wave_b),
        "snr_db": estimate_snr_db(clean_combined, observed),
        "decision": "HIGH" if strength >= decision_threshold else "LOW",
    }


def frequency_match_score(
    input_frequency_hz: float,
    target_frequency_hz: float,
    *,
    tolerance_hz: float = 2.0,
) -> float:
    """Return a normalized resonance-like score from 0.0 to 1.0."""
    if tolerance_hz <= 0:
        raise ValueError("tolerance_hz must be positive")
    delta = abs(input_frequency_hz - target_frequency_hz)
    return float(max(0.0, 1.0 - (delta / tolerance_hz)))


def classify_frequency_match(
    input_frequency_hz: float,
    target_frequency_hz: float,
    *,
    tolerance_hz: float = 2.0,
    threshold: float = 0.75,
) -> str:
    """Classify whether an input frequency matches a target resonance band."""
    score = frequency_match_score(input_frequency_hz, target_frequency_hz, tolerance_hz=tolerance_hz)
    return "MATCH" if score >= threshold else "MISS"


def accuracy(expected: Iterable[str], observed: Iterable[str]) -> float:
    """Return simple classification accuracy."""
    expected_list = list(expected)
    observed_list = list(observed)
    if len(expected_list) != len(observed_list):
        raise ValueError("expected and observed must have equal length")
    if not expected_list:
        return 0.0
    correct = sum(1 for truth, prediction in zip(expected_list, observed_list) if truth == prediction)
    return correct / len(expected_list)
