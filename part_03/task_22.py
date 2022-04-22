# Найти сумму чисел списка стоящих на нечетной позиции
import random
sum = 0
list = []
for i in range(random.randint(10, 15)):
    list.append(random.randint(0, 100))
for i in range(1, len(list), 2):
    sum += list[i]
print(list)
print(sum)