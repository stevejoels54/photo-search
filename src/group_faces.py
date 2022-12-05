# import the modules
import os
import face_recognition
from os import listdir
from PIL import Image

# paths and directories
foundFacesDir = "../foundFaces"
groupedFacesDir = "../groupedFaces"


#group the faces
def groupFaces(folder_dir):
    faceNum = 1
    clientNum = 1

    files = listdir(folder_dir)
    for file in files:
        if file.endswith(".jpg") or file.endswith(".png") or file.endswith(
                ".jpeg"):
            file_path = os.path.join(folder_dir, file)

            try:
                #encode image
                image = face_recognition.load_image_file(file_path)
                image_encoding = face_recognition.face_encodings(image)[0]
                print("Image %s has a clear face" % file)

                for file1 in files:
                    if file1.endswith(".jpg") or file1.endswith(
                            ".png") or file1.endswith(".jpeg"):
                        file_path1 = os.path.join(folder_dir, file1)

                        try:
                            # read and encode image
                            image1 = face_recognition.load_image_file(
                                file_path1)
                            image_encoding1 = face_recognition.face_encodings(
                                image1)[0]

                            # compare the face encodings

                            results = face_recognition.compare_faces(
                                [image_encoding],
                                image_encoding1,
                                tolerance=0.4)
                            if results[0]:
                                # check if the groupedFaces directory exists
                                if not os.path.exists(groupedFacesDir):
                                    os.makedirs(groupedFacesDir)
                                # create a folder for the filtered faces named client inside the filteredFaces directory
                                if not os.path.exists(
                                        "../groupedFaces/client " +
                                        str(clientNum)):
                                    os.makedirs("../groupedFaces/client " +
                                                str(clientNum))
                                # save the filtered faces in the client folder
                                filteredFace = Image.open(file_path1)
                                # move the matched face to the filteredFaces directory and rename it to face1, face2, face3 etc
                                filteredFace.save("../groupedFaces/client " +
                                                  str(clientNum) + "/face" +
                                                  str(faceNum) + ".jpeg")
                                faceNum += 1

                                # print matched file with file1
                                print("Matched: %s with %s" % (file, file1))

                                # delete the matched face from the foundFaces directory
                                os.remove(file_path1)

                        except:
                            pass

                clientNum += 1

            except:
                pass

    print("Total number of clients: ", int(clientNum) - 1)
    print("Total number of faces: ", int(faceNum) - 1)
    print("Done processing")


groupFaces(foundFacesDir)