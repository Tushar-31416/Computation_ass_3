# THIS CODE IS WRITTEN TO COMMPARE THE RUNTIMES FOR A MANUAL CALCULATION OF DFT AND NUMPY.FFT FOR 50 ITERATIONS **************************************

import numpy as np
import time
import matplotlib.pyplot as plt


def dft_m(x,N):
        xt = []
        for i in range(N):
            s = 0
            for j in range(N):
                s = s+x[j]*np.exp(-1j*2*np.pi*i*j/N)
            xt.append(s/(N)**0.5)
        return xt


manual_t = []
numpy_t = []
s = []
itr = 50

for p in range(4,101):
    m_t = []
    n_t = []
    for l in range(itr):
        x = []
        for k in range(p):
            x.append(np.random.randint(0,10))
        N = len(x)
        

        t1 = time.time_ns()
        dft_ex = dft_m(x,N)
        t2 = time.time_ns()
        dft_np = np.fft.fft(x,norm='ortho')
        t3 = time.time_ns()
        m_t.append(t2-t1)
        n_t.append(t3-t2)
    manual_t.append(sum(m_t)/len(m_t))
    numpy_t.append(sum(n_t)/len(n_t))    
    s.append(p)
    
plt.plot(s,manual_t,label='manual')
plt.plot(s,numpy_t,label='numpy')
plt.xlabel('Size of the sample')
plt.ylabel('Time (ns)')
plt.legend()
plt.show()