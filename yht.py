import numpy as np
# import tensor
from cv2 import*
from tkinter import*
from tkinter import filedialog

# types = (("jpeg files", "*.jpg"), ("all files", "*.*"))
# Tk().withdraw()

# filename = filedialog.askopenfilename(
#     initialdir="/", title="Select file", filetypes=types)
xx = cv2.imread("sodoku.jpg", 1)
# xx = ~xx
trial = cv2.cvtColor(xx, cv2.COLOR_BGR2GRAY)
# tim nguong 200 - 255 (mau den)
k, trial = cv2.threshold(trial, 200, 255, 0)
# tim duong vien cua kin
contours, hierarchy = cv2.findContours(
    trial, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# print(contours)
#ve cac duong vien
img = cv2.drawContours(xx, contours, -1, (0, 255, 0), 1)

cv2.imshow('test', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
