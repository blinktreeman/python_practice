# 16. Написать программу проверки, является ли строка палиндромом

str = input('Введите строку: ')
is_palindrome = True
for i in range(int(len(str)/2)):
    if str[i] != str[-i - 1]:
        is_palindrome = False
        break
if is_palindrome: print('Строка палиндром')
else: print('Строка не палиндром')