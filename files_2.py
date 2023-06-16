# 4.1 Напишите функцию с тремя параметрами (путь к каталогу, расширение файла и булев флажок), которая возвращает
# список из двух списков имён: список всех файлов с заданным расширением в заданном каталоге (включая файлы из его
# подкаталогов одного уровня вложенности, если флажок = True), и список всех подкаталогов в заданном каталоге
# (включая подкаталоги одного уровня вложенности, если флажок = True).

import os
import shutil


def get_files_with_extension(directory_path, extension, include_subdirectories):
    file_list = []
    subdirectory_file_list = []

    for root, directories, files in os.walk(directory_path):
        for file in files:
            if file.endswith(extension):
                if include_subdirectories or root == directory_path:
                    file_list.append(os.path.join(root, file))
                else:
                    subdirectory_file_list.append(os.path.join(root, file))

    return [file_list, subdirectory_file_list]


directory = '/Users/mikhailsaharov/Desktop/programming_homeworks/lection_14'
extension = '.txt'
include_subdirs = True

result = get_files_with_extension(directory, extension, include_subdirs)
print(result)

# 4.2 Напишите функцию, которая удаляет заданный каталог (возможно, непустой) и все файлы внутри него.
# Если внутри каталога есть подкаталоги, ничего удалять не надо.
# Функция возвращает флажок успешно/неудача.

def delete_directory(directory_path):
    try:
        shutil.rmtree(directory_path)
        return True
    except Exception as e:
        print(f"Failed to delete directory: {e}")
        return False



