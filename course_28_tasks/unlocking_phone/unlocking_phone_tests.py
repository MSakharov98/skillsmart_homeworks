import unittest
from unlocking_phone import PatternUnlock
class PatternUnlockTests(unittest.TestCase):

    def test_example(self):
        hits = [1, 2, 3, 4, 5, 6, 2, 7, 8, 9]
        result = PatternUnlock(10, hits)
        self.assertEqual(result, '115365')

    def test_no_zeros(self):
        hits = [9, 6, 3, 8, 7]
        result = PatternUnlock(5, hits)
        self.assertEqual(result, '52367')

    def test_diagonal(self):
        hits = [2, 1, 9]
        result = PatternUnlock(3, hits)
        self.assertEqual(result, '2')

    def test_zeroes(self):
        hits = [9, 1]
        result = PatternUnlock(2, hits)
        self.assertEqual(result, '41')

    def test_rounding(self):
        hits = [1, 2, 5, 6]
        result = PatternUnlock(4, hits)
        self.assertEqual(result, '4242')

    def test_all(self):
        hits = [9, 8, 7, 6, 5, 4, 3, 2, 1]
        result = PatternUnlock(9, hits)
        self.assertEqual(result, '83748374')

if __name__ == '__main__':
    unittest.main()
