import cv2
import numpy as np

tuval = np.zeros((512,512,3),dtype=np.uint8) + 255

cv2.line(tuval,(50,50),(512,512),(255,0,0),thickness=5)
cv2.line(tuval,(100,50),(200,250),(0,0,255),5) # thickness kalınlık yazmamıza da gerek yok.
# line fonksiyonu çizgi çeker
''' (50,50) → Çizginin başlangıç noktası (x=50, y=50).
 (512,512) → Çizginin bitiş noktası (x=512, y=512).
 (255,0,0) → Çizginin rengi (BGR formatında mavi).
 thickness=5 → Çizginin kalınlığı 5 piksel.'''
 
 # dikdörtgen
cv2.rectangle(tuval,(20,20),(50,50),(0,255,0),thickness=3)  # dikdörtgen yapma için bu fonksiyon
cv2.rectangle(tuval,(50,50),(150,150),(0,255,0),thickness=-1) # dikdörtgen,n içinin dolu olması için thickness = -1 yaz

# çember
cv2.circle(tuval,(250,250),100,(0,0,255),thickness=5)  # ilk parametre merkez noktası sonraki yarıçap uzunluğu sonraki de renk

# üçgen çizme 3 farklı noktadan çizgi çekerek yapıyoruz.özel bi fonksiyonu yok.

p1 = (100,200)
p2 = (50,50)
p3 = (300,100)

cv2.line(tuval,p1,p2,(0,0,0),4)
cv2.line(tuval,p2,p3,(0,0,0),4)
cv2.line(tuval,p3,p1,(0,0,0),4)

# çokgen oluşturma birden fazla noktaya ihtiyacımız var ama tek tek tanımlamıycaz.diizi oluşturucaz.
# polylines fonksiyonu kullanıyoruz.

points = np.array([[[110, 200], [330, 200], [290, 220], [100,100]]], np.int32) # dizilerde veritipini tanımlamayı unutma!
cv2.polylines(tuval,[points], True, (0,0,100), 5) # false dersek açık şekil oluyo true olursa kapalı.


# elips 

cv2.ellipse(tuval, (300, 300), (100, 50), 0, 0, 360, (255, 255, 0), -1)
# sırasıyla Elipsin merkezi ,Elipsin büyük ekseni 100, küçük ekseni 50,Elipsin dönüş açısı (burada dönüş yok, yatay),Çizimin başlangıç açısı,Çizimin bitiş açısı (360 derece olduğu için tam elips çizer)







cv2.imshow("Tuvalimiz",tuval)
cv2.waitKey(0)
cv2.destroyAllWindows()