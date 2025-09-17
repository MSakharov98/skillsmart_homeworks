import unittest
from even_indices import even_indices

class MyTestCase(unittest.TestCase):

    def test_regular(self):
        self.assertEqual(even_indices([1, 2, 3, 4, 5, 6]), [3, 5])

    def test_empty(self):
        self.assertEqual(even_indices([]), [])


if __name__ == '__main__':
    unittest.main()