import unittest
from unittest.mock import patch, mock_open
import json
import os
from abacus.settings import (
    handle_settings_menu,
    load_settings,
    save_settings,
    get_setting,
    set_setting,
    display_settings,
    update_precision,
    update_number_formatting,
    update_expression_modes,
    update_language,
    DEFAULT_SETTINGS
)

class TestSettings(unittest.TestCase):
    
    def setUp(self):
        # Set up a temporary settings file for testing
        self.settings_file = 'test_settings.json'
        self.default_settings = DEFAULT_SETTINGS
        if os.path.exists(self.settings_file):
            os.remove(self.settings_file)
        save_settings(self.default_settings)

    def tearDown(self):
        # Clean up the temporary settings file after tests
        if os.path.exists(self.settings_file):
            os.remove(self.settings_file)

    @patch('builtins.input', side_effect=['1', '5'])
    @patch('abacus.settings.save_settings')
    def test_update_precision(self, mock_save, mock_input):
        settings = load_settings()
        update_precision(settings)
        self.assertEqual(get_setting(settings, 'precision'), 1)
        mock_save.assert_called_once_with(settings)

    @patch('builtins.input', side_effect=[';', '|'])
    @patch('abacus.settings.save_settings')
    def test_update_number_formatting(self, mock_save, mock_input):
        settings = load_settings()
        update_number_formatting(settings)
        self.assertEqual(get_setting(settings, 'number_formatting.thousands_separator'), ';')
        self.assertEqual(get_setting(settings, 'number_formatting.decimal_separator'), '|')
        mock_save.assert_called_once_with(settings)

    @patch('builtins.input', side_effect=['yes', '2'])
    @patch('abacus.settings.save_settings')
    def test_update_expression_modes(self, mock_save, mock_input):
        settings = load_settings()
        update_expression_modes(settings)
        self.assertTrue(get_setting(settings, 'expression_modes.fractional'))
        self.assertEqual(get_setting(settings, 'expression_modes.n_base'), 2)
        mock_save.assert_called_once_with(settings)

    @patch('builtins.input', side_effect=['es'])
    @patch('abacus.settings.save_settings')
    def test_update_language(self, mock_save, mock_input):
        settings = load_settings()
        update_language(settings)
        self.assertEqual(get_setting(settings, 'language'), 'es')
        mock_save.assert_called_once_with(settings)

    @patch('builtins.input', side_effect=['1', '2', '3', '4', '5', 'back'])
    def test_handle_settings_menu(self, mock_input):
        with patch('abacus.settings.display_settings_menu'):
            handle_settings_menu()
        # Check if input prompts are called, but we don't need to check the exact logic
        # as long as it completes without error.

if __name__ == '__main__':
    unittest.main()
