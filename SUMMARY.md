# Simulation 003 Summary

Statistical validation and channel stress testing for GreyNOC wave carriers.

SNR sweep: `-16.0 dB` to `8.0 dB`
Trials per SNR point: `6`
Random payload length: `16` characters
Usable BER threshold: `0.01`
Reliability threshold: `0.8`

## Overall resilience ranking

| Rank | Waveform | Modulation | Profiles passed | Median threshold | Avg BER |
|---:|---|---|---:|---:|---:|
| 1 | chirp | PSK | 5/7 | -8.0 | 0.22066 |
| 2 | sine | PSK | 5/7 | -8.0 | 0.19927 |
| 3 | square | PSK | 5/7 | -8.0 | 0.18806 |
| 4 | triangle | PSK | 5/7 | -8.0 | 0.20286 |
| 5 | square | FSK | 5/7 | -4.0 | 0.10964 |
| 6 | chirp | FSK | 5/7 | -4.0 | 0.10789 |
| 7 | pulse | PSK | 0/7 | not_reached | 0.32066 |

## Best carrier by stress profile

| Stress profile | Best carrier | Threshold |
|---|---|---:|
| attenuation | sine / PSK | -12.0 |
| baseline_awgn | chirp / PSK | -12.0 |
| frequency_drift | chirp / FSK | not_reached |
| multipath_echo | sine / PSK | -8.0 |
| narrowband_interference | chirp / PSK | -8.0 |
| phase_jitter | chirp / PSK | -12.0 |
| timing_offset | square / FSK | not_reached |

## Interpretation

Simulation 003 is meant to verify whether Simulation 002 rankings survive repeated randomized payloads and more realistic channel distortions.
A strong carrier should pass many stress profiles, maintain a low median usable SNR threshold, and keep average BER low across all conditions.
