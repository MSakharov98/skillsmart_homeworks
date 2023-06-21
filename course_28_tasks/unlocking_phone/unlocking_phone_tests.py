import unittest
from unlocking_phone import PatternUnlock


class PatternUnlockTests(unittest.TestCase):
    def test_example_input(self):
        hits = [6, 9, 8, 5, 1, 0, 4, 7, 2, 3]
        result = PatternUnlock(10, hits)
        self.assertEqual(result, "1189947")

    def test_zero_distance(self):
        hits = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
        result = PatternUnlock(11, hits)
        self.assertEqual(result, "10")

    def test_horizontal_vertical_distance(self):
        hits = [1, 2, 3, 2, 1, 2]
        result = PatternUnlock(6, hits)
        self.assertEqual(result, "707105")

    def test_diagonal_distance(self):
        hits = [5, 2, 7, 8, 4]
        result = PatternUnlock(5, hits)
        self.assertEqual(result, "524263")

    def test_rounding(self):
        hits = [2, 2, 2, 2]
        result = PatternUnlock(4, hits)
        self.assertEqual(result, "3")


if __name__ == '__main__':
    unittest.main()
