# Реализуем метод строки str.center(int)
#   center(self, width, fillchar=' ', /)
#  |      Return a centered string of length width.
#  |
#  |      Padding is done using the specified fill character (default is a space).

class CenteredString:

    def center(self, string, width, fillchar = ' '):

        if width <= len(string):
            assert len(string) != 0

            return string

        left_padding = (width - len(string)) // 2
        print(f'Left padding = {left_padding}')
        assert left_padding <= width

        right_padding = width - len(string) - left_padding
        print(f'Right padding = {right_padding}')
        assert right_padding <= width

        result = (left_padding * fillchar) + string + (right_padding * fillchar)
        assert result != 0

        return result

s = CenteredString()
s1 = 'ABC'
print(s.center('ABC', 2, '*'))
print(s.center('ABC', 10, '*'))
print(s1.center(10, '*'))