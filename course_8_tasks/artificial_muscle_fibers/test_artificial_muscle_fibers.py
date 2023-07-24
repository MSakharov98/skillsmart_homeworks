import unittest
from artificial_muscle_fibers import artificial_muscle_fibers

class MyTestCase(unittest.TestCase):

    def test_study1(self):
        self.assertEqual(artificial_muscle_fibers([1, 2, 3, 4, 5]), 0)

    def test_study2(self):
        self.assertEqual(artificial_muscle_fibers([1, 2, 3, 2, 1]), 2)

    def test_study3(self):
        self.assertEqual(artificial_muscle_fibers([1, 2, 3, 2, 1, 2, 4, 2, 1]), 2)

if __name__ == '__main__':
    unittest.main()
