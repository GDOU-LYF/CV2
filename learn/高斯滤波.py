import cv2
import numpy as np
img=cv2.imread('img\\gaussian_noise.bmp')
img=cv2.copyMakeBorder(img,5,5,5,5,cv2.BORDER_CONSTANT,value=(255,255,255))
blur=cv2.blur(img,(5,5))
gaussian=cv2.GaussianBlur(img,(5,5),1)
ret=np.hstack((img,blur,gaussian))

cv2.imshow('ret',ret)
cv2.waitKey(0)