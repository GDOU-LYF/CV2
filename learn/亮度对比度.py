import cv2
import matplotlib.pyplot as plt
import numpy as np

img =cv2.imread('lena.jpg')
alpha,beta=100,0

def light(x):
    global beta
    beta=x
    tran()

def comparison(x):
    global alpha
    alpha=x
    tran()

def tran():
    global alpha,beta
    res=np.uint8(np.clip((alpha*0.01*img+beta*0.01),0,255))
    tmp=np.hstack((img,res))
    cv2.imshow('painting',tmp)

cv2.namedWindow('painting')
cv2.createTrackbar('comparison', 'painting', 0, 300, comparison)
cv2.setTrackbarPos('comparison', 'painting',alpha)
cv2.createTrackbar('light', 'painting', 0, 300, light)
tmp=np.hstack((img,img))
cv2.imshow('painting',tmp)
cv2.waitKey(0)
