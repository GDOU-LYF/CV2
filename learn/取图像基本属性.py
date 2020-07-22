import cv2
img =cv2.imread('lena.jpg')

px=img[100,90] #Y,X
print(px)

px_blue=img[100,90,0]#px[0] 取蓝色通道 B   BGR
print(px_blue)
# img[100,90]=[255,255,255]
# print(img.item(100,90))

print(img.shape,img.dtype)
print(img.size)


#gray
img2 =cv2.imread('lena.jpg',0)

px=img2[100,90] #Y,X
print(px)

print(img2.shape)
print(img2.size)
