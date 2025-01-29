import cv2

video = cv2.VideoCapture(0)

dosyaAdi = "/Users/enesaltinel/Desktop/webcam_output.mp4"
codec = cv2.VideoWriter_fourcc(*'H264')  # Videonun sıkıştırma formatını belirler.
kareHizi = 30
cozunurluk = (640, 480)

videoFileOutput = cv2.VideoWriter(dosyaAdi, codec, kareHizi, cozunurluk)
# Video dosyasını kaydetmek için kullanılır. Seçilen dosya adı, codec, kare hızı ve çözünürlük parametreleri ile oluşturulur.

while True:
    ret, frame = video.read()
    frame = cv2.flip(frame,1)
    videoFileOutput.write(frame)

    cv2.imshow("Webcam Live", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

videoFileOutput.release()
video.release()
cv2.destroyAllWindows()