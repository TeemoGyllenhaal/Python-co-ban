import matplotlib.pyplot as plt
import numpy as np
from math import pi, cos, sin
fig, ax = plt.subplots()
def cos_chia_pi(x):
    f = np.cos(x/pi)
    return f
def sin_pi_chia_3(x):
    f = np.sin(pi/3*x)
    return f
x = np.linspace(start=-10.0,stop=10.0, num=200)
y1 = cos_chia_pi(x)
y2 = sin_pi_chia_3(x)
ax.plot(x, y1)
ax.plot(x, y2)
ax.set_xlabel("Trục hoành - x")
ax.set_ylabel("Trục tung - y")
ax.plot(x,y1, label = r'$cos(x/pi)$')
ax.plot(x,y2, label = r'$sin(pi/3)*x$')
ax.legend()
plt.show()

