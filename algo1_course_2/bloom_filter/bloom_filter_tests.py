import unittest
from bloom_filter import BloomFilter

test_data = [
    "0123456789",
    "1234567890",
    "2345678901",
    "3456789012",
    "4567890123",
    "5678901234",
    "6789012345",
    "7890123456",
    "8901234567",
    "9012345678",
]


class TestBloomFilter(unittest.TestCase):
    def test_bloom_filter(self):
        bloom_filter = BloomFilter(32)
        for string in test_data:
            bloom_filter.add(string)
            self.assertTrue(bloom_filter.is_value(string))


if __name__ == '__main__':
    unittest.main()