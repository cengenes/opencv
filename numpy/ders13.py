import numpy as np
import matplotlib.pyplot as plt

img = plt.imread("13.2 map.jpeg.jpeg")

plt.subplot(4,2,1)              # 4 satır ve 2 sütunluk bir ızgara (grid) oluşturur. 1. konum: İlk alt grafik için bu alanı ayırır.
plt.title("Original Image")     # Bu alt grafik için başlık ekler: “Original Image”.
plt.imshow(img)

plt.subplot(4,2,2)
plt.title("img+img")   # toplamak için aynı boyutta olması lazım. biz aynı resmi kullandığımız için sorun yok.
plt.imshow(img+img)    # Görüntünün her piksel değerini kendisiyle toplar.(R, G, B) piksel değeri (100, 120, 130) olsun.
		               # Toplama sonrası: (200, 240, 260) → (200, 240, 255).

plt.subplot(4,2,3)
plt.title("img-img")   # Piksel değerleri kendi değerlerinden çıkarılır.Sonuç her zaman sıfır olur (tüm pikseller siyah).Çıkarma sonrası: (0, 0, 0)
plt.imshow(img-img)

plt.subplot(4,2,4)   
plt.title("np.flip(img,0)")         # Üst taraf ve alt taraf yer değiştirir. x e göre ters çevrilir.
plt.imshow(np.flip(img,0)) 

plt.subplot(4,2,5)
plt.title("np.flip(img,1)")         # Sol taraf ve sağ taraf yer değiştirir. y ye göre ters çevrilir.
plt.imshow(np.flip(img,1)) 


plt.subplot(4,2,6)
plt.title("np.flip(img,2)")         # Görüntünün üçüncü eksenindeki renk kanallarını ters çevirir. Kırmızı (R), yeşil (G), mavi (B) sırasını tersine çevirir:
plt.imshow(np.flip(img,2))          # Örneğin (R, G, B) → (B, G, R).

plt.subplot(4,2,7)
plt.title("np.fliplr(img)") # left to right 5. resimle aynı aslında 0 1 2 yazmak yerine fliplr fonksiyonu kullandık.
plt.imshow(np.fliplr(img)) 

plt.subplot(4,2,8)
plt.title("np.flipud(img)") # updown  4.resimle aynı. 0 1 2 yazmak yerine flipud fonksiyonu yazabiliriz direkt
plt.imshow(np.flipud(img)) 

plt.show()