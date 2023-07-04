import face_recognition
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.conf import settings
from .models import User
import numpy as np
from PIL import Image
import requests
from io import BytesIO


def recognize_user(image: InMemoryUploadedFile) -> User:
    # Load all the known images and encode them
    users = User.objects.all()
    known_face_encodings = []
    known_user_ids = []
    for user in users:
        if user.profile_pic:
            image_url = (
                settings.CLOUDINARY_BASE_URL
                + user.profile_pic.public_id
                + "."
                + user.profile_pic.format
            )
            response = requests.get(image_url)
            user_image = Image.open(
                BytesIO(response.content)
            )  # rename the variable here
            face_encoding = face_recognition.face_encodings(np.array(user_image))[0]
            known_face_encodings.append(face_encoding)
            known_user_ids.append(user.id)

    # Load the image to be recognized and encode it
    image_bytes = image.read()
    image_np = np.array(Image.open(BytesIO(image_bytes)))
    face_locations = face_recognition.face_locations(image_np)
    face_encodings = face_recognition.face_encodings(image_np, face_locations)

    # Loop through each face in the test image to see if it matches any of the known faces
    for face_encoding, face_location in zip(face_encodings, face_locations):
        # See if the face is a match for the known face(s)
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        face_distances = face_recognition.face_distance(
            known_face_encodings, face_encoding
        )

        # Use the known face with the smallest distance to the new face
        best_match_index = np.argmin(face_distances)
        if matches[best_match_index]:
            user_id = known_user_ids[best_match_index]
            user = User.objects.get(id=user_id)
            return user

    return None
