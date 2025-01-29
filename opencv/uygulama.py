import cv2

video = cv2.VideoCapture(0)

dosyaAdi = "/Users/enesaltinel/Desktop/webcam_output.mp4"
codec = cv2.VideoWriter_fourcc(*'H264')  
kareHizi = 30
cozunurluk = (640, 480)

videoFileOutput = cv2.VideoWriter(dosyaAdi, codec, kareHizi, cozunurluk)


while True:
    ret, frame = video.read()
    frame = cv2.flip(frame,1)
    videoFileOutput.write(frame)

    cv2.imshow("Webcam Live", frame)
    if cv2.waitKey(1) & 0xFF == ord("e"):
        break

videoFileOutput.release()
video.release()
cv2.destroyAllWindows()