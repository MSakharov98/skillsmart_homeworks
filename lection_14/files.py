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
