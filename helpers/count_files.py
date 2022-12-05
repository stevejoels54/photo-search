import os
import shutil

# folder path
dir_path = "people"
# Iterate directory
for path in os.listdir(dir_path):
    for person in os.listdir(os.path.join(dir_path, path)):

        # if len(os.listdir(os.path.join(dir_path, path))) > 10 and len(
        #         os.listdir(os.path.join(dir_path, path))) < 100:
        #     # move it to people folder
        #     shutil.move(os.path.join(dir_path, path), "people")
        #     print("Moved %s to people folder" % path)
        #     break

        # more than 100 images in a folder print the folder name
        if len(os.listdir(os.path.join(dir_path, path))) > 50 and len(
                os.listdir(os.path.join(dir_path, path))) <= 100:
            print("Folder %s has images btn 10 and 50" % path)
            break