# bir renk belirleyip bunu webcamde ayırt ettim.


import cv2
import numpy as np

# Beyaz Rengin HSV Aralıkları
lower_white = np.array([0, 0, 200]) 
upper_white = np.array([180, 30, 255]) 


video = cv2.VideoCapture(0)

while True:
    ret, frame = video.read()
    if not ret:
        break

    
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)  # hsvye çevirdik.

    # Beyaz renk için maske oluştur
    mask = cv2.inRange(hsv, lower_white, upper_white)

    # Orijinal görüntüden sadece beyaz renkleri al
    result = cv2.bitwise_and(frame, frame, mask=mask)

    # Görüntüleri göster
    cv2.imshow("Original", frame)
    cv2.imshow("Mask", mask)
    cv2.imshow("sonuc", result)

    # 'q' tuşuna basılınca çık
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Kaynakları serbest bırak
video.release()
cv2.destroyAllWindows()
