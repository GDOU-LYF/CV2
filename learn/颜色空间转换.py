import cv2

img = cv2.imread('lena.jpg')
# # 转换为灰度图
# B,G,R=cv2.split(img)

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# img_gray=cv2.merge((B*0.114,G*0.587,R*0.299))
cv2.imshow('img', img)
cv2.imshow('gray', img_gray)
cv2.waitKey(0)
