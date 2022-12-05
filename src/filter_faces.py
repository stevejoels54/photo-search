# import the modules
import os
import face_recognition
from os import listdir
from PIL import Image

# get the path or directory
found_faces_dir = "../foundFaces"


#group the faces
def filterFaces(folder_dir):
    count = 0

    # check if the foundFaces directory exists
    if not os.path.exists(found_faces_dir):
        print("No filter faces folder found, please run find_faces.py first")
        exit()
    # get the list of files in the directory
    files = listdir(folder_dir)
    for file in files:
        if file.endswith(".jpg") or file.endswith(".png") or file.endswith(
                ".jpeg"):
            file_path = os.path.join(folder_dir, file)

            try:
                #encode image
                image = face_recognition.load_image_file(file_path)
                image_encoding = face_recognition.face_encodings(image)[0]
                print("Image %s has face" % file)
                count += 1

            except:
                print("Image %s has no face" % file)
                # delete the image
                os.remove(file_path)

    print("Total clear faces found: %s" % count)


filterFaces(found_faces_dir)