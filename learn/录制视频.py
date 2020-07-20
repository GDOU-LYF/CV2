import cv2
capture=cv2.VideoCapture(1,cv2.CAP_DSHOW)

fourcc=cv2.VideoWriter_fourcc(*'MJPG')
outfile=cv2.VideoWriter('output.avi',fourcc,25.,(640,480))

while(capture.isOpened()):
    # 获取一帧
    ret, frame = capture.read()
    if ret:
        outfile.write(frame)
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) == ord('q'):
            break
    else:
        break
capture.release()