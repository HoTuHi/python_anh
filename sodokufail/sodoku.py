import numpy as np
# import tensor
from cv2 import*
from tkinter import*
import remove as rm
import writer as wt
import giai as gt
# getStructuringElement value
x = 20
path = 'sodokunot7.jpg'
# aaaaa = cv2.mread(path)
img = cv2.imread(path, 0)
result = img.copy()
img = rm.renmove_lines(img, x)
img = cv2.resize(img, (180, 180))
# cut the image to sigle number
cell = [np.hsplit(row, 9) for row in np.vsplit(img, 9)]
x = np.array(cell)
alist = []
#  detect number in image
for i in x:
    a = wt.xxxx(i)
    retime = a.tolist()
    alist.append(retime)
    print(retime)

cv2.imshow('haha', img)
cv2.imshow('haha2', result)

# gt.solve_sudoku(alist, 0, 0)
cv2.waitKey(0)
cv2.destroyAllWindows()
