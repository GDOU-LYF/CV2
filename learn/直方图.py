import cv2
import numpy as np
import matplotlib.pyplot as plt
img=cv2.imread('img\\hist.jpg',0)
# mask=np.zeros(img.shape,dtype=np.uint8)
# mask[:200,:200]=255
# hist=cv2.calcHist([img],[0],mask,[256],[0,256])
# plt.plot(hist)
clahe=cv2.createCLAHE(clipLimit=2.0,tileGridSize=(8,8))
cl1=clahe.apply(img)
# equ=cv2.equalizeHist(img)
cv2.imshow('equ',np.hstack((img,cl1)))
cv2.waitKey(0)
# plt.hist(equ.ravel(),256,[0,256])
# plt.show()