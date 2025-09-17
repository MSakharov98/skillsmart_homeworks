import unittest
from riding_bike import odometer

class OdometerTestCase(unittest.TestCase):
    def test_odometer(self):
        # Тестирование обычного случая
        distance = odometer([10, 1, 20, 2])
        self.assertEqual(distance, 30)

        # Тестирование случая с нулевой дистанцией
        distance = odometer([0, 2, 0, 3, 0, 1])
        self.assertEqual(distance, 0)

        # Тестирование случая с изменением скорости
        distance = odometer([10, 1, 20, 2, 15, 0.5])
        self.assertEqual(distance, 7.5)

        # Тестирование случая с большим количеством промежутков времени
        distance = odometer([10, 1, 5, 0.5, 15, 2, 8, 0.75, 12, 1.25])
        self.assertEqual(distance, 26.0)  # Исправленное значение


if __name__ == '__main__':
    unittest.main()
