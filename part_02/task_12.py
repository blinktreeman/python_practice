# 12. Сложить числа вещественного числа

num = 123.45
sum = 0

print('Вещественное число {}' .format(num))
num *= 10**len(str(num))

while num >= 1:
    sum += num % 10
    num //= 10

print('Сумма разрядов числа {}' .format(sum))