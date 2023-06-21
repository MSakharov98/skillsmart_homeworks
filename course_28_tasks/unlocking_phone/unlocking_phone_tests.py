import unittest
from unlocking_phone import PatternUnlock
def test_PatternUnlock():
    # Тест 1: Проверка для примера из условия задачи
    N = 10
    hits = [1, 2, 3, 4, 5, 6, 2, 7, 8, 9]
    assert PatternUnlock(N, hits) == '982843'

    # Тест 2: Проверка для случая с одним шагом
    N = 2
    hits = [3, 5]
    assert PatternUnlock(N, hits) == '2'

    # Тест 3: Проверка для случая с переходом на диагональные точки
    N = 3
    hits = [1, 5, 9]
    assert PatternUnlock(N, hits) == '314'

    # Тест 4: Проверка для случая с длиной кода разблокировки равной 1
    N = 1
    hits = [4]
    assert PatternUnlock(N, hits) == '0'

    # Тест 5: Проверка для случая с кодом разблокировки [2, 1, 9]
    N = 3
    hits = [2, 1, 9]
    assert PatternUnlock(N, hits) == '2'

    print("Все тесты пройдены успешно.")


# Запуск unit-тестов
test_PatternUnlock()

