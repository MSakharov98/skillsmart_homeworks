import unittest
from unlocking_phone import PatternUnlock

class TestPatternUnlock(unittest.TestCase):

    def test_example(self):
        self.assertEqual(PatternUnlock(10, [1, 2, 3, 4, 5, 6, 2, 7, 8, 9]), '1141421')

    def test_zeroes(self):
        self.assertEqual(PatternUnlock(2, [9, 1]), '41')

    def test_rounding(self):
        self.assertEqual(PatternUnlock(4, [1, 2, 5, 6]), '4242')

    def test_short(self):
        self.assertEqual(PatternUnlock(2, [2, 1]), '1')

    def test_diagonal(self):
        self.assertEqual(PatternUnlock(3, [2, 1, 9]), '2')

    def test_no_zeros(self):
        self.assertEqual(PatternUnlock(5, [9, 6, 3, 8, 7]), '5')

    def test_all(self):
        self.assertEqual(PatternUnlock(9, [9, 8, 7, 6, 5, 4, 3, 2, 1]), '83748374')


if __name__ == '__main__':
    unittest.main()
