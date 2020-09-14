import cv2
import numpy as np

img=cv2.imread('img\\j.bmp',0)
# kernel=np.ones((5,5),np.uint8) 
# kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))  # 矩形结构
# kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))  # 椭圆结构
kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (5, 5))  # 十字形结构
erosion=cv2.erode(img,kernel)
dilation=cv2.dilate(img,kernel)
cv2.imshow('img',np.hstack((img,erosion,dilation)))
cv2.waitKey(0)

