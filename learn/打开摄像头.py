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

capture=cv2.VideoCapture(1,cv2.CAP_DSHOW)
width,height=capture.get(3),capture.get(4)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, width * 2)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, height * 2)
print(width,height)
while(True):
    # 获取一帧
    ret, frame = capture.read()
    # 将这帧转换为灰度图
    # gray = cv2.cvtColor(frame,0)

    cv2.imshow('frame', frame)
    if cv2.waitKey(1) == ord('q'):
        break
capture.release()