import unittest
from calculate_volume import calculate_volume

class TestParameterization(unittest.TestCase):
    def test_calculate_volume(self):
        self.assertAlmostEqual(calculate_volume(1), 4.188790133333333)
        self.assertAlmostEqual(calculate_volume(0), 0)
        self.assertRaises(ValueError, calculate_volume, -1)

if __name__ == '__main__':
    unittest.main()
