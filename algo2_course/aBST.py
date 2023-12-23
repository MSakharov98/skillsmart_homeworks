class aBST:

    def __init__(self, depth):
        tree_size = (2 ** (depth + 1)) - 1
        self.Tree = [None] * tree_size

    def FindKeyIndex(self, key):
        currentIndex = 0
        if len(self.Tree) == 1: return 0
        while True:
            if currentIndex >= len(self.Tree):
                return None
            currentNodeKey = self.Tree[currentIndex]
            if currentNodeKey is None:
                return -currentIndex

            if currentNodeKey == key:
                return currentIndex
            if key < currentNodeKey:
                currentIndex = (2 * currentIndex + 1)
                continue
            if currentNodeKey < key:
                currentIndex = (2 * currentIndex + 2)
                continue

    def AddKey(self, key):
        index = self.FindKeyIndex(key)
        if index is None:
            return -1
        if index == 0 and len(self.Tree) >= 1 and self.Tree[0] is None:
            self.Tree[0] = key
            return 0
        if index >= 0:
            return index
        if index < 0:
            insertionPos = -index
            self.Tree[insertionPos] = key
            return insertionPos