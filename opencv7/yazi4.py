import cv2
import numpy as np

tuval = np.zeros((512,512,3), dtype=np.uint8) + 255

font1 = cv2.FONT_HERSHEY_SIMPLEX
font2 = cv2.FONT_HERSHEY_COMPLEX
font3 = cv2.FONT_HERSHEY_SCRIPT_COMPLEX

cv2.putText(tuval, "OpenCV", (30, 100), font1, 2, (0,0,0), cv2.LINE_AA)
# OpenCV’de cv2.putText() fonksiyonu, bir görüntü üzerine yazı eklemek için kullanılır.
# önce metin,yazının sol alt köşesinin koordinatları (x=30, y=100),Kullanılacak font türü ,Siyah renk,Yazının kalınlığı,(yumuşak) çizgi kullanarak daha düzgün bir yazı çizer



cv2.imshow("Canvas", tuval)
cv2.waitKey(0)
cv2.destroyAllWindows()
