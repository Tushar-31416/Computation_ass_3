import numpy as np
import matplotlib.pyplot as plt

def g(x):
    return np.exp(-x**2)

def h(x):
    return np.exp(-4*x**2)

xmin = -5
xmax = 5
N = 200
delx = (xmax-xmin)/(N-1)


x,sample_g,sample_h =[],[],[]
for i in range(N):
    sample_g.append(g(xmin+i*delx))
    sample_h.append(h(xmin+i*delx))
    x.append(xmin+i*delx)

xmin=x[0]
xmax=x[-1]
for i in range(N):
    sample_g.append(0)
    sample_h.append(0)
    if (i<N/2):
        x.append(xmin-i*delx)
    else:
        x.append(i*delx)

x.sort()

dft_g = np.fft.fft(sample_g,norm='ortho')
dft_h = np.fft.fft(sample_h,norm='ortho')



prod = []
for i in range(2*N):
    prod.append(dft_g[i]*dft_h[i])

conv = delx*(2*N)**0.5*np.fft.ifft(prod,norm='ortho')



def exact(x):
    return (np.pi/5)**0.5*np.exp(-4*x**2/5)

exact_sol = []
for i in range(len(x)):
    exact_sol.append(exact(x[i]))




plt.plot(x,conv,label='numerical')
plt.plot(x,exact_sol,'--',label='exact')
plt.xlabel('x')
plt.ylabel(r'$[g \otimes h](x)$')
plt.legend()
plt.show()