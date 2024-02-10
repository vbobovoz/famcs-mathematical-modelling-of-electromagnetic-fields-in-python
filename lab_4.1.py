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

def create_composite_matrix(matrix, matrix_size):
    # Создаем нулевую и единичную матрицы
    zeros_matrix = np.zeros((matrix_size, matrix_size), dtype=int)
    identity_matrix = np.eye(matrix_size, dtype=int)

    # Создаем матрицу, в которой Aij = exp(Aij)
    exp_matrix = np.exp(matrix)

    # Объединяем матрицы в новые матрицы. axis=1 - добавление справа, axis=0 - добавление снизу
    upper_submatrix = np.concatenate((matrix, identity_matrix), axis=1)
    lower_submatrix = np.concatenate((zeros_matrix, exp_matrix), axis=1)
    composite_matrix = np.concatenate((upper_submatrix,lower_submatrix), axis=0)
    return composite_matrix


if __name__ == "__main__":
    size = int(input("Введите размер матрицы: "))
    matrix_a = create_matrix_a(size)
    composite_matrix = create_composite_matrix(matrix_a, size)
    np.savetxt("composite_matrix.txt", composite_matrix, fmt="%10.6f", delimiter=" ")