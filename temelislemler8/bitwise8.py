# Bu işleçler, nesne algılama, maskeleme ve görüntü işlemede sıkça kullanılır.

import cv2
import numpy as np

img1 = cv2.imread("9.1 bitwise_2.png.png")
img2 = cv2.imread("9.2 bitwise_1.png.png")

bit_and = cv2.bitwise_and(img2,img1) # siyah kısma 0 beyaz kısma 1 dedik.mantık kapıları mantığı 0 and 1 = 0 yani siyah oluyo.1 and 1 beyaz oluyo
bit_or = cv2.bitwise_or(img2,img1) # bunda da veya mantığı
bit_xor = cv2.bitwise_xor(img2,img1)
bit_not = cv2.bitwise_not(img2)
bit_not2 = cv2.bitwise_not(img1)


cv2.imshow("img1",img1)
cv2.imshow("img2",img2)
cv2.imshow("bit_and",bit_and)
cv2.waitKey(0)
cv2.destroyAllWindows()
