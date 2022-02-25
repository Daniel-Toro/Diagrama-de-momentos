#Librerias

import numpy as np
import matplotlib.pyplot as plt

#Parámetros de distancias
x1= np.linspace(0,2,10)
x2= np.linspace(2,4,10)
x3= np.linspace(4,5.5,10)
x_total= np.hstack([x1, x2, x3])

#Momentos flectores
M1=6.5625*x1
M2=-15*(x2**2)+66.5625*x2 - 60
M3=-15*(x3**2)+165.*x3 - 453.75
M_total= np.hstack([M1, M2, M3])


#Tamaño de letras en ejes
plt.rc('xtick', labelsize =10)
plt.rc('ytick', labelsize =10)


#Propiedades en ejes
fig,axl = plt.subplots(1, 1, figsize=(4, 2))
axl.plot(x_total, M_total, '--k', lw=1.5)
axl.spines['top'].set_visible(False)
axl.spines['right'].set_visible(False)
axl.spines['bottom'].set_position(('data',0))
plt.yticks(np.arange(-40, 20, 10))
axl.invert_yaxis()
plt.savefig('vigaPpy.pdf')

