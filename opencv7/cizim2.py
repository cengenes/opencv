import cv2
import numpy as np

""" img = np.zeros((10,10,3),np.uint8)
img[0,0] = (255,255,255)
img[0,1] = (255,255,200)
img[0,2] = (255,255,150)
img[0,3] = (255,255,15) """

img = np.zeros((10,10),np.uint8)  # SİYAH BEYAZ GÖRÜNTÜ İÇİN 3 KANAL YOK.
img[0,0] = 255 # beyaz
img[0,1] = 200 # açık gri
img[0,2] = 150 # orta gri
img[0,3] = 15 # neredeyse siyah 
# 0 yaklaştıkça siyahlık artıyo.




img = cv2.resize(img,(1000,1000),interpolation=cv2.INTER_AREA)   # resize fonksiyonu ile tekrar boyutlandırabiliyorduk. ilk parametre resim sonraki boyutu olacaktı.




cv2.imshow("Resim",img)
cv2.waitKey(0)
cv2.destroyAllWindows()