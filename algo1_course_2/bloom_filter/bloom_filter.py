class BloomFilter:

    def __init__(self, f_len):
        self.filter_len = f_len
        self.filter = 0

    def hash1(self, str1):
        result = 0
        for c in str1:
            result = (result * 17 + ord(c)) % self.filter_len
        return result

    def hash2(self, str1):
        result = 0
        for c in str1:
            result = (result * 223 + ord(c)) % self.filter_len
        return result

    def bit_mask(self, bit):
        return 1 << bit

    def set_bit(self, bit):
        self.filter |= self.bit_mask(bit)

    def get_bit(self, bit):
        return (self.filter & self.bit_mask(bit)) != 0

    def add(self, str1):
        self.set_bit(self.hash1(str1))
        self.set_bit(self.hash2(str1))

    def is_value(self, str1):
        return self.get_bit(self.hash1(str1)) and self.get_bit(self.hash2(str1))