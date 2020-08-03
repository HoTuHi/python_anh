from tkinter import *
from PIL import ImageTk, Image
import os
import cv2


def brightness(img, value=30):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)

    lim = 255 - value
    v[v > lim] = 255
    v[v <= lim] += value

    final_hsv = cv2.merge((h, s, v))
    img = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
    return img


root = Tk()
var1 = DoubleVar()
scale1 = Scale(root, activebackground="gray55", variable=var1,
               orient=HORIZONTAL, from_=0, to=100)
scale1.pack()
img = cv2.imread('neu.jpg')
img = brightness(img, 100)
panel = Label(root, image=img)
panel.pack(side="bottom", fill="both", expand="yes")
root.mainloop()
