import numpy as np
# import tensor
from cv2 import*
from tkinter import*
from tkinter import filedialog

# types = (("all files", "*.*"), ("jpeg files", "*.jpg"))
# Tk().withdraw()

# filename = filedialog.askopenfilename(
#     initialdir="/", title="Select file", filetypes=types)
img = cv2.imread('chucorong.png', 0)


# cat anh thanh cac cell
cell = [np.hsplit(row, 100) for row in np.vsplit(img, 55)]
# k = cv2.imwrite('yeuem.jpg', cell[12][12])
x = np.array(cell)


# chuyen mang 2 chieu thanh 1 chieu
train = x[:, :100].reshape(-1, 400).astype(np.float32)

# gan nhan cho du lieu
k = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
tran_labels = np.repeat(k, 500)[:, np.newaxis]

# begin
knn = cv2.ml.KNearest_create()
knn.train(train, 0, tran_labels)
# ketqua1, ketqua2, ketqua3, ketqua4 = knn.findNearest(texx, 5)
# test 2
# trial = cv2.imread(filename, 0)
# trial = cv2.resize(trial, (200, 200))
# cv2.imshow("finaly", trial)
# ckss = [np.hsplit(i, 10) for i in np.vsplit(trial, 10)]
# # cv2.imwrite("anh2.jpg",ckss[0][1])
# css = np.array(ckss)
# kss = css[:, :10].reshape(-1, 400).astype(np.float32)
# retval, results, neigh_resp, dists = knn.findNearest(kss, 1)
# print(format(results))

# cv2.waitKey(0)
# cv2.destroyAllWindows()

# test 1
# trial = cv2.imread(filename, 0)
# trial = ~trial
# cv2.imshow("paint", trial)
# trial = cv2.resize(trial, (20, 20))
# trial = np.array(trial)
# test = trial.reshape(-1, 400).astype(np.float32)
# kqts = knn.findNearest(test, 5)
# print(int(kqts[1]))
# cv2.waitKey(0)
# cv2.destroyAllWindows()


def xxxx(trial):
    trial = ~ trial
    test = trial.reshape(-1, 400).astype(np.float32)
    kqts = knn.findNearest(test, 1)
    # print(int(kqts[1]))
    return (kqts[1].astype(int))
