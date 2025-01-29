import cv2

img = cv2.imread("klon.jpg",0) # 0 gri yapıyo hiçbi şey yazmazsak orijinal hali gelir.
# print(img) elde ettiğimiz resmin matrisler karşılığı

cv2.namedWindow("image") # resmin boyutunu kenarlardan artırabiliyoruz.

img = cv2.resize(img,(900,300))   # resmi biz boyutlandırıyoruz istediğimiz genişlik ve yükseklikte.

cv2.imshow("image",img)      # imshow resmi görüntülüyor ilk parametre resmin başlığı
cv2.imwrite("klon1.jpg",img) # yeni hali resmin görüntüleniyo
cv2.waitKey(0)               # bi tuşa basana kadar kapanmıyo
cv2.destroyAllWindows()      # kapattığımızda tüm opencv kapanıyo

