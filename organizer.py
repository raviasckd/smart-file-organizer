import os
import shutil
import sys

def organize_folder(folder_path):
    for filename in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, filename)):
            ext = filename.split('.')[-1]
            ext_folder = os.path.join(folder_path, ext.upper() + '_Files')

            if not os.path.exists(ext_folder):
                os.makedirs(ext_folder)

            shutil.move(os.path.join(folder_path, filename), os.path.join(ext_folder, filename))
    print("Files organized successfully!")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        organize_folder(sys.argv[1])
    else:
        print("Please provide a folder path.")
