import numpy as np #libreria numérica de python
import matplotlib.pyplot as plt #libreria para gráficas y figuras  de python

a=np.linspace(0,  2, 30)

b = np.sin(a) - 0.5*a

#tecnica de subplots y manejo de figuras con ejes
#es una de las tecnicas más rapidas para dar el formato

#Propiedades de los ejes
plt.rc('xtick',labelsize=7)
plt.rc('ytick',labelsize=7)

##Propiedades de figura fi, axl
##figsize=(x,y) es el tamaño de la figura en pulgadas
fig,ax = plt.subplots(1,1, figsize=(4,2))

#ax.plot(a,b) #Plot b en función de a, usando ax
#spines es propiedades de los ejes
ax.spines['bottom'].set_position(('data',0))
ax.spines['left'].set_position(('data',0))
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

'''
#Propiedades de los ejes
plt.rc('xtick',labelsize=7)
plt.rc('ytick',labelsize=7)
'''

ax.set_xlabel('Longitud [m]', fontsize=8, loc='center')
ax.set_ylabel('Funcion [m]', fontsize=8, loc='center')
ax.plot(a,b, '--k', lw=1.4) #Plot b en función de a, usando ax
#plt.savefig('ejemplo.png')
plt.show() #es necesaria para ver la grafica