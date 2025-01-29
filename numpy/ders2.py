# 2 boyutlu diziler

import numpy as np

x = np.array([[1,2,3],[4,5,6]],np.int16)
print(x)

print("-----")
print(x[0])    # [1,2,3] verir
print(x[0,0])  # 1 i verir

print("-----")
print(x[1])    # [4,5,6] verir
print(x[1,0])

# sütunları çekeriz
print(x[:,0])  # hepsini tarıyo ve 0.indekslerini alıyo  [1,4]
print(x[:,1])  # hepsini tarıyo ve 1.indekslerini alıyo  [2,5]

print("-----")
# satırları çekeriz
print(x[0,:])  # [1,2,3]
print(x[1,:])  # [4,5,6]