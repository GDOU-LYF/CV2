import cv2
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
#线性变换+平移

img =cv2.imread('drawing.jpg')
rows,cols=img.shape[:2]

M=np.float32([[1,0,100],[0,1,50]])
平移=cv2.warpAffine(img,M,(cols,rows))
print(M)
M = cv2.getRotationMatrix2D((cols / 2, rows / 2), 45, 0.5)
旋转=cv2.warpAffine(img, M, (cols, rows))

#刚体变换:旋转+平移
tx1,ty1=M[:,0]
tx2,ty2=M[:,1]
M=np.float32([[tx1,tx2,100],[ty1,ty2,50]])
刚体变换=cv2.warpAffine(img, M, (cols, rows))


翻转x=cv2.flip(img,0)
pst1=np.float32([[1,0,0],[0,-1,0]])
M = cv2.getAffineTransform(img,pst1)
翻转y=cv2.warpAffine(img, M, (cols, rows))
# 翻转x=cv2.flip(img,0)




#输出
titles=["img",r'翻转x',r'翻转y',r"平移",r'旋转',r'刚体变换']#标题
plt.figure(figsize=(12,8))
for i in range(len(titles)):
    plt.subplot2grid((3, 3), (0+i//3, 0+i%3))
    if titles[i]!=-1:
        plt.imshow(cv2.cvtColor(eval(titles[i]),\
                                cv2.COLOR_BGR2RGB))
        plt.title(titles[i], fontsize=10)
    else:
        plt.xticks([]), plt.yticks([])#隐藏x,y
plt.show()
cv2.waitKey(0)
#输出