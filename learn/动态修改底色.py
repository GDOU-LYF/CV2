import cv2
import numpy as np

drawing = False  # 是否开始画图
start,end = (0, 0),(0,0)
color=(255,255,255)

def mouse_event(event, x, y, flags, param):
    global start, drawing,end,color
    if event==cv2.EVENT_MOUSEWHEEL:
        if flags<0:
            color=(color[0]-10,color[1]-10,color[2]-10)
        else:
            color=(color[0]+10,color[1]+10,color[2]+10)
        img[:]=color


img = np.zeros((512, 512, 3), np.uint8)
img[:]=color
cv2.namedWindow('image')
cv2.setMouseCallback('image', mouse_event)

while(True):
    if drawing and end!=(0,0):
        cv2.rectangle(img,start,end,(255,0,0),2)
    cv2.imshow('image', img)
    if cv2.waitKey(20) == 27:
        break