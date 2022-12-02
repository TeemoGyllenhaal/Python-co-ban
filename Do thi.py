
def ham_bac_2(a, b, c, x):
    f = a*x**2 + b*x + c
    return f
#1
import numpy as np
import matplotlib.pyplot as plt
#2
fig, ax = plt.subplots()
#3
x = np.linspace(start=-10.0, stop = 10.0, num = 200)
y = ham_bac_2(2,3,-5,x)
#4
ax.plot(x,y)
#5
ax.set_xlabel ("Trục hoành - x")
ax.set_ylabel ("Trục tùng - y")
#6
ax.plot(x,y,label=r'$y=2x^{2}+3x-5$')
#7
ax.set_title("Đồ thị phương trình bậc 2")
#8
ax.legend()
plt.show()




