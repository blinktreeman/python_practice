# lambda функции: sum = lambda x: x+10; mult = lambda x: x**2; sum(mult(2))
# Функция map()
import random


def select(f, col):
    return [f(x) for x in col]


def where(f, col):
    return [x for x in col if f(x)]


data = '1 2 3 5 8 15 23 38'.split()
print(data)
data = select(int, data)
print(data)
data = where(lambda e: not e % 2, data)
print(data)
data = list(select(lambda e: (e, e**2), data))
print(data)

data = '1 2 3 5 8 15 23 38'.split()
data = list(map(int, data))
print(data)
data = list(filter(lambda e: not e % 2, data))
print(data)
data = list(map(lambda e: [e, e**2, 1], data))
print(data)

# Функция zip()
print(data)
for i,j,k in zip(data[0], data[1], data[2]):
    print(i, j, k)

# Функция enumerate
data = '1 2 3 5 8 15 23 38'.split()
print(data)
for count, value in enumerate(data):
    print(count, value)

# map again
data = list(map(lambda e: random.randint(1, 100), range(0, 10)))
print(data)

# List Comprehension
data = [random.randint(1, 100) for i in range(10)]
print(data)
data = [my_rand for _ in range(10) if (my_rand := random.randint(1, 100)) % 2]
print(data)

if 67 in data: print('yes!')