import cv2
import numpy as np

img =cv2.imread('lena.jpg')
blur=cv2.blur(img,(3,3))

ret=np.hstack((img,blur))

cv2.imshow('ret',ret)
cv2.waitKey(0)
