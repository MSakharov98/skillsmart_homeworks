
# Эмулируем перевод из десятичной системы в двоичную
def decimal_to_binary(number):
    binary = ""
    while number > 0:
        binary = str(number % 2) + binary
        number = number // 2
    return binary

# decimal_number = 42
# binary_number = decimal_to_binary(decimal_number)
# print(binary_number)

# Рисуем окружность по двум точкам и радиусу
def draw_circle(point1, point2, radius):
    # Вычисляем координаты центра окружности
    center_x = (point1[0] + point2[0]) / 2
    center_y = (point1[1] + point2[1]) / 2

    # Визуализируем центр окружности
    print(f"Центр окружности: ({center_x}, {center_y})")

    # Визуализируем радиус окружности
    print(f"Радиус окружности: {radius}")

# Пример использования
# point1 = (2, 3)
# point2 = (5, 7)
# radius = 4

# draw_circle(point1, point2, radius)

# Напишем функцию set() с точки зрения ООП

class CustomSet:
    def __init__(self, sequence):
        self._sequence = sequence
    def unique_values(self):
        resulting_sequence = []
        for element in self._sequence:
            if element in resulting_sequence:
                continue
            else:
                resulting_sequence.append(element)
        return  resulting_sequence

test_sequence = CustomSet([1, 3, 5, 7, 4, 5, 1, 2, 2])
# print(test_sequence.unique_values())

# Реализуем методы строк

class StringMethod:
    def lower(self, string):
        lower_string = ''
        for char in string:
            if 'A' <= char <= 'Z':  # проверка для английского алфавита
                lower_char = chr(ord(char) + 32)
            elif 'А' <= char <= 'Я':  # проверка для русского алфавита
                lower_char = chr(ord(char) + 32)
            else:
                lower_char = char

            if char == 'Ё' or char == 'Ё':  # проверка для символа 'ё'
                lower_char = chr(ord(char) - 80)

            lower_string += lower_char
        return lower_string

    def upper(self, string):
        upper_string = ''
        for char in string:
            if 'a' <= char <= 'z':
                upper_char = chr(ord(char) - 32)
            elif 'а' <= char <= 'я':
                upper_char = chr(ord(char) - 32)
            else:
                upper_char = char

            if char == 'ё' or char == 'Ё':  # проверка для символа 'ё'
                upper_char = chr(ord(char) + 80)

            upper_string += upper_char

        return upper_string

    def capitalize(self, string):
        return string[0].upper() + string[1::].lower()


# s = StringMethod()
# print(s.upper('РУССкий алфавит & England alFAbet'))
# print(s.lower('АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЭЬЭЮЯ'))
# print(s.capitalize('ABCDEFGOIJKLMNOPQRSTXZW'))

# Реализуем метод строки str.center(int)
#   center(self, width, fillchar=' ', /)
#  |      Return a centered string of length width.
#  |
#  |      Padding is done using the specified fill character (default is a space).

class CenteredString:

    def center(self, string, width, fillchar = ' '):
        if width <= len(string):
            return string

        left_padding = (width - len(string)) // 2
        right_padding = width - len(string) - left_padding

        result = (left_padding * fillchar) + string + (right_padding * fillchar)
        return result

# s = CenteredString()
# s1 = 'ABC'
# print(s.center('ABC', 2, '*'))
# print(s.center('ABC', 10, '*'))
# print(s1.center(10, '*'))

# Реализуем метод строки .isdigit()
'''
isdigit(self, /)
    Return True if the string is a digit string, False otherwise.
    
    A string is a digit string if all characters in the string are digits and there
    is at least one character in the string.
'''
class IsDigit:

    def isdigit(self, string):

        if not string:
            return 'Строка пуста'

        counter = 0

        for char in string:
            if 48 <= ord(char) <= 57:
                counter += 1

        return counter == len(string)

# s = IsDigit()
# print(s.isdigit(''))
# print(s.isdigit('1998'))
# print(s.isdigit('9979'))
# print(s.isdigit('Nfv nhb 334 hjerhio'))
# print(s.isdigit('deer3k4'))

# Реализуем метод строки .split()

class Split:

    def split(self, string, delimiter=None):

        if delimiter is None:
            delimiter = ' '

        result = []
        current_word = ''

        for char in string:
            if char == delimiter:
                if current_word:
                    result.append(current_word)
                    current_word = ''
            else:
                current_word += char

        if current_word:
            result.append(current_word)

        return result

# s = Split()
# string = 'Пример строки для разделения'
# string2 = 'Еще*один*пример*строки'
# print(s.split(string))
# print(s.split(string2, '*'))


def is_happy_ticket(number):
    first_half = number[:len(number) // 2]
    second_half = number[len(number) // 2:]

    counter1 = 0
    counter2 = 0

    for char in first_half:
        counter1 += int(char)

    for char in second_half:
        counter2 += int(char)

    return counter1 == counter2

# print(is_happy_ticket('053044'))

def is_perfect(number):
    if number <= 0:
        return False

    counter = 0

    for i in range(1, number):
        if (number % i) == 0:
            counter += i

    return counter == number

print(is_perfect(6))












