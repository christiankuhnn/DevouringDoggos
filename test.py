import unittest

class TestKnapsack(unittest.TestCase):

    def test_knapsack(self):
        items = [('Textbook', 4, 50), ('HardDrive', 10, 2), ('DogFood', 10, 5), 
                 ('FavoriteGame', 20, 60), ('SuperComputer', 100, 100)]
        capacity = 15
        expected_output = ['DogFood', 'Textbook', '55']

        # Test the function with the sample input
        self.assertEqual(knapsack(items, capacity), expected_output)

        # Test the function with an empty list of items
        self.assertEqual(knapsack([], 10), [])

        # Test the function with a capacity of 0
        self.assertEqual(knapsack(items, 0), [0])

        # Test the function with a list of items with only one element
        self.assertEqual(knapsack([('Item1', 5, 10)], 10), ['Item1', 10])

if __name__ == '__main__':
    unittest.main()
