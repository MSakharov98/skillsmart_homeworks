import unittest
from digital_rain import digital_rain

class MyTestCase(unittest.TestCase):

    def test_study_case1(self):
        self.assertEqual(digital_rain("1111000"), "111000")

    def test_study_case2(self):
        self.assertEqual(digital_rain("11101000"), "11101000")

    def test_study_case3(self):
        self.assertEqual(digital_rain("011111110"), "10")

    def test_study_empty(self):
        self.assertEqual(digital_rain("11111111"), "")


if __name__ == '__main__':
    unittest.main()
