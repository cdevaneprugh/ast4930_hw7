# when installing miniconda, I used >sh *miniconda file* instead of >./*miniconda file*
# installed astropy, matplotlib, and numpy with conda install *package*

import numpy as np
import matplotlib.pyplot as plt
from astropy import units as u

# load in sed textfile
# first column is wavelength (micron)
# second column is specific luminosity (L Sun/micron)
data = np.loadtxt('sed.txt', delimiter = ',')

# print all data in left hand column
#print(data[:,0])

# graph full spectrum

x = data[:,0]
y = data[:,1]

plt.figure(figsize=(9,6))
plt.plot(x, y, color = 'k')
plt.title('Spectral Energy Distribution')
plt.xlabel('Wavelength')
plt.ylabel('Luminosity')
plt.xscale('log')
plt.yscale('log')

#plt.savefig('full spectrum', dpi=300)

# create mask to limit wavelength
mask = (data[:,0] >= 10) & (data[:,0] <= 10000)

# create new array of masked data
new_data = data[mask]

# print and look at how much data was reduced
#print('Number of data points removed =',len(data)-len(new_data))
#print(new_data)

# plot new data
x = new_data[:,0]
y = new_data[:,1]

# graph limited python
plt.figure(figsize=(9,6))
plt.plot(x,y, color='b')
plt.title('Limited Distribution')
plt.xlabel('Wavelength')
plt.ylabel('Luminosity')
plt.xscale('log')
plt.yscale('log')

#plt.savefig('reduced spectrum', dpi=300)
