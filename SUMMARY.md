# Simulation 002 Summary

Noise tolerance ranking for GreyNOC wave information carriers.

Message: `GREYNOC WAVE TEST`
SNR sweep: `-30.0 dB` to `30.0 dB`
Trials per SNR point: `3`
Usable BER threshold: `0.01`

## Top carriers

| Rank | Waveform | Modulation | Usable threshold SNR | Avg BER | Worst BER |
|---:|---|---|---:|---:|---:|
| 1 | chirp | PSK | -12.0 | 0.06191 | 0.37010 |
| 2 | triangle | PSK | -12.0 | 0.06981 | 0.43382 |
| 3 | square | PSK | -10.0 | 0.06602 | 0.37010 |
| 4 | gaussian_pulse | PSK | -10.0 | 0.06618 | 0.40931 |
| 5 | sine | PSK | -10.0 | 0.06697 | 0.39461 |
| 6 | sawtooth | PSK | -8.0 | 0.08523 | 0.39461 |
| 7 | chirp | FSK | -8.0 | 0.11385 | 0.49020 |
| 8 | square | FSK | -8.0 | 0.11638 | 0.51471 |
| 9 | gaussian_pulse | FSK | -6.0 | 0.11591 | 0.48039 |
| 10 | triangle | FSK | -6.0 | 0.11820 | 0.49510 |

## Interpretation

Lower usable threshold SNR is better. A carrier that remains usable at -20 dB is more resilient than one that only becomes usable at +4 dB.

The ranking prioritizes the lowest usable threshold first, then the number of usable SNR points, then average BER across the full sweep.
