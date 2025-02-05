"""Kontur, bir görüntüde aynı renge veya yoğunluğa sahip olan alanların sınırlarını belirleyen eğrilerdir.
Bir başka deyişle, nesnelerin dış hatlarını belirlemek için kullanılır.
Konturlar, özellikle nesne tanıma, şekil analizi ve nesne segmentasyonu gibi görüntü işleme uygulamalarında önemli bir rol oynar."""

"""penCV’de kontur tespiti yapmak için genellikle şu adımlar izlenir:
	1.	Gri tonlamalı görüntüye çevirme (Grayscale)
	2.	Bulanıklık uygulama (Opsiyonel)
	3.	Kenar tespiti (Canny) veya eşikleme (Threshold)
	4.	Kontur bulma (cv2.findContours())
	5.	Konturları çizme (cv2.drawContours())"""
 
import cv2

img = cv2.imread('2.1 contour1.png.png')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

_,thresh = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)  # Thresholding, bir görüntüyü sadece siyah ve beyaz (binary) hale getirir.
contours,_=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE) # cv2.findContours(), görüntüdeki konturları (nesne kenarlarını) bulur.
# 2 ve 3. parametreler kalıp gibi düşün.
# _ yapmamızın nedeni bu fonksiyonlar 2 şer parametre atıyo. bunlar gereksiz o yüzden _ kullandık.

cv2.drawContours(img,contours,-1,(0,0,255),3) # Konturları görüntüye çizer. -1: Tüm konturların çizilmesini sağlar. renk çizginin rengi burada red. 3 kalınlık.

cv2.imshow("contour",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

