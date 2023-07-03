import unittest
from mr_robot import MisterRobot

class MyTestCase(unittest.TestCase):
    def test_study_case1(self):
        self.assertTrue(MisterRobot(7, [1, 3, 4, 5, 6, 2, 7]))

    def test_case_25_numbers(self):
        self.assertTrue(MisterRobot(25, [17, 3, 22, 9, 12, 4, 20, 7, 18, 5, 10, 25, 8, 16, 21, 14, 23, 1, 19, 13, 2, 6, 15, 24, 11]))




if __name__ == '__main__':
    unittest.main()
