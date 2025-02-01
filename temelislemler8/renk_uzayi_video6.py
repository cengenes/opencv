import cv2
import numpy as np

video = cv2.VideoCapture("antalya.mp4")

while True:
    ret,frame = video.read()
    frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    cv2.imshow("video",frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
    
video.release()
cv2.destroyAllWindows()