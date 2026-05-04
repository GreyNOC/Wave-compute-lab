# Simulation 007 Summary

Pilot-overhead optimization for GreyNOC wave carriers.

SNR sweep: `-4.0 dB` to `8.0 dB`
Trials per SNR point: `1`
Random payload length: `16` characters
Overhead variants tested: `12`
Usable BER threshold: `0.01`
Optimization target average BER: `0.01`

## Best efficient configuration

Carrier: `chirp + PSK`
Preamble: `8` bits
Pilot: `4` bits
Payload chunk: `32` bits
Overhead ratio: `0.135`
Average BER: `0.00000`
Profiles passed: `5/5`
Median threshold: `-4.0`
Meets target: `True`

Configurations meeting target: `7`

## Top 10 efficiency ranking

| Rank | Carrier | Preamble | Pilot | Chunk | Overhead | Avg BER | Profiles passed | Meets target |
|---:|---|---:|---:|---:|---:|---:|---:|---|
| 1 | chirp / PSK | 8 | 4 | 32 | 0.135 | 0.00000 | 5/5 | True |
| 2 | chirp / PSK | 16 | 4 | 32 | 0.179 | 0.00000 | 5/5 | True |
| 3 | chirp / PSK | 8 | 8 | 32 | 0.200 | 0.00104 | 5/5 | True |
| 4 | sine / PSK | 8 | 8 | 32 | 0.200 | 0.00156 | 5/5 | True |
| 5 | square / PSK | 8 | 8 | 32 | 0.200 | 0.00521 | 5/5 | True |
| 6 | chirp / PSK | 16 | 8 | 32 | 0.238 | 0.00000 | 5/5 | True |
| 7 | sine / PSK | 16 | 8 | 32 | 0.238 | 0.00313 | 5/5 | True |
| 8 | square / PSK | 8 | 4 | 32 | 0.135 | 0.01875 | 5/5 | False |
| 9 | sine / PSK | 16 | 4 | 32 | 0.179 | 0.01719 | 5/5 | False |
| 10 | square / PSK | 8 | 4 | 64 | 0.086 | 0.12865 | 4/5 | False |

## Best configuration by carrier

| Carrier | Preamble | Pilot | Chunk | Overhead | Avg BER | Profiles passed |
|---|---:|---:|---:|---:|---:|---:|
| chirp / PSK | 8 | 4 | 32 | 0.135 | 0.00000 | 5/5 |
| sine / PSK | 8 | 8 | 32 | 0.200 | 0.00156 | 5/5 |
| square / PSK | 8 | 8 | 32 | 0.200 | 0.00521 | 5/5 |

## Interpretation

Simulation 007 asks how much synchronization overhead can be removed while preserving the Simulation 006 pilot-tracking breakthrough.
The ranking favors configurations that pass all stress profiles, keep BER low, and use the lowest overhead ratio.
