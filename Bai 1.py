import matplotlib.pyplot as plt
import numpy as np
fig, ax = plt.subplots()
def ham_bac_2(a, b, c, x):
    f = a*x**2 + b*x + c
    return f
def ham_bac_1(a,b,x):
    f = a*x + b
    return f
def ham_bac_3(a,b,c,d,x):
    f = a*x**3 + b*x**2 + c*x + d
    return f
x = np.linspace(start=-10.0,stop=10.0, num=200)
y1 = ham_bac_3(2,-3,5,-9,x)
y2 = ham_bac_2(-2,-5,3,x)
y3 = ham_bac_1(-5,3,x)
ax.plot(x, y1)
ax.plot(x, y2)
ax.plot(x, y3)
ax.set_xlabel("Trục hoành - x")
ax.set_ylabel("Trục tung - y")
ax.plot(x,y1, label = r'$y=2x*{3}-3x*{2}+5x-9$')
ax.plot(x,y2, label = r'$y=-2x*{2}-5x+3$')
ax.plot(x,y2, label = r'$y=-5x+3$')
ax.set_title("Đồ thị phương trình bậc 3, bậc 2 và bậc 1")
ax.legend()
plt.show()