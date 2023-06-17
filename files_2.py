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

# Внесение корректировок. Не используется конструкция try...except, добавлена собственная функция
# по созданию каталогов и подкаталогов
def delete_directory(directory_path):
    def get_file_list(directory_path):
        file_list = []
        for root, directories, files in os.walk(directory_path):
            for file in files:
                file_path = os.path.join(root, file)
                file_list.append(file_path)
        return file_list

    if os.path.exists(directory_path):
        file_list = get_file_list(directory_path)
        for file_path in file_list:
            if os.path.isfile(file_path):
                os.remove(file_path)
            else:
                shutil.rmtree(file_path)
        return True
    else:
        print("Directory does not exist.")
        return False



