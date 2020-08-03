from tkinter import filedialog
from tkinter import *
from cv2 import*
import numpy as np
types = (("jpeg files", "*.jpg"), ("all files", "*.*"))
Tk().withdraw()
face_cascade = cv2.CascadeClassifier(
    "haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier(
    "haarcascade_eye.xml")
filename = filedialog.askopenfilename(
    initialdir="/", title="Select file", filetypes=types)
print(filename)
xa = cv2.imread(filename, 1)
pre = 700 / xa.shape[1]
print(xa[1][1])
# x.shape[0:1],x.shape[1:1]
w = int(xa.shape[0] * pre)
h = int(xa.shape[1] * pre)
xa = cv2.resize(xa, (h, w))
xs = cv2.cvtColor(xa, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(
    xs,
    scaleFactor=1.1,
    minNeighbors=5,
)
eye = eye_cascade.detectMultiScale(xs, 1.3, 5)
print(faces)
print(eye)
# Bước 4: Vẽ các khuôn mặt đã nhận diện được lên tấm ảnh gốc
for (x, y, w, h) in faces:
    cv2.rectangle(xa, (x, y), (x + w, y + h), (0, 255, 0), 2)
for (x, y, w, h) in eye:
    cv2.rectangle(xa, (x, y), (x + w, y + h), (255, 0, 0), 2)

# Bước 5: Vẽ lên màn hình
cv2.imshow("this is my vsa", xa)
# cv2.resizeWindow('image', w,h)
cv2.waitKey(0)
cv2.destroyAllWindows()
