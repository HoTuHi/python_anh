from tkinter import*
import numpy as np
import cv2

x = 'neu.jpg'
thamso = 1
img = cv2.imread(x, thamso)
# 1 : mau, 0 : gray, -1 : luoi anpha
cv2.imshow(img)
# show hinh voi kich thuoc cua hinh
cv2.waitKey(0)
# 0 cho doi vo thoi han, neu so khac thi neu nhu bam bat cu phim gi
# thi chtrinh se tiep tuc, k thi ket thuc
cv2.destroyAllWindows()
# k cho cua so khac bat lenNếu bạn muốn phá hủy bất kỳ cửa sổ cụ thể nào,
# sử dụng hàm cv2.destroyWindow ()
# trong đó bạn chuyển tên cửa sổ chính xác làm đối số.
cv2.imwrite('messigray.png', img)
# xuat img voi ten messigray.png

#----chuyen video thanh tung frame---
# using the in-built webcam of my laptop)
cap = cv2.VideoCapture()
while(True):
    # Capture frame-by-frame
cv2.VideoWriter()
''' video demo
            from tkinter import filedialog
            from tkinter import *
            from cv2 import*
            import numpy as np
            font = cv2.FONT_HERSHEY_SIMPLEX
            types = (("jpeg files", "*.jpg"), ("all files", "*.*"))
            Tk().withdraw()
            filename = filedialog.askopenfilename(
                initialdir="/", title="Select file", filetypes=types)
            print(filename)
            cap = cv2.VideoCapture(filename)
            while(cap.isOpened()):
                ret, frame = cap.read()
                gray = frame
                cv2.putText(gray, 'OpenCV', (10, 500), font, 4,
                            (255, 255, 255), 2, cv2.LINE_AA)
                cv2.imshow('frame', gray)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            cap.release()
            cv2.destroyAllWindows()
'''
# event in cv2
'''['EVENT_FLAG_ALTKEY', 'EVENT_FLAG_CTRLKEY',
'EVENT_FLAG_LBUTTON', 'EVENT_FLAG_MBUTTON',
 'EVENT_FLAG_RBUTTON', 'EVENT_FLAG_SHIFTKEY',
  'EVENT_LBUTTONDBLCLK', 'EVENT_LBUTTONDOWN',
   'EVENT_LBUTTONUP', 'EVENT_MBUTTONDBLCLK',
    'EVENT_MBUTTONDOWN', 'EVENT_MBUTTONUP',
     'EVENT_MOUSEHWHEEL', 'EVENT_MOUSEMOVE',
      'EVENT_MOUSEWHEEL', 'EVENT_RBUTTONDBLCLK',
       'EVENT_RBUTTONDOWN', 'EVENT_RBUTTONUP']'''
# demo
        ''' import cv2
        import numpy as np
        # mouse callback function


        def draw_circle(event, x, y, flags, param):
            if event == cv2.EVENT_LBUTTONDBLCLK:
                cv2.circle(img, (x, y), 100, (255, 0, 0), -1)


        # Create a black image, a window and bind the function to window
        img = np.zeros((512, 512, 3), np.uint8)
        cv2.namedWindow('image')
        cv2.setMouseCallback('image', draw_circle)
        while(1):
            cv2.imshow('image', img)
            if cv2.waitKey(0):
                break
        cv2.destroyAllWindows() '''
        '''
        import cv2
import numpy as np
drawing = False  # true if mouse is pressed
mode = True  # if True, draw rectangle. Press 'm' to toggle to curve
ix, iy = -1, -1
# mouse callback function


def draw_circle(event, x, y, flags, param):
    global ix, iy, drawing, mode
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            if mode == True:
                cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), -1)
            else:
                cv2.circle(img, (x, y), 5, (0, 0, 255), -1)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        if mode == True:
            cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), -1)
        else:
            cv2.circle(img, (x, y), 5, (0, 0, 255), -1)


img = np.zeros((512, 512, 3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_circle)
while(1):
    cv2.imshow('image', img)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('m'):
        mode = not mode
    elif k == 27:
        break
cv2.destroyAllWindows()



import cv2
import numpy as np
from matplotlib import pyplot as plt

BLUE = [255, 0, 0]
img1 = cv2.imread('neu.jpg')
replicate = cv2.copyMakeBorder(img1, 10, 10, 10, 10, cv2.BORDER_REPLICATE)
reflect = cv2.copyMakeBorder(img1, 10, 10, 10, 10, cv2.BORDER_REFLECT)
reflect101 = cv2.copyMakeBorder(img1, 10, 10, 10, 10, cv2.BORDER_REFLECT_101)
wrap = cv2.copyMakeBorder(img1, 10, 10, 10, 10, cv2.BORDER_WRAP)
constant = cv2.copyMakeBorder(
    img1, 10, 10, 10, 10, cv2.BORDER_CONSTANT, value=BLUE)
plt.subplot(231), plt.imshow(img1, 'gray'), plt.title('ORIGINAL')
plt.subplot(232), plt.imshow(replicate, 'gray'), plt.title('REPLICATE')
plt.subplot(233), plt.imshow(reflect, 'gray'), plt.title('REFLECT')
plt.subplot(234), plt.imshow(reflect101, 'gray'), plt.title('REFLECT_101')
plt.subplot(235), plt.imshow(wrap, 'gray'), plt.title('WRAP')
plt.subplot(236), plt.imshow(constant, 'gray'), plt.title('CONSTANT')
plt.show()
plt.de


import cv2


img1 = cv2.imread('neuvexam.jpg')
img2 = cv2.imread('neu.jpg')
dst = cv2.addWeighted(img1, 0.6, img2, 0.1, 0)
cv2.imshow('dst', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

'''

91/273

