# BGR RGB çatışması 

import cv2
import matplotlib.pyplot as plt

path = "10.1 coins.jpg.jpg"
img = cv2.imread(path,0) # BGR griye çevirdik
#img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
plt.imshow(img,cmap='gray',interpolation = 'BICUBIC') # RGB
plt.show()