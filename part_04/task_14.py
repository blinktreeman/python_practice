# Дано число. Составить список чисел Фибоначчи, в том числе для отрицательных индексов.
# Т е для k = 8, список будет выглядеть так: [-21 ,13, -8, 5, −3,  2, −1,  1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
# Негафибоначчи

fibo_cache = {0:0, 1:1}


def fibo(n):
    if n in fibo_cache:
        return fibo_cache[n]
    else:
        fibo_cache[n] = fibo(n - 1) + fibo(n - 2)
        return fibo_cache[n]


count = int(input('Задайте количество чисел Фибоначчи '))
fibo_list = [0]
for i in range(1, count + 1):
    current_fibo = fibo(i)
    fibo_list.append(current_fibo)
    # Числа негафибоначчи F−n = Fn*(−1)^(n+1)
    current_fibo *= (-1)**(i+1)
    fibo_list.insert(0, current_fibo)
print('Список чисел Фибоначчи {}' .format(fibo_list))

# Output:
# Задайте количество чисел Фибоначчи 8
# Список чисел Фибоначчи [-21, 13, -8, 5, -3, 2, -1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
