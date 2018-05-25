# Ejercicio1
# A partir de los arrays x y fx calcule la segunda derivada de fx con respecto a x. 
# Esto lo debe hacer sin usar ciclos 'for' ni 'while'.
# Guarde esta segunda derivada en funcion de x en una grafica llamada 'segunda.png'

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

x = np.linspace(0,2.,10)
fx = np.array([0., 0.0494, 0.1975, 0.4444, 0.7901,1.2346 , 1.7778, 2.4198, 3.1605, 4.])

dx=x[1]-x[0]#pues es linear en x

ff=np.append(fx[1:],np.array([0]))#corro uno a la izquierda
fb=np.append(np.array([0]),fx[:-1])#corro uno a la derecha
#print(fx)
#print(ff)
#print(fb)
d2=(ff+fb-2.0*fx)/(dx**2.0)#posiciones 0 y N-1 son de relleno. ESTO ES CON DIFERENCIA CENTRAL (f[i+1]+f[i-1]-2*f[i])/dx**2
#print(d2)
plt.plot(x[1:-1],d2[1:-1])
plt.xlabel('x')
plt.ylabel(r'frac{$d^2f(x)}{dx^2}$')
plt.title('segunda derivada con diferencia central')
plt.savefig('segunda.png')


