# Simulation 008 Summary

Statistical validation of optimized GreyNOC pilot-tracking protocols.

SNR sweep: `-8.0 dB` to `8.0 dB`
Trials per SNR point: `8`
Random payload length: `32` characters
Protocol variants tested: `4`
Stress profiles tested: `8`
Usable BER threshold: `0.01`
CI95 upper BER target: `0.02`

## Top validated protocol

Protocol: `chirp_psk_p16_pi4_c32`
Carrier: `chirp + PSK`
Preamble: `16` bits
Pilot: `4` bits
Payload chunk: `32` bits
Overhead ratio: `0.147`
Average BER: `0.00027`
Average CI95 upper BER: `0.00051`
Profiles passed: `8/8`
Median threshold: `-8.0`
Meets validation target: `True`

Protocols meeting target: `3`

## Validation ranking

| Rank | Protocol | Carrier | Overhead | Avg BER | CI95 upper BER | Profiles passed | Meets target |
|---:|---|---|---:|---:|---:|---:|---|
| 1 | chirp_psk_p16_pi4_c32 | chirp / PSK | 0.147 | 0.00027 | 0.00051 | 8/8 | True |
| 2 | chirp_psk_p8_pi4_c32 | chirp / PSK | 0.123 | 0.00052 | 0.00106 | 8/8 | True |
| 3 | sine_psk_p8_pi8_c32 | sine / PSK | 0.200 | 0.00165 | 0.00229 | 8/8 | True |
| 4 | square_psk_p8_pi8_c32 | square / PSK | 0.200 | 0.00530 | 0.00637 | 7/8 | False |

## Best protocol by stress profile

| Stress profile | Best protocol | Best carrier | Threshold | Avg BER | Protocols passing |
|---|---|---|---:|---:|---:|
| attenuation | chirp_psk_p8_pi4_c32 | chirp / PSK | -8.0 | 0.00000 | 4/4 |
| baseline_awgn | chirp_psk_p8_pi4_c32 | chirp / PSK | -8.0 | 0.00000 | 4/4 |
| combined_drift_timing | chirp_psk_p16_pi4_c32 | chirp / PSK | -4.0 | 0.00146 | 3/4 |
| moderate_negative_drift | sine_psk_p8_pi8_c32 | sine / PSK | -8.0 | 0.00020 | 4/4 |
| moderate_positive_drift | chirp_psk_p16_pi4_c32 | chirp / PSK | -8.0 | 0.00010 | 4/4 |
| multipath_echo | chirp_psk_p16_pi4_c32 | chirp / PSK | -8.0 | 0.00000 | 4/4 |
| narrowband_interference | chirp_psk_p16_pi4_c32 | chirp / PSK | -8.0 | 0.00000 | 4/4 |
| severe_positive_drift | sine_psk_p8_pi8_c32 | sine / PSK | -8.0 | 0.00010 | 4/4 |

## Interpretation

Simulation 008 freezes the best Simulation 007 protocols and reruns them with more trials, longer random payloads, and broader stress coverage.
The validation target requires low average BER, low CI95 upper BER, and no failed stress profiles.
