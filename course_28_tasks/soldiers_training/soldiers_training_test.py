import unittest
from soldiers_training import ConquestCampaign

class ConquestTest(unittest.TestCase):
    def test_case1(self):
        N = 3
        M = 4
        L = 2
        battalion = [2, 2, 3, 4]
        self.assertEqual(ConquestCampaign(N, M, L, battalion), 4)

    def test_case2(self):
        N = 5
        M = 5
        L = 5
        battalion = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
        self.assertEqual(ConquestCampaign(N, M, L, battalion), 2)

    def test_case3(self):
        N = 4
        M = 4
        L = 6
        battalion = [1, 1, 2, 2, 2, 3, 3, 2, 4, 3, 4, 4]
        self.assertEqual(ConquestCampaign(N, M, L, battalion), 2)

    def test_case4(self):
        N = 2
        M = 3
        L = 0
        battalion = []
        self.assertEqual(ConquestCampaign(N, M, L, battalion), 1)

    def test_case5(self):
        N = 10
        M = 10
        L = 20
        battalion = [1, 1, 2, 1, 3, 1, 4, 1, 5, 1, 6, 1, 7, 1, 8, 1, 9, 1, 10, 1,
                     10, 2, 9, 2, 8, 2, 7, 2, 6, 2, 5, 2, 4, 2, 3, 2, 2, 2, 1, 2]
        self.assertEqual(ConquestCampaign(N, M, L, battalion), 10)

if __name__ == '__main__':
    unittest.main()
