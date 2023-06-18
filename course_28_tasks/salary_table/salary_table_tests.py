import unittest
from salary_table import SynchronizingTables
class TestSynchronizingTables(unittest.TestCase):

    def test_synchronizing_tables(self):
        N = 4
        ids = [10, 67, 68, 28]
        salary = [55, 73, 10, 6]
        expected = [6, 55, 73, 10]
        result = SynchronizingTables(N, ids, salary)
        self.assertEqual(result, expected)

    def test_synchronizing_tables_empty(self):
        N = 0
        ids = []
        salary = []
        expected = []
        result = SynchronizingTables(N, ids, salary)
        self.assertEqual(result, expected)

    def test_synchronizing_tables_duplicates(self):
        N = 5
        ids = [1, 2, 3, 4, 5]
        salary = [100, 200, 200, 100, 300]
        expected = [100, 100, 200, 200, 300]
        result = SynchronizingTables(N, ids, salary)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()

