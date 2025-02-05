# Bu kod, OpenCV kullanarak bir görüntüdeki nesnelerin merkezini (ağırlık merkezini) bulur 

import cv2

img = cv2.imread('5.1 contour.png.png')

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

_,thresh = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
M = cv2.moments(thresh)
# 	cv2.moments(thresh), verilen binary görüntünün momentlerini hesaplar.
#	Momentler, görüntünün geometrik özelliklerini analiz etmeye yardımcı olan matematiksel değerlerdir.


X = int(M["m10"]/M["m00"])
Y = int(M["m01"]/M["m00"])
# 	m10, m01: Ağırlık merkezi hesaplaması için kullanılan momentler. sabit değerler nerden geldiğini bilmene gerek yok.

cv2.circle(img,(X,Y),5,(0,255,0),-1) # 5 yarıçaptı

cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
