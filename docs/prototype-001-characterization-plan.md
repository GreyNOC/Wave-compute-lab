# Prototype 001 Characterization Plan

## Purpose

Prototype 001 has moved beyond a clean interference-gate demo. The next phase is to characterize where the gate works, where it becomes unstable, and what design rules should guide any hardware attempt.

The core question is:

> How reliable is a wave-interference decision gate under imperfect conditions?

## Characterization experiments

### 1. Borderline noise sweep

Script:

```bash
PYTHONPATH=. python experiments/prototype-001-interference-gate/borderline_noise_sweep.py
```

CSV output:

```text
results/prototype-001/borderline_noise_sweep.csv
```

Purpose:

Measure phase angles near the known decision boundary under different noise levels.

Tested phases:

```text
75, 85, 90, 95, 100, 105, 110, 115, 120 degrees
```

Tested noise amplitudes:

```text
0.00, 0.02, 0.05, 0.10, 0.20, 0.40
```

What this should reveal:

- below-boundary HIGH stability
- above-boundary LOW stability
- unstable transition band around the decision threshold

### 2. Threshold calibration

Script:

```bash
PYTHONPATH=. python experiments/prototype-001-interference-gate/threshold_calibration.py
```

CSV output:

```text
results/prototype-001/threshold_calibration.csv
```

Purpose:

Compare multiple HIGH/LOW thresholds so the default threshold is justified by data rather than intuition.

Tested thresholds:

```text
1.00, 1.10, 1.20, 1.25, 1.30, 1.40, 1.50
```

What this should reveal:

- which threshold best separates the intended HIGH and LOW regions
- whether the current `1.25` threshold remains a good default
- how many false HIGH and false LOW decisions each threshold produces

### 3. Amplitude mismatch

Script:

```bash
PYTHONPATH=. python experiments/prototype-001-interference-gate/amplitude_mismatch.py
```

CSV output:

```text
results/prototype-001/amplitude_mismatch.csv
```

Purpose:

Test destructive interference when the two source amplitudes do not match.

This matters because real hardware sources will not always produce equal signal strength.

Tested second-wave amplitudes:

```text
1.00, 0.90, 0.75, 0.50, 0.25
```

What this should reveal:

- how quickly LOW classification degrades when cancellation is incomplete
- how tightly matched hardware amplitudes need to be
- whether amplitude normalization is required before hardware testing

### 4. Frequency mismatch

Script:

```bash
PYTHONPATH=. python experiments/prototype-001-interference-gate/frequency_mismatch.py
```

CSV output:

```text
results/prototype-001/frequency_mismatch.csv
```

Purpose:

Test interference when the two wave sources drift apart in frequency.

This matters because real oscillators are imperfect.

Tested second-wave frequencies:

```text
10.00, 10.05, 10.10, 10.25, 10.50, 11.00, 12.00 Hz
```

What this should reveal:

- how much oscillator drift Prototype 001 can tolerate
- whether the gate requires locked frequencies
- whether longer or shorter measurement windows change reliability

## Current guardrail tests

Run:

```bash
PYTHONPATH=. python -m unittest discover -s tests -v
```

The suite now protects:

- clean constructive interference
- clean destructive interference
- noisy constructive interference
- noisy destructive interference
- phase decision-boundary behavior
- reproducible seeded noise
- amplitude mismatch behavior
- frequency mismatch behavior
- CSV result writing
- frequency bit decoding
- resonance detection

## Phase 1B completion criteria

Prototype 001 characterization is complete when we can answer:

1. Where is the stable HIGH region?
2. Where is the stable LOW region?
3. Where is the unstable transition band?
4. Which threshold should be the default?
5. How much noise is tolerable?
6. How much amplitude mismatch is tolerable?
7. How much frequency mismatch is tolerable?
8. Is this ready for a simple hardware audio prototype?

## Current recommendation

Use Prototype 001 primarily as a learning and measurement primitive. It is useful for proving controlled wave interaction and building discipline around simulation-first research.

For practical GreyNOC applications, the later frequency encoder and resonance detector paths may become more useful than the interference gate itself.
