import unittest
from power import power

class MyTestCase(unittest.TestCase):

    def test_regular(self):
        self.assertEqual(power(5, 3), 125)

    def test_negative(self):
        self.assertEqual(power(4, -2), 1/16)

    def test_zero(self):
        self.assertEqual(power(5, 0), 1)

    def test_big_number(self):
        self.assertEqual(power(34, 12), 34 ** 12)


if __name__ == '__main__':
    unittest.main()
