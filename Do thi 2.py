#1
import matplotlib.pyplot as plt
import numpy as np
def ham_bac_2(a, b, c, x):
    f = a*x**2 + b*x + c
    return f
def ham_bac_1(a,b,x):
    f = a*x + b
    return f
#2
fig, ax = plt.subplots()
#3
x = np.linspace(start=-10.0, stop = 10.0, num = 200)
y1 = ham_bac_2(2,3,-5,x)
y2 = ham_bac_1(3,-5,x)
#4
ax.plot(x, y1)
ax.plot(x, y2)
#5
ax.set_xlabel("Trục hoành - x")
ax.set_ylabel("Trục tung - y")
#6
ax.plot(x, y1, label=r'$y=2x^{2}+3x-5$')
ax.plot(x, y2, label=r'$y=3x-5$')
#7
ax.set_title("Đồ thị phương trình bậc 2 và bậc 1")
#8
ax.legend()
plt.show()
