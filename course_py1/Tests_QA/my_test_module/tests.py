import unittest
from bubble_sort import bubble_sort

# Напишем тесты

class BubblesortTestCase(unittest.TestCase):

    # Тестируем на случайном массиве
    def test_random_array(self):
        test_array = [4, 2, 9, 1, 6]
        expected_result = [1, 2, 4, 6, 9]
        sorted_array = bubble_sort(test_array)
        self.assertEqual(sorted_array,expected_result)

    # Тестируем на равенство с отсортированным массивом
    def test_sorted_array(self):
        test_array = [1, 2, 4, 6, 9]
        expected_result = [1, 2, 4, 6, 9]
        sorted_array = bubble_sort(test_array)
        self.assertEqual(sorted_array,expected_result)

    # Проверяем на равенство с перевернутым массивом
    def test_reversed_array(self):
        test_array = [9, 6, 4, 2, 1]
        expected_result = [1, 2, 4, 6, 9]
        sorted_array = bubble_sort(test_array)
        self.assertEqual(sorted_array, expected_result)

    # Тестируем на пустой массив
    def test_empty_array(self):
        test_array = []
        expected_result = []
        sorted_array = bubble_sort(test_array)
        self.assertEqual(sorted_array, expected_result)

    if __name__ == '__main__':
        unittest.main()







