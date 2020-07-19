from cv2 import*
img=imread("lena.jpg")
imwrite('img\\img_bmp.bmp',img)
imwrite('img\\img_jpg1.jpg',img)
imwrite('img\\img_jpg2.jpg',img,[int(IMWRITE_JPEG_QUALITY),20])
imwrite('img\\img_jpg3.jpg',img,[int(IMWRITE_JPEG_QUALITY),100])

imwrite('img\\img_png1.png',img)
imwrite('img\\img_png2.png',img,[int(IMWRITE_PNG_COMPRESSION),9])