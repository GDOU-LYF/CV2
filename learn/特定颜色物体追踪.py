import cv2
import numpy as np
import matplotlib.pyplot as plt
# capture=cv2.VideoCapture(1)
capture=cv2.imread('getblue.png')
lower_blue=np.array([100,110,110])
upper_blue=np.array([130,255,255])

frame=capture
hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

mask=cv2.inRange(hsv,lower_blue,upper_blue)

res=cv2.bitwise_and(frame,frame,mask=mask)

# cv2.imshow('frame',frame)
# cv2.imshow('mask',mask)
# cv2.imshow('res',res)

titles=['frame','mask','res']
images=[frame,mask,res]
for i in range(len(images)):
    plt.subplot(2, 2, i + 1)
    plt.imshow(cv2.cvtColor(eval(titles[i]), cv2.COLOR_BGR2RGB))
    plt.title(titles[i], fontsize=8)
    plt.xticks([]), plt.yticks([])
plt.show()
cv2.waitKey(0)