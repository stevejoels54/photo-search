# Rename pics in pics folder to 1.jpg, 2.jpg, 3.jpg, etc.
# Compare this snippet from rename_files.py:
import os
import shutil

# folder path
dir_path = "pics"


def renamePics(dir_path, name):
    count = 1
    for file in os.listdir(dir_path):
        if file.endswith(".jpg") or file.endswith(".png") or file.endswith(
                ".jpeg"):
            src = dir_path + "/" + file
            dst = dir_path + "/" + name + str(count) + ".jpg"
            os.rename(src, dst)
            count += 1


def renameFolders(dir_path, name):
    count = 1
    for file in os.listdir(dir_path):
        src = dir_path + "/" + file
        dst = dir_path + "/" + name + str(count)
        os.rename(src, dst)
        count += 1