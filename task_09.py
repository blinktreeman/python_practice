# 9. Указав номер четверти прямоугольной системы координат, 
# показать допустимые значения координат для точек этой четверти

quarter_num = int(input('Укажите номер четверти '))
print('Допустимые значения координат для данной четверти:', end=' ')
if quarter_num == 1: print('x ∈ (0, +∞) и y ∈ (0, +∞)')
elif quarter_num == 2: print('x ∈ (0, -∞) и y ∈ (0, +∞)')
elif quarter_num == 3: print('x ∈ (0, -∞) и y ∈ (0, -∞)')
elif quarter_num == 4: print('x ∈ (0, +∞) и y ∈ (0, -∞)')
