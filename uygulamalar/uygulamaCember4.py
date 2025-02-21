# verilen resimdeki para sayısını bulup ekrana yazdırdım.


import cv2
import numpy as np


img1 = cv2.imread("parasayisi.jpg")

gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)

img1_blur = cv2.medianBlur(gray1, 5)# Gürültüyü azaltmak için bulanıklaştırıyoruz.

# HoughCircles ile çemberleri bul
circles = cv2.HoughCircles(img1_blur, cv2.HOUGH_GRADIENT, 1, img1.shape[0] / 6,param1=200, param2=30, minRadius=15, maxRadius=89) # / 12 diyince mesela fazla buluyo burayı kendin oyna ve bul.

# Eğer çemberler bulunduysa
if circles is not None:
    circles = np.uint16(np.around(circles))  # Değerleri tam sayıya yuvarla
    para_sayisi = len(circles[0, :])  # Bulunan çember sayısı = para sayısı

    # Çemberleri çiz ve merkezine nokta koy
    for i in circles[0, :]:
        cv2.circle(img1, (i[0], i[1]), i[2], (0, 255, 0), 2)  # Çemberi çiz
        cv2.circle(img1, (i[0], i[1]), 2, (0, 0, 255), 3)  # Merkez noktasını çiz

  
    cv2.putText(img1, f"Toplam Para: {para_sayisi}", (50, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)

# Sonucu göster
cv2.imshow("Paralar", img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
