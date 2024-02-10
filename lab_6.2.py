import numpy as np
import matplotlib.pyplot as plt


k = 3.8
t = np.linspace(0, 10*np.pi, 1000)

x = (k - 1) * np.cos(t) + np.cos((k - 1) * t)
y = (k - 1) * np.sin(t) - np.sin((k - 1) * t)

plt.plot(x, y)

plt.grid(True)

plt.xlabel('x(t)')
plt.ylabel('y(t)')

plt.title('Гипоциклоида')

plt.legend()

plt.show()