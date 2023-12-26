
import os
import cv2
import numpy as np
from PIL import Image
import os


def train():
    data_set_path = os.path.join(os.getcwd(),'facerog', 'trainer','dataset')

    recognizer = cv2.face.LBPHFaceRecognizer_create()
    detector = cv2.CascadeClassifier(os.path.join(
        os.getcwd(), 'cascade', 'haarcascade_frontalface_default.xml'))

    # function to get the images and label data
    def getImagesAndLabels(path):

        imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
        faceSamples = []
        Ids = []

        for imagePath in imagePaths:

            PIL_img = Image.open(imagePath).convert('L')
            img_numpy = np.array(PIL_img, 'uint8')

            face_id = os.path.split(imagePath)[-1].split(".")[0]
            
            faces = detector.detectMultiScale(
                img_numpy, scaleFactor=1.5, minNeighbors=5)

            for (x, y, w, h) in faces:
                faceSamples.append(img_numpy[y:y + h, x:x + w])
                Ids.append(int(face_id))

        return faceSamples, Ids

    print("\n [INFO] Training faces. It will take a few seconds. Wait ...")
    faces, Ids = getImagesAndLabels(data_set_path)
    print(Ids)
    recognizer.train(faces, np.array(Ids))

    # Save the model into trainer/trainer.yml
    trainer_path = os.path.join(os.getcwd(),'facerog','trainer','trainer.yml')
    recognizer.write(trainer_path)

    # Print the numer of faces trained and end program
    print("\n [INFO] {0} faces trained. Exiting Program".format(
        len(np.unique(Ids))))
    return True
