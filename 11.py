import numpy as np
import matplotlib.pyplot as plt

def f(x):
    if (-1<x<1):
        return 1
    else:
        return 0

xmin = -5
xmax = 5
N = 200
delx = (xmax-xmin)/(N-1)


x,sample =[],[]
for i in range(N):
    sample.append(f(xmin+i*delx))
    x.append(xmin+i*delx)

xmin=x[0]
xmax=x[-1]
for i in range(N):
    sample.append(0)
    if (i<N/2):
        x.append(xmin-i*delx)
    else:
        x.append(i*delx)

x.sort()

dft = np.fft.fft(sample,norm='ortho')


prod = []
for i in range(2*N):
    prod.append(dft[i]**2)

conv = delx*(2*N)**0.5*np.fft.ifft(prod,norm='ortho')



shifted_sample = np.zeros(2*N)
for k in range(N):
    shifted_sample[int(N/2)+k] = sample[k]




plt.plot(x,conv,label='convoluted')
plt.plot(x,shifted_sample,label='function')
plt.legend()
plt.show()