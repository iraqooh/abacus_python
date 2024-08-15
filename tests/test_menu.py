import unittest
from abacus.menu import handle_main_menu_input, handle_calculator_menu

class TestMenu(unittest.TestCase):
    def test_handle_main_menu_input(self):
        
        self.assertIsNone(handle_main_menu_input('1'))
        self.assertIsNone(handle_main_menu_input('4'))

    def test_handle_calculator_menu(self):
        
        self.assertIsNone(handle_calculator_menu())

if __name__ == '__main__':
    unittest.main()
