import os
import numpy as np
import cv2
import time
face_detector = cv2.CascadeClassifier(os.path.join(
    os.getcwd(), 'cascade', 'haarcascade_frontalface_default.xml'))
# trja path C:\Users\MOHAMED\Desktop\face_rog\cascade\haarcascade_frontalface_default.xml


def collect(face_id):
    cam = cv2.VideoCapture(0)
    print("\n [INFO] Initializing face capture. Look the camera and wait ...")
    count = 0

    while (True):

        ret, img = cam.read()
        # time.sleep(2)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_detector.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            count += 1

            # Save the captured image into the datasets folder
            cv2.imwrite(os.path.join(os.getcwd(), 'facerog', 'trainer', 'dataset', str(face_id) +
                        '.' + str(count) + ".jpg"), gray[y:y + h, x:x + w])

            cv2.imshow('image', img)

        k = cv2.waitKey(100) & 0xff  # Press 'ESC' for exiting video
        if k == 27:
            break
        elif count >= 30:  # Take 30 face sample and stop video
            break

    # Do a bit of cleanup
    cam.release()
# data('test')
