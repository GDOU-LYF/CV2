import cv2
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread('img\\mario.jpg')
img_gary=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
template=cv2.imread('img\\mario_coin.jpg',0)
h,w=template.shape[:2]

res=cv2.matchTemplate(img_gary,template,cv2.TM_CCOEFF_NORMED)
threshold=0.8
# min_val,max_val,min_loc,max_loc=cv2.minMaxLoc(res)

# left_top=max_loc
loc=np.where(res>=threshold)
for pt in zip(*loc[::-1]):
    right_bottom=(pt[0]+w,pt[1]+h)
    cv2.rectangle(img,pt,right_bottom,(0,152,243,255),-1)
cv2.imshow('img',img)
cv2.waitKey(0)

