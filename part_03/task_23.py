import time
import datetime

# 22. Реализовать алгоритм перемешивания списка.


def my_random(a=0, b=100):
    """ Use my_random(from int (default 0), to int (default 100 - 1))

    Берется время в микросекундах.
    В цикле возведение в квадрат, берем 5 разрядов из середины, снова в цикл.
    Возвращается остаток от деления на диапазон.
    """
    rand_range = b - a
    time.sleep(0.001)
    ns = datetime.datetime.now().microsecond
    for i in range(2):
        ns **= 2
        ns //= 100000
        ns %= 100000
    return ns % rand_range + a


def my_shuffle(init_list):
    for i in range(len(init_list)):
        index = my_random(0, len(init_list))
        (init_list[i], init_list[index]) = (init_list[index], init_list[i])
    return init_list


initial_list = '22. Реализовать алгоритм перемешивания списка.'.split()
print(initial_list)
print(my_shuffle(initial_list))
