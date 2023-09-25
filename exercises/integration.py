import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

## exercise 1: integral of sin^2(x)

#def f(x):
#    return np.sin(x)**2
#def err(f):
#    return abs(f/(np.pi/2) - 1)

#def f(x):
#    return np.exp(x)
#def err(f):
#    y = np.exp(np.pi)-1
#    return np.abs(f-y)/y

#def f(x):
#    return np.cos(x)
#def err(f):
#    return abs(f/1 - 1)

def f(x):
    return np.cos(2*x)
def err(f):
    return abs(f)

def integrate(N):
    # simpson requires odd N
    N = int(N)
    if N%2==0: N+=1

    x = np.linspace(0,np.pi,N)

    dx = x[1]-x[0]

    I1 = dx * np.sum(f(x[:-1]))
    I2 = dx/2 * (f(x[0]) + f(x[-1]) + 2*np.sum(f(x[1:-1])))
    I3 = dx/3 * ( f(x[0]) + f(x[-1]) + 4*np.sum(f(x[1:-1:2])) + 2*np.sum(f(x[2:-1:2])) )

    return err(I1),err(I2),err(I3)

#Ns = np.logspace(1,4,10)
Ns = (3,5,7,9,11)

i1,i2,i3 = [],[],[]
for n in Ns:
    a,b,c = integrate(n)
    i1.append(a)
    i2.append(b)
    i3.append(c)

print(i1)
print(i2)
print(i3)

plt.figure()
plt.loglog(Ns,i1,label="rectangle")
plt.loglog(Ns,i2,label="trapezoidal")
plt.loglog(Ns,i3,label="simpson")
plt.legend()
plt.show()
