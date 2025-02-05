# Bu kod OpenCV kullanarak bir video dosyasından nesne tespiti yapıyor ve özellikle beyaz renge duyarlı bir maskeleme işlemi gerçekleştiriyor.

import cv2
import numpy as np

cap = cv2.VideoCapture("4.2 dog.mp4.mp4")

while 1:

	_,frame = cap.read()  # _ işareti gereksiz dönen değeri (ret) saklamamak için kullanılır.
	hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV) # OpenCV, görüntüleri BGR formatında okur.
 #	HSV (Hue, Saturation, Value) renk uzayı, belirli renkleri daha kolay tespit etmek için kullanılır
	
	sensitivity = 15 # sensitivity = 15: Beyaz rengin ne kadar hassas algılanacağını belirler.
	lower_white = np.array([0,0,255-sensitivity])
	upper_white = np.array([255,sensitivity,255])
 # Bu aralık, beyaza yakın renkleri tespit etmeyi sağlar. siteden aldık bu sayıları.
 
	maskeleme = cv2.inRange(hsv,lower_white,upper_white) # cv2.inRange() fonksiyonu, belirtilen HSV aralığındaki pikselleri beyaz (255), diğer pikselleri siyah (0) yapar.
 
	sonuc = cv2.bitwise_and(frame,frame,mask=maskeleme) # cv2.bitwise_and() fonksiyonu, mask ile frame’i birleştirir.
	# Sadece maskede beyaz olan bölgeler görüntüde bırakılır, diğer bölgeler siyah olur.•	Yani beyaz renkler korunur, diğer tüm renkler kaybolur.
	
	cv2.imshow("frame",frame)
	cv2.imshow("mask",maskeleme)
	cv2.imshow("result",sonuc)
	
	k = cv2.waitKey(5) & 0xFF
	if k == 27:  # 	•	Kullanıcı ESC (27) tuşuna basarsa, döngüden çıkılır.
		break
	

cv2.destroyAllWindows()