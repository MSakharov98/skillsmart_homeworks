class NativeDictionary:
    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size
        self.step = 1

    def hash_fun(self, key):
        return sum([ord(ch) for ch in key]) % self.size

    def seek_slot(self, key):
        index = self.hash_fun(key)
        initial_index = index
        while index < self.size:
            if self.slots[index] is None or self.slots[index] == key:
                return index
            index += self.step
        index -= self.step
        index = self.step - (self.size - index)
        while index < initial_index:
            if self.slots[index] is None or self.slots[index] == key:
                return index
            index += self.step
        return None

    def seek_key(self, key):
        index = self.hash_fun(key)
        initial_index = index
        while index < self.size:
            if self.slots[index] == key:
                return index
            index += self.step
        index -= self.step
        index = self.step - (self.size - index)
        while index < initial_index:
            if self.slots[index] == key:
                return index
            index += self.step
        return None

    def is_key(self, key):
        return self.seek_key(key) is not None

    def put(self, key, value):
        index = self.seek_slot(key)
        if index is not None:
            self.slots[index] = key
            self.values[index] = value

    def get(self, key):
        index = self.seek_key(key)
        if index is not None:
            return self.values[index]
        return None
