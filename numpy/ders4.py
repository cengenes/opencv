# ndarray


import numpy as np
x = np.array([[-2,-1,0,5],[9,4,5,-7],[9,7,6,5]],np.int16) # unsigned int

print(x)

print(x.shape) # 3 satır 4 sütundan oluştuğunu veriyor
print(x.ndim)  # kaç boyutlu olduğu
print(x.dtype) # veri türü
print(x.size)  # eleman sayısı
print(x.T)     # transpoze satırı sütün, sütunu satır yapıyo öğrenmiştik lineerde.