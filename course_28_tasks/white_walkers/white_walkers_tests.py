import unittest
from white_walkers import make_digit_indexes
from white_walkers import count_white_walkers
from white_walkers import white_walkers

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertTrue(white_walkers("axxb6===4xaf5===eee5"))
        self.assertTrue(white_walkers("abc=7==hdjs=3gg1=======5"))
        self.assertTrue(white_walkers("9===1===9===1===9"))
        self.assertFalse(white_walkers("5==ooooooo=5=5"))
        self.assertFalse(white_walkers("aaS=8"))


if __name__ == '__main__':
    unittest.main()
