import cv2
import numpy as np

# 1.加载图片，转为二值图
img = cv2.imread('img\\shapes1.jpg')
drawing = np.zeros(img.shape[:], dtype=np.uint8)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 50, 150)

# 2.霍夫直线变换
# lines = cv2.HoughLines(edges, 0.8, np.pi / 180, 90)

circles = cv2.HoughCircles(edges, cv2.HOUGH_GRADIENT, 1, 20, \
    param1=50,param2=30,minRadius=0,maxRadius=0)

print(circles)
circles = np.int0(np.around(circles))

for i in circles[0,:]:
    cv2.circle(drawing,(i[0],i[1]),i[2],(0,255,0),2)
    cv2.circle(drawing,(i[0],i[1]),2,(0,0,255),3)

cv2.imshow('img',np.hstack((img,drawing)))
cv2.waitKey(0)