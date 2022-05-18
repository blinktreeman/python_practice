# Реализовать RLE алгоритм. реализовать модуль сжатия и восстановления данных.
# входные и выходные данные хранятся в отдельных текстовых файлах

data_str = 'aaaabbbbbnnnneeeebbbjjjjjjjjjaaaaaa'
current_char = data_str[0]
count = 0
result_list = []

for i in data_str:
    if i == current_char:
        count += 1
    else:
        result_list.append(current_char + str(count))
        current_char = i
        count = 1
result_list.append(current_char + str(count))
print(''.join(result_list))

