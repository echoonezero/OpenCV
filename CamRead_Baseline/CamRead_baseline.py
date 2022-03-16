import cv2
dispW = 640
dispH = 480
flip = 2
#below 2 lines for RPi camera CSI
#camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=YUYV, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
#cam=cv2.VideoCapture(camSet)

#below line for webcamera
cam=cv2.VideoCapture(0)
while True:
    ret, frame = cam.read()

    #Do all the video or image operations here between reading and showing frame

    cv2.imshow('nanoCam', frame)
    if cv2.waitKey(1) == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
