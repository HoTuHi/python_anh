import numpy as np
import cv2
import random
No = cv2.imread("haha.jpg", cv2.IMREAD_UNCHANGED)
X = No.shape[0]
Y = No.shape[1]
scale_percent = 30
width = int(No.shape[1] * scale_percent / 100)
height = int(No.shape[0] * scale_percent / 100)
dim = (width, height)
enother = cv2.resize(No, dim)
f = open("demofile2.txt", "w")
for i in range(height - 1):
    for j in range(width - 1):
        x = enother[i, j, 0] * 0.3 + enother[i, j, 1] * \
            0.59 + enother[i, j, 2] * 0.11
        x = int(x)
        if x < 25:
            f.write(' @')
        if x >= 25 and x < 50:
            f.write(' w')
        if x >= 50 and x < 75:
            f.write(' #')
        if x >= 75 and x < 100:
            f.write(' $')
        if x >= 100 and x < 125:
            f.write(' k')
        if x >= 125 and x < 150:
            f.write(' d')
        if x >= 150 and x < 175:
            f.write(' t')
        if x >= 175 and x < 200:
            f.write(' j')
        if x >= 200 and x < 225:
            f.write(' i')
        if x >= 225 and x < 250:
            f.write(' .')
        if x > 250:
            f.write('  ')
    f.write('\n')
cv2.imwrite("neuemdi.jpg", enother)

# thoi deo lam nua
cv2.imshow("age", enother)
cv2.waitKey(0)
cv2.destroyAllWindows()
