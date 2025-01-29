# webcam açma

import cv2


video = cv2.VideoCapture(0)  # Bu, kamera cihazını başlatır.
# Sisteminizde varsayılan olarak ayarlanmış dahili kamerayı seçer. Harici bir kamera kullanıyorsanız 1, 2 gibi değerler deneyebilirsiniz.



while True:                        # Sonsuz bir döngü oluşturur. Kamera çalıştığı sürece görüntü karelerini okuyup işleyebilirsiniz.
    ret, frame = video.read()      # video.read(): Kameradan bir kare (görüntü) alır.
# ret: Kameradan görüntü başarıyla alınmışsa True, aksi halde False döner.
# frame: Kameradan alınan görüntü (bir numpy dizisi olarak) bu değişkende saklanır.
   
    frame = cv2.flip(frame,1)    # Bu, görüntüyü yatay eksende ters çevirir (ayna görüntüsü gibi).
    cv2.imshow("webcam", frame)  # İkinci parametre frame, gösterilecek görüntüdür.
    if cv2.waitKey(10) & 0xFF == ord("q"): # Bu satırın amacı, bir tuş olayını yakalayıp döngüyü sonlandırmaktır.OpenCV’deki cv2.waitKey() fonksiyonuyla birlikte kullanılır.
        break


video.release()                  # Bu, kamera kaynağını serbest bırakır ve başka bir programın kamerayı kullanabilmesine olanak tanır.
cv2.destroyAllWindows()          # OpenCV tarafından açılmış tüm pencereleri kapatır.