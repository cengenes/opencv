import numpy as np

x = np.empty([3,3],np.uint8)  # boş bi dizi oluşturur.Hafızadan rastgele değerler atanır.[3,3] ifadesi, 3 satır ve 3 sütundan oluşan 2 boyutlu bir dizi tanımlar.
print("x: ",x)
print("-------")

y = np.full((3,3,3),dtype=np.int16,fill_value=10) #  3x3x3 boyutlarında bir dizi oluşturur ve tüm elemanlarını 10 değeriyle doldurur.
print("y: ",y)
print("-------")

z = np.ones((2,5,5),dtype=np.int8)  # 2x5x5 boyutlarında, tüm elemanları 1 olan bir dizi oluşturur.
print("z: ",z)

j = np.zeros((2,3,3),dtype=np.int8)  # 2x3x3 boyutlarında, tüm elemanları 0 olan bir dizi oluşturur.
print("j: ",j)