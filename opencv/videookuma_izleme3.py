# videoyu dahil etme

import cv2

# video dosyası
video = cv2.VideoCapture("antalya.mp4")



while True:
    ret, frame = video.read()

    if ret == 0:  # 	Eğer video dosyasındaki tüm kareler işlendi (video bitti) veya bir hata oluştuysa ret değeri False döner.Döngüden çıkılır ve video işleme sonlanır.
        break  


    cv2.imshow("Antalya", frame)
    if cv2.waitKey(10) & 0xFF == ord("q"):
        break

video.release()
cv2.destroyAllWindows()