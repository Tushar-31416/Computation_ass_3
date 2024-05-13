import numpy as np
import matplotlib.pyplot as plt


#********* CREATING THE MESH *********************8
meshlim = 500
meshsize = 5001
delta = 2*meshlim/(meshsize-1)
x = np.linspace(-meshlim, meshlim, meshsize)
y = np.linspace(-meshlim, meshlim, meshsize)
xg, yg = np.meshgrid(x, y)


zg = np.exp(-(xg**2 + yg**2))


# ********* FOURIER TRANSFORM USING FFT2 ********************************
ftz = np.fft.fft2(zg,norm="ortho")
ftz = np.fft.fftshift(ftz)

kx = (2*np.pi/(meshsize*delta))*np.arange(-(meshsize-1)/2,(meshsize-1)/2+1)
ky = (2*np.pi/(meshsize*delta))*np.arange(-(meshsize-1)/2,(meshsize-1)/2+1)
kxg, kyg = np.meshgrid(kx, ky)
ft_z = (delta**2)*(meshsize/(2*np.pi))*np.exp(-1j*(kxg*np.min(x)+kyg*np.min(y)))*ftz



# ********* ANALYTIC FOURIER TRANSFORM ***************************************

kzg = 0.5*np.exp(-(kxg**2+kyg**2)/4)


#  ********* PLOTTING **************************


fig = plt.figure(figsize=(10, 5))
ax1 = fig.add_subplot(121, projection='3d')
ax1.plot_surface(kxg, kyg, ft_z, cmap='viridis')
ax1.set_title('Numerical Fourier Transform')

ax2 = fig.add_subplot(122, projection='3d')
ax2.plot_surface(kxg, kyg, kzg , cmap='viridis')
ax2.set_title('Analytical Fourier Transform')

plt.tight_layout()
plt.show()
