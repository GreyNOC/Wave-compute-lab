# Simulation 005 Summary

Adaptive frequency drift recovery testing for GreyNOC wave carriers.

SNR sweep: `-4.0 dB` to `8.0 dB`
Trials per SNR point: `1`
Random payload length: `16` characters
Preamble length: `16` bits
Adaptive drift search: `-800.0 ppm` to `800.0 ppm`
Usable BER threshold: `0.01`

## Top adaptive carrier

Top carrier: `chirp + FSK`
Profiles passed: `2/5`
Median threshold: `2.0`
Average BER: `0.06328`

## Overall adaptive ranking

| Rank | Waveform | Modulation | Profiles passed | Median threshold | Avg BER | Preamble match | Avg freq error ppm |
|---:|---|---|---:|---:|---:|---:|---:|
| 1 | chirp | FSK | 2/5 | 2.0 | 0.06328 | 1.000 | 405.0 |
| 2 | sine | PSK | 1/5 | -4.0 | 0.38359 | 1.000 | 420.0 |
| 3 | triangle | PSK | 1/5 | -4.0 | 0.39883 | 1.000 | 420.0 |
| 4 | square | PSK | 1/5 | -4.0 | 0.42500 | 1.000 | 465.0 |
| 5 | chirp | PSK | 1/5 | -4.0 | 0.44844 | 1.000 | 435.0 |

## Adaptive receiver impact

Average BER improvement versus coarse synchronization: `-0.00375`
Average drift-profile BER improvement versus coarse synchronization: `-0.00469`

## Interpretation

Simulation 005 replaces the coarse three-value frequency correction from Simulation 004 with a fine-grained preamble-scored drift sweep.
The goal is to determine whether frequency drift failures are receiver-correction failures rather than carrier failures.
