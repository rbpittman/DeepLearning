# Opens webcam and uses Movidius NCS to run inception.
import cv2, time

cam = cv2.VideoCapture(1)

while True:
    ret, frame = cam.read()
    if frame == None:
        print("No image grabbed")
    else:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame', gray)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    time.sleep(0.5)
cam.release()
cv2.destroyAllWindows()
