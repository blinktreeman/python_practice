# Даны два файла в каждом из которых находится запись многочлена. Сформировать файл содержащий сумму многочленов.
# файл mn1.txt содержит 1*x^6 + 1*x^5 + 4*x^4 + 2*x^3 + 9*x^2 + 8*x^1 + 8 = 0
# файл mn2.txt содержит 9*x^7 + 7*x^5 + 4*x^4 + 5*x^3 + 9*x^1 + 1 = 0


def make_dict(r_file):
    f = open(r_file, 'r')
    str = f.read()          # 1*x^6 + 1*x^5 + 4*x^4 + 2*x^3 + 9*x^2 + 8*x^1 + 8 = 0
    f.close()
    list = str.split(' ')
    list = [i if len(i) > 1 else i + '*x^0' for i in list if i not in {'+', '=', '0'}]
    list = [i.split('*x^') for i in list]
    return {int(i[1]): int(i[0]) for i in list}     # {6: 1, 5: 1, 4: 4, 3: 2, 2: 9, 1: 8, 0: 8}


# Составляем словари для многочленов в файлах mn1.txt, mn2.txt
dict_mn1 = make_dict('mn1.txt')
dict_mn2 = make_dict('mn2.txt')

# Суммируем коэффициенты с одинаковыми ключами
for i in dict_mn1:
    if i in dict_mn2:
        dict_mn1[i] += dict_mn2[i]
# Обновляем с учетом просуммированных коэффициентов
dict_mn2.update(dict_mn1)
dict_indexes = [i for i in dict_mn2]
# Сортировка индексов словаря
dict_indexes.sort(reverse=True)

res = [f'{dict_mn2[i]}*x^{i}' if i !=0 else f'{dict_mn2[i]}' for i in dict_indexes]

f = open('res_file.txt', 'w')
f.write(' + '.join(res) + ' = 0')
f.close()

# Output:
# file res_file.txt: 9*x^7 + 1*x^6 + 8*x^5 + 8*x^4 + 7*x^3 + 9*x^2 + 17*x^1 + 9 = 0
