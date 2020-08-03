import cv2
import numpy as np
# Bước 1: Tấm ảnh và tệp tin xml
face_cascade = cv2.CascadeClassifier(
    "haarcascade_frontalface_default.xml")
image = cv2.imread("neu.jpg")
# Bước 2: Tạo một bức ảnh xám
image2 = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# Bước 3: Tìm khuôn mặt
faces = face_cascade.detectMultiScale(image2, 1.3, 5)

# '''Tham số thứ nhất là nguồn / bức ảnh xám.
# scaleFactor: độ scale sau mỗi lần quét, tính theo 0.01 = 1 % .
#  Nếu như để scaleFactor = 1 thì tấm ảnh sẽ giữ nguyên
# minNeighbors: scale và quét ảnh cho đến khi không thể scale
# được nữa thì lúc này sẽ xuất hiện những khung ảnh trùng nhau,
#  số lần trùng nhau chính là tham số minNeighbors để quyết định
#  cho việc có chọn khung ảnh này là khuôn mặt hay không.'''
# Bước 4: Vẽ các khuôn mặt đã nhận diện được lên tấm ảnh gốc
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

# Bước 5: Vẽ lên màn hình
cv2.imshow("Faces found", image)

cv2.waitKey(0)
cv2.destroyAllWindows()
