"""Core simulation functions for wave-based computing prototypes.

The module intentionally uses only the Python standard library so the first
prototype can run anywhere Python 3.10+ is available.  It models simple sine
waves, interference, frequency encoding/decoding, resonance detection, and
controlled noise injection for tolerance testing.
"""

from __future__ import annotations

from dataclasses import dataclass
import math
import random
from typing import Iterable, Sequence


@dataclass(frozen=True)
class WaveSignal:
    """A sampled 1-D signal."""

    samples: tuple[float, ...]
    sample_rate: int

    @property
    def duration(self) -> float:
        return len(self.samples) / self.sample_rate


def _validate_sample_args(frequency_hz: float, sample_rate: int, duration_s: float) -> None:
    if frequency_hz <= 0:
        raise ValueError("frequency_hz must be positive")
    if sample_rate <= 0:
        raise ValueError("sample_rate must be positive")
    if duration_s <= 0:
        raise ValueError("duration_s must be positive")
    if sample_rate <= 2 * frequency_hz:
        raise ValueError("sample_rate must be greater than twice the frequency to satisfy Nyquist")


def generate_sine(
    frequency_hz: float,
    *,
    sample_rate: int = 8_000,
    duration_s: float = 1.0,
    amplitude: float = 1.0,
    phase_radians: float = 0.0,
) -> WaveSignal:
    """Generate a sampled sine wave."""

    _validate_sample_args(frequency_hz, sample_rate, duration_s)
    sample_count = int(sample_rate * duration_s)
    if sample_count < 2:
        raise ValueError("duration_s and sample_rate must produce at least two samples")

    samples = tuple(
        amplitude * math.sin((2.0 * math.pi * frequency_hz * n / sample_rate) + phase_radians)
        for n in range(sample_count)
    )
    return WaveSignal(samples=samples, sample_rate=sample_rate)


def add_uniform_noise(signal: WaveSignal, *, noise_amplitude: float, seed: int | None = None) -> WaveSignal:
    """Add reproducible uniform noise to a signal.

    noise_amplitude is the largest absolute noise value added to each sample.
    A value of 0.05 means every sample receives noise in the range [-0.05, 0.05].
    """

    if noise_amplitude < 0:
        raise ValueError("noise_amplitude must be non-negative")
    rng = random.Random(seed)
    noisy_samples = tuple(
        sample + rng.uniform(-noise_amplitude, noise_amplitude)
        for sample in signal.samples
    )
    return WaveSignal(samples=noisy_samples, sample_rate=signal.sample_rate)


def combine_waves(*waves: WaveSignal) -> WaveSignal:
    """Add two or more sampled waves."""

    if not waves:
        raise ValueError("at least one wave is required")
    sample_rate = waves[0].sample_rate
    sample_count = len(waves[0].samples)
    for wave in waves:
        if wave.sample_rate != sample_rate:
            raise ValueError("all waves must use the same sample_rate")
        if len(wave.samples) != sample_count:
            raise ValueError("all waves must have the same number of samples")

    combined = tuple(sum(wave.samples[i] for wave in waves) for i in range(sample_count))
    return WaveSignal(samples=combined, sample_rate=sample_rate)


def peak_amplitude(signal: WaveSignal) -> float:
    """Return the largest absolute sample value."""

    return max(abs(sample) for sample in signal.samples)


def average_power(signal: WaveSignal) -> float:
    """Return the mean squared sample value."""

    return sum(sample * sample for sample in signal.samples) / len(signal.samples)


def correlation(signal_a: WaveSignal, signal_b: WaveSignal) -> float:
    """Return normalized correlation in the range roughly [-1, 1]."""

    if signal_a.sample_rate != signal_b.sample_rate or len(signal_a.samples) != len(signal_b.samples):
        raise ValueError("signals must share sample_rate and length")

    numerator = sum(a * b for a, b in zip(signal_a.samples, signal_b.samples))
    power_a = math.sqrt(sum(a * a for a in signal_a.samples))
    power_b = math.sqrt(sum(b * b for b in signal_b.samples))
    if power_a == 0.0 or power_b == 0.0:
        return 0.0
    return numerator / (power_a * power_b)


def interference_gate_from_signals(
    wave_a: WaveSignal,
    wave_b: WaveSignal,
    *,
    high_threshold: float = 1.25,
) -> dict[str, float | str]:
    """Decide HIGH/LOW from two already-generated waves."""

    combined = combine_waves(wave_a, wave_b)
    strength = peak_amplitude(combined)
    return {
        "strength": strength,
        "power": average_power(combined),
        "correlation": correlation(wave_a, wave_b),
        "decision": "HIGH" if strength >= high_threshold else "LOW",
    }


def interference_gate(
    *,
    phase_difference_radians: float,
    frequency_hz: float = 10.0,
    sample_rate: int = 2_000,
    duration_s: float = 1.0,
    high_threshold: float = 1.25,
    noise_amplitude: float = 0.0,
    seed: int | None = None,
) -> dict[str, float | str]:
    """Prototype 001: decide HIGH/LOW from wave interference strength.

    Two unit-amplitude waves of the same frequency are generated.  The second
    wave is shifted by phase_difference_radians.  Constructive interference
    produces a peak near 2.0, while destructive interference produces a peak
    near 0.0.  Optional reproducible noise can be added before measurement.
    """

    return interference_gate_custom(
        phase_difference_radians=phase_difference_radians,
        frequency_a_hz=frequency_hz,
        frequency_b_hz=frequency_hz,
        amplitude_a=1.0,
        amplitude_b=1.0,
        sample_rate=sample_rate,
        duration_s=duration_s,
        high_threshold=high_threshold,
        noise_amplitude=noise_amplitude,
        seed=seed,
    )


def interference_gate_custom(
    *,
    phase_difference_radians: float,
    frequency_a_hz: float = 10.0,
    frequency_b_hz: float = 10.0,
    amplitude_a: float = 1.0,
    amplitude_b: float = 1.0,
    sample_rate: int = 2_000,
    duration_s: float = 1.0,
    high_threshold: float = 1.25,
    noise_amplitude: float = 0.0,
    seed: int | None = None,
) -> dict[str, float | str]:
    """Interference gate with separate frequency and amplitude controls."""

    wave_a = generate_sine(
        frequency_a_hz,
        sample_rate=sample_rate,
        duration_s=duration_s,
        amplitude=amplitude_a,
    )
    wave_b = generate_sine(
        frequency_b_hz,
        sample_rate=sample_rate,
        duration_s=duration_s,
        amplitude=amplitude_b,
        phase_radians=phase_difference_radians,
    )
    if noise_amplitude:
        wave_a = add_uniform_noise(wave_a, noise_amplitude=noise_amplitude, seed=seed)
        wave_b = add_uniform_noise(wave_b, noise_amplitude=noise_amplitude, seed=None if seed is None else seed + 1)
    return interference_gate_from_signals(wave_a, wave_b, high_threshold=high_threshold)


def encode_bit(bit: int, *, zero_hz: float = 100.0, one_hz: float = 200.0, **kwargs: float) -> WaveSignal:
    """Encode a binary bit as one of two carrier frequencies."""

    if bit not in (0, 1):
        raise ValueError("bit must be 0 or 1")
    return generate_sine(one_hz if bit else zero_hz, **kwargs)


def _frequency_energy(signal: WaveSignal, candidate_hz: float) -> float:
    """Measure how strongly a sampled signal matches a candidate frequency."""

    cosine = 0.0
    sine = 0.0
    for n, sample in enumerate(signal.samples):
        angle = 2.0 * math.pi * candidate_hz * n / signal.sample_rate
        cosine += sample * math.cos(angle)
        sine += sample * math.sin(angle)
    return math.hypot(cosine, sine)


def decode_frequency(signal: WaveSignal, candidate_frequencies_hz: Sequence[float]) -> tuple[float, dict[float, float]]:
    """Decode a signal by selecting the candidate frequency with the most energy."""

    if not candidate_frequencies_hz:
        raise ValueError("candidate_frequencies_hz must not be empty")
    energy = {frequency: _frequency_energy(signal, frequency) for frequency in candidate_frequencies_hz}
    best = max(energy, key=energy.get)
    return best, energy


def resonance_detector(
    signal: WaveSignal,
    *,
    target_hz: float,
    off_target_hz: Iterable[float],
    activation_ratio: float = 2.0,
) -> dict[str, float | bool]:
    """Activate when the target frequency has enough energy over off-target bins."""

    target_energy = _frequency_energy(signal, target_hz)
    other_energies = [_frequency_energy(signal, hz) for hz in off_target_hz]
    strongest_other = max(other_energies, default=0.0)
    ratio = target_energy / strongest_other if strongest_other else math.inf
    return {
        "target_energy": target_energy,
        "strongest_other_energy": strongest_other,
        "ratio": ratio,
        "activated": ratio >= activation_ratio,
    }
