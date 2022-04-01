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

    cv2.imshow('nanoCam1', frame)
    cv2.moveWindow('nanoCam1', 650,0)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frameSmall = cv2.resize(frame, (320,240))
    graySmall = cv2.resize(gray, (320,240))

    cv2.moveWindow('BW', 0,255)
    cv2.moveWindow('nanoSmall', 0,0)
    cv2.imshow('BW', graySmall)
    cv2.imshow('nanoSmall', frameSmall)   

    cv2.moveWindow('BW2', 375,255)
    cv2.moveWindow('nanoSmall2', 375,0)
    cv2.imshow('BW2', graySmall)
    cv2.imshow('nanoSmall2', frameSmall) 
    if cv2.waitKey(1) == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
