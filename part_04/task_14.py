# Дано число. Составить список чисел Фибоначчи, в том числе для отрицательных индексов.
# Т е для k = 8, список будет выглядеть так: [-21 ,13, -8, 5, −3,  2, −1,  1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
# Негафибоначчи


def fibo(num, a=0, b=1):
    if num > 0:
        num -= 1
        return fibo(num, b, a+b)
    else: return a + b


count = int(input('Задайте количество чисел Фибоначчи '))
fibo_list = [1, 0, 1]
for i in range(count-1):
    current_fibo = fibo(i)
    fibo_list.append(current_fibo)
    # Числа негафибоначчи F−n = Fn*(−1)^n+1
    current_fibo *= (-1)**(i+1)
    fibo_list.insert(0, current_fibo)
print('Список чисел Фибоначчи {}' .format(fibo_list))
