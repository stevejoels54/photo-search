# This script has a function that passes a directory to the dataset folder then removes all pictures that have no detectected faces and stores them in an unknown folder

import os
import face_recognition


def remove_unknown_faces(dataset_folder):
    count = 0
    unknown_dir = "../../unknown/unknown1"
    # Create the "unknown" folder if it does not exist
    if not os.path.exists(unknown_dir):
        os.makedirs(unknown_dir)

    # Get the list of image filenames in the dataset folder
    filenames = os.listdir(dataset_folder)

    # Process each image in the dataset folder
    for filename in filenames:
        # check if the file is a picture
        if filename.endswith(".jpg") or filename.endswith(
                ".png") or filename.endswith(".jpeg"):
            # Load the image
            image = face_recognition.load_image_file(
                os.path.join(dataset_folder, filename))

            # Try to detect the faces in the image
            try:
                face_locations = face_recognition.face_locations(image)

                # If no faces are detected, move the image to the "unknown" folder
                if len(face_locations) == 0:
                    os.rename(os.path.join(dataset_folder, filename),
                              os.path.join(unknown_dir, filename))
            except face_recognition.api.FaceNotFoundError:
                # If no faces are detected, move the image to the "unknown" folder
                os.rename(os.path.join(dataset_folder, filename),
                          os.path.join(unknown_dir, filename))


remove_unknown_faces("../../dataset/dataset1")
