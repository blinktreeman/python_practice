# Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример: [2, 3, 4, 5, 6] => [12, 15, 16]; [2, 3, 5, 6] => [12, 15]

import random

init_list = [random.randint(0, 100) for _ in range(10)]
print(init_list)

mult_list = [init_list[i]*init_list[-i] for i in range(int(len(init_list)/2))]
print(mult_list)