
import numpy as np
import matplotlib.pyplot as plt

path = '10.1 coins.jpg.jpg'
img = plt.imread(path)
print(img)
print("min value: ",img.min())  # 0 siyah illaki remin bi yerinde siyah yer vardır
print("max value: ", img.max())  # 255 beyaz illaki bi yerde beyaz yer vardır
print("mean: ", img.mean())     # resmin tüm piksel değerlerinin ortalamasını hesaplar
print("median: ",np.median(img)) # ortada kalan değeri 
print("average: ",np.average(img))  # ort
print("mean1: ",np.mean(img))     # ort