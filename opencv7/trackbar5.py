""" OpenCV’deki trackbar, bir GUI (grafiksel arayüz) bileşenidir ve bir pencere içinde kaydırma çubuğu (slider) oluşturmanıza olanak tanır.
Kullanıcı, trackbar’ı hareket ettirerek belirli bir değeri değiştirebilir.

Trackbar, genellikle:
Görüntü işleme parametrelerini dinamik olarak ayarlamak için kullanılır.
Filtrelerin etkisini gerçek zamanlı görmek için kullanılır."""

import cv2
import numpy as np

# Trackbar oluştururken dümenden bi tane fonksiyona ihtiyaç duyulur.herhangi bir işlem yapmayacağımız için pass komutunu kullandık.
def nothing(x):
    pass

img = np.zeros((512,512,3),np.uint8)
cv2.namedWindow("image")
# “image” isimli bir pencere açıyoruz.Bu pencereyi trackbar eklemek için oluşturuyoruz.


cv2.createTrackbar("R","image",0,255,nothing)
cv2.createTrackbar("G","image",0,255,nothing)
cv2.createTrackbar("B","image",0,255,nothing)
# Bu satırlar, “image” penceresine üç farklı trackbar ekler:Trackbar’ın başlangıç değeri 0 ve maksimum değeri 255 olarak ayarlandı.
# 	Trackbar her değiştirildiğinde nothing fonksiyonu çağrılır (ama bir işlem yapmaz).

switch = "0:OFF 1:ON"
cv2.createTrackbar(switch,"image",0,1,nothing) # trackbarın yazacagı metini değişkende tanımladık.yukardakilerden farkı yok
# Bu trackbar, 0 (kapalı) ve 1 (açık) olmak üzere iki durumda olabilir.


while True:
    cv2.imshow("image",img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
    
    #  Trackbar Değerlerini Alıyoruz
    r = cv2.getTrackbarPos("R","image")   
    g = cv2.getTrackbarPos("G","image")
    b = cv2.getTrackbarPos("B","image")
    s = cv2.getTrackbarPos(switch,"image")
    
    if s == 0:
        img[:] == [0,0,0]    # s == 0 ise tüm pikseller (0,0,0) olarak kalıyor yani ekran siyah oluyor.
        
    if s == 1:
        img[:] = [b,g,r]     # s == 1 ise kullanıcının seçtiği RGB renkleri tuvale uygulanıyor.
        
cv2.destroyAllWindows()
            
    
    
    

