# Prototype 002: Frequency Message Encoder / Decoder

## Purpose

Prototype 002 moves Wave Compute Lab from a single interference decision toward information transfer in the frequency domain.

The basic question is:

> Can a bit string be encoded as wave frequencies, transmitted through a simulated signal, and decoded correctly?

## Why this matters

Prototype 001 proves wave interaction can create a decision.

Prototype 002 starts proving that information can move through a wave-domain representation.

This is closer to the long-term strategic target of a wave or photonic accelerator because useful accelerators need more than a single HIGH/LOW gate. They need to encode, route, compare, and decode information.

## Current encoding model

The first encoding is intentionally simple:

```text
0 = 100 Hz
1 = 200 Hz
```

A message like:

```text
1011001
```

becomes a sequence of frequency chunks:

```text
200 Hz, 100 Hz, 200 Hz, 200 Hz, 100 Hz, 100 Hz, 200 Hz
```

Each bit occupies a fixed time window.

## Current implementation

Core functions:

- `encode_bit_message(...)`
- `decode_bit_message(...)`
- `concatenate_signals(...)`
- `slice_signal(...)`

Experiment:

```bash
PYTHONPATH=. python experiments/prototype-002-frequency-message/message_roundtrip.py
```

CSV output:

```text
results/prototype-002/message_roundtrip.csv
```

## Success criteria

Prototype 002 is minimally successful when:

1. clean messages round-trip with 100% bit accuracy
2. light-noise messages round-trip with 100% bit accuracy
3. moderate-noise behavior is measured and documented
4. bit accuracy is reported, not just success/failure
5. frequency spacing and bit duration become tunable experiment parameters

## Next experiment targets

1. Sweep noise amplitude against bit accuracy.
2. Sweep bit duration to find minimum reliable window size.
3. Sweep frequency spacing to find how close 0 and 1 can be before decoding fails.
4. Add multi-symbol encoding beyond binary.
5. Add energy-per-correct-bit estimates.

## Long-term relevance

This prototype starts the path toward:

- wave-domain communication
- frequency-coded feature streams
- resonance-based signature detection
- photonic wavelength-channel encoding
- signal-classification coprocessors

It is still classical wave computing, not quantum computing. Its value is practical speed and signal-processing alignment.
