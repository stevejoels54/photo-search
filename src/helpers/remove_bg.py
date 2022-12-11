# Remove of all images in the dataset/dataset8 folder and save them in the dataset/dataset8_no_bg folder
import os
from rembg import remove
from os import listdir
from PIL import Image

# get the path or directory
folder_dir = "../../dataset/dataset2"
output_dir = "../../dataset/dataset2_no_bg"

# get the list of files in the directory
files = listdir(folder_dir)

count = 0

# loop through the files in the directory
for file in files:
    count += 1
    # get the path of the file
    file_path = os.path.join(folder_dir, file)
    # get the image
    input = Image.open(file_path)
    # remove the background
    output = remove(input)
    # save the image
    # check if the dataset/dataset8_no_bg directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    output_path = os.path.join(output_dir, file.split(".")[0] + ".png")
    output.save(output_path)
    print("Saved image " + str(count) + " of " + str(len(files)))