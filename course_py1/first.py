# Эмулируем перевод из десятичной системы в двоичную
def decimal_to_binary(number):
    binary = ""
    while number > 0:
        binary = str(number % 2) + binary
        number = number // 2
    return binary

decimal_number = 42
binary_number = decimal_to_binary(decimal_number)
print(binary_number)