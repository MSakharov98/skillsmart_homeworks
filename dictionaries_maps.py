# 1
import random

# Создаем пустой словарь и массив ключей
dictionary = {}
keys = []

# Добавляем 100 случайных пар в словарь и сохраняем ключи в массив
for _ in range(100):
    key = random.randint(1, 1000)
    value = random.choice(['строка1', 'строка2', 'строка3', 'строка4'])
    dictionary[key] = value
    keys.append(key)

# Выводим значения по ключам
for key in keys:
    print(f"Значение для ключа {key}: {dictionary[key]}")

# Удаляем все пары из словаря
dictionary.clear()

# 2
def find_repeated_values(numbers, repeats):
    count_dict = {}  # Словарь для подсчета повторений значений
    repeated_values = []  # Список для хранения повторяющихся значений

    # Подсчитываем количество повторений для каждого значения в списке
    for number in numbers:
        if number in count_dict:
            count_dict[number] += 1
        else:
            count_dict[number] = 1

    # Добавляем значения, которые повторяются не менее N раз, в список repeated_values
    for number, count in count_dict.items():
        if count >= repeats:
            repeated_values.append(number)

    return repeated_values

# Создаем список из 100 значений в диапазоне от 1 до 10
numbers = [random.randint(1, 10) for _ in range(100)]

# Вызываем функцию для списка numbers и числа repeats (например, repeats = 3)
repeats = 3
result = find_repeated_values(numbers, repeats)

# Выводим результат
print(f"Значения, повторяющиеся не менее {repeats} раз: {result}")
