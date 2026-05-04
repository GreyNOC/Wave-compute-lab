# Simulation 006 Summary

Pilot-symbol tracking for continuous receiver lock in GreyNOC wave carriers.

SNR sweep: `-4.0 dB` to `8.0 dB`
Trials per SNR point: `2`
Random payload length: `16` characters
Preamble length: `16` bits
Pilot length: `8` bits
Payload chunk size: `32` bits
Estimated sync overhead: `40` bits per `128` payload bits
Pilot drift search: `-800.0 ppm` to `800.0 ppm`
Usable BER threshold: `0.01`

## Top pilot-tracking carrier

Top carrier: `sine + PSK`
Profiles passed: `5/5`
Median threshold: `-4.0`
Average BER: `0.00684`
Average pilot match rate: `1.000`

## Overall pilot-tracking ranking

| Rank | Waveform | Modulation | Profiles passed | Median threshold | Avg BER | Pilot match | Avg freq error ppm |
|---:|---|---|---:|---:|---:|---:|---:|
| 1 | sine | PSK | 5/5 | -4.0 | 0.00684 | 1.000 | 147.5 |
| 2 | square | PSK | 5/5 | -4.0 | 0.00684 | 1.000 | 145.0 |
| 3 | chirp | PSK | 5/5 | 0.0 | 0.00664 | 1.000 | 135.0 |
| 4 | triangle | PSK | 4/5 | -4.0 | 0.01387 | 1.000 | 152.5 |
| 5 | chirp | FSK | 2/5 | -4.0 | 0.03848 | 1.000 | 355.0 |

## Pilot receiver impact

Average BER improvement versus preamble-only tracking: `0.34488`
Average drift-profile BER improvement versus preamble-only tracking: `0.43110`

## Interpretation

Simulation 006 adds known pilot markers between payload chunks.
The receiver scores both the preamble and the pilots, which tests whether continuous sync markers can keep the decoder locked after the start of the message.
