def sum_of_nums(a, b):
    a += b
    return a


def write_data():
    info_data = open('my_data.txt', 'w')
    for i in range(1000):
        info_data.write('iter {}\n'.format(i))
    info_data.close()


def read_data():
    info_data = open('my_data.txt', 'r')
    for item in info_data:
        print(item, end='')
