import cv2
import numpy as np

img = cv2.imread("klon.jpg",0)
row,col = img.shape

M= np.float32([[1,0,50],[0,1,200]])  # Bu matris, görüntüyü X ekseninde 50 piksel, Y ekseninde 200 piksel öteleyecek bir dönüşüm matrisidir.
# 	tx = 50 → X ekseninde 50 piksel sağa kaydırma
#	ty = 200 → Y ekseninde 200 piksel aşağı kaydırma

dst = cv2.warpAffine(img,M,(row,col)) # cv2.warpAffine() fonksiyonu, görüntüye dönüşüm matrisi uygular.
"""Parametreler:
	•	img: İşlenecek görüntü.
	•	M: Öteleme matrisimiz.
	•	(row, col): Çıktı görüntüsünün boyutu.
	•	Sonuç olarak, dst değişkenine kaydırılmış yeni görüntü atanır."""
 
 
cv2.imshow("dst",dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
