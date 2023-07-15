import unittest
from imperative_second_max import find_second_max

class MyTestCase(unittest.TestCase):
    def test_regular_case(self):
        self.assertEqual(find_second_max([1, 2, 3, 4, 5]), 4)

    def test_with_duplicates(self):
        self.assertEqual(find_second_max([1, 2, 3, 4, 5, 5]), 5)

    def test_empty_array(self):
        self.assertEqual(find_second_max([]), [])


if __name__ == '__main__':
    unittest.main()
