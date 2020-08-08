import cv2
import numpy as np

img =cv2.imread('lena.jpg')
img2=cv2.copyMakeBorder(img,5,5,5,5,cv2.BORDER_CONSTANT,value=0)
img3=cv2.copyMakeBorder(img,5,5,5,5,cv2.BORDER_DEFAULT)
img4=cv2.copyMakeBorder(img,5,5,5,5,cv2.BORDER_ISOLATED)
img5=cv2.copyMakeBorder(img,5,5,5,5,cv2.BORDER_WRAP)
ret1=np.hstack((img2,img3,img4,img5))
cv2.imshow('img',ret1)
cv2.waitKey(0)
