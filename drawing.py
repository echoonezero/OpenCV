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
    frame = cv2.rectangle(frame, (140,100), (180,140), (255,0,0), 7) #draw rectangle- Blue colour and thickness 7
    frame = cv2.circle(frame, (320,240), 50, (0,0, 255), 7)  #draw circle- Red colour, 50 radius and thickness 7
    frame = cv2.circle(frame, (220,140), 50, (0,255,0), -1)  #draw circle- Green colour, 50 radius and thickness 'solid'
    fnt = cv2.FONT_HERSHEY_DUPLEX
    frame = cv2.putText(frame, 'Data',(300,300), fnt, 1, (255,255,0), 3)    #add data to the live image
    frame = cv2.line(frame, (10,10), (630, 500), (0,0,0), 4)    #draw a line
    frame = cv2.arrowedLine(frame,(10,470), (630, 10), (255,255,255),3) #draw arrowed line

    cv2.imshow('nanoCam', frame)
    cv2.moveWindow('nanoCam', 0, 0)
    if cv2.waitKey(1) == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
