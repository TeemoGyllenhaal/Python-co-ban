#1
import matplotlib.pyplot as plt
import numpy as np
from math import pi, cos

def ham_bac_2(a, b, c, x):
    f = a*x**2 + b*x + c
    return f
def ham_bac_1(a,b,x):
    f = a*x + b
    return f
#2
fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2)
#3
x1 = np.linspace(start=-10.0, stop = 10.0, num = 2000)
y1 = 2*x1**2 + 3*x1 -5
y2 = 3*x1 - 5
x2 = np.linspace(start=0, stop= 3*pi, num = 1000)
y3 = np.cos(x2)
#4
ax1.plot(x1,y1, label= r'$y=2x^{2}+3x-5$')
ax1.plot(x1,y2, label= r'$y=3*x-5$')
ax1.set_xlabel("Trục hoành - x")
ax1.set_ylabel("Trục tung - y")
ax1.legend()
#5
ax2.plot(x2,y3, label=r'$y=cos(x)$')
ax2.set_xlabel("Trục hoành - x")
ax2.set_ylabel("Trục tung - y")
ax2.legend()
#6
plt.show()
#huhu
