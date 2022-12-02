import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
def ham_Rosenbrock(b, x, y):
    z = (x -1)**2 + b*(y - x**2)**2
    return z
#2
x = np.linspace(start=-2.0, stop=2.0,num=200)
y = np.linspace(start=-1.0, stop=3.0,num=200)
x, y = np.meshgrid(x, y)
z = ham_Rosenbrock(10, x, y)
#3
fig, ax = plt.subplots(subplot_kw={"projection":"3d"})
#4
rosen_surf = ax.plot_surface(x, y, z,cmap=cm.gist_heat_r,linewidth=0, antialiased=False)
ax.set_zlim(0, 200)
fig.colorbar(rosen_surf, shrink=0.5,aspect=5)
plt.show()