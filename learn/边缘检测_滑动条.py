import cv2
import numpy as np

img=cv2.imread('img\\sudoku.jpg',0)

smin,smax=0,50
def setmin(x):
    global smin
    smin=x
    setimg()

def setmax(x):
    global smax
    smax=x
    setimg()


def setimg():
    global smin,smax,edges
    edges = cv2.Canny(img, smin, smax)
    cv2.imshow('img',edges)

cv2.namedWindow('img')
cv2.createTrackbar('SetMin','img',0,100,setmin)
cv2.createTrackbar('SetMax','img',0,100,setmax)
cv2.setTrackbarPos('SetMax','img',50)
edges = cv2.Canny(img,smin,smax)

while True:
    cv2.imshow('img',edges)
    if cv2.waitKey(30)==27:
        break



