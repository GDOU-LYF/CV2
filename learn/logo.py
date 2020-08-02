import cv2
import numpy as np
import matplotlib.pyplot as plt

img=np.zeros((200,200,3),np.uint8)

#红色
cv2.ellipse(img, (90,40), (45, 45), 120, 0, 300, (0, 0, 255),\
     -1,lineType=cv2.LINE_AA)
cv2.circle(img, (90, 40), 15, (0, 0, 0),\
    -1,lineType=cv2.LINE_AA)
#绿色
cv2.ellipse(img, (43,125), (45, 45), 0, 0, 300, (0,255,  0),\
    -1,lineType=cv2.LINE_AA)
cv2.circle(img, (43, 125), 15, (0, 0, 0),\
    -1,lineType=cv2.LINE_AA)
#蓝色
cv2.ellipse(img, (137,125), (45, 45), -60, 0, 300, (255, 0, 0),\
    -1,lineType=cv2.LINE_AA)
cv2.circle(img, (137, 125), 15, (0, 0, 0),\
    -1,lineType=cv2.LINE_AA)

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.imwrite('black.jpg',img)