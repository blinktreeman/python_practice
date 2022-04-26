# Вычислить число pi c заданной точностью d
# Пример: при d = 0.001, pi = 3.141. 10^-1 <= d <= 10^-10

import math

# Вычисление pi с помощь ряда Эйлера pi^2/6 = 1/1^2 + 1/2^2 + 1/3^2 ... 1/n^2

accuracy = float(input('Задайте точность вычисления числа Пи '))
init_pi = 0
count = 1

while abs(math.pi**2/6 - init_pi) > accuracy*0.1:
    # 1/1^2 + 1/2^2 + 1/3^2 ... 1/n^2
    init_pi += count ** -2
    count += 1
init_pi = math.sqrt(init_pi * 6)

print('Значение числа Пи полученное с помощью math.pi: {}' .format(math.pi))
print('Вычисленное значение Пи: {}' .format(init_pi))

# Output:
# Задайте точность вычисления числа Пи 0.000001
# Значение числа Пи полученное с помощью math.pi: 3.141592653589793
# Вычисленное значение Пи: 3.141592558096828
