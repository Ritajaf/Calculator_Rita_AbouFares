import sys
import os


# Add the src/main/python directory to the path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../src/main/python')))

import unittest
from calculator_Rita_AbouFares import add, subtract, multiply, divide, modulus, power, square_root


class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 2), 3)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)

    def test_multiply(self):
        self.assertEqual(multiply(3, 4), 12)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        with self.assertRaises(ValueError):
            divide(10, 0)

    def test_modulus(self):
        self.assertEqual(modulus(10, 3), 1)

    def test_power(self):
        self.assertEqual(power(2, 3), 8)

    def test_square_root(self):
        self.assertEqual(square_root(9), 3)


if __name__ == '__main__':
    unittest.main()
