class HashTable:
    def __init__(self, sz, stp):
        self.size = sz
        self.step = stp
        self.slots = [None] * self.size

    def hash_fun(self, value):
        return abs(hash(value)) % self.size

    def seek_slot(self, value):
        ind = self.hash_fun(value)
        if self.slots[ind] is None:
            return ind
        return None

    def put(self, value):
        ind = self.seek_slot(value)
        if ind is not None:
            self.slots[ind] = value
            return ind
        return None

    def find(self, value):
        ind = self.hash_fun(value)
        if self.slots[ind] == value:
            return ind
        return None