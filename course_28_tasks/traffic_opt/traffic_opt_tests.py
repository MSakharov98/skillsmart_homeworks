import unittest
from traffic_opt import Unmanned

class MyTestCase(unittest.TestCase):
    def test_study_case1(self):
        self.assertEqual(Unmanned(10, 2, [[3,5,5], [5,2,2]]), 12)

    def test_study_case2(self):
        self.assertEqual(Unmanned(10, 2, [[11, 5, 5], [15, 2, 2]]), 10)

    def test_case(self):
        self.assertEqual(Unmanned(15, 3, [[8,3,4], [12,2,2], [18,3,4]]), 17)



if __name__ == '__main__':
    unittest.main()
