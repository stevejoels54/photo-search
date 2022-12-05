# Search face in a group of faces
import cv2
import face_recognition
import os
from os import listdir
from PIL import Image
from helpers.count_files import countFiles

# get the path or directory
folder_dir = "../groupedFaces"

countFiles(folder_dir)

# # get the path or directory
# #searchable_faces = "dataset"

# searchable_faces = "foundFaces"

# face = "face22"
# # face_file_path = os.path.join("searchable", face24.jpeg)

# # face_path = os.path(os.listdir("searchable"), "face46.jpeg")

# # get unknown file encoding

# print("Processing pictures.......")

# reference_picture = cv2.imread(
#     "/Users/ssekyewajoelsteven/Documents/PROJECTS/G-and-B-projects/photo-search/foundFaces/face32.jpeg"
# )
# reference_picture = cv2.cvtColor(reference_picture, cv2.COLOR_BGR2RGB)
# try:
#     reference_picture_encoding = face_recognition.face_encodings(
#         reference_picture)[0]
# except:
#     print("Image %s has a blurry face" % face)

# # get the list of files in the directory

# files = listdir(searchable_faces)
# for file in files:  # loop through the files in the directory
#     if file.endswith(".jpg") or file.endswith(".png") or file.endswith(
#             ".jpeg"):
#         file_path = os.path.join(searchable_faces, file)

#         # read and encode file

#         image = cv2.imread(file_path)
#         image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
#         try:
#             file_encoding = face_recognition.face_encodings(image)[0]

#             # compare the face encodings

#             results = face_recognition.compare_faces(
#                 [file_encoding], reference_picture_encoding, tolerance=0.4)
#             if results[0]:
#                 print("Matched: %s" % file)
#         except:
#             pass
# print("Done processing")