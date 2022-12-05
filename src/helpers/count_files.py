import os
import shutil

# folder path
dir_path = "../groupedFaces"


def countPics(dir_path):
    print("Total files in %s: %s" % (dir_path, len(os.listdir(dir_path))))
    return len(os.listdir(dir_path))


def countFiles(dir_path):
    count = 0
    for file in os.listdir(dir_path):
        if file.endswith(".jpg") or file.endswith(".png") or file.endswith(
                ".jpeg"):
            count += 1
    print("Total files in %s: %s" % (dir_path, count))
    return count


def countFolders(dir_path):
    print("Total folders in %s: %s" % (dir_path, len(os.listdir(dir_path))))
    return len(os.listdir(dir_path))


def countPicsInFolders(dir_path):
    for folder in os.listdir(dir_path):
        count = countFiles(dir_path + "/" + folder)
        print("Total files in %s: %s" % (folder, count))


countPicsInFolders(dir_path)