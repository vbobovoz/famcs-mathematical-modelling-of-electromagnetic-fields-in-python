import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(0, 2*np.pi, 100)
y = np.linspace(0, np.pi, 50)

X, Y = np.meshgrid(x, y)
Z = np.sin(X) * np.cos(Y)

plt.contour(X, Y, Z, levels=20)
plt.xlabel('x')
plt.ylabel('y')
plt.colorbar(label='z')
plt.show()

fig = plt.figure()
axes = fig.add_subplot(projection='3d')
axes.plot_surface(X, Y, Z)
axes.set_xlabel('x')
axes.set_ylabel('y')
axes.set_zlabel('z')
plt.show()