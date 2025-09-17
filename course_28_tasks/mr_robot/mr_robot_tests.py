import unittest
from mr_robot import MisterRobot

class MyTestCase(unittest.TestCase):
    def test_study_case1(self):
        self.assertTrue(MisterRobot(7, [1, 3, 4, 5, 6, 2, 7]))

    def test_study_case2(self):
        self.assertFalse(MisterRobot(7,[1, 4, 3, 5, 7, 6, 2]))




if __name__ == '__main__':
    unittest.main()
