import numpy as np


def generate(filename, rows, cols):
    # Генерируем случайную матрицу с значениями от -10 до 20
    random_matrix = np.random.randint(-10, 21, size=(rows, cols))

    # Сохраняем матрицу в текстовый файл
    np.savetxt(filename, random_matrix, fmt='%3d')

def sum_of_cubes(filename):
    matrix = np.loadtxt(filename)
    column = matrix[(matrix[:, 0] > 0) & (matrix[:, 0] < 10), 0]
    return int(np.sum(column ** 3))


if __name__ == "__main__":
    generate("generated_matrix.txt", 5, 5)
    result = sum_of_cubes("generated_matrix.txt")
    print(f"Сумма кубов положительных элементов первого столбца матрицы < 10 = {result}")