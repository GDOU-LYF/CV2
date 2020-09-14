import cv2
import numpy as np

img=cv2.imread('img\\school.bmp',0)
# kernel=np.ones((5,5),np.uint8) 
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))  # 矩形结构
gradinent=cv2.morphologyEx(img,cv2.MORPH_GRADIENT,kernel)
cv2.imshow('img1',np.hstack((img,gradinent)))

cv2.waitKey(0)

