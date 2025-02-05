# Histogram, bir görüntüdeki piksel yoğunluğunun (parlaklık seviyelerinin) dağılımını gösteren grafiksel bir temsildir.

import cv2
import numpy as np
from matplotlib import pyplot as plt  

img = cv2.imread("klon.jpg")
b,g,r = cv2.split(img)    # # Görüntüyü BGR (Mavi, Yeşil, Kırmızı) kanallarına ayır

"""	•	b.ravel() → Mavi kanalın tüm piksel değerlerini tek bir diziye dönüştürür.
	•	plt.hist(b.ravel(), 256, [0, 256]) → Mavi kanal için histogram oluşturur.
	•	plt.hist(g.ravel(), 256, [0, 256]) → Yeşil kanal için histogram oluşturur.
	•	256 → Piksel değerlerinin 0-255 aralığında olduğunu belirtir.
	•	plt.show() → Histogramı ekrana çizer."""
 
 
cv2.imshow("img",img)

plt.hist(b.ravel(),256,[0,256])
plt.hist(g.ravel(),256,[0,256])

plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
