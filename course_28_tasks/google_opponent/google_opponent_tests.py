import unittest
from google_opponent import WordSearch

class MyTestCase(unittest.TestCase):
    def test_word_search_study_case_1(self):
        length = 3
        text = "12345"
        word = "123"
        expected = [1, 0]
        result = WordSearch(length, text, word)
        self.assertEqual(result, expected)

    def test_word_search_study_case_2(self):
        length = 12
        text = " строка разбивается на набор строк через выравнивание по заданной ширине."
        word = "строк"
        expected = [0, 0, 0, 1, 0, 0, 0]
        result = WordSearch(length, text, word)
        self.assertEqual(result, expected)

    def test_word_search_simple_case(self):
        length = 10
        text = "Это пример текста"
        word = "пример"
        expected = [1, 0]
        result = WordSearch(length, text, word)
        self.assertEqual(result, expected)

    def test_word_search_word_at_beginning_and_end(self):
        length = 10
        text = "слово находится в начале и в конце"
        word = "слово"
        expected = [1, 0, 0, 0]
        result = WordSearch(length, text, word)
        self.assertEqual(result, expected)

    def test_word_search_word_not_found(self):
        length = 8
        text = "Это текст без искомого слова"
        word = "слово"
        expected = [0, 0, 0, 0, 0]
        result = WordSearch(length, text, word)
        self.assertEqual(result, expected)

    def test_word_search_empty_string(self):
        length = 5
        text = ""
        word = "слово"
        expected = []
        result = WordSearch(length, text, word)
        self.assertEqual(result, expected)

    def test_word_search_wider_than_line(self):
        length = 5
        text = "это короткая строка"
        word = "строка"
        expected = [0, 0, 1]
        result = WordSearch(length, text, word)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
