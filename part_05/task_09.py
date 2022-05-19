# Написать программу вычисления арифметического выражения заданного строкой. Используются операции +,-,/,*.
# приоритет операций стандартный. Пример: 2+2 => 4; 1+2*3 => 7; 1-2*3 => -5;
# Добавить возможность использования скобок, меняющих приоритет операций. Пример: 1+2*3 => 7; (1+2)*3 => 9

expression_str = '-1+6/3*2+(1+2)*3'


def math_expr(init_str):
    # Производим действия умножения и деления, выражение в строке заменяем на результат действия
    while '*' in init_str:
        i = init_str.index('*')
        temp = str(int(init_str[i-1]) * int(init_str[i+1]))
        init_str = init_str[:(i-1)] + temp + init_str[(i+2):]
    while '/' in init_str:
        i = init_str.index('/')
        temp = str(int(init_str[i-1]) / int(init_str[i+1]))
        init_str = init_str[:(i-1)] + temp + init_str[(i+2):]
    # В строке добавляем "+" перед отрицательными числами
    init_str = ''.join([i if i != '-' else '+-' for i in init_str])
    # Разбиваем строку (разделитель +), возвращаем сумму
    return sum([float(i) for i in init_str.split('+') if i != ''])


# Определяем наличие скобок в выражении.
# Если скобка "(" присутствует, все выражение между "(" и ")" вычисляем в math_expr
# В исходной строке "(хххххххх)" заменяем на результат вычисления
while '(' in expression_str:
    left_bracket = expression_str.index('(')
    right_bracket = expression_str.index(')')
    temp_expression = expression_str[left_bracket+1:right_bracket]
    temp = math_expr(temp_expression)
    expression_str = expression_str[:(left_bracket)] + str(temp) + expression_str[(right_bracket+1):]

print(f'Выражение: {expression_str}')
print(f'Результат вычисления: {math_expr(expression_str)}')

# Output:
# Выражение: -1+6/3*2+3.0*3
# Результат вычисления: 3.0
