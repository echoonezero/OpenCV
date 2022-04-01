import cv2
evt = -1
coord=[]
def click(event, x, y, flags, params):
    global pnt
    global evt
    if event == cv2.EVENT_LBUTTONDOWN:
        #print('Mouse event was:   ', event)
        #print(x, ', ', y)
        pnt = (x,y)
        coord.append(pnt)
        evt = event

dispW = 640
dispH = 480
flip = 2
cv2.namedWindow('nanoCam')
cv2.setMouseCallback('nanoCam', click)
#below 2 lines for RPi camera CSI
#camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=YUYV, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
#cam=cv2.VideoCapture(camSet)

#below line for webcamera
cam=cv2.VideoCapture(0)
while True:
    ret, frame = cam.read()
    for pnts in coord:
        cv2.circle(frame, pnts, 5, (0,0,255), -1)
        font = cv2.FONT_HERSHEY_PLAIN
        myStr = str(pnts)
        cv2.putText(frame, myStr, pnts, font, 2, (255,0,0),2)

    #Do all the video or image operations here between reading and showing frame

    cv2.imshow('nanoCam', frame)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
    if key == ord('c'):
        coord = []
cam.release()
cv2.destroyAllWindows()