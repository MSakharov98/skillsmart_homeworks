import unittest
from mission_impossible import TheRabbitFoot

class MyTestCase(unittest.TestCase):
        def test_encode(self):
            # Тестовая строка
            input_string = "Hello, world!"
            expected_output = "Horel ollewd!"

            # Вызов функции для шифрования
            encoded_string = TheRabbitFoot(input_string, encode=True)

            # Проверка результата
            self.assertEqual(encoded_string, expected_output)

        def test_decode(self):
            # Закодированная строка
            input_string = "Horel ollewd!"
            expected_output = "Hello, world!"

            # Вызов функции для дешифрования
            decoded_string = TheRabbitFoot(input_string, encode=False)

            # Проверка результата
            self.assertEqual(decoded_string, expected_output)

        def test_empty_string(self):
            # Пустая строка
            input_string = ""
            expected_output = ""

            # Вызов функции для шифрования
            encoded_string = TheRabbitFoot(input_string, encode=True)

            # Проверка результата
            self.assertEqual(encoded_string, expected_output)

            # Вызов функции для дешифрования
            decoded_string = TheRabbitFoot(input_string, encode=False)

            # Проверка результата
            self.assertEqual(decoded_string, expected_output)

        def test_no_spaces(self):
            # Строка без пробелов
            input_string = "Hello"
            expected_output = "Helo"

            # Вызов функции для шифрования
            encoded_string = TheRabbitFoot(input_string, encode=True)

            # Проверка результата
            self.assertEqual(encoded_string, expected_output)

            # Вызов функции для дешифрования
            decoded_string = TheRabbitFoot(input_string, encode=False)

            # Проверка результата
            self.assertEqual(decoded_string, expected_output)


if __name__ == '__main__':
    unittest.main()
