import cv2
import numpy as np

img=cv2.imread('img\\j_noise_out.bmp',0)
# kernel=np.ones((5,5),np.uint8) 
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))  # 矩形结构
opening=cv2.morphologyEx(img,cv2.MORPH_OPEN,kernel)#开运算,腐蚀后膨胀
img2=cv2.imread('img\\j_noise_in.bmp',0)
closing=cv2.morphologyEx(img2,cv2.MORPH_CLOSE,kernel)#闭运算,膨胀后腐蚀

cv2.imshow('img1',np.hstack((img,opening)))
cv2.imshow('img2',np.hstack((img2,closing)))
cv2.waitKey(0)

