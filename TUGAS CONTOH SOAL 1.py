import numpy as np
import matplotlib.pyplot as plt
import math

g = 9.8  
v0 = 0   
h0 = float(input("Masukkan ketinggian awal (h0) dalam meter: "))  

t = math.sqrt(2 * h0 / g)
print("Waktu yang diperlukan untuk mencapai tanah = ", t , " s")
v = g * t
print("Kecepatan yang diperlukan untuk mencapai tanah = ", v, " m/s")

t = np.arange(0.0, t, 10**(-6))  
v_t = g * t  
h_t = h0 - (0.5 * g * t**2) 
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(6, 8)) 

ax1.plot(t, v_t, 'r')  
ax1.set(xlabel='Waktu (s)', ylabel='Kecepatan (m/s)', title='Grafik Kecepatan sebagai Fungsi Waktu (Jatuh Bebas)')
ax1.grid()
ax2.plot(t, h_t, 'b')  
ax2.set(xlabel='Waktu (s)', ylabel='Ketinggian (m)', title='Grafik Posisi Benda sebagai Fungsi Waktu (Jatuh Bebas)')
ax2.grid()
plt.tight_layout()  
plt.show()
