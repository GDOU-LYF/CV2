import cv2
import numpy as np
import matplotlib.pyplot as plt

img=np.zeros((180,172,3),np.uint8)
# cv2.circle(img, (90, 50), 40, (0, 0, 255),-1)
# cv2.circle(img, (90, 50), 25, (0, 0, 0),-1)

# cv2.circle(img, (40, 128), 40, (0, 255, 0),-1)
# cv2.circle(img, (130, 128),40, (255, 0, 0),-1)
#RGB ->BGR
cv2.ellipse(img, (90,45), (40, 40), 0, 120, 420, (0, 0, 255), -1)
cv2.circle(img, (90, 45), 15, (0, 0, 0),-1)
cv2.ellipse(img, (45,135), (40, 40), 0, 0, 300, (0,255,  0), -1)
cv2.circle(img, (45, 135), 15, (0, 0, 0),-1)
cv2.ellipse(img, (135,135), (40, 40), 0, -120, -420, (255, 0, 0), -1)
cv2.circle(img, (135, 135), 15, (0, 0, 0),-1)

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.imwrite('black.jpg',img)