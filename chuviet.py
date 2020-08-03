import numpy as np
import cv2
from matplotlib import pyplot as plt

im = cv2.imread("chu.png", 0)
# cho ảnh vào
cel = [np.hsplit(row, 100) for row in np.vsplit(im, 50)]
# cắt ảnh có kích thước 100, lấy 50 trong 100
cv2.imwrite("anh.jpg", cel[0][0])
# show ảnh thứ 0.0
print(cel[0][0])
# in ảnh cel 0 0 ra
x = np.array(cel)
# convert to array
# chuyển x từ mảng 2 chiều về mảng 1 chiều có 400 điểm ảnh , -1 là để tự tính
xx = x[0, 0].reshape(-1, 400)
print(xx)
# cv2.waitKey()
# cv2.destroyAllWindows
