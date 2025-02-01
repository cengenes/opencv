# toplamada aynı boyut olmak zorunda o yüzden aynı boyutlu yaptık ikisini de


import cv2
import numpy as np

cember = np.zeros((512,512,3),np.uint8) + 255     # beyaz tuval oluşturduk.
cv2.circle(cember,(256,256),60,(255,0,0),-1) 

dikdortgen = np.zeros((512,512,3),np.uint8) + 255
cv2.rectangle(dikdortgen,(150,150),(350,350),(0,0,255),-1)

toplama = cv2.add(cember,dikdortgen)


cv2.imshow("CEMBER",cember)
cv2.imshow("Dikdortgen",dikdortgen)
cv2.imshow("toplam",toplama)   # morumsu oluştu toplayınca


cv2.waitKey(0)
cv2.destroyAllWindows()