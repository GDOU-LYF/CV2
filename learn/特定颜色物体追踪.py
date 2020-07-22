import cv2
import numpy as np
# capture=cv2.VideoCapture(1)
capture=cv2.imread('getblue.png')
lower_blue=np.array([100,110,110])
upper_blue=np.array([130,255,255])

frame=capture
hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

mask=cv2.inRange(hsv,lower_blue,upper_blue)

res=cv2.bitwise_and(frame,frame,mask=mask)

cv2.imshow('frame',frame)
cv2.imshow('mask',mask)
cv2.imshow('res',res)
cv2.waitKey(0)