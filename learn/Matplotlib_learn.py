#显示图片
import cv2
import matplotlib.pyplot as plt
img0 = cv2.imread('lena.jpg',0)
img = cv2.imread('lena.jpg')
# 灰度图显示，cmap(color map)设置为gray
plt.subplot(121)
plt.imshow(img0, cmap='gray')
#plt.show()

#彩色图片
plt.subplot(122)
plt.xticks([]), plt.yticks([])# 隐藏x和y轴
img2=img[:,:,::-1] #BGR->RGB
plt.imshow(img2)
plt.show()