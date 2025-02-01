""" ROI (Region of Interest), görüntü işleme ve bilgisayarla görmede ilgilenilen belirli bir bölgeyi (kare, dikdörtgen, daire vb.) seçmek anlamına gelir.
Bir görüntünün tamamını işlemeden, yalnızca belirli bir kısmını analiz etmek veya işlemek için kullanılır.
    """

import cv2
import numpy as np

img = cv2.imread("klon.jpg")
print(img.shape) # resmin boyutlarını öğrendik. şimdi istediğimiz bölgeyi buna göre tahmin edicez.

roi = img[30:200,200:400]
# Bu, img dizisinden 30-200 arasındaki satırları ve 200-400 arasındaki sütunları keser.

cv2.imshow("KLON",img)
cv2.imshow("ROİ",roi)


cv2.waitKey(0)
cv2.destroyAllWindows()