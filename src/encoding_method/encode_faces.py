# Description: This script encodes the faces in the images in the dataset folder

import face_recognition
import pickle
import os


def process_images(dataset_dir):
    # Initialize an empty dictionary to store the image names and the face encodings
    face_encodings = {}

    # Loop through all images in the dataset
    for img_name in os.listdir(dataset_dir):

        try:
            # Load the image
            image = face_recognition.load_image_file(dataset_dir + img_name)
        except (IOError, OSError):
            # Skip the file if it cannot be loaded
            continue

        try:
            # Get the face encodings for the faces in the image
            face_encodings_in_image = face_recognition.face_encodings(image)
            # Print the number of face encodings in the image
            print(f'{img_name}: {len(face_encodings_in_image)} face encodings')
            # Add the face encodings to the dictionary, using the image name as the key
            face_encodings[img_name] = face_encodings_in_image

        except face_recognition.api.FaceNotFoundError:
            # Skip the file if no faces are found
            continue

    # Save the face encodings in a pickle file
    with open('../../faceEncodings/datasetEncodings/face_encodings.pickle',
              'wb') as f:
        pickle.dump(face_encodings, f)


# Process the images in the dataset/dataset1 folder
process_images('../../dataset/dataset1/')