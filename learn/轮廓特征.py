import cv2
import numpy as np

img = cv2.imread('img\\handwriting.jpg', 0)
_, thresh = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
contours, hierarchy = cv2.findContours(thresh, 3, 2)


img_color1=cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
img_color2 = np.copy(img_color1)
cnt=contours[1]
cv2.drawContours(img_color1,[cnt],0,(0,0,255),2)
area=cv2.contourArea(cnt)
perimeter=cv2.arcLength(cnt,True)
x, y, w, h = cv2.boundingRect(cnt)
cv2.rectangle(img_color1, (x, y), (x + w, y + h), (0, 255, 0), 2)
cv2.imshow('img',img_color1)
cv2.waitKey(0)
