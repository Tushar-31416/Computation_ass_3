import numpy as np
import matplotlib.pyplot as plt



def f(x):
    if (x==0):
        return 1
    else:
        return np.sin(x)/x


xmin = -50
xmax = 50
N = 200
delx = (xmax-xmin)/(N-1)


sample =[]
for i in range(N):
    sample.append(f(xmin+i*delx))




dft = np.fft.fft(sample,norm='ortho')
k = (2*np.pi/delx)*np.fft.fftfreq(N)               #JUST GIVES q/N

sorted = []

for i in range(N):
    sorted.append([k[i],dft[i]])

sorted.sort(key=lambda x:x[0])

final_k,final_dft = [],[]
for l in range(N):
    final_dft.append(delx*(N/(2*np.pi))**0.5*np.exp(-1j*xmin*sorted[l][0])*sorted[l][1])
    final_k.append(sorted[l][0])



plt.plot(final_k,final_dft)
plt.xlim(-5,5)
plt.show()