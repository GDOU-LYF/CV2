import cv2
import numpy
img=cv2.imread('img\\handwriting.jpg')
# img=cv2.imread('text_red.png')
img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh =cv2.threshold(img_gray,0,255,\
    cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

contours,hierarchy=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
print(len(contours))
cv2.drawContours(img,contours,-1,(0,0,255),2)
cv2.imshow('img',img)
cv2.waitKey(0)
