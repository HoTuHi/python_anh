from tkinter import filedialog
from tkinter import *
from cv2 import*
import numpy as np

face_cascade = cv2.CascadeClassifier(
    "haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier(
    "haarcascade_eye.xml")

font = cv2.FONT_HERSHEY_SIMPLEX
types = (("jpeg files", "*.jpg"), ("all files", "*.*"))
Tk().withdraw()

filename = filedialog.askopenfilename(
    initialdir="/", title="Select file", filetypes=types)

print(filename)

cap = cv2.VideoCapture(filename)
while(cap.isOpened()):
    ret, frame = cap.read()
    pre = 700 / frame.shape[1]
    # x.shape[0:1],x.shape[1:1]
    w = int(frame.shape[0] * pre)
    h = int(frame.shape[1] * pre)
    frame = cv2.resize(frame, (h, w))
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 7)
    eye = eye_cascade.detectMultiScale(gray, 1.3, 7)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    for (x, y, w, h) in eye:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
