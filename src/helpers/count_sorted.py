# get all sorted images sortedPics directory under each client and store them in a set
import os
from os import listdir

# get the path or directory
folder_dir = "../sortedPics"
data_set = "../dataset"

# get the list of files in the directory
files = listdir(folder_dir)
data = listdir(data_set)

# create a set to store the images
sorted_pics = set()

# loop through the files in the directory
for file in files:
    # get the path of the file
    file_path = os.path.join(folder_dir, file)
    # get the list of files in the directory
    client_pics = listdir(file_path)
    # loop through the files in the directory
    for client_pic in client_pics:
        # get the path of the file
        client_pic_path = os.path.join(file_path, client_pic)
        # add the file to the set
        sorted_pics.add(client_pic)

for file in data:
    # get the path of the file
    file_path = os.path.join(folder_dir, file)
    # check if the file is in the set
    if file not in sorted_pics:
        print(file)