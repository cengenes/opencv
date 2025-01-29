import matplotlib.pyplot as plt
import numpy as np

x = np.arange(3) # [0,1,2] verileri oluşturduk
plt.plot(x,[y**2 for y in x])  # y ekseni x in karesi şekşinde öğrenmiştik
plt.plot(x,[y**3 for y in x])

plt.legend(["x**2","x**3"],loc = "upper center")  # hangi çizginin hangi fonksiyon olduğunu grafikte gösterir.loc nereye yerleştirileceği

plt.grid(True)  # ızgara oluşturur

plt.xlabel("np.arange(3) ten geliyo")  # grafiklerin altına y de soluna bir şeyler yazmak için.
plt.ylabel("y = f(x)")

print(plt.axis())  # x ve y eksenlerindeki min ve maks noktalarını verir

plt.axis([0,2,0,8]) # başlangıç ve bitiş değerlerini biz verdik ilk 2 si x in sonraki y nin min ve maksı

plt.title("Basit bir grafik")

plt.savefig("/Users/enesaltinel/Desktop/plt.png") # grafiği kaydetmek için bi yere dosya yolu ve adını yazıyoruz


plt.show()