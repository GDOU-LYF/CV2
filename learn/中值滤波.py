import cv2
import numpy as np
img=cv2.imread('img\\salt_noise.bmp',0)
img=cv2.copyMakeBorder(img,5,5,5,5,cv2.BORDER_CONSTANT,value=(255,255,255))
blur=cv2.blur(img,(5,5))
medianblur=cv2.medianBlur(img,5)
ret=np.hstack((img,blur,medianblur))

cv2.imshow('ret',ret)
cv2.waitKey(0)