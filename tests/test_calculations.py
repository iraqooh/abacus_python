# test_calculations.py
import unittest
from unittest.mock import patch
from io import StringIO
from abacus.calculations import (
    arithmetic_operations,
    algebra_operations,
    trigonometry_operations,
    logarithm_operations,
    statistics_operations,
    finance_operations,
    calculus_operations,
    conversion_operations,
    constants_operations
)

class TestCalculations(unittest.TestCase):

    def test_arithmetic_operations(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            with patch('builtins.input', side_effect=[5, 3, 'add']):
                arithmetic_operations()
                output = fake_out.getvalue().strip()
                self.assertIn("Result:", output)

    def test_algebra_operations(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            with patch('builtins.input', side_effect=[1, -3, 2, 1]):
                algebra_operations()
                output = fake_out.getvalue().strip()
                self.assertIn("Roots:", output)

    def test_trigonometry_operations(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            with patch('builtins.input', side_effect=[30, 'sin']):
                trigonometry_operations()
                output = fake_out.getvalue().strip()
                self.assertIn("Result:", output)

    def test_logarithm_operations(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            with patch('builtins.input', side_effect=[10, 100, '10']):
                logarithm_operations()
                output = fake_out.getvalue().strip()
                self.assertIn("Result:", output)

    def test_statistics_operations(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            with patch('builtins.input', side_effect=['mean', '1 2 3 4 5']):
                statistics_operations()
                output = fake_out.getvalue().strip()
                self.assertIn("Mean:", output)

            with patch('builtins.input', side_effect=['median', '1 3 5']):
                statistics_operations()
                output = fake_out.getvalue().strip()
                self.assertIn("Median:", output)

    def test_finance_operations(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            with patch('builtins.input', side_effect=[1000, 5, 4, 10, 'compound_interest']):
                finance_operations()
                output = fake_out.getvalue().strip()
                self.assertIn("Future Value:", output)

    def test_calculus_operations(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            with patch('builtins.input', side_effect=[2, 'derivative']):
                calculus_operations()
                output = fake_out.getvalue().strip()
                self.assertIn("Derivative result:", output)

    def test_conversion_operations(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            with patch('builtins.input', side_effect=[10, 'meters to feet']):
                conversion_operations()
                output = fake_out.getvalue().strip()
                self.assertIn("Converted value:", output)

    def test_constants_operations(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            with patch('builtins.input', side_effect=['pi']):
                constants_operations()
                output = fake_out.getvalue().strip()
                self.assertIn("Pi:", output)

            with patch('builtins.input', side_effect=['e']):
                constants_operations()
                output = fake_out.getvalue().strip()
                self.assertIn("E:", output)

if __name__ == '__main__':
    unittest.main()
