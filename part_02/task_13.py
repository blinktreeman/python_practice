# 13. Пользователь задаёт две строки. Определить количество вхождений одной строки в другой

full_string = input('Введите строку ')
find_string = input('Что ищем? ')
count = 0

for i in full_string.split():
    if i == find_string:
        count += 1
print('Число вхождений строки "{}" равно {}' .format(find_string, count))