import time

# 23. Реализовать алгоритм задания случайных чисел. Без использования встроенного генератора псевдослучайных чисел


def my_random(a=0, b=100):
    """ my_random(from int (default 0), to int (default 100 - 1))

    Берется время в наносекундах.
    В цикле возведение в квадрат, берем 5 разрядов из середины, снова в цикл.
    Возвращается остаток от деления на диапазон.
    """
    rand_range = b - a
    time.sleep(0.00001)
    ns = time.time_ns() // 100
    for i in range(2):
        ns **= 2
        ns //= 100000
        ns %= 100000
    return ns % rand_range + a


def freq_dictionary(a, b, count=1000):
    """ freq_dictionary(from int, to int, count int (iterations default 1000))

    Частотный словарь для my_random
    """
    dict = {}
    for i in range(a, b):
        dict[i] = 0
    for i in range(count):
        dict[my_random(a, b)] += 1
    for i in range(a, b):
        dict[i] = f'{dict[i] * 100 / count}%'
    print(dict)


freq_dictionary(0, 100)