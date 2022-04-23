# 26. Определить, позицию второго вхождения строки в списке либо сообщить, что её нет.
# Примеры
# список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3

init_list = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
search = "qwe"
count = 0
find_twice = False

for i in range(0, len(init_list)-1):
    if init_list[i] == search:
        count += 1
        if count == 2:
            find_twice = True
            print('Второе вхождение строки "{}" на позиции с индексом {}' .format(search, i))
            break
if not find_twice:
    print('Второе вхождение строки "{}" не найдено'.format(search))