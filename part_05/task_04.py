# В файле находится N натуральных чисел, записанных через пробел. Среди чисел не хватает одного, чтобы выполнялось
# условие A[i] - 1 = A[i-1]. Найти его.
# файл t_4.txt содержит: '1 2 3 4 6 7 8 9'

with open('t_4.txt', 'r') as f:
    nums_list = [int(i) for i in f.read().split(' ')]
for i in range(len(nums_list)):
    if nums_list[i] + 1 != nums_list[i + 1]:
        print(f'Пропущенное число: {nums_list[i] + 1}')
        break

# Output:
# Пропущенное число: 5
