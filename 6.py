import numpy as np
import matplotlib.pyplot as plt

x_min = -2
x_max = 2
n = 500
delta = (x_max-x_min)/n
x = np.linspace(x_min,x_max,n)
k,dft = [],[]
for i in range(-int(n/2),int(n/2)):
    fk = 0
    for j in range(n):
        fk = fk + 1*np.exp(-1j*2*np.pi*i*x[j]/(n*delta))
    dft.append(fk)
    k.append(2*np.pi*i/(n*delta))

plt.plot(k,dft)
plt.show()