import numpy as np

def solve(*args):
    if len(args) == 0:
        raise ValueError("Как минимум введите матрицу C!")
    if len(args) == 1:
        C = args[0]
        b = np.random.uniform(1, 3, (C.shape[0], 1))
        # C.shape[0] вернет количество строк матрицы С
    elif len(args) == 2:
        C, b = args
        b = np.array(b).reshape(-1, 1)
        # -1 означает что он должен сам посчитать количество строк, 1 - количество столбцов
    else:
        raise ValueError("Ошибка!")

    if np.linalg.det(C) == 0:
        raise ValueError("Матрица C вырожденная!")

    print(b.shape)
    x = np.linalg.solve(C, b) # Решение Cx = b, ravel() - матрица в вектор
    norm = np.linalg.norm(x.ravel(), ord=np.inf)
    print(f"Вектор b: {b}")
    return x, norm

if __name__ == "__main__":
    C1 = np.array([[1, 2], [3, 4]])
    solution1, norm1 = solve(C1)
    print(f"Матрица C: {C1}")
    print(f'Решение системы: {solution1}')
    print(f"Кубическая норма: {norm1}")

    print("~"*100)

    C2 = np.array([[1, 2], [3, 4]])
    b2 = [5, 6]
    solution2, norm2 = solve(C2, b2)
    print(f"Матрица C: {C2}")
    print(f"Вектор b: {b2}")
    print(f"Решение системы: {solution2}")
    print(f"Кубическая норма: {norm2}")