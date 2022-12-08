# Description: This script will find all the face encodings that compare to the first encoding in the pickle file and find the images that have the same encoding

import face_recognition
import os
import pickle
import numpy as np

# Set the location of the pickle file with encodings
pickle_file = '../../faceEncodings/datasetEncodings/all_face_encodings.pickle'

# Load the face encodings from the pickle file
with open(pickle_file, 'rb') as f:
    face_encodings = pickle.load(f)

client = 1
# Iterate through all the face encodings in the pickle file
for face_encoding in face_encodings:
    encodings = []
    # iterate through all the face encodings in the pickle file while following the index
    for index, face_encoding2 in enumerate(face_encodings):
        # compare the face encoding to the first face encoding
        match = face_recognition.compare_faces([face_encoding],
                                               face_encoding2,
                                               tolerance=0.4)
        # print the match
        if match[0]:
            encodings.append(face_encoding2)
            # After the encoding is added to the list, remove it from the pickle file face encodings
            face_encodings.pop(index)
    # Save the list of all face encodings to a pickle file
    with open(f'../../faceEncodings/clientEncodings/client{client}.pickle',
              'wb') as f:
        pickle.dump(encodings, f)
    client += 1
