import cv2
import numpy as np

img=cv2.imread('img\\school.bmp',0)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))  
tophat=cv2.morphologyEx(img,cv2.MORPH_TOPHAT,kernel)
blackhat=cv2.morphologyEx(img,cv2.MORPH_BLACKHAT,kernel)
cv2.imshow('img1',np.hstack((img,tophat,blackhat)))

cv2.waitKey(0)

