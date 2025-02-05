import cv2
import numpy as np

img = cv2.imread("klon.jpg",0)
row,col = img.shape

M= cv2.getRotationMatrix2D((col/5,row/3),180,1) # cv2.getRotationMatrix2D() fonksiyonunu kullanarak bir döndürme matrisi oluşturur.
""" Ölçek (Scale): 1
	•	1, görüntünün boyutunu değiştirmeden döndürme işlemini yapar.
	•	Daha büyük bir değer (>1) görüntüyü büyütür, daha küçük bir değer (<1) ise küçültür."""
 
 
dst = cv2.warpAffine(img,M,(col,row))

cv2.imshow("dst",dst)

cv2.waitKey(0)
cv2.destroyAllWindows()