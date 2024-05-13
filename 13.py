import numpy as np
import matplotlib.pyplot as plt


# READING THE FILE ******************************************************

with open('noise.txt') as file:
    f = file.readlines()
    f = [float(item.rstrip()) for item in f]


N = len(f)
x = [i for i in range(N)]
#*************************************************************************

# FINDING DFT ***********************************************************


dft = np.fft.fft(f,norm='ortho')
k = np.fft.fftfreq(N)               #JUST GIVES q/N

sorted = []
for i in range(N):
    sorted.append([k[i],dft[i]])
sorted.sort(key=lambda x:x[0])

kf,dftf = [],[]
for i in range(N):
    kf.append(sorted[i][0])
    dftf.append(sorted[i][1])


# OBTAINING THE POWER SPECTRUM ********************************************

period = [np.abs(x)**2 for x in dftf]

# BINNING THE SPECTRUM (10 K POINTS IN EACH BIN)****************************************************

kmin,kmax = kf[0],kf[-1]
bin = 51
delta = (kmax-kmin)/bin
k_bin,per_bin = [],[]

d = delta
n = 0
for i in range(1,bin+1):
    dftb = 0
    while(kf[n]<kf[0]+i*d):
        dftb = dftb + period[n]
        n = n+1
        if(n==len(kf)):
            break
    per_bin.append(dftb)
    k_bin.append(kf[0]+i*d)






# PLOTTING EVERYTHING *************************************************************

figure, ax = plt.subplots(2, 2) 

ax[0,0].plot(x,f)
ax[0,0].set_xlabel('Time')
ax[0,0].set_ylabel('Data')

ax[0,1].plot(kf,dftf)
ax[0,1].set_xlabel('Freuquency')
ax[0,1].set_ylabel('Fourier Tranform')

ax[1,0].plot(kf,period)
ax[1,0].set_xlabel('Freuquency')
ax[1,0].set_ylabel('P(k)')


ax[1,1].plot(k_bin,per_bin)
ax[1,1].set_xlabel('Binned Freuquency')
ax[1,1].set_ylabel('P(k)')

plt.show()
