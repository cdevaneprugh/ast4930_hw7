import numpy as np
import matplotlib.pyplot as plt
from astropy import units as u

# load in sed textfile
# first column is wavelength (micron)
# second column is specific luminosity (L Sun/microns)
data = np.loadtxt('sed.txt', delimiter = ',')

# sort data by increasing wavelength
sorted_data = np.sort(data)[::-1]

# set bounds for integration
wavelength = sorted_data[:,0]
data_to_integrate = sorted_data[np.where((wavelength > 10) & (wavelength < 1000))]

# add units
wavelength = data_to_integrate[:,0] * u.micron
luminosity = data_to_integrate[:,1] * u.Lsun / u.micron

# convert luminosity to erg/s/micron
luminosity = luminosity.to(u.erg/u.s/u.micron)

# integrate to obtain total luminosity
total_luminosity = np.trapz(luminosity, wavelength)
print('Total luminosity = ', '{:.3e}'.format(total_luminosity))

# plot spectrum and save image
wav = sorted_data[:,0]
lum = sorted_data[:,1]

plt.style.use('dark_background')
plt.figure(figsize=(9,6))
plt.plot(wav, lum, color='r')
plt.title('Spectral Energy Distribution', fontsize=14)
plt.xlabel('Wavelength [$\mu m$]', fontsize=12)
plt.ylabel('$L_{\odot}$ / $\mu m$', fontsize=12)
plt.xscale('log')
plt.yscale('log')

plt.savefig('devaneprugh_cooper_hw7.png', dpi=300)