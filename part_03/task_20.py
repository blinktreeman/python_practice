# Задать список из N элементов, заполненных числами из [-N, N].
# Найти произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число

n = int(input('Введите n '))
list = []
mult = 1

for i in range(-n, n+1):
    list.append(i)
print(list)
f = open('my_data.txt', 'r')
for i in f:
    mult *= (list[int(i)])
print(mult)
f.close()