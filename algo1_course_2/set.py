class PowerSet():
    def __init__(self):
        self.storage = {}

    def size(self):
        return len(self.storage)

    def put(self, value):
        self.storage[value] = 0

    def get(self, value):
        return self.storage.get(value) is not None

    def remove(self, value):
        return self.storage.pop(value, None) is not None

    def intersection(self, set2):
        result = PowerSet()
        for key in self.storage:
            if set2.get(key):
                result.storage[key] = 0
        return result

    def union(self, set2):
        result = PowerSet()
        for key in self.storage:
            result.storage[key] = 0
        for key in set2.storage:
            result.storage[key] = 0
        return result

    def difference(self, set2):
        result = PowerSet()
        for key in self.storage:
            result.storage[key] = 0
        for key in set2.storage:
            result.storage.pop(key, None)
        return result

    def issubset(self, set2):
        for key in set2.storage:
            if not self.get(key):
                return False
        return True