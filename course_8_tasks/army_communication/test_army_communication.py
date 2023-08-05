import unittest
from army_communication import army_communication_matrix

class MyTestCase(unittest.TestCase):

    def test_study1(self):
        self.assertEqual(army_communication_matrix(3,
                                                   [
                                                       [1, 2, 3],
                                                       [4, 5, 6],
                                                       [7, 8, 9]
                                                   ]
                                                   ), '1 1 2')

    def test_study2(self):
        self.assertEqual(army_communication_matrix(4,
                                                   [
                                                       [1, 9, 2, 3],
                                                       [4, 8, 5, 6],
                                                       [0, 7, 1, 2],
                                                       [0, 0, 0, 0]
                                                   ]
                                                   ), '1 0 3')



if __name__ == '__main__':
    unittest.main()
