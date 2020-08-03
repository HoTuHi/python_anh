import numpy as np
# import tensor
from cv2 import*
from tkinter import*
# from tkinter import filedialog
# from matplotlib import pyplot as plt


def detectLetters(img):
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_sobel = cv2.Sobel(img_gray, CV_8U, 1, 0, 3, 1, 0, cv2.BORDER_DEFAULT)
    kernel = np.ones((5, 5), np.uint8)
    img_threshold = cv2.threshold(img_sobel, 0, 255, 0)
    erosion = cv2.erode(img_threshold, kernel, iterations=1)
    dilation = cv2.dilate(img_threshold, kernel, iterations=1)

    img_threshold = cv2.morphologyEx(img_threshold, cv2.MORPH_CLOSE, kenel)
    _, contours = cv2.findContours(
        img_threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    img = cv2.drawContours(img, contours, -1, (0, 255, 0), 1)
    return img


path = 'sodoku.jpg'
aaaaa = cv2.imread(path)
img = cv2.imread(path)
# img = ~img
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_sobel = cv2.Sobel(img_gray, CV_8U, 1, 0, cv2.BORDER_DEFAULT)
# cv2.imshow('hahxa', img_sobel)
kernel = np.ones((5, 5), np.uint8)
_, img_threshold = cv2.threshold(img_sobel, 220, 255, 0)
img_threshold = cv2.morphologyEx(img_threshold, cv2.MORPH_CLOSE, kernel)
cv2.imshow('hahad', img_threshold)
contours, s = cv2.findContours(img_threshold, 0, 1)
img = cv2.drawContours(aaaaa, contours, -1, (0, 0, 255), 1)
cv2.imshow('haha', img)


cv2.waitKey(0)
cv2.destroyAllWindows()
