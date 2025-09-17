import unittest
from balance_of_parenthesis import generate_balanced_parentheses

class MyTestCase(unittest.TestCase):

    def test_regular(self):
        self.assertEqual(generate_balanced_parentheses(3), \
                         ['((()))', '(()())', '(())()', '()(())', '()()()'])

    def test_study1(self):
        self.assertEqual(generate_balanced_parentheses(1), ['()'])

    def test_study2(self):
        self.assertEqual(generate_balanced_parentheses(2), ['(())', '()()'])


if __name__ == '__main__':
    unittest.main()
