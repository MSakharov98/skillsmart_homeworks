import os

def find_files(directory):
    files_list = []
    search_files_recursive(directory, files_list)

    return files_list

def search_files_recursive(directory, files_list):

    for root, dirs, files in os.walk(directory):

        for file in files:
            file_path = os.path.join(root, file)
            files_list.append(file_path)

        for dir in dirs:
            dir_path = os.path.join(root, dir)
            search_files_recursive(dir_path, files_list)
