# Написать программу преобразования десятичного числа в двоичное

dec_num = int(input('Десятичное число '))
binary_num = ''

while dec_num > 0:
    binary_num = str(dec_num % 2) + binary_num
    dec_num //= 2

print(binary_num)