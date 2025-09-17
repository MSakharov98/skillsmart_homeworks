import unittest
from sum_of_numbers import sum_of_numbers

class MyTestCase(unittest.TestCase):
    def test_regular(self):
        self.assertEqual(sum_of_numbers(123), 6)

    def test_zero(self):
        self.assertEqual(sum_of_numbers(0), 0)

    def test_negative(self):
        self.assertEqual(sum_of_numbers(-123), 6)

    def test_big_number(self):
        self.assertEqual(sum_of_numbers(93835793589), 69)


if __name__ == '__main__':
    unittest.main()
