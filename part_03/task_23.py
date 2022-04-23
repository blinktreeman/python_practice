import time

# 22. Реализовать алгоритм перемешивания списка.


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


def my_shuffle(init_list):
    for i in range(len(init_list)):
        index = my_random(0, len(init_list))
        (init_list[i], init_list[index]) = (init_list[index], init_list[i])
    return init_list


initial_list = ['22', '.', 'Реализовать', '_', 'алгоритм', '_', 'перемешивания', '_', 'списка', '.']
print(initial_list)
print(my_shuffle(initial_list))

