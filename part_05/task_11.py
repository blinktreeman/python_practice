# Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.
# Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]

init_list = [1, 2, 3, 5, 1, 5, 3, 10]
result_list = [i for i in init_list if init_list.count(i) == 1]
print(result_list)
