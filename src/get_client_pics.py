# This script gets all the pictures from the dataset that match each photo in the groupedFaces clients then stores them in a folder named sortedPics

import os
import shutil
from os import listdir
import face_recognition
import cv2
from PIL import Image

# get the paths or directories of the dataset and the groupedFaces folders outside the src folder
pics_dir = "../dataset"
clients_dir = "../groupedFaces"

try:
    # get the list of files in the directory
    pics = listdir(pics_dir)
    clients = listdir(clients_dir)

    # loop through the directories in the directory
    for client in clients:
        # get the path of the file
        client_path = os.path.join(clients_dir, client)
        # get the list of files in the directory
        client_pics = listdir(client_path)
        # loop through the files in the directory
        for client_pic in client_pics:
            # get the path of the file
            client_pic_path = os.path.join(client_path, client_pic)
            # read and encode file
            client_pic_image = cv2.imread(client_pic_path)
            client_pic_image = cv2.cvtColor(client_pic_image,
                                            cv2.COLOR_BGR2RGB)
            try:
                client_pic_encoding = face_recognition.face_encodings(
                    client_pic_image)[0]
                # loop through the files in the directory
                for pic in pics:
                    # get the path of the file
                    pic_path = os.path.join(pics_dir, pic)
                    # read and encode file
                    pic_image = cv2.imread(pic_path)
                    pic_image = cv2.cvtColor(pic_image, cv2.COLOR_BGR2RGB)
                    try:
                        pic_encoding = face_recognition.face_encodings(
                            pic_image)[0]
                        # compare the face encodings
                        results = face_recognition.compare_faces(
                            [pic_encoding], client_pic_encoding, tolerance=0.4)
                        if results[0]:
                            # check if the sortedPics directory exists
                            if not os.path.exists("../sortedPics"):
                                os.makedirs("../sortedPics")
                            # check if the client directory exists
                            if not os.path.exists("../sortedPics/" + client):
                                os.makedirs("../sortedPics/" + client)
                            # copy the file to the sortedPics directory
                            shutil.copy(pic_path, "../sortedPics/" + client)
                    except:
                        pass
            except:
                pass

except:
    print("Error")
    pass
