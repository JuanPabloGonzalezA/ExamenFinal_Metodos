# Ejercicio5
# Resuelva el siguiente sistema acoplado de ecuaciones diferenciales 
# dx/dt = sigma * (y - x)
# dy/dt = rho * x - y -x*z
# dz/dt = -beta * z + x * y
# con sigma = 10, beta=2.67, rho=28.0,
# condiciones iniciales t=0, x=0.0, y=0.0, z=0.0, hasta t=5.0.
# Prepare dos graficas con la solucion: de x vs y (xy.png), x vs. z (xz.png) 
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

#TODO VA A DAR 0 POR LAS CONDICIONES INICIALES PERO IGUAL LO HAGO

sigma = 10.0
beta=2.67
rho=28.0

def dxt(x,y,z):
    return sigma * (y - x)

def dyt(x,y,z):
    return rho * x - y -x*z

def dzt(x,y,z):
    return -1.0*beta * z + x * y

dt=0.01
Nt=int(5.0/dt)+1

xo=0.0
yo=0.0
zo=0.0
x=np.zeros(Nt)
y=np.zeros(Nt)
z=np.zeros(Nt)
for i in range(Nt):
    xn=xo+dt*dxt(xo,yo,zo)
    yn=yo+dt*dyt(xo,yo,zo)
    zn=zo+dt*dzt(xo,yo,zo)
    xo=xn
    yo=yn
    zo=zn
    x[i]=xo
    y[i]=yo
    z[i]=zo
    
    
    
plt.plot(y,x)
plt.savefig('xy.png')
plt.close()
plt.plot(z,x)
plt.savefig('xz.png')