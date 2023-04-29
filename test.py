import unittest
from answer import knapsack

class KnapsackTest(unittest.TestCase):
    def test_find_optimal_items(self):
        # Test with given input
        self.assertEqual(knapsack('items.txt'), (['DogFood', 'Textbook'], 55))
        
    def test_empty_file(self):
        # Test with an empty file
        self.assertEqual(knapsack('empty.txt'), ([], 0))

    def test_zero_capacity(self):
        # Test with zero capacity
        self.assertEqual(knapsack('zero_capacity.txt'), ([], 0))

    def test_zero_items(self):
        # Test with zero items
        self.assertEqual(knapsack('zero_items.txt'), ([], 0))

    def test_single_item(self):
        # Test with a single item
        self.assertEqual(knapsack('single_item.txt'), (['Textbook'], 50))

    def test_all_items_selected(self):
        # Test where all items can be selected
        self.assertEqual(knapsack('all_items.txt'), (['Textbook', 'HardDrive', 'DogFood', 'FavoriteGame', 'SuperComputer'], 217))

    def test_mix_items(self):
        # Test with mixed items
        self.assertEqual(knapsack('mix_items.txt'), (['DogFood', 'FavoriteGame'], 65))

    def test_small_and_big_items(self):
        # Test with a mix of small and big items
        self.assertEqual(knapsack('small_and_big_items.txt'), (['Textbook', 'SuperComputer'], 150))

    def test_items_with_small_differences(self):
        # Test with items having small differences
        self.assertEqual(knapsack('small_differences.txt'), (['Textbook', 'HardDrive', 'DogFood', 'FavoriteGame'], 117))

    def test_items_with_large_differences(self):
        # Test with items having large differences
        self.assertEqual(knapsack('large_differences.txt'), (['Textbook', 'FavoriteGame', 'SuperComputer'], 210))

    def test_different_weights(self):
        # Test with different weights
        self.assertEqual(knapsack('different_weights.txt'), (['DogFood', 'FavoriteGame', 'SuperComputer'], 165))

    def test_same_weight_items(self):
        # Test with items having same weight
        self.assertEqual(knapsack('same_weight_items.txt'), (['Textbook', 'FavoriteGame'], 110))

if __name__ == '__main__':
    unittest.main()
