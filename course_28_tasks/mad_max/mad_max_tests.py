import unittest
from mad_max import MadMax

class MadMaxTests(unittest.TestCase):
    def test_MadMax(self):
        # Тест 1
        N = 7
        Tele = [1, 2, 3, 4, 5, 6, 7]
        expected = [1, 2, 3, 7, 6, 5, 4]
        self.assertEqual(MadMax(N, Tele), expected)

        # Тест 2
        N = 5
        Tele = [9, 3, 7, 1, 5]
        expected = [1, 3, 9, 5, 7]
        self.assertEqual(MadMax(N, Tele), expected)

        # Тест 3
        N = 9
        Tele = [5, 2, 8, 4, 9, 1, 6, 3, 7]
        expected = [1, 2, 3, 9, 8, 7, 6, 5, 4]
        self.assertEqual(MadMax(N, Tele), expected)

        # Тест 4 (минимальный размер массива)
        N = 1
        Tele = [0]
        expected = [0]
        self.assertEqual(MadMax(N, Tele), expected)

        # Тест 5 (максимальный размер массива)
        N = 127
        Tele = [i for i in range(N)]
        expected = [i for i in range(N)]
        self.assertEqual(MadMax(N, Tele), expected)


if __name__ == '__main__':
    unittest.main()
