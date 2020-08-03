import cv2
import random
import numpy as np

im = cv2.imread("be.jpg", 1)
im = im[50: 450, 50: 650]
for i in range(1000):
    x = random.randrange(1, 50, 1)
    y = random.randrange(10, 100, 10)
    im[x, 8 * x + y, 0] = 0
    im[x, 8 * x + y, 1] = 0
    im[x, 8 * x + y, 2] = 0
for i in range(1000):
    x = random.randrange(1, 35, 1)
    y = random.randrange(10, 100, 10)
    im[x, 12 * x + y, 0] = 0
    im[x, 12 * x + y, 1] = 0
    im[x, 12 * x + y, 2] = 0
cv2.imwrite("mua.jpg", im)
cv2.imshow("image", im)
cv2.waitKey(0)
