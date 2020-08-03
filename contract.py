from tkinter import*
import numpy as np
import cv2
import random
import time
window = Tk()
cv = Canvas(window)
var1 = IntVar()
scale1 = Scale(window, activebackground="gray55", variable=var1,
               orient=HORIZONTAL, from_=0, to=100)
scale1.pack()


def brightness(img, value=30):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    # convert sang hsv color space
    print(hsv)
    h, s, v = cv2.split(hsv)
    # tach h s v (brightness) ra khoi hsv
    lim = 255 - value
    # gioi han = 255-value
    v[v > lim] = 255
    v[v <= lim] += value
    #gop hsv thang final hsv va chuyen sang RGB color
    final_hsv = cv2.merge((h, s, v))
    img = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
    return img



im = cv2.imread("neu.jpg", 1)
ha = cv2.imread("neu.jpg", 1)
im = cv2.resize(im, (450, 450))

k = 0
x = 0

while True:
    im = brightness(im, k)
    cv2.imshow("contrast", im)
    cv2.waitKey(100)
    k += 100
    if k > 1000:
        break


window.mainloop()

# cv2.destroyAllWindows()
