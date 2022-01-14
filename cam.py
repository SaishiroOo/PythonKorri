import cv2

cap = cv2.VideoCapture("http://admin:admin@192.168.5.158/video.cgi")

while (cap.isOpened() ):
    ret, frame = cap.read()
    if ret == True:
        frame=cv2.imshow("Video",frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()