# 8. Сообщить в какой четверти координатной плоскости или на какой оси находится точка с координатами Х и У

coord_x =int(input('Задайте координату X: '))
coord_y =int(input('Задайте координату Y: '))
print('Точка с координатами ({}, {})' .format(coord_x, coord_y), end=' ')
if coord_x == 0: print('лежит на оси Y')
elif coord_y == 0: print('лежит на оси X')
elif coord_x > 0 and coord_y > 0: print('лежит в первой четверти')
elif coord_x < 0 and coord_y > 0: print('лежит во второй четверти')
elif coord_x < 0 and coord_y < 0: print('лежит в третьей четверти')
elif coord_x > 0 and coord_y < 0: print('лежит в четвертой четверти')