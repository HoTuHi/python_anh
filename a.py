import numpy as np
import cv2
import random
im = cv2.imread("neu.jpg", 1)
ha= cv2.imread("neu.ipg",1)
for i in range(950):
    for j in range(960):
        if im[i, j, 0] > 210:
            im[i, j, 0] = 0
            im[i, j, 1] = 0
            im[i, j, 2] = 0
for i in range(950):
    for j in range(960):
        if im[i, j, 0] == 0:
            im[i, j, 0] = random.randrange(244)
            im[i, j, 1] = random.randrange(244)
            im[i, j, 2] = random.randrange(244)
cv2.imwrite("neuemdi.jpg", im)
cv2.imshow("image", im)
cv2.waitKey(0)
cv2.destroyAllWindows()
