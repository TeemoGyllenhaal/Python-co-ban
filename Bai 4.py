import numpy as np
from math import cos
import matplotlib.pyplot as plt
from matplotlib import cm
x = np.linspace(start=-1.0, stop=1.0,num=200)
y = np.linspace(start=-1.0, stop=1.0,num=200)
def ham_rastrigin(b,x,y):
    z = x**2 + y**2 - np.cos(12*x) - np.cos(18*y)
    return z
x, y = np.meshgrid(x,y)
g = ham_rastrigin(3,x,y)
fig, ax = plt.subplots(subplot_kw={"projection":"3d"})
rosen_surf = ax.plot_surface(x,y,g,cmap=cm.gist_heat_r,linewidth=0, antialiased=False)
ax.set_zlim(0, 200)
fig.colorbar(rosen_surf, shrink=0.5,aspect=5)
plt.show()