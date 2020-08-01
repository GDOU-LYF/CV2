#线性变换+平移
import cv2
import numpy as np
import matplotlib.pyplot as plt

img= cv2.imread('black.png')
rows,cols=img.shape[:2]

pst1=np.float32([[50,65],[150,65],[210,210]])
pst2=np.float32([[50,100],[150,65],[100,250]])

M=cv2.getAffineTransform(pst1,pst2)
dst=cv2.warpAffine(img,M,(cols,rows))

plt.subplot(221)
plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
plt.title("input")
plt.xticks([]), plt.yticks([])
plt.subplot(222)
plt.imshow(cv2.cvtColor(dst,cv2.COLOR_BGR2RGB))
plt.title("output")
plt.xticks([]), plt.yticks([])

plt.show()
