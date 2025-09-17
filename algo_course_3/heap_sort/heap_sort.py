
class HeapSort:

    def __init__(self, array):
        self.HeapObject = Heap()
        self.HeapObject.MakeHeap(array, self.DepthCalc(array))

    def DepthCalc(self, array, i=0):
        depth = 2 ** (i + 1) - 1
        if len(array) > depth:
            return self.DepthCalc(array, i + 1)
        return depth

    def GetNextMax(self):
        return self.HeapObject.GetMax()


class Heap:

    def __init__(self):
        self.HeapArray = []
        self.count = 0

    def Swap(self, i, j):
        self.HeapArray[i], self.HeapArray[j] = \
            self.HeapArray[j], self.HeapArray[i]

    def SiftDown(self, i, array):
        left = 2 * i + 1
        right = 2 * i + 2
        largest = i
        size = len(array)
        if left < size and array[left] != None:
            if array[left] > array[largest]:
                largest = left
        if right < size and array[right] != None:
            if array[right] > array[largest]:
                largest = right
        if largest != i:
            self.Swap(largest, i)
            return self.SiftDown(largest, array)

    def SiftUp(self, i, array):
        while i > 0 and (array[(i - 1) // 2] is None or \
                         array[i] > array[(i - 1) // 2]):
            self.Swap((i - 1) // 2, i)
            i = (i - 1) // 2

    def GetLast(self, isNone):
        i = len(self.HeapArray) - 1
        while i >= 0:
            if isNone and self.HeapArray[i] is None:
                return i
            elif not isNone and self.HeapArray[i] is not None:
                return i
            i -= 1

    def MakeHeap(self, array, depth):
        if len(array) <= (2 ** (depth + 1) - 1):
            self.HeapArray = array[:]
            self.count = len(array)
            for i in range(2 ** (depth + 1) - 1 - len(array)):
                self.HeapArray.append(None)
            for key in range(self.count - 1, -1, -1):
                self.SiftUp(key, self.HeapArray)

    def GetMax(self):
        if self.count:
            max_key = self.HeapArray[0]
            i = self.GetLast(False)
            self.HeapArray[0] = self.HeapArray[i]
            self.HeapArray[i] = None
            self.SiftDown(0, self.HeapArray)
            self.count -= 1
            return max_key
        return -1

    def Add(self, key):
        if self.count == len(self.HeapArray):
            return False
        i = self.GetLast(True)
        self.HeapArray[i] = key
        self.SiftUp(i, self.HeapArray)
        self.count += 1
        return True