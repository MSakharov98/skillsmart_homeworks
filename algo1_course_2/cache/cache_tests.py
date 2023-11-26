import unittest
import string
import random
from cache import NativeCache


def generate_random_string(length=10):
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(length))


def init_cache(size, value):
    cache = NativeCache(size)
    for _ in range(size):
        cache.put(generate_random_string(), value)
    return cache

class TestNativeCache(unittest.TestCase):
    def test_put_enough_space(self):
        size = 1000
        value = 0
        cache = init_cache(size, value)
        for i in range(size):
            self.assertIsNotNone(cache.slots[i])
            self.assertEqual(cache.values[i], value)
            self.assertEqual(cache.hits[i], 1)

    def test_queries_registering(self):
        size = 1000
        value = 0
        queries = 5
        cache = init_cache(size, value)
        for i in range(int(size / 2)):
            key = cache.slots[i]
            for _ in range(queries):
                self.assertEqual(cache.get(key), value)
        for i in range(int(size / 2)):
            self.assertIsNotNone(cache.slots[i])
            self.assertEqual(cache.values[i], value)
            self.assertEqual(cache.hits[i], queries + 1)
        for i in range(int(size / 2), size):
            self.assertIsNotNone(cache.slots[i])
            self.assertEqual(cache.values[i], value)
            self.assertEqual(cache.hits[i], 1)

    def test_put_with_replacement(self):
        size = 1000
        value = 0
        queries = 5
        cache = init_cache(size, value)
        least_accessed_index = random.randrange(0, size)
        for i in range(size):
            key = cache.slots[i]
            if i == least_accessed_index:
                self.assertEqual(cache.get(key), value)
                continue
            for _ in range(queries):
                self.assertEqual(cache.get(key), value)
        self.assertEqual(cache.hits[least_accessed_index], 2)
        new_key = generate_random_string(15)
        new_value = 1
        cache.put(new_key, new_value)
        for i in range(size):
            if i == least_accessed_index:
                self.assertEqual(cache.slots[i], new_key)
                self.assertEqual(cache.values[i], new_value)
                self.assertEqual(cache.hits[i], 1)
            else:
                self.assertEqual(cache.values[i], value)
                self.assertEqual(cache.hits[i], queries + 1)


if __name__ == '__main__':
    unittest.main()