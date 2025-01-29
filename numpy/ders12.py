import numpy as np
import matplotlib.pyplot as plt


path = '13.2 map.jpeg.jpeg'
img = plt.imread(path)


"""
[r,g,b]
[50,50,0] 50 ye 50 pikselinin red değeri bu mesela
[70,70,1]
[:,:,2]    tüm piksellerdeki blue değeri
r -> 0-255
g -> 0-255   
b -> 0-255  arasında değer alabilir hepsi 
"""

r = img[:,:,0]
g = img[:,:,1]
b = img[:,:,2]

output = np.dstack((r,g,b))  # Ayrılan RGB kanallarını yeniden birleştirir. Bu, orijinal renkli görüntüyü oluşturur.
plt.imshow(output)
plt.show()



"""
output = [img,r,g,b]
titles = ["Image","Red","Green","Blue"]

for i in range(4):
    plt.subplot(2,2,i+1)
    plt.axis("off")
    plt.title(titles[i])
    if i ==0:
        plt.imshow(output[i])
    else:
        plt.imshow(output[i],cmap='gray')
    plt.show()


"""





