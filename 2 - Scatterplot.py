import numpy as np
import matplotlib.pyplot as plt

y = np.array([4,3,0,5,1,2,3,1,0,2,1,3])
x = np.array([3,3,0,2,1,2,3,2,1,2,3,2])

plt.scatter(x,y)

x_line = np.linspace(0,100,100)
y_line = 2*x_line + 1
z_line = x**2

plt.scatter(x,y)


plt.plot(x_line,y_line)


plt.show()
