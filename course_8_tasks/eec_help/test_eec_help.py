import unittest
from eec_help import EEC_help

class MyTestCase(unittest.TestCase):

    def test_study1(self):
        self.assertFalse(EEC_help([1,2,3], [1,2,3,4]))

    def test_study2(self):
        self.assertTrue(EEC_help([1,2,3], [1,2,3]))

    def test_study3(self):
        self.assertTrue(EEC_help([1,3,2], [1,2,3]))

    def test_study4(self):
        self.assertFalse(EEC_help([1,3,2,3], [1,2,2,3]))

    def test_study5(self):
        self.assertTrue(EEC_help([1,1], [1,1]))





if __name__ == '__main__':
    unittest.main()
