import unittest
from second_max import find_second_max


class MyTestCase(unittest.TestCase):

    def test_regular(self):
        self.assertEqual(find_second_max([1,2,3,4,5]), 4)

    def test_empty(self):
        self.assertEqual(find_second_max([]), None)

    def test_duplicates(self):
        self.assertEqual(find_second_max([1,2,3,5,4,5]), 5)


if __name__ == '__main__':
    unittest.main()
