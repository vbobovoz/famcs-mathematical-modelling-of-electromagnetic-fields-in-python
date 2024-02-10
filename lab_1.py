from math import sqrt


def task_1():
    # Введите натуральное число n
    # Подсчитайте количество решений неравенства x^2 + y^2 < n в натуральных числах

    n = int(input("Введите натуральное число n для неравенства x^2 + y^2 < n : "))
    count = 0
    r = int(sqrt(n))
    for x in range(1, r + 1):
        for y in range(1, r + 1):
            if x ** 2 + y ** 2 < n:
                count += 1
    print(f"Количество натуральных решений данного неравенства = {count}")
    return


def task_2():
    # Дано натуральное число n
    # Определить длину периода десятичной записи дроби 1/n

    n = int(input("Введите натуральное число n : "))
    print(f"Десятичная запись дроби = {1/n}")
    remainder = 1 % n 
    set_of_remainders = {remainder}
    position = 0

    while remainder != 0:
        remainder = (remainder * 10) % n
        position += 1

        if remainder in set_of_remainders:
            answ = position - list(set_of_remainders).index(remainder)
            print(f"Длина периода десятичной записи дроби 1/{n} = {answ}")
            return

        set_of_remainders.add(remainder)

    print(f"Десятичная запись дроби 1/{n} не имеет периода")
    return


def task_3():
    # Заданы два натуральных числа n, k
    # Вывести наименьшее n-значное число, делящееся на k

    n = int(input("Введите натуральное число n : "))
    k = int(input("Введите натуральное число k : "))
    result = -1

    num = (10 ** (n - 1)) // k
    if num * k != 10 ** (n - 1):
        result = k * (num + 1)
    elif num * k == 10 ** (n - 1):
        result = 10 ** (n - 1)

    if 10**n - 1 < result:
        print(f"Не существует {n}-значного числа, делящегося на {k}")
    else:
        print(f"Наименьшее {n}-значное число, делящееся на {k} = {result}")
    return


if __name__ == "__main__":
    task_1()
    print("~"*80)
    task_2()
    print("~"*80)
    task_3()
