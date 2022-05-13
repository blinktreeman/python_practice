# 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x²
import random
k = 6

list = [random.randint(0, 10) for _ in range(k + 1)]
print(list)
res = [f'{list[i]}*x^{len(list)-i-1}' if len(list)-i-1 !=0 else f'{list[i]}' for i in range(len(list)) if list[i] != 0]
print(' + '.join(res) + ' = 0')
f = open('mn2.txt', 'w')
f.write(' + '.join(res) + ' = 0')
f.close()