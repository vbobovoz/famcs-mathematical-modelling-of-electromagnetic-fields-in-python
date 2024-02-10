import random


def task_1():
    # Сформируйте случайным образом список чисел.
    # Выведите максимальное значение списка, состоящего из
    # произведений смежных элементов исходного списка

    random_list = []
    size = random.randint(5, 15)

    for i in range(size):
        random_list.append(random.randint(1, 100))


    new_list = [random_list[1]]

    for i in range(1, size - 1):
        new_list.append(random_list[i - 1] * random_list[i + 1])

    new_list.append(random_list[size - 2])

    print("Random list :", random_list)
    print("New list :", new_list)
    print("Max value :", max(new_list))
    return


def task_2():
    # Дан список натуральных чисел. Вывести сумму всех натуральных
    # чисел между минимальным и максимальным, которых нет в списке

    # 1 9 4 7
    # 2 + 3 + 5 + 6 + 8 = 24

    input_list = list(map(int, input("Введите элементы списка : ").split()))

    min_in_list = min(input_list)
    max_in_list = max(input_list)

    sum_of_nums = 0
    for i in range(min_in_list, max_in_list):
        if i not in input_list:
            sum_of_nums += i

    print(f"Сумма всех натуральных чисел между {min_in_list} и {max_in_list}, которых нет в списке = {sum_of_nums}")

    return


if __name__ == '__main__':
    task_1()
    print("~"*110)
    task_2()