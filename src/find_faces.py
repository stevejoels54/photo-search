import os
import face_recognition
from os import listdir
from PIL import Image

# get the path or directory
folderDir = "../dataset"
foundFacesDir = "../foundFaces"


def getFaces(folderDir):
    faceNum = 1

    # check if dataset directory exists
    if not os.path.exists(folderDir):
        print(
            "No dataset folder found, please add your images to the dataset folder"
        )
        exit()
    # get the list of files in the directory
    files = listdir(folderDir)

    # loop through the files
    for file in files:
        # get the path of the file
        if file.endswith(".jpg") or file.endswith(".png") or file.endswith(
                ".jpeg"):
            file_path = os.path.join(folderDir, file)

            # get the image
            image = face_recognition.load_image_file(file_path)

            # get the face locations
            face_locations = face_recognition.face_locations(image)

            #loop through the face locations
            for face_location in face_locations:
                # get the top, right, bottom and left locations
                top, right, bottom, left = face_location

                # get the face image
                face_image = image[top:bottom, left:right]

                # save the face image

                # check if the foundFaces directory exists
                if not os.path.exists(foundFacesDir):
                    os.makedirs(foundFacesDir)
                face_image_path = os.path.join(foundFacesDir,
                                               "face" + str(faceNum) + ".jpeg")
                face_image_pil = Image.fromarray(face_image)
                face_image_pil.save(face_image_path, quality=95)

                # increment the face number
                faceNum += 1


getFaces(folderDir)