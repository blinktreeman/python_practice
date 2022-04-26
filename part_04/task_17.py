#  Найти НОК двух чисел

a = int(input('Число a '))
b = int(input('Число b '))

least_comm_mult = a
count = 1
while least_comm_mult % a != 0 or least_comm_mult % b != 0:
    count += 1
    least_comm_mult = a * count

print('Наименьшее общее кратное чисел {} и {} равно {}' .format(a, b, least_comm_mult))