import cv2
import numpy as np
from time import sleep

face_cascade_path = '/usr/local/lib/python3.7/site-packages/cv2/data/haarcascade_frontalface_default.xml'
eye_cascade_path = '/usr/local/lib/python3.7/site-packages/cv2/data/haarcascade_eye.xml'

face_cascade = cv2.CascadeClassifier(face_cascade_path)
#eye_cascade = cv2.CascadeClassifier(eye_cascade_path)

cap = cv2.VideoCapture(0)
ratio = 0.05

filename = "kabo.png"
imgcv = cv2.imread(filename)

thick = 0

finish_flag = False

while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

    for x, y, w, h in faces:
        #トホホ
        """
        img[0: -1, 0: x] = [0, 0, 0]
        img[0: -1, x+w: -1] = [0, 0, 0]
        #img[0:y, x:x+w] = [0,0,0]
        #img[y+h:-1, x:x+w] = [0,0,0]
        rcircle = int(w/2)
        img[0:h-rcircle, x:x+w] = [0,0,0]
        img[y+h:-1, x:x+w] = [0,0,0]
        """
        #cv2.circle(img, (int(w/2+x), int(h)), int(w/2), (0,0,0), thickness=10, lineType=cv2.LINE_AA)

        cv2.circle(img, (int(w/2+x), int(h)), int(w+x), (0,0,0), thickness=thick, lineType=cv2.LINE_AA)
        if thick < 1400:
            thick += 200
            print(thick)
            sleep(0.1)
        if (thick > 1399) and (thick < 1800):
            key_circle = cv2.waitKey(1)
            if key_circle == 32:
                sleep(0.1)
                finish_flag = True
                thick += 200
                sleep(0.1)
                thick += 200
                sleep(0.1)
                thick += 200
                print(thick)
        if finish_flag:
            cv2.putText(img, 'END', (200, 700), cv2.FONT_HERSHEY_SIMPLEX, 5.0, (255, 255, 255), thickness=5)


        #img[y: y+h, x: x+w] = [0, 128, 255] #顔を隠す

        #モザイク
        #small = cv2.resize(img[y: y+h, x: x+w], None, fx=ratio, fy=ratio, interpolation=cv2.INTER_NEAREST)
        #img[y: y+h, x: x+w] = cv2.resize(small, (w,h), interpolation=cv2.INTER_NEAREST)

        #cv2.rectangle(img, (x,y), (x + w, y + h), (255, 0, 0), 2)
        #face = img[y: y+h, x: x+w]
        #face_gray = gray[y: y+h, x: x+w]
        #eyes = eye_cascade.detectMultiScale(face_gray)
        #for (ex, ey, ew, eh) in eyes:
            #cv2.rectangle(face, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

    cv2.imshow('video image', img)
    key = cv2.waitKey(10)
    if key == 27: #ESCキーで終了
        break


cap.release()
cv2.destroyAllWindows()
