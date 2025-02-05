import cv2

img = cv2.imread('5.1 contour.png.png')

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

_,thresh = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)

contours,_ = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

cnt = contours[0] # Genellikle en büyük veya ilk bulunan nesneyi analiz etmek istediğimiz için ilk konturu seçiyoruz.
alan = cv2.contourArea(cnt) 
print(alan)
M = cv2.moments(cnt)
print(M['m00'])

cevre = cv2.arcLength(cnt,True) # cv2.arcLength(cnt, True): Konturun uzunluğunu hesaplar.
print(cevre)


cv2.waitKey(0)
cv2.destroyAllWindows()
