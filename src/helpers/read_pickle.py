# Print all the contents in a pickle file
import pickle
import os

# Set the location of the pickle file with encodings
pickle_file = '../faceEncodings/clientEncodings/client14.pickle'

# Load the face encodings from the pickle file
with open(pickle_file, 'rb') as f:
    face_encodings = pickle.load(f)

# for face_encoding in face_encodings:
#     print("Encoding: ", face_encoding)
# Print the number of face encodings in the pickle file
print(f'Number of face encodings: {len(face_encodings)}')

# Print the first face encoding in the pickle file
print(f'First face encoding: {face_encodings[0]}')

# Print the last face encoding in the pickle file
print(f'Last face encoding: {face_encodings[-1]}')
