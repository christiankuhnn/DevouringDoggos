import unittest
from answer import knapsack

class KnapsackTest(unittest.TestCase):
    def test_find_optimal_items(self):
        # Test with given input
        self.assertEqual(knapsack('items.txt'), (['DogFood', 'Textbook'], 55))

if __name__ == '__main__':
    unittest.main()
