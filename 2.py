import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


#QUESTION 1

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


def anal(k):
    return 1/2.* np.sqrt(np.pi/2)*(np.sign(1-k)+np.sign(1+k))

k = np.array(final_k)





#**** QUESOTION 2 ****************************************************************************
dataframe = pd.read_csv('q2_data.csv',sep=",",header=None)
print(dataframe)



xmin = -50
xmax = 50
N = 200
delx = (xmax-xmin)/(N-1)

factor = (delx)*np.sqrt(N/(2*np.pi))*np.exp(-1j*k*xmin)
data_array = dataframe.to_numpy()
ft_C = data_array[:,0]+1j*data_array[:,1]
ft_C = factor*np.fft.fftshift(ft_C)/np.sqrt(N)



plt.plot(k,np.real(ft_C),label='c code')
plt.plot(final_k,final_dft,'--',label='Numerical')
#plt.plot(k,anal(k),label='Analytical')
plt.xlim(-5,5)
plt.legend()
plt.show()