import unittest
from dynamic_array import DynArray


class TestDynArrayMethods(unittest.TestCase):
    def setUp(self):
        self.dyn_array = DynArray()

    def test_insert_within_capacity(self):
        self.dyn_array.append(1)
        self.dyn_array.append(2)
        self.dyn_array.insert(1, 5)
        self.assertEqual(len(self.dyn_array), 3)
        self.assertEqual(self.dyn_array[1], 5)

    def test_insert_exceed_capacity(self):
        for i in range(16):
            self.dyn_array.append(i)
        self.dyn_array.insert(8, 100)
        self.assertEqual(len(self.dyn_array), 17)
        self.assertEqual(self.dyn_array[8], 100)

    def test_insert_invalid_index(self):
        with self.assertRaises(IndexError):
            self.dyn_array.insert(10, 5)

    def test_delete_within_capacity(self):
        self.dyn_array.append(1)
        self.dyn_array.append(2)
        self.dyn_array.append(3)
        self.dyn_array.delete(1)
        self.assertEqual(len(self.dyn_array), 2)
        self.assertEqual(self.dyn_array[1], 3)

    def test_delete_shrink_capacity(self):
        for i in range(16):
            self.dyn_array.append(i)
        for i in range(8):
            self.dyn_array.delete(0)
        self.assertEqual(len(self.dyn_array), 8)
        self.assertEqual(self.dyn_array[0], 8)

    def test_delete_invalid_index(self):
        with self.assertRaises(IndexError):
            self.dyn_array.delete(10)


if __name__ == '__main__':
    unittest.main()
