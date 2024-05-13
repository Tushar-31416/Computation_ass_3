import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

xlim = 100
n = 1001
Delta = 2*xlim/(n-1)
x = np.linspace(-xlim, xlim, n)
k = (2*np.pi/(n*Delta))*np.arange(-(n-1)/2,(n-1)/2+1)


#***** NUMERICAL RESULT *******************************************************
factor = (Delta)*np.sqrt(n/(2*np.pi))*np.exp(-1j*k*np.min(x))
dataframe = pd.read_csv('q4_data.csv',sep=",",header=None)
#print(dataframe)

data_array = dataframe.to_numpy()
ft_C = data_array[:,0]+1j*data_array[:,1]
ft_C = factor*np.fft.fftshift(ft_C)/np.sqrt(n)


#******** ANALYTICAL RESULT **************************************************

def anal(x):
    return np.exp(-x**2/4)/(2)**0.5





plt.plot(k,ft_C,label='Numerical')
plt.plot(k,anal(k),'--',label='Analytical')
plt.xlabel('k')
plt.ylabel('Fourier transform (k)')
plt.legend()
plt.show()