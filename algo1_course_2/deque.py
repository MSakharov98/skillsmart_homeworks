class Deque:
    def __init__(self):
        self.deque = []

    def addFront(self, item):
        self.deque.insert(0, item)

    def addTail(self, item):
        self.deque.append(item)

    def removeFront(self):
        if self.size() != 0:
            x = self.deque[0]
            self.deque.remove(self.deque[0])
            return x
        return None

    def removeTail(self):
        if self.size() != 0:
            x = self.deque[-1]
            self.deque.pop()
            return x
        return None

    def size(self):
        return len(self.deque)