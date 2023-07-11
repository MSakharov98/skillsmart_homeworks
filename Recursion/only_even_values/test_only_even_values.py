import unittest
from only_even_values import only_even_values

class MyTestCase(unittest.TestCase):

    def test_regular(self):
        self.assertEqual(only_even_values([1, 2, 3, 4, 5, 6]), [2, 4, 6])

    def test_empty(self):
        self.assertEqual(only_even_values([]), [])


if __name__ == '__main__':
    unittest.main()
