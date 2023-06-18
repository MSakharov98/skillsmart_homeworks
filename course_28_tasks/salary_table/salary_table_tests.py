import unittest
from salary_table import SynchronizingTables


class MyTestCase(unittest.TestCase):

    class TestSynchronizingTables(unittest.TestCase):

        def test_synchronized_salary(self):
            ids = [50, 1, 1024]
            salary = [20000, 100000, 90000]
            expected_result = [90000, 20000, 100000]

            synchronized_salary = SynchronizingTables(len(ids), ids, salary)
            self.assertEqual(synchronized_salary, expected_result)

        def test_empty_lists(self):
            ids = []
            salary = []
            expected_result = []

            synchronized_salary = SynchronizingTables(len(ids), ids, salary)
            self.assertEqual(synchronized_salary, expected_result)

        def test_duplicate_salaries(self):
            ids = [1, 2, 3]
            salary = [10000, 20000, 10000]
            expected_result = [10000, 20000, 10000]

            synchronized_salary = SynchronizingTables(len(ids), ids, salary)
            self.assertEqual(synchronized_salary, expected_result)

        def test_unordered_ids(self):
            ids = [3, 2, 1]
            salary = [10000, 20000, 30000]
            expected_result = [30000, 20000, 10000]

            synchronized_salary = SynchronizingTables(len(ids), ids, salary)
            self.assertEqual(synchronized_salary, expected_result)

    if __name__ == '__main__':
        unittest.main()


