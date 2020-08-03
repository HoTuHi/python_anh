import numpy as np
import cv2
import random
No = cv2.imread("neu.jpg", 1)
No = cv2.imread("neu.jpg", 1)
# blur
for i in range(948):
    for j in range(958):
        No[i + 1, j + 1, 0] = (No[i, j - 1, 0] / 9 + No[i, j, 0] / 9 + No[i, j + 1, 0] / 9 + No[i + 1, j - 1, 0] / 9 +
                               No[i + 1, j, 0] / 9 + No[i + 1, j + 1, 0] / 9 + No[i - 1, j - 1, 0] / 9 + No[i - 1, j, 0] / 9 + No[i - 1, j + 1, 0] / 8.7)
        No[i + 1, j + 1, 1] = (No[i, j - 1, 1] / 9 + No[i, j, 1] / 9 + No[i, j + 1, 1] / 9 + No[i + 1, j - 1, 1] / 9 +
                               No[i + 1, j, 1] / 9 + No[i + 1, j + 1, 1] / 9 + No[i - 1, j - 1, 1] / 9 + No[i - 1, j, 1] / 9 + No[i - 1, j + 1, 1] / 8.7)
        No[i + 1, j + 1, 2] = (No[i, j - 1, 2] / 9 + No[i, j, 2] / 9 + No[i, j + 1, 2] / 9 + No[i + 1, j - 1, 2] / 9 +
                               No[i + 1, j, 2] / 9 + No[i + 1, j + 1, 2] / 9 + No[i - 1, j - 1, 2] / 9 + No[i - 1, j, 2] / 9 + No[i - 1, j + 1, 2] / 8.7)
cv2.imwrite("daylablur.jpg", No)
# brightness
for i in range(948):
    for j in range(958):
        No[i + 1, j + 1, 0] += 1
        No[i + 1, j + 1, 1] += 1
        No[i + 1, j + 1, 2] += 1
cv2.imwrite("daylabrightness.jpg", No)
# Contrast
# thoi deo lam nua
cv2.imshow("image", No)
cv2.waitKey(0)
cv2.destroyAllWindows()
