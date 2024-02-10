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
    H[j + 1, N - 1] = -tau/(2*h) * (E[j+1, 0] - E[j+1, N-2]) + H[j, N-1]

# Количество строк в сетке, количество столбцов в сетке, индекс текущего подграфика
plt.subplot(221)
plt.plot(z, E[0, :])
plt.plot(z, E[M//2, :])
plt.plot(z, E[-1, :])
plt.title('E')

plt.subplot(222)
plt.plot(z, H[0, :])
plt.plot(z, H[M//2, :])
plt.plot(z, H[-1, :])
plt.title('H')

def exact_solution(z, t):
    return 0.1 * np.sin(2 * np.pi * z * (z - t) / 100)

# Рассчет погрешности для E и H
error_E = np.zeros((M, N))
error_H = np.zeros((M, N))

for j in range(M):
    for i in range(N):
        error_E[j, i] = np.abs(E[j, i] - exact_solution(z[i], j * tau))
        error_H[j, i] = np.abs(H[j, i] - exact_solution(z[i], j * tau))

plt.subplot(223)
for j in range(M):
    plt.plot(z, error_E[j, :], label=f'Time = {j * tau:.2f}')
plt.xlabel('z')
plt.ylabel('Error')
plt.legend()
plt.title('Error in E')

plt.subplot(224)
for j in range(M):
    plt.plot(z, error_H[j, :], label=f'Time = {j * tau:.2f}')
plt.xlabel('z')
plt.ylabel('Error')
plt.legend()
plt.title('Error in H')

plt.show()