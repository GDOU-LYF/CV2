import cv2 as cv
import sys
start=cv.getTickCount()
img =cv.imread('lena.jpg',0)
cv.namedWindow('lena2',cv.WINDOW_NORMAL)
cv.imshow('lena2',img)
k=cv.waitKey(0)

if k is ord('s'):#或者chr(k) is 's'
    cv.imwrite('lena_save.bmp',img)
else:
    sys.exit(0)
# print((cv.getTickCount()-start)/cv.getTickFrequency())