
# cv2.cvtColor() → Görüntüyü farklı renk uzaylarına çevirir.

import cv2
import numpy as np

img = cv2.imread("klon.jpg")
img_rgb = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)  # ilk parametre ana resim sonra fonksiyonla değiştirmek istediğimiz format
img_hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) # griye çevirmek görüntü işlemede mantıklı. çünkü kanal 2 daha kolay bgr da kanal sayısı 3.




cv2.imshow("Klon BGR",img)
cv2.imshow("Klon RGB",img_rgb)
cv2.imshow("Klon HSV",img_hsv)
cv2.imshow("Klon GRAY",img_hsv)



cv2.waitKey(0)
cv2.destroyAllWindows()