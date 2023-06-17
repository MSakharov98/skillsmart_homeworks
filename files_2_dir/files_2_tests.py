import os
import shutil
import unittest
from files_2 import get_files_with_extension, delete_directory


class FilesTestCase(unittest.TestCase):
    def setUp(self):
        # Создаем тестовый каталог
        self.test_dir = "test_dir"
        self.subdir = "subdir"
        os.makedirs(self.test_dir)
        os.makedirs(os.path.join(self.test_dir, self.subdir))
        with open(os.path.join(self.test_dir, "file1.txt"), "w"):
            pass
        with open(os.path.join(self.test_dir, "file2.txt"), "w"):
            pass
        with open(os.path.join(self.test_dir, self.subdir, "file3.txt"), "w"):
            pass
        with open(os.path.join(self.test_dir, self.subdir, "file4.txt"), "w"):
            pass

    def tearDown(self):
        # Проверяем существование каталога перед удалением
        if os.path.exists(self.test_dir):
            # Удаляем тестовый каталог
            shutil.rmtree(self.test_dir)

    def test_get_files_with_extension(self):
        result = get_files_with_extension(self.test_dir, ".txt", True)
        expected_result = ([
            os.path.join(self.test_dir, "file1.txt"),
            os.path.join(self.test_dir, "file2.txt"),
            os.path.join(self.test_dir, self.subdir, "file3.txt"),
            os.path.join(self.test_dir, self.subdir, "file4.txt")
        ], [])
        self.assertEqual(result, expected_result)

    def test_delete_directory(self):
        # Проверяем существование каталога перед удалением
        self.assertTrue(os.path.exists(self.test_dir))

        success = delete_directory(self.test_dir)
        self.assertTrue(success)  # Проверяем успешное удаление каталога
        self.assertFalse(os.path.exists(self.test_dir))  # Проверяем, что каталог был удален


if __name__ == '__main__':
    unittest.main()
