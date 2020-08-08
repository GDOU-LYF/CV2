import cv2
import numpy as np
img =cv2.imread('lena.jpg')
kernel=np.ones((3,3),np.float32)/10
dst=cv2.filter2D(img,-1,kernel)
ret=np.hstack((img,dst))
cv2.imshow('ret',ret)
cv2.waitKey(0)