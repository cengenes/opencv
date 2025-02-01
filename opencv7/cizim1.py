import cv2
import numpy as np

tuval = np.zeros((512,512,3),dtype=np.uint8) + 255    # OpenCV’de np.zeros() varsayılan olarak tamamen siyah bir görüntü (0 değerleriyle dolu) oluşturur.
# (512, 512, 3): 512 genişlik, 512 yükseklik ve 3 kanal (RGB - renkli görüntü) anlamına gelir.
# belli bir alanı siyah bir tuval oluşturur. 255 ekledik tüm matrisler 255 oldu yani beyaz rengi.


cv2.imshow("Tuvalimiz",tuval)
cv2.waitKey(0)
cv2.destroyAllWindows()