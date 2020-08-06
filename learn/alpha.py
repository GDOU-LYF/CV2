import numpy as np
import cv2

img =cv2.imread('text_red.png')
b_channel, g_channel, r_channel = cv2.split(img)
alpha_channel = np.ones(b_channel.shape, dtype=b_channel.dtype) * 255
alpha_channel[:, :int(b_channel.shape[0] / 2)] = 0
img_BGRA = cv2.merge((b_channel, g_channel, r_channel, alpha_channel))
cv2.imwrite("lena.png", img_BGRA)
cv2.imshow("img",img_BGRA)
cv2.waitKey(0)