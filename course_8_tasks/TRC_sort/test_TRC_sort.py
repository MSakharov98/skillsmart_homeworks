import unittest
from TRC_sort import TRC_sort

class MyTestCase(unittest.TestCase):

    def test_study1(self):
        self.assertEqual(TRC_sort([2, 1, 0]), [0, 1, 2])

    def test_study2(self):
        self.assertEqual(TRC_sort([0, 1, 2, 1, 0, 2]), [0, 0, 1, 1, 2, 2])


if __name__ == '__main__':
    unittest.main()
