import unittest
from palindrom import is_palindrom

class MyTestCase(unittest.TestCase):

    def test_regular(self):
        self.assertTrue(is_palindrom('123321'))

    def test_symbols(self):
        self.assertTrue(is_palindrom('geeg'))

    def test_not_palindrom(self):
        self.assertFalse(is_palindrom('abc'))

    def test_empty_string(self):
        self.assertTrue(is_palindrom(''))

    def test_one_symbol(self):
        self.assertTrue(is_palindrom('a'))

if __name__ == '__main__':
    unittest.main()
