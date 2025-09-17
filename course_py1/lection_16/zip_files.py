import zipfile
import os

def create_archive(filename, extension):
    try:
        with zipfile.ZipFile(filename, 'w') as zipf:
            for file in os.listdir('../..'):
                if file.endswith(extension):
                    zipf.write(file)
        return True
    except Exception as e:
        print(f"Failed to create archive: {e}")
        return False

