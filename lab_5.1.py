import numpy as np


def create_matrix_a(matrix_size):
    # Создаем матрицу N x N типа int
    A = np.zeros((matrix_size, matrix_size), dtype=int)

    # Заполняем главную диагональ
    # np.fill_diagonal(matrix, value)   np.arange(start, stop, step)
    np.fill_diagonal(A, np.arange(-1, -2 * matrix_size, -2))
    np.fill_diagonal(A[0: , 1:], 2)

    # Заполняем последнюю строку, выбирая "подматрицу"
    A[-1 , :] = -13

    return A

if __name__ == "__main__":
    size = int(input("Введите размер матрицы: "))
    matrix_a = create_matrix_a(size)

    eigenvalues, eigenvectors = np.linalg.eig(matrix_a)
    print(f"Собственные значения: {eigenvalues}")
    print(f"Собственные векторы: {eigenvectors}")

    min_index = np.argmin(np.abs(eigenvalues))
    min_eigenvalue = eigenvalues[min_index]
    min_eigenvector = eigenvectors[:, min_index]

    result = np.allclose(np.dot(matrix_a, min_eigenvector), min_eigenvalue * min_eigenvector)
    print(f"Выполняется ли Ax=kx: {result}")