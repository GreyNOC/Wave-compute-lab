# Prototype 001 Results - Interference Gate

## Goal

Build a repeatable software simulation showing that controlled wave interference can act as a primitive decision gate.

## Prototype behavior

Two sine waves with the same frequency are sampled and combined:

- In phase: constructive interference, peak strength near 2.0, decision HIGH
- 180 degrees out of phase: destructive interference, peak strength near 0.0, decision LOW
- 90 degrees out of phase: partial interference, peak strength near sqrt(2), decision HIGH with the current 1.25 threshold

## Test run

Command:

```bash
PYTHONPATH=. python -m unittest discover -s tests -v
```

Result:

```text
Ran 6 tests
OK
```

## Demo run

Command:

```bash
PYTHONPATH=. python simulations/interference_gate.py
```

Result:

```text
Prototype 001 - Interference Gate
in_phase        phase=0.000 strength=2.000 power=2.000 corr=1.000 decision=HIGH
quarter_phase   phase=1.571 strength=1.414 power=1.000 corr=-0.000 decision=HIGH
opposite_phase  phase=3.142 strength=0.000 power=0.000 corr=-1.000 decision=LOW
```

## Additional simulation primitives added

The first prototype now includes reusable standard-library-only primitives for:

- sine wave generation
- wave combination / superposition
- peak amplitude measurement
- average power measurement
- normalized signal correlation
- bit-to-frequency encoding
- frequency decoding by candidate-bin energy
- resonance-style target frequency detection

## Current status

Working simulation prototype achieved. The repository can now run a repeatable Prototype 001 interference gate simulation and a small test suite without requiring NumPy, SciPy, or Matplotlib.

## Next test targets

1. Add configurable noise and measure decision tolerance.
2. Sweep phase differences from 0 to pi and map threshold behavior.
3. Add multi-bit frequency encoding and decoding.
4. Add simple CSV or JSON output for experiment logs.
5. Add plotting as an optional extra dependency after the pure simulation core stays stable.
