import matplotlib.pyplot as plt
import numpy as np
from math import pi, cos, sin
fig, (ax1,ax2) = plt.subplots(nrows=1, ncols=2)
def ham_bac_1(a,b,x):
    f = a*x + b
    return f
def ham_bac_2(a, b, c, x):
    f = a*x**2 + b*x + c
    return f
def ham_bac_3(a,b,c,d,x):
    f = a*x**3 + b*x**2 + c*x + d
    return f
def cos_chia_pi(x):
    f = np.cos(x/pi)
    return f
def sin_pi_chia_3(x):
    f = np.sin(pi/3*x)
    return f
x1 = np.linspace(start=-10.0, stop = 10.0, num = 2000)
y1 = ham_bac_3(2,-3,5,-9,x1)
y2 = ham_bac_2(-2,-5,3,x1)
y3 = ham_bac_1(-5,3,x1)
x2 = np.linspace(start=-10.0,stop=10.0, num=200)
y4 = cos_chia_pi(x2)
y5 = sin_pi_chia_3(x2)
ax1.set_xlabel("Trục hoành - x")
ax1.set_ylabel("Trục tung - y")
ax1.plot(x1,y1, label = r'$y=2x*{3}-3x*{2}+5x-9$')
ax1.plot(x1,y2, label = r'$y=-2x*{2}-5x+3$')
ax1.plot(x1,y3, label = r'$y=-5x+3$')
ax1.legend()
ax2.set_xlabel("Trục hoành - x")
ax2.set_ylabel("Trục tung - y")
ax2.plot(x2,y4, label = r'$cos(x/pi)$')
ax2.plot(x2,y5, label = r'$sin(pi/3)*x$')
ax2.legend()
plt.show()
