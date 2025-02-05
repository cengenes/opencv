import cv2
import numpy as np

#img = cv2.imread("text.png.png")
img1 = cv2.imread("klon.jpg")

gray = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)

gray = np.float32(gray)
"""float32: Bu tip, daha hassas sayısal hesaplamalar yapabilmek için kullanılır.
Köşe tespiti gibi algoritmalar, daha hassas hesaplamalar yapabilmek adına genellikle float32 veri tipine ihtiyaç duyar.
"""
corners = cv2.goodFeaturesToTrack(gray,1000,0.01,10) # 0.01 kalite gibi düşün.genelde bunu kullan.
# 10: Bu parametre, köşeler arasındaki minimum mesafeyi belirler. Bu, yakın olan köşelerin birleştirilmesini engeller.
# 1000: Maksimum köşe sayısı.

corners = np.int0(corners)
"""goodFeaturesToTrack fonksiyonu köşe koordinatlarını float olarak döndürebilir.
Ancak tam sayı olması gerektiği için burada bu koordinatlar int veri tipine dönüştürülür."""

for corner in corners:
    x,y = corner.ravel()
    cv2.circle(img1,(x,y),3,(0,0,255),-1)

cv2.imshow("corner",img1)

cv2.waitKey(0)
cv2.destroyAllWindows()

    


