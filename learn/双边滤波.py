import cv2
import numpy as np
img=cv2.imread('lena.jpg',0)
img=cv2.copyMakeBorder(img,5,5,5,5,cv2.BORDER_CONSTANT,value=(255,255,255))
gaussian=cv2.GaussianBlur(img,(5,5),0)
blur=cv2.bilateralFilter(img,9,75,75)
ret=np.hstack((img,gaussian,blur))

cv2.imshow('ret',ret)
cv2.waitKey(0)