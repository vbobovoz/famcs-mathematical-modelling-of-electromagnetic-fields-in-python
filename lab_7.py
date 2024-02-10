import numpy as np
import matplotlib.pyplot as plt


N = 200
M = 1000
T = 1

E = np.zeros((M, N))
H = np.zeros((M, N))
h = 200/N
tau = T/M

z = np.linspace(0, 200, N)

E[0, :] = 0.1 * np.sin(2 * np.pi * z / 100)
H[0, :] = 0.1 * np.sin(2 * np.pi * z / 100)

for j in range(M-1):
    for i in range(N-1):
        E[j + 1, i] = E[j, i] - tau/h * (H[j, i + 1] - H[j, i])
        H[j + 1, i] = H[j, i] - tau/h * (E[j, i + 1] - E[j, i])
    E[j + 1, N - 1] = E[j + 1, 0]
    H[j + 1, N - 1] = H[j + 1, 0]

# Количество строк в сетке, количество столбцов в сетке, индекс текущего подграфика
plt.subplot(121)
plt.plot(z, E[0, :])
plt.plot(z, E[M//2, :])
plt.plot(z, E[-1, :])
plt.title('E')

plt.subplot(122)
plt.plot(z, H[0, :])
plt.plot(z, H[M//2, :])
plt.plot(z, H[-1, :])
plt.title('H')

plt.show()