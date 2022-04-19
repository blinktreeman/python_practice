# 14. Посчитайте, сколько раз символ встречается в строке.

full_string = input('Введите строку ')
find_char = input('Символ для поиска: ')

count = 0
for i in full_string:
    if i == find_char: count += 1

print('Количество символов "{}" в строке равно {}' .format(find_char, count))