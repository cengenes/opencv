import matplotlib.pyplot as plt
import numpy as np

path = "10.1 coins.jpg.jpg"

img = plt.imread(path)


print(img)
print("type: ",type(img))
print("shape: ",img.shape)  # (yükseklik, genişlik, renk kanalları)
print("ndim: ",img.ndim)    # Boyut sayısı yazdırılır. RGB bir resim genelde 3 boyutludur.
print("size: ",img.size)
print("dtype:", img.dtype)  # Piksel değerlerinin veri tipi yazdırılır.


#RGB modelinde her pikselin üç renk kanalı vardır: kırmızı (Red), yeşil (Green) ve mavi (Blue). Bu kanallar, sırasıyla 0, 1 ve 2 indeksleriyle erişilebilir.
print("red channel: ",img[50,50,0]) # rgb--> r =0, g=1, b=2
print("green channel: ",img[50,50,1])
print("blue channel: ",img[50,50,2])
print("rgb channel value: ",img[50,50,:])



plt.imshow(img)
plt.show()     # resmi görüntülemek için imshow ve show ikisini de yazmam gerekli.
