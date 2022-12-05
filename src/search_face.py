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