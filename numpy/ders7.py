
import numpy as np
import matplotlib.pyplot as plt

"""
N = 11
x = np.linspace(0,10,N)  # linspace fonksiyonu girdiğim aralıkta veri üretir N kaç tane olduğu.0'dan 10'a kadar N (11) tane eşit aralıklı sayı üretir.

y = x

plt.plot(x,y,"o--")
plt.axis("off")  # eksenleri yok etmek için aynen bu kullanım
plt.show()
"""

x = [1,2,3,4]
plt.plot(x,[y**2 for y in x])      # 2.parametre y x'in içinde forla dolaşıyo ve karesini alıyo. y eksenimiz bu şekilde.
#plt.plot(x,[x**2]) bu şekilde olunca hatalı ama 

plt.show()