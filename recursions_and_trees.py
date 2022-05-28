### print all files in directory and subdirectories
import os

def list_files(current_path):
    if not os.path.isdir(current_path):
        print(current_path)
    else:
        for name in os.listdir(current_path):
            joined = os.path.join(current_path, name)
            list_files(joined)
list_files('folder')

