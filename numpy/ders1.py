import numpy as np 
# np burada NumPy kütüphanesinin kısaltmasıdır. Bu şekilde NumPy fonksiyonlarını daha kısa yazabiliriz. Örneğin, np.array() şeklinde kullanılır.


# tek boyutlu dizi tanımladık
x = np.array([1,2,3],np.int16)  # ilk girilen dizi 2.parametre veritürü . 8 16 32 farketmez ne kadar yer kapladığı.

print(x)
print(type(x))
print(x[0]);  print(x[1]);  print(x[2])   # aynı satırda yazmak istersek araya ; koyarız aklımızda bulunsun