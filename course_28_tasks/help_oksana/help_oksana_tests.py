import unittest
from help_oksana import SumOfThe

class TestSumOfThe(unittest.TestCase):
    def test_sum_of_the(self):
        self.assertEqual(SumOfThe(10, [2, 5, 10, 20, -7, -5, 6, -2, 3, 8]), 20)
        self.assertEqual(SumOfThe(7, [100, -50, 10, -25, 90, -35, 90]), 90)
        self.assertEqual(SumOfThe(5, [5, -25, 10, -35, -45]), -45)
        self.assertEqual(SumOfThe(4, [10, -25, -45, -35]), None)
        self.assertEqual(SumOfThe(6, [1, 1, 1, 1, 1, 5]), 5)
        self.assertEqual(SumOfThe(3, [10, 20, 30]), 30)
        self.assertIsNone(SumOfThe(5, [1, 2, 3, 4, 5]))
        self.assertIsNone(SumOfThe(2, [5, 10]))

if __name__ == '__main__':
    unittest.main()
