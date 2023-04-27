from io import StringIO
import sys
import unittest
from answer import knapsack

class TestKnapsack(unittest.TestCase):
    def test_knapsack(self):
        input_str = '5\n15\nTextbook 4 50\nHardDrive 10 2\nDogFood 10 5\nFavoriteGame 20 60\nSuperComputer 100 100\n'
        expected_output_str = 'Textbook\nDogFood\n55\n'

        # Redirect standard input and output to StringIO objects
        sys.stdin = StringIO(input_str)
        sys.stdout = output_str = StringIO()

        # Call the knapsack function
        knapsack()

        # Get the actual output from the StringIO object
        actual_output_str = output_str.getvalue()

        # Restore standard input and output
        sys.stdin = sys.__stdin__
        sys.stdout = sys.__stdout__

        # Compare the actual output with the expected output
        self.assertEqual(actual_output_str, expected_output_str)
