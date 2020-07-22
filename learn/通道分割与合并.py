import cv2
img=cv2.imread('lena.jpg')
# b,g,r=cv2.split(img)
# img=cv2.merge((r,g,b))
r=img[:,:,2]
print(r)
cv2.imshow('lena_red',r)
cv2.waitKey(0)