# Проверить истинность утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат

variants = [[True, True, True],
            [True, True, False],
            [True, False, True],
            [True, False, False],
            [False, True, True],
            [False, True, False],
            [False, False, True],
            [False, False, False]]
for i in range(len(variants)):
    print('Для значений X={}, Y={}, Z={}' .format(variants[i][0], variants[i][1], variants[i][2]), end=' ')
    print('результат:', end=' ')
    # ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z
    print(not (variants[i][0] and variants[i][1] and variants[i][2]) == 
            (not variants[i][0] or not variants[i][1] or not variants[i][2]))
