import cv2
import numpy as np

img =cv2.imread('lena.jpg')
# print(img.depth())
blur=cv2.boxFilter(img,-1,(3,3),normalize=False)

ret=np.hstack((img,blur))

cv2.imshow('ret',ret)
cv2.waitKey(0)
