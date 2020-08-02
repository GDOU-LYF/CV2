import cv2
import numpy as np
import matplotlib.pyplot as plt

img=np.zeros((200,200,3),np.uint8)


cv2.ellipse(img, (50,50), (45, 45), 0, 0, 300, (0, 0, 255),\
     -1,lineType=cv2.LINE_AA)

cv2.ellipse(img, (150,50), (45, 45), 90, 0, 300, (0, 0, 255),\
     -1,lineType=cv2.LINE_AA)
     
cv2.ellipse(img, (50,150), (45, 45), 180, 0, 300, (0, 0, 255),\
     -1,lineType=cv2.LINE_AA)

cv2.ellipse(img, (150,150), (45, 45), 270, 0, 300, (0, 0, 255),\
     -1,lineType=cv2.LINE_AA)



cv2.imshow('img', img)
cv2.waitKey(0)