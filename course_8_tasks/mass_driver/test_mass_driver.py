import unittest
from mass_driver import massdriver

class MyTestCase(unittest.TestCase):

    def test_study1(self):
        self.assertEqual(massdriver([1, 2, 3, 1, 2, 3, 4]), 0)

    def test_study2(self):
        self.assertEqual(massdriver([1, 2, 3, 4, 3, 4, 2]), 1)

    def test_study3(self):
        self.assertEqual(massdriver([1, 2, 3, 4, 5, 6, 7]), -1)

if __name__ == '__main__':
    unittest.main()
