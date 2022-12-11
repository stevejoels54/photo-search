import face_recognition
import os
import pickle
import numpy as np

# Set the location of the pickle file with encodings
path = '../../faceEncodings/clientEncodings/'
# face encodings pickle file path
pickle_file = '../../faceEncodings/datasetEncodings/face_encodings.pickle'

# Create a set to store the image names
image_names = set()

# Load the face encodings from the pickle file
with open(pickle_file, 'rb') as f:
    face_encodings = pickle.load(f)

# iterate through all the pickle files in the folder
for file in os.listdir(path):
    if file.endswith('.pickle'):
        print("Sorting: ", file.split(".")[0])
        # Load the face encodings from the pickle file
        with open(path + file, 'rb') as f:
            client_encodings = pickle.load(f)
            for client_encoding in client_encodings:
                for img_name, face_encodings_in_image in face_encodings.items(
                ):
                    # loop through the face encodings in the image
                    for face_encoding_in_image in face_encodings_in_image:
                        # compare the face encoding to the first face encoding
                        match = face_recognition.compare_faces(
                            [client_encoding],
                            face_encoding_in_image,
                            tolerance=0.25)
                        # print the match
                        if match[0]:
                            image_names.add(img_name)

        # Copy the image to the client folder so that each client has a folder of their pictures labeled client1, client2 ...
        # Create the client folder if it does not exist
        if not os.path.exists(f'../../sorted/{file.split(".")[0]}'):
            os.makedirs(f'../../sorted/{file.split(".")[0]}')
        # copy the image names in the image_names set to the client folder so that the dataset initial pictures remain

        for image_name in image_names:
            os.system(
                f'cp ../../dataset/dataset2/{image_name.split(".")[0]+".jpg"} ../../sorted/{file.split(".")[0]}/{image_name.split(".")[0]+".jpg"}'
            )
        # Clear the image names set
        image_names.clear()