import ctypes

class DynArray:

    def __init__(self):
        self.count = 0
        self.capacity = 16
        self.array = self.make_array(self.capacity)

    def __len__(self):
        return self.count

    def make_array(self, new_capacity):
        return (new_capacity * ctypes.py_object)()

    def __getitem__(self,i):
        if i < 0 or i >= self.count:
            raise IndexError('Index is out of bounds')
        return self.array[i]

    def resize(self, new_capacity):
        new_array = self.make_array(new_capacity)
        for i in range(self.count):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    def append(self, itm):
        if self.count == self.capacity:
            self.resize(2*self.capacity)
        self.array[self.count] = itm
        self.count += 1

    def insert(self, i, itm):
        if i > self.count or i < 0:
            raise IndexError('Index is out of bounds')
        elif i == self.count:
            self.append(itm)
        else:
            if self.count == self.capacity:
                self.resize(2*self.capacity)
            for j in range(self.count - 1, i - 1, -1):
                self.array[j+1] = self.array[j]
            self.array[i] = itm
            self.count += 1


    def delete(self, i):
        if i >= self.count or i < 0:
            raise IndexError('Index is out of bounds')
        else:
            for j in range(i, self.count - 1):
                self.array[j] = self.array[j+1]

            self.array[self.count - 1] = None
            self.count = self.count - 1
            if self.count <= self.capacity // 2 and self.count > 16:
                self.resize(int(self.capacity // 1.5))
            elif self.count <= 16:
                self.resize(16)