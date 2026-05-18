import math
import unittest

from wave_compute_lab import (
    decode_frequency,
    encode_bit,
    generate_sine,
    interference_gate,
    resonance_detector,
)


class InterferenceGateTests(unittest.TestCase):
    def test_in_phase_waves_produce_high_output(self):
        result = interference_gate(phase_difference_radians=0.0)
        self.assertEqual(result["decision"], "HIGH")
        self.assertGreater(result["strength"], 1.9)
        self.assertGreater(result["correlation"], 0.99)

    def test_opposite_phase_waves_produce_low_output(self):
        result = interference_gate(phase_difference_radians=math.pi)
        self.assertEqual(result["decision"], "LOW")
        self.assertLess(result["strength"], 0.01)
        self.assertLess(result["correlation"], -0.99)


class FrequencyEncodingTests(unittest.TestCase):
    def test_bit_zero_decodes_to_zero_frequency(self):
        signal = encode_bit(0, zero_hz=100, one_hz=200, sample_rate=2000, duration_s=1.0)
        decoded, energy = decode_frequency(signal, [100, 200])
        self.assertEqual(decoded, 100)
        self.assertGreater(energy[100], 10 * energy[200])

    def test_bit_one_decodes_to_one_frequency(self):
        signal = encode_bit(1, zero_hz=100, one_hz=200, sample_rate=2000, duration_s=1.0)
        decoded, energy = decode_frequency(signal, [100, 200])
        self.assertEqual(decoded, 200)
        self.assertGreater(energy[200], 10 * energy[100])


class ResonanceDetectorTests(unittest.TestCase):
    def test_detector_activates_on_target_frequency(self):
        signal = generate_sine(440, sample_rate=8000, duration_s=1.0)
        result = resonance_detector(signal, target_hz=440, off_target_hz=[220, 330, 550])
        self.assertTrue(result["activated"])
        self.assertGreater(result["ratio"], 100)

    def test_detector_rejects_wrong_frequency(self):
        signal = generate_sine(550, sample_rate=8000, duration_s=1.0)
        result = resonance_detector(signal, target_hz=440, off_target_hz=[550])
        self.assertFalse(result["activated"])


if __name__ == "__main__":
    unittest.main()
