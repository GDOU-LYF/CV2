import cv2
img=cv2.imread('lena.jpg')
hat=img[22:160,55:291,2]
cv2.imshow('hat',hat)
cv2.waitKey(0)