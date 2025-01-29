import cv2

video = cv2.VideoCapture(0)

dosyaAdi = "/Users/enesaltinel/Desktop/webcam_output.mp4"
codec = cv2.VideoWriter_fourcc(*'mp4v')  
kareHizi = 30
genislik = int(video.get(3))  # Kameranın genişliğini al  video.get(3)	Kameranın genişliğini (WIDTH) alır.
yukseklik = int(video.get(4))  # Kameranın yüksekliğini al  video.get(4)	Kameranın yüksekliğini (HEIGHT) alır.
cozunurluk = (genislik, yukseklik)

videoFileOutput = cv2.VideoWriter(dosyaAdi, codec, kareHizi, cozunurluk)

while True:
    ret, frame = video.read()

    frame = cv2.flip(frame, 1)
    videoFileOutput.write(frame)

    cv2.imshow("Webcam Live", frame)
    if cv2.waitKey(1) & 0xFF == ord("e"):
        break

videoFileOutput.release()
video.release()
cv2.destroyAllWindows()
