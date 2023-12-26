
import cv2
import numpy as np
import os
from db import DataBase

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read(os.path.join(os.getcwd(), 'facerog', 'trainer', 'trainer.yml'))
faceCascade = cv2.CascadeClassifier(os.path.join(
    os.getcwd(), 'cascade', 'haarcascade_frontalface_default.xml'))


def predict(db:DataBase):
    cam = cv2.VideoCapture(0)


    while True:
        ret, img = cam.read()

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.2,
            minNeighbors=5,
        )

        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (118, 41, 155), 2)
            face_id, confidence = recognizer.predict(gray[y:y + h, x:x + w])
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

            if (confidence <= 80):
                name = db.get_face_name(face_id)
                cv2.putText(img,str(name)+str(confidence),(x,y-10),cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,0.9,(0,0,0),2)
            else:
                name="unkown"
        cv2.imshow('prediction', img)

        k = cv2.waitKey(10) & 0xff  # Press 'ESC' for exiting video
        if k == 27:
            break
    print("\n [INFO] Exiting Program and cleanup stuff")
    cam.release()
    cv2.destroyAllWindows()
