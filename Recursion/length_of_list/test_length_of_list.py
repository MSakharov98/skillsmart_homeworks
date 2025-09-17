import unittest
from length_of_list import length_of_list

class MyTestCase(unittest.TestCase):
    def test_regular(self):
        self.assertEqual(length_of_list([1, 2, 3]), 3)

    def test_empty(self):
        self.assertEqual(length_of_list([]), 0)

if __name__ == '__main__':
    unittest.main()
