import numpy as np
import matplotlib.pyplot as plt


t_values = np.linspace(0.1, 5, 100)

y_values = t_values * np.log(t_values) + np.sqrt(1 + t_values**2 * np.sin(t_values))
z_values = (1 + t_values**3)/(1 + t_values**2)**(1/3)
w_values = z_values - y_values

plt.plot(t_values, y_values, label='y(t)', color='red', linestyle='-')
plt.plot(t_values, z_values, label='z(t)', color='green', linestyle='--')
plt.plot(t_values, w_values, label='w(t)', color='blue', linestyle='-.')

plt.legend()

plt.xlabel('t')
plt.ylabel('y(t), z(t), w(t)')

plt.title('Графики функций y(t), z(t), w(t)')

plt.show()