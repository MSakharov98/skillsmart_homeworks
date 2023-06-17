import unittest
import os
import zipfile
from zip_files import create_archive

class CreateArchiveTests(unittest.TestCase):

    def test_create_archive_with_existing_files(self):
        # Создаем временный каталог и несколько файлов с расширением '.txt'
        os.makedirs('test_directory', exist_ok=True)
        with open('test_directory/file1.txt', 'w') as f:
            f.write('Content of file1.txt')
        with open('test_directory/file2.txt', 'w') as f:
            f.write('Content of file2.txt')

        # Вызываем функцию create_archive для создания архива
        result = create_archive('test_archive.zip', '.txt')

        # Проверяем, что архив был создан успешно
        self.assertTrue(result)
        self.assertTrue(os.path.exists('test_archive.zip'))

        # Открываем созданный архив и проверяем его содержимое
        with zipfile.ZipFile('test_archive.zip', 'r') as zipf:
            archive_contents = zipf.namelist()

        self.assertIn('test_directory/file1.txt', archive_contents)
        self.assertIn('test_directory/file2.txt', archive_contents)

        # Удаляем временные файлы и архив
        os.remove('test_archive.zip')
        os.remove('test_directory/file1.txt')
        os.remove('test_directory/file2.txt')
        os.rmdir('test_directory')

    def test_create_archive_with_no_matching_files(self):
        # Создаем временный каталог и несколько файлов с расширением '.png'
        os.makedirs('test_directory', exist_ok=True)
        with open('test_directory/file1.png', 'w') as f:
            f.write('Content of file1.png')
        with open('test_directory/file2.png', 'w') as f:
            f.write('Content of file2.png')

        # Вызываем функцию create_archive для создания архива с расширением '.txt'
        result = create_archive('test_archive.zip', '.txt')

        # Проверяем, что архив не был создан
        self.assertFalse(result)
        self.assertFalse(os.path.exists('test_archive.zip'))

        # Удаляем временные файлы и каталог
        os.remove('test_directory/file1.png')
        os.remove('test_directory/file2.png')
        os.rmdir('test_directory')

if __name__ == '__main__':
    unittest.main()
