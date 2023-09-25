import numpy as np
import matplotlib.pyplot as plt
import random

lam = 0.5

def f(x):
    return lam*np.exp(-lam*x)

xmax = 10
xx = np.linspace(0,xmax)

plt.figure()
plt.ylim([0,lam])
plt.xlim([0,xmax])
plt.plot(xx, f(xx), 'k-', label="True distribution", lw=2)

N = 500_000 # seems enough

# Rejection method
accept = []
for _ in range(N):
    x = random.uniform(0,xmax)
    y = random.uniform(0,1)
    if y < f(x):
        accept.append(x)
plt.hist(accept, density=True, bins=50, color="b", label="Rejection", alpha=0.5)

# Transformation method
y = np.array([random.uniform(-1/lam,0) for _ in range(N)])
x = -1/lam * np.log(-lam*y)
plt.hist(x, density=True, bins=50, color="r", label="Transformation", alpha=0.5)

# Ratio of uniforms
accept = []
for _ in range(N):
    u = random.random()
    v = random.random()
    if u < np.sqrt(2*lam*f(v/u)):
        accept.append(v/u)
plt.hist(accept, density=True, bins=50, color="g", label="Kinderman", alpha=0.5)

plt.legend(loc=1, frameon=False)
plt.show()
