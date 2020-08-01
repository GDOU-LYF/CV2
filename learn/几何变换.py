import cv2
import matplotlib.pyplot as plt
import numpy as np
#缩放图片
img =cv2.imread('drawing.jpg')
res=cv2.resize(img,(75,150))
res2=cv2.resize(img,None,fx=2,fy=2,\
    interpolation=cv2.INTER_LINEAR)

#翻转图片
img2=cv2.imread('lena.jpg')
dst=cv2.flip(img2,0)#垂直翻转
dst1=cv2.flip(img2,1)#水平翻转
dst2=cv2.flip(img2,-1)#水平垂直翻转

#平移图片
rows,cols=img.shape[:2]
#创建矩阵
M=np.float32([[1,0,100],[0,1,50]])#x平移100,y平移50
#1,0,tx
#0,1,ty
shift=cv2.warpAffine(img,M,(cols,rows))

#旋转图片
M=cv2.getRotationMatrix2D((cols/2,rows/2),45,0.5)#逆时针45度,缩小一半
rotation=cv2.warpAffine(img,M,(cols,rows))
M=cv2.getRotationMatrix2D((cols/2,rows/2),-45,0.5)
rotation_45=cv2.warpAffine(img,M,(cols,rows))

M=cv2.getRotationMatrix2D((cols/2,rows/2),90,0.5)#逆时针45度,缩小一半
rotation90=cv2.warpAffine(img,M,(cols,rows))
M=cv2.getRotationMatrix2D((cols/2,rows/2),-90,0.5)
rotation_90=cv2.warpAffine(img,M,(cols,rows))

titles=['img','res','res2','shift',-1,\
    'img2','dst','dst1','dst2',-1,'img',\
        'rotation','rotation_45','rotation90','rotation_90']#标题
plt.figure(figsize=(12,8))
for i in range(len(titles)):
    plt.subplot2grid((3, 5), (0+i//5, 0+i%5))
    if titles[i]!=-1:
        plt.imshow(cv2.cvtColor(eval(titles[i]),\
                                cv2.COLOR_BGR2RGB))
        plt.title(titles[i], fontsize=8)
    else:
        plt.xticks([]), plt.yticks([])#隐藏x,y
plt.show()
cv2.waitKey(0)

