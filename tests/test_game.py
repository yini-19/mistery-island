import unittest
from game_logic.game import is_even

class TestEvenness(unittest.TestCase):
    def test_is_even_is_true(self):
        self.assertTrue(is_even(6))
        self.assertEqual(is_even(6), True)
        
    def test_is_even_is_false(self):
        self.assertFalse(is_even(5))
        self.assertEqual(is_even(5), False)
