class Stack:
    def __init__(self):
        self.stack = []

    def size(self):
        return len(self.stack)

    def pop(self):
        if self.size() != 0:
            x = self.stack[-1]
            self.stack.pop()
            return x
        return None

    def push(self, value):
        self.stack.append(value)

    def peek(self):
        if self.size() != 0:
            return self.stack[-1]
        return None