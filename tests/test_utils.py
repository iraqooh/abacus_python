# test_utils.py
import unittest
from abacus.utils import convert_units, format_number, parse_number, validate_positive_number, get_user_input

class TestUtils(unittest.TestCase):

    def test_convert_units(self):
        # Test length conversion
        self.assertAlmostEqual(convert_units(1, 'meters', 'feet'), 3.28084, places=5)
        self.assertAlmostEqual(convert_units(1, 'feet', 'meters'), 0.3048, places=4)
        
        # Test weight conversion
        self.assertAlmostEqual(convert_units(1, 'kg', 'lbs'), 2.20462, places=5)
        self.assertAlmostEqual(convert_units(1, 'lbs', 'kg'), 0.453592, places=6)
        
        # Test invalid unit
        with self.assertRaises(ValueError):
            convert_units(1, 'invalid_unit', 'meters')

    def test_format_number(self):
        self.assertEqual(format_number(1234567.890, precision=2), '1,234,567.89')
        self.assertEqual(format_number(1234567.890, precision=3, thousands_separator=' '), '1 234 567.890')
        
    def test_parse_number(self):
        self.assertEqual(parse_number('1,234,567.89'), 1234567.89)
        self.assertEqual(parse_number('1234567.89'), 1234567.89)
        
    def test_validate_positive_number(self):
        self.assertTrue(validate_positive_number(1))
        self.assertTrue(validate_positive_number(0.1))
        self.assertFalse(validate_positive_number(-1))
        self.assertFalse(validate_positive_number(0))
        
    def test_get_user_input(self):
        # This test is a bit tricky as it involves user input. Here we can only provide a placeholder.
        def always_valid_input(value):
            return True
        
        # Mocking input function for testing
        with unittest.mock.patch('builtins.input', return_value='test_input'):
            self.assertEqual(get_user_input('Enter something: ', always_valid_input), 'test_input')

if __name__ == '__main__':
    unittest.main()
