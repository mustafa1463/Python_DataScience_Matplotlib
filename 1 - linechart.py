import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,10,10)
y = np.sin(x)

plt.plot(x,y)
plt.xlabel("Time")
plt.ylabel("Some function of time")
plt.title("My cool chart")

plt.show()


z = np.linspace(0,10,100)
k = np.sin(z)
plt.plot(z,k)
plt.show()
