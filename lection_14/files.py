import random
# 3.1
# Импортировали модуль random для генерации случайных чисел  в строках файлов
# Создаем 10 файлов и записываем туда по строкам случайные числа, разделенные символом перевода строки

for i in range(1, 11):
    file_name = str(i) + '.txt'
    with open(file_name, 'w') as file:
        for _ in range(3):
            number = random.randint(1, 100)
            file.write(str(number) + '\n')

# 3.2
# Напишем функцию, которая принимает два случайных числа от 1 до 10 включительно и путь к файлам
# Она открывает файлы, считывает и возвращает сумму шести чисел из ранее записанных
# Если содержимое файлов неполное или поврежденное, функция вернет ошибку и сведения о ней

def calculate_sum(num1, num2, path):
    try:
        file_name1 = str(num1) + '.txt'
        file_name2 = str(num2) + '.txt'

        with open(path + file_name1, 'r') as file1, open(path + file_name2, 'r') as file2:
            numbers1 = [int(line.strip()) for line in file1]
            numbers2 = [int(line.strip()) for line in file2]

        if len(numbers1) != 3 or len(numbers2) != 3:
            return 'Ошибка: не хватает чисел для подсчета суммы'

        sum_of_numbers = sum(numbers1) + sum(numbers2)

        return sum_of_numbers

    except FileNotFoundError:
        return 'Ошибка. Файл не найден'

    except ValueError:
        return 'Ошибка. Содержимое файла испорчено'

