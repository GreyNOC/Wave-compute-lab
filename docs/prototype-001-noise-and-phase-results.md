# Prototype 001 Noise and Phase Results

## Goal

Move Prototype 001 from a clean demo into a measured simulation experiment.

This commit adds two checks:

1. Phase sweep: measure the interference gate from 0 degrees through 180 degrees.
2. Noise tolerance: run repeated deterministic trials with increasing uniform noise.

## Phase sweep result

Command:

```bash
PYTHONPATH=. python experiments/prototype-001-interference-gate/phase_sweep.py
```

Result:

```text
phase_degrees,strength,power,correlation,decision
0,2.000000,2.000000,1.000000,HIGH
15,1.982863,1.965926,0.965926,HIGH
30,1.931746,1.866025,0.866025,HIGH
45,1.847531,1.707107,0.707107,HIGH
60,1.731956,1.500000,0.500000,HIGH
75,1.586685,1.258819,0.258819,HIGH
90,1.414214,1.000000,-0.000000,HIGH
105,1.217506,0.741181,-0.258819,LOW
120,0.999945,0.500000,-0.500000,LOW
135,0.765272,0.292893,-0.707107,LOW
150,0.517610,0.133975,-0.866025,LOW
165,0.261049,0.034074,-0.965926,LOW
180,0.000000,0.000000,-1.000000,LOW
```

## Initial interpretation

With the current `high_threshold = 1.25`, the clean decision boundary sits between 90 and 105 degrees of phase difference.

Plain-language behavior:

- 0 to 90 degrees: the waves reinforce enough to classify HIGH.
- 105 to 180 degrees: the waves cancel enough to classify LOW.
- 90 degrees is still HIGH because the combined peak is about 1.414, above the 1.25 threshold.

## Noise tolerance result

Command:

```bash
PYTHONPATH=. python experiments/prototype-001-interference-gate/noise_tolerance.py
```

Result:

```text
noise_amplitude,in_phase_high_accuracy,opposite_phase_low_accuracy,combined_accuracy
0.00,1.00,1.00,1.00
0.02,1.00,1.00,1.00
0.05,1.00,1.00,1.00
0.10,1.00,1.00,1.00
0.20,1.00,1.00,1.00
0.40,1.00,1.00,1.00
```

## Initial interpretation

The current gate is very stable for the two extreme cases:

- fully in-phase input
- fully opposite-phase input

Even with uniform per-sample noise up to 0.40, the simple peak-amplitude threshold classifies those two extremes correctly in this deterministic 100-trial run.

This does not mean the prototype is complete. It means the easy cases are stable. The next useful tests should target harder borderline cases around 90 to 120 degrees, where the threshold decision is more sensitive.

## Tests added

The test suite now checks:

- clean in-phase HIGH behavior
- clean opposite-phase LOW behavior
- noisy in-phase HIGH behavior
- noisy opposite-phase LOW behavior
- phase sweep decision boundary behavior
- reproducible seeded noise
- frequency bit decoding
- resonance detection

Command:

```bash
PYTHONPATH=. python -m unittest discover -s tests -v
```

Result:

```text
Ran 10 tests
OK
```

## Next recommended step

Add borderline noise tests around 90, 100, 105, 110, and 120 degrees. That will tell us how reliable the gate is near the actual decision boundary instead of only testing the easy extremes.
