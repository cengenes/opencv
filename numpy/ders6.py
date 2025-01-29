# matplotlib.pyplot: Grafik çizimi için kullanılan bir modüldür. plt kısaltmasıyla kullanılır.

import matplotlib.pyplot as plt  # matplotlib kütüphanesinin dahil edilme şekli
import numpy as np

x = np.arange(5)  # arange ile mesela burda 5 e kadar sayıları seçer dizi şeklinde  [0,1,2,3,4] 5 hariç
y = x  # y ye de aynı değerleri gönderdik

plt.plot(x,y,"o--")  # grafiği çizmek için plt.plot
# 3. parametre çizginin nası çizildiği bir şey yazmazsak düz çizgi "o" "o-" "o--" gibi yapabiliriz


plt.plot(x,-y)       

plt.plot(-x,y,"s")   # s o falan bunlar işaretleme şekli o daire ; s kare

plt.title("y=x, y=-x") # en üstte grafiğin adını vermek adına plt.title


plt.show()# grafiği göstermek için plt.show