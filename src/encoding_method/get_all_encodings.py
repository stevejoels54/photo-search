# Read  the face encodings from the pickle file and create another pickle file with all the face encodings grouped together
# The face encodings pickle file stored the image names and the face encodings as a dictionary
# The new pickle file will store the face encodings as a list of lists

import os
import pickle
# Set the location of the pickle file with encodings
pickle_file = '../../faceEncodings/datasetEncodings/face_encodings.pickle'

# Load the face encodings from the pickle file
with open(pickle_file, 'rb') as f:
    face_encodings = pickle.load(f)

all_face_encodings = []

# Loop through all of the face encodings in the dictionary
for img_name, face_encodings_in_image in face_encodings.items():
    # Loop through all of the face encodings in the image
    for face_encoding in face_encodings_in_image:
        # Add the face encoding to the list of all face encodings
        all_face_encodings.append(face_encoding)

# Save the list of all face encodings to a pickle file
with open('../../faceEncodings/datasetEncodings/all_face_encodings.pickle',
          'wb') as f:
    pickle.dump(all_face_encodings, f)
