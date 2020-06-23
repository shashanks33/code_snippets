import cv2
from cv2 import CascadeClassifier, imread, rectangle, waitKey, imshow, 

pixels = imread('E:\\Project\\face_detection\\images\\IMG-20200129-WA0014.jpg')

classifier = cv2.CascadeClassifier('E:\\Project\\face_detection\\haarcascade_frontalface_default.xml')

bboxes = classifier.detectMultiScale(pixels, 1.15, 5)
for box in bboxes:
    x, y, width, height = box
    x2, y2 = x + width, y + height
    rectangle(pixels, (x, y), (x2, y2), (0,0,255), 1)

imshow('Face detected', pixels)

waitKey(0)
destroyAllWindows()
