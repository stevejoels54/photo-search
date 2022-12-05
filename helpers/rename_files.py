# Rename pics in pics folder to 1.jpg, 2.jpg, 3.jpg, etc.
# Compare this snippet from rename_files.py:
import os
import shutil

# folder path
dir_path = "pics"
# Iterate directory
count = 1
for file in os.listdir(dir_path):
    # if file is an image
    if file.endswith(".jpg") or file.endswith(".png") or file.endswith(
            ".jpeg"):
        file_path = os.path.join(dir_path, file)
        new_file_path = os.path.join(dir_path, "pic" + str(count) + ".jpeg")
        shutil.move(file_path, new_file_path)
        count += 1
        print("Renaming %s to %s" % (file_path, new_file_path))