import cv2
dispW = 640
dispH = 480
flip = 2
#below 2 lines for RPi camera CSI
#camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=YUYV, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
#cam=cv2.VideoCapture(camSet)

#below line for webcamera
cam=cv2.VideoCapture(0)
dispW = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
dispH = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))
BW = int(0.3*dispW)
BH = int(0.2*dispH)
posX = 10
posY = 270
dx = 5
dy = 5

while True:
    ret, frame = cam.read()

    #Do all the video or image operations here between reading and showing frame
    frame = cv2.rectangle(frame, (posX, posY), (posX+BW,posY+BH), (255,0,0), -1)
    
    cv2.imshow('nanoCam', frame)
    cv2.moveWindow('nanoCam', 0, 0)
    posX = posX + dx
    posY = posY + dy

    if posX <= 0 or posX+BW >= dispW:
        dx = dx*(-1)
    if posY <= 0 or posY+BH >= dispH:
        dy = dy*(-1)

    if cv2.waitKey(1) == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()