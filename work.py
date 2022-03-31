import numpy as np
import cv2

# Load an color image in grayscale
img = cv2.imread('./opencv.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


faces = face_cascade.detectMultiScale(gray)

for (x,y,w,h) in faces:
    print("x" + str(x));
    print("y"+str(y));
    print("w"+str(w));
    print("h"+str(h));
    cv2.rectangle(img,(x,y),(x+w,y+h),(1,1,1),5)





# show image
cv2.imshow('image',img)
cv2.waitKey(0)


