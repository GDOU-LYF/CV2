import cv2
img=cv2.imread('lena.jpg')
face=img[100:200,115:188]
cv2.imshow('face',face)
cv2.waitKey(0)
