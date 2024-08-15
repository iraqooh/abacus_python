import unittest
import os
from abacus.history import display_history

class TestHistory(unittest.TestCase):
    def setUp(self):
        # Set up a temporary history file
        self.history_file = 'data/history.txt'
        with open(self.history_file, 'w') as file:
            file.write("Test History Entry\n")

    def tearDown(self):
        # Clean up the history file
        if os.path.exists(self.history_file):
            os.remove(self.history_file)

    def test_display_history(self):
        # Test the history display function
        self.assertIsNone(display_history())

if __name__ == '__main__':
    unittest.main()
