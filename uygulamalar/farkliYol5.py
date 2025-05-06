import cv2
import numpy as np

resim = cv2.imread("para.jpg")

gri = cv2.cvtColor(resim, cv2.COLOR_BGR2GRAY)

bulanık = cv2.GaussianBlur(gri, (15, 15), 0)

_, esiklenmis = cv2.threshold(bulanık, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU) # Otsu yöntemi ile eşikleme uygula

cekirdek = np.ones((3, 3), np.uint8)

acilmis = cv2.morphologyEx(esiklenmis, cv2.MORPH_OPEN, cekirdek, iterations=2)# Gürültü temizliği: açma işlemi

arka_plan = cv2.dilate(acilmis, cekirdek, iterations=5) # Arka planı belirlemek için genişletme

mesafe_donusumu = cv2.distanceTransform(acilmis, cv2.DIST_L2, 5) #  nesne merkezlerini bulma

_, on_plan = cv2.threshold(mesafe_donusumu, 0.7 * mesafe_donusumu.max(), 255, 0) # Ön planı belirle paraların iç kısımları yani
on_plan = np.uint8(on_plan)

bilinmeyen = cv2.subtract(arka_plan, on_plan) # Bilinmeyen alanları hesaplar

_, isaretleyiciler = cv2.connectedComponents(on_plan) # Marker (işaretleyici) alanları oluşturuyoruzz

isaretleyiciler = isaretleyiciler + 1 # Marker etiketlerini +1 yap (arka plan = 1 olacak)

# Bilinmeyen alanlara 0 ata
isaretleyiciler[bilinmeyen == 255] = 0

# Watershed algoritması
isaretleyiciler = cv2.watershed(resim, isaretleyiciler)

# Watershed algoritmasından gelen çıktı int32 türünde, bunu uint8'e dönüştür
isaretleyiciler_uint8 = np.uint8(isaretleyiciler)

# Sınırları kırmızıya boya
resim[isaretleyiciler == -1] = [0, 0, 255]

# Tespit edilen bozuk para sayısını hesapla
etiketler = np.unique(isaretleyiciler)
para_sayisi = len(etiketler[etiketler > 1])  # 0 = bilinmeyen, 1 = arka plan

# HoughCircles ile daire tespiti yap
daireler = cv2.HoughCircles(gri, cv2.HOUGH_GRADIENT, dp=1.2, minDist=30,
                            param1=100, param2=30, minRadius=20, maxRadius=100)

if daireler is not None:
    daireler = np.uint16(np.around(daireler))
    for daire in daireler[0, :]:
        merkez = (daire[0], daire[1])
        yaricap = daire[2]
        cv2.circle(resim, merkez, yaricap, (255, 0, 0), 2)  # Dairenin kenarını mavi çiz
        

cv2.putText(resim, f'Bozuk Para Sayisi: {para_sayisi}', (10, 40),
            cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 0), 3)

print("Tespit edilen bozuk para sayısı:", para_sayisi)
cv2.imshow("Bozuk Paralar", resim)
cv2.waitKey(0)
cv2.destroyAllWindows()