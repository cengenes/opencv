# 3 boyutlu diziler

import numpy as np

x = np.array([ [[1,2,3],[4,5,6]], [[7,8,9],[10,11,12]] ],np.int16) # 0 ve 1 diye ayırdık sonra yine ayrılıyo
print(x)
print("*************")

print(x[0,0,0])
print("*************")
print(x[0,1,0])
print("*************")
print(x[1,1,1])