# 13. Пользователь задаёт две строки. Определить количество вхождений одной строки в другой

full_string = input('Введите строку ')
find_string = input('Что ищем? ')
count = 1

list = find_string.split(' ')

for i in list:
    if i == find_string: count += 1
print('Число вхождений строки "{}" равно {}' .format(find_string, count))