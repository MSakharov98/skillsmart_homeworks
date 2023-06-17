import os
import shutil
import unittest
from files_2 import get_files_with_extension, delete_directory


class FilesTestCase(unittest.TestCase):
    def setUp(self):
        # Создаем тестовый каталог
        os.makedirs("/tmp/test_dir")
        os.makedirs("/tmp/test_dir/subdir")
        with open("/tmp/test_dir/file1.txt", "w"):
            pass
        with open("/tmp/test_dir/file2.txt", "w"):
            pass
        with open("/tmp/test_dir/subdir/file3.txt", "w"):
            pass
        with open("/tmp/test_dir/subdir/file4.txt", "w"):
            pass

    def tearDown(self):
        # Проверяем существование каталога перед удалением
        if os.path.exists("/tmp/test_dir"):
            # Удаляем тестовый каталог
            shutil.rmtree("/tmp/test_dir")

    def test_get_files_with_extension(self):
        result = get_files_with_extension("/tmp/test_dir", ".txt", True)
        expected_result = (['/tmp/test_dir/file1.txt', '/tmp/test_dir/file2.txt', '/tmp/test_dir/subdir/file3.txt', '/tmp/test_dir/subdir/file4.txt'], [])
        self.assertEqual(result, expected_result)

    def test_delete_directory(self):
        # Проверяем существование каталога перед удалением
        self.assertTrue(os.path.exists("/tmp/test_dir"))

        success = delete_directory("/tmp/test_dir")
        self.assertTrue(success)  # Проверяем успешное удаление каталога
        self.assertFalse(os.path.exists("/tmp/test_dir"))  # Проверяем, что каталог был удален


if __name__ == '__main__':
    unittest.main()


