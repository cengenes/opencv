import cv2
import numpy as np

img = cv2.imread("klon.jpg")
cv2.imshow("klon asker",img)

boyut = img.shape  # (426, 640, 3) boyuta sahipmiş shape fonksiyonu ile bulduk.
print(boyut)


color = img[150,200] # resmin 150 ye 200 noktasındaki pikselin değerine ulaşmak bu kadar.
print("BGR: ",color)  # 150 ye 200 deki pikselin BGR değerlerini verdi.  BGR:  [158 153 144]

# bir pikseldeki mavi değerine ulaşmak için.
blue = img[150,200,0]  # 0.indeksini alıyoruz
print(blue)  # 158

green = img[150,200,1]
print(green) # 153

red = img[150,200,2]
print(red)   # 144



# pikselin değerini değiştirmek için
img[150,200,0] = 250
print("yeni blue değerim: ",img[150,200,0])



cv2.waitKey(0)
cv2.destroyAllWindows()