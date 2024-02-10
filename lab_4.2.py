import numpy as np
import time


def series_sum_with_loop(z_value, n_value = 10):
    if z_value<=0:
        raise ValueError("Значение z НЕ должно быть <= 0")

    result = 0
    ln_z = np.log(z_value)

    for k in range(1, n_value + 1):
        result += (ln_z ** k) / k

    return result

def series_sum_without_loop(z_value, n_value = 10):
    if z_value<=0:
        raise ValueError("Значение z НЕ должно быть <= 0")

    ln_z = np.log(z_value)

    k = np.arange(1, n_value + 1)
    value = (ln_z ** k)/k
    result = np.sum(value)

    return result

if __name__ == "__main__":
    z = float(input("Введите аргумент функции z: "))
    n = int(input("Введите необязательный аргумент функции N или -1, если хотите оставить его по умолчанию = 10: "))

    if n == -1:
        start_time = time.time()
        with_loop = series_sum_with_loop(z)
        time_with_loop = time.time() - start_time

        start_time = time.time()
        without_loop = series_sum_without_loop(z)
        time_without_loop = time.time() - start_time

        print(f"Результат работы функции с циклом: {with_loop}")
        print(f"Время работы функции с циклом: {time_with_loop}\n")
        print(f"Результат работы функции без цикла: {without_loop}")
        print(f"Время работы функции без цикла: {time_without_loop}")
    else:
        start_time = time.time()
        with_loop = series_sum_with_loop(z, n)
        time_with_loop = time.time() - start_time

        start_time = time.time()
        without_loop = series_sum_without_loop(z, n)
        time_without_loop = time.time() - start_time

        print(f"Результат работы функции с циклом: {with_loop}")
        print(f"Время работы функции с циклом: {time_with_loop}\n")
        print(f'Результат работы функции без цикла: {without_loop}')
        print(f"Время работы функции без цикла: {time_without_loop}\n")
        print(f"Функция без цикла приблизительно в {round(time_with_loop/time_without_loop, 2)} раз быстрее")