import cv2
import numpy as np

drawing = False  # 是否开始画图
start,end = (0, 0),(0,0)

def mouse_event(event, x, y, flags, param):
    global start, drawing,end

    # 左键按下：开始画图
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        start = (x, y)
    # 鼠标移动，画图
    elif event == cv2.EVENT_MOUSEMOVE:
        pass
        if drawing:
            end=(x,y)
    # 左键释放：结束画图
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.rectangle(img,start,(x, y),(255,0,0),2)



img = np.zeros((512, 512, 3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image', mouse_event)

while(True):
    temp=np.copy(img)
    if drawing and end!=(0,0):
        cv2.rectangle(temp,start,end,(255,0,0),2)
    cv2.imshow('image', temp)
    if cv2.waitKey(20) == 27:
        break