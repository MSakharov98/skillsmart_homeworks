class ksort:

    def __init__(self):
        self.items = [None] * 1000

    def check(self, s):
        if len(s) == 3 and s[0] in 'abcdefgh' and \
                s[1].isnumeric() and s[2].isnumeric():
            return True
        return False

    def index(self, s):
        if self.check(s):
            return (ord(s[0]) * 100 + int(s[1]) * 10 + int(s[2])) - 9700
        return -1

    def add(self, s):
        if self.check(s):
            i = self.index(s)
            while i >= len(self.items):
                self.items.append(None)
            self.items[i] = s
            return True
        return False
