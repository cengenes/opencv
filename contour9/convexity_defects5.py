import cv2
import numpy as np

img =cv2.imread("9.1 star.png.png")

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
_,thresh = cv2.threshold(gray,127,255,0)

contours,_ = cv2.findContours(thresh,2,1)
cnt = contours[0]

hull =cv2.convexHull(cnt, returnPoints = False) # cv2.convexHull() fonksiyonu, konturun en dış noktalarını içeren dışbükey bir zarf (konveks gövde) oluşturur.
# returnPoints=False: Sadece dizinleri döndürmesini istiyoruz (X, Y koordinatları yerine nokta indeksleri)

kusur = cv2.convexityDefects(cnt,hull) # cv2.convexityDefects() fonksiyonu, konturun dışbükey zarfına göre çöküntü noktalarını bulur.


for i in range(kusur.shape[0]):  # defects.shape[0], bulunan kusurların sayısını verir.
    s, e, f, d = kusur[i,0]             
    start = tuple(cnt[s][0])
    end = tuple(cnt[e][0])
    far = tuple(cnt[f][0])
    """	•	Her kusur dört bileşenden oluşur:
	•	s → Başlangıç noktası (start)
	•	e → Bitiş noktası (end)
	•	f → İçbükey nokta (far)
	•	d → Derinlik değeri (ne kadar içeri çökük olduğu)"""
 
    """	•	cnt[s][0] → Başlangıç noktasının koordinatlarını alır.
	•	cnt[e][0] → Bitiş noktasının koordinatlarını alır.
	•	cnt[f][0] → İçbükey noktanın koordinatlarını alır.
	•	tuple() kullanarak bunları (x, y) koordinatlarına çeviriyoruz."""
 
    cv2.line(img,start,end,[0,255,0],2) # cv2.line() fonksiyonu, start ve end noktaları arasında yeşil (0,255,0) renkli bir çizgi çizer.
    cv2.circle(img,far,5,[0,255,0],-1)

cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
