import cv2
import numpy as np

def nothing(x):
    r=cv2.getTrackbarPos('R','image')
    g=cv2.getTrackbarPos('G','image')
    b=cv2.getTrackbarPos('B','image')
    img[:]=[b,g,r]
    cv2.imshow('image',img)
    return (r,g,b)

img=np.zeros((300,512,3),np.uint8)
cv2.namedWindow('image')
cv2.createTrackbar('R','image',0,255,nothing)
cv2.createTrackbar('G','image',0,255,nothing)
cv2.createTrackbar('B','image',0,255,nothing)

cv2.imshow('image',img)
k=cv2.waitKey(0)#等待按下按键
cv2.destroyWindow('image') #销毁指定窗口
