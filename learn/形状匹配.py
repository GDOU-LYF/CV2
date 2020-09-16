import cv2
import numpy as np

img=cv2.imread('img\\shapes.jpg',0)
_,thresh =cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
contours,hierarchy=cv2.findContours(thresh,3,2)
lor=cv2.cvtColor(thresh,cv2.COLOR_GRAY2BGR)

cnt_a,cnt_b,cnt_c=contours[0],contours[1],contours[2]
print(cv2.matchShapes(cnt_b,cnt_b,1,0.0))
print(cv2.matchShapes(cnt_b,cnt_c,1,0.0))
print(cv2.matchShapes(cnt_b,cnt_a,1,0.0))