# Simulation 004 Summary

Synchronization and recovery testing for GreyNOC wave carriers.

SNR sweep: `-8.0 dB` to `8.0 dB`
Trials per SNR point: `2`
Random payload length: `16` characters
Preamble length: `16` bits
Usable BER threshold: `0.01`
Reliability threshold: `0.8`

## Overall ranking after synchronization recovery

| Rank | Waveform | Modulation | Profiles passed | Median threshold | Avg BER | Preamble match |
|---:|---|---|---:|---:|---:|---:|
| 1 | chirp | PSK | 2/4 | -4.0 | 0.26348 | 1.000 |
| 2 | sine | PSK | 2/4 | -2.0 | 0.20078 | 1.000 |
| 3 | triangle | PSK | 2/4 | -2.0 | 0.20273 | 1.000 |
| 4 | chirp | FSK | 2/4 | 0.0 | 0.06445 | 0.975 |
| 5 | square | PSK | 1/4 | -8.0 | 0.22734 | 1.000 |
| 6 | pulse | PSK | 0/4 | not_reached | 0.32051 | 0.000 |

## Synchronization impact

Recovered not-reached cases: `3`
Average numeric threshold improvement: `0.67 dB`

## Interpretation

Simulation 004 adds a known preamble and a receiver-side search over timing offsets and frequency-drift corrections.
The purpose is to test whether the major Simulation 003 failures were carrier failures or receiver synchronization failures.
