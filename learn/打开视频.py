import cv2
# def returnCameraIndexes(): #取摄像头编号
#     # checks the first 10 indexes.
#     index = 0
#     arr = []
#     i = 10
#     while i > 0:
#         cap = cv2.VideoCapture(index,cv2.CAP_DSHOW   )
#         if cap.read()[0]:
#             arr.append(index)
#             print(cap.getBackendName())
#             cap.release()
#         index += 1
#         i -= 1
#     return arr
def nothing(x):
    capture.set(cv2.CAP_PROP_POS_FRAMES,FPS_end*x*0.01)
    return (x)

capture=cv2.VideoCapture('demo_video.mp4')
cv2.namedWindow('image')
FPS_end=int(capture.get(cv2.CAP_PROP_FRAME_COUNT))
cv2.createTrackbar('pass','image',0,100,nothing)
# width,height=capture.get(3),capture.get(4)

while(capture.isOpened()):
    # 获取一帧
    ret, frame = capture.read()
    # 将这帧转换为灰度图
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame', gray)
    cv2.setTrackbarPos('pass','image',int(capture.get(cv2.CAP_PROP_POS_FRAMES)/FPS_end*100))
    if cv2.waitKey(30) == ord('q'):
        break
capture.release()