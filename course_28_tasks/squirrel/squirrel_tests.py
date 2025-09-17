import unittest
from squirrel import squirrel

class SquirrelTestCase(unittest.TestCase):
    def test_squirrel(self):
        self.assertEqual(squirrel(0), 1)   # Факториал 0 равен 1, первая цифра - 1
        self.assertEqual(squirrel(1), 1)   # Факториал 1 равен 1, первая цифра - 1
        self.assertEqual(squirrel(5), 1)   # Факториал 5 равен 120, первая цифра - 1
        self.assertEqual(squirrel(10), 3)  # Факториал 10 равен 3628800, первая цифра - 3
        self.assertEqual(squirrel(15), 1)  # Факториал 15 равен 1307674368000, первая цифра - 1

if __name__ == '__main__':
    unittest.main()
