class Heap:

    def __init__(self):
        self.HeapArray = []  # хранит неотрицательные числа-ключи
        self.size = 0

    def MakeHeap(self, a, depth):
        storageLen = 2 ** (depth + 1) - 1
        if storageLen < len(a): return None
        self.HeapArray = [None] * storageLen
        for item in a:
            self.Add(item)

        return self
        # создаём массив кучи HeapArray из заданного
        # размер массива выбираем на основе глубины depth

    def ReplaceMaxWithRightmostLeaf(self):
        lastElem = self.size - 1
        self.HeapArray[0] = self.HeapArray[lastElem]
        self.HeapArray[lastElem] = None
        self.size -= 1

    def GetMax(self):
        if self.size == 0:
            return -1
        max = self.HeapArray[0]
        self.ReplaceMaxWithRightmostLeaf()
        self.DownHeap(0)
        return max

    def Swap(self, index1, index2):
        tmp = self.HeapArray[index1]
        self.HeapArray[index1] = self.HeapArray[index2]
        self.HeapArray[index2] = tmp

    def UpHeap(self, itemIndex):
        currentItemIndex = itemIndex
        while (0 < currentItemIndex < self.size):
            parentIndex = self.GetParentIndex(currentItemIndex)
            if self.HeapArray[parentIndex] > self.HeapArray[currentItemIndex]:
                break
            self.Swap(parentIndex, currentItemIndex)
            currentItemIndex = parentIndex

    def MaxItemIndex(self, index1, index2):
        if index1 is None and index2 is None: return -1
        if index1 is None: return index2
        if index2 is None: return index1
        if self.HeapArray[index1] > self.HeapArray[index2]: return index1
        return index2

    def GetNextIndex(self, parentIndex, leftChildIndex, rightChildIndex):
        maxItemIndex = self.MaxItemIndex(leftChildIndex, rightChildIndex)
        if maxItemIndex == -1: return -1
        parent = self.HeapArray[parentIndex]
        maxItem = self.HeapArray[maxItemIndex]
        if parent > maxItem:
            return -1
        return maxItemIndex

    def DownHeap(self, itemIndex):
        currentIndex = itemIndex
        while 0 <= currentIndex < self.size:
            leftChildIndex = self.GetLeftChildIndex(currentIndex)
            rightChildIndex = self.GetRightChildIndex(currentIndex)
            indexMax = self.GetNextIndex(currentIndex, leftChildIndex, rightChildIndex)
            if indexMax == -1: break
            self.Swap(currentIndex, indexMax)
            currentIndex = indexMax

    def GetParentIndex(self, itemIndex):
        index = (itemIndex - 1) // 2
        return index if 0 <= index < self.size else None

    def GetLeftChildIndex(self, itemIndex):
        index = itemIndex * 2 + 1
        return index if index < self.size else None

    def GetRightChildIndex(self, itemIndex):
        index = itemIndex * 2 + 2
        return index if index < self.size else None

    def InsertKey(self, key):
        if self.size >= len(self.HeapArray): return None
        addedItemIndex = self.size
        self.HeapArray[addedItemIndex] = key
        self.size += 1
        return addedItemIndex

    def Add(self, key):
        addedItemIndex = self.InsertKey(key)
        if addedItemIndex is None: return False
        self.UpHeap(addedItemIndex)
        return True  # если куча заполнена