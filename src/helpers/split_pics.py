# Split the dataset into folders of 100 pics each
# Compare this snippet from src/helpers/split_pics.py:

import os
from os import listdir
import shutil

# get the path or directory
pics_dir = "../../dataset"
# get the list of files in the directory
pics = listdir(pics_dir)
# create a set to store the images
pics_set = set()
# loop through the files in the directory
for pic in pics:
    # get the path of the file
    pic_path = os.path.join(pics_dir, pic)
    # add the file to the set
    pics_set.add(pic_path)

# create a list of the set
pics_list = list(pics_set)
# create a counter
count = 0
# create a counter for the folder
folder_count = 1
# loop through the list
for pic in pics_list:
    # check if the counter is less than 100
    if count < 100:
        # check if the folder exists in the pics_dir
        if not os.path.exists(pics_dir + "/dataset" + str(folder_count)):
            # create the folder
            os.makedirs(pics_dir + "/dataset" + str(folder_count))
        # move the file to the folder
        shutil.move(pic, pics_dir + "/dataset" + str(folder_count))
        # increment the counter
        count += 1
    # check if the counter is equal to 100
    elif count == 100:
        # increment the folder counter
        folder_count += 1
        # reset the counter
        count = 0
        # check if the folder exists in the pics_dir
        if not os.path.exists(pics_dir + "/dataset" + str(folder_count)):
            # create the folder
            os.makedirs(pics_dir + "/dataset" + str(folder_count))
        # move the file to the folder
        shutil.move(pic, pics_dir + "/dataset" + str(folder_count))
        # increment the counter
        count += 1
