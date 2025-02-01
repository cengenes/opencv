
import cv2
import numpy as np

cember = np.zeros((512,512,3),np.uint8) + 255     
cv2.circle(cember,(256,256),60,(255,0,0),-1) 

dikdortgen = np.zeros((512,512,3),np.uint8) + 255
cv2.rectangle(dikdortgen,(150,150),(350,350),(0,0,255),-1)

dst = cv2.addWeighted(cember,0.7,dikdortgen,0.3,0)
""" 	•	img1 → İlk görüntü (cember).
	•	alpha (0.7) → İlk görüntünün ağırlığı.
	•	img2 → İkinci görüntü (dikdortgen).
	•	beta (0.3) → İkinci görüntünün ağırlığı.
	•	gamma (0) → Ekstra parlaklık eklemek için kullanılır (şu an 0). 0 yaz geç ne olduğu önemli değil"""

cv2.imshow("CEMBER",cember)
cv2.imshow("Dikdortgen",dikdortgen)
cv2.imshow("agirlikli toplama",dst)



cv2.waitKey(0)
cv2.destroyAllWindows()