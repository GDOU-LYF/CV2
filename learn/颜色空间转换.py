import cv2
import matplotlib.pyplot as plt
img = cv2.imread('lena.jpg')
# # 转换为灰度图
# B,G,R=cv2.split(img)

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# img_gray=cv2.merge((B*0.114,G*0.587,R*0.299))
images=[img,img_gray]
titles=['img','gray']
for i in range(2):
    plt.subplot(121+i)
    plt.imshow(images[i],'gray')
    plt.title(titles[i],fontsize=8)
    plt.xticks([])
    plt.yticks([])
plt.show()
cv2.waitKey(0)
