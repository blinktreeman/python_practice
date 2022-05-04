# lambda функции: sum = lambda x: x+10; mult = lambda x: x**2; sum(mult(2))
# Функция map()
import math
import random


def select(f, col):
    return [f(x) for x in col]


def where(f, col):
    return [x for x in col if f(x)]


data = '1 2 3 5 8 15 23 38'.split()
print(data)
data = select(int, data)
print(data)
data = where(lambda e: not e % 2, data)
print(data)
data = list(select(lambda e: (e, e**2), data))
print(data)

data = '1 2 3 5 8 15 23 38'.split()
data = list(map(int, data))
print(data)
data = list(filter(lambda e: not e % 2, data))
print(data)
data = list(map(lambda e: [e, e**2, 1], data))
print(data)

# Функция zip()
print(data)
for i,j,k in zip(data[0], data[1], data[2]):
    print(i, j, k)

# Функция enumerate
data = '1 2 3 5 8 15 23 38'.split()
print(data)
for count, value in enumerate(data):
    print(count, value)

# map again
data = list(map(lambda e: random.randint(1, 100), range(0, 10)))
print(data)

# List Comprehension
data = [random.randint(1, 100) for i in range(10)]
print(data)
data = [my_rand for _ in range(10) if (my_rand := random.randint(1, 100)) % 2]
print(data)

if 67 in data: print('yes!')

n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print('({}) {}-{}' .format(''.join(str(n[:3])), n[3:6], n[6:]))
k = 5
lk = [_ for _ in range(1, k+1)]
print(lk)
n = (k-1)*k+1
print(n)

def dig_pow(n, p):
    # your code
    digits = [int(i) for i in str(n)]
    digits = [digits[i] ** (p + i) for i in range(len(digits))]
    print(digits)
    sum = 0
    for i in range(len(digits)): sum += i
    print(sum)
    if sum / n % 1 == 0: return sum / n
    return -1

print(dig_pow(89, 1))

n = 255
hex_str = '0123456789ABCDEF'
#str = hex_str[n // 16] + hex_str[n % 16]

def rgb(r, g, b):
    #your code here :)
    hex_str = '0123456789ABCDEF'
    rgb_list = [r, g, b]
    rgb_list = [255 if e > 255 else e for e in rgb_list]
    rgb_list = [0 if e < 0 else e for e in rgb_list]
    rgb_list = [hex_str[i // 16] + hex_str[i % 16] for i in rgb_list]
    return rgb_list


print(rgb(-10, 20, 300))
#    rgb_hex = hex_str[r//16] + hex_str[r%16]
#    rgb_hex += hex_str[g//16] + hex_str[g%16]
#    rgb_hex += hex_str[b//16] + hex_str[b%16]


#print(hex(n).split('x')[-1])

n = 3
part_2 = 0
part_3 = 0
for i in range(n):
    part_2 += 2 * n * i
print(part_2)
for i in range(n):
    part_3 += i ** 2
print(part_3)
res = n ** 3 - part_2 + part_3
print(res)


init_str = 'abcd'
#sum_of_nums = (len(init_str)*(len(init_str)-1)//2)
#print(sum_of_nums)
init_nums = [str(i) for i in range(len(init_str))]
#print(init_nums)
num_arr = []
for j in range(len(init_nums)):
    for i in range(len(init_nums)-1):
        init_nums.insert(len(init_nums)-i-2, init_nums.pop(-(i+1)))
        print(init_nums)
        num_arr.append(int(''.join(init_nums)))
num_arr.sort()
str_arr = [str(i) if len(str(i)) == len(init_nums) else '0' + str(i) for i in num_arr]
print(str_arr)
res_arr = []
for i in str_arr:
    temp = ''
    for j in i:
        temp += init_str[int(j)]
    if temp not in res_arr: res_arr.append(temp)
#res_arr_final = []
#res_arr_final = [i for i in res_arr if i not in res_arr_final] res_arr = [init_str[::-1]]
print(res_arr)

my_set = {'0', '1'}
print(my_set)
my_set.add('a')
print(my_set)
print(len(my_set))
if '1' in my_set: print('opps')

def add_in_set(lst):
    in_temp = []
    for i in lst:
        if i not in in_temp: in_temp.append(i)
    return in_temp
my_str = 'abcd'
init_str = '1234'

import itertools
#my_list = set(map(''.join, itertools.product(init_str, repeat=len(init_str))))
my_list = list(itertools.product(init_str, repeat=len(init_str)))
print(my_list)
hit_1 = [add_in_set(i) for i in my_list]
print(hit_1)
hit_2 = [''.join(i) for i in hit_1 if len(i) == len(init_str)]
hit_2.sort()
print(hit_2)
hit_3 = set(i for i in hit_2)
print(hit_3)
#hit_3 = set(map(''.join, hit_2))
#print(hit_3)

def permutations(string):
    init_nums = [str(i) for i in range(len(string))]
    num_arr = list(itertools.product(init_nums, repeat=len(init_nums)))
    print(num_arr)
    num_arr = [add_in_set(i) for i in num_arr]
    print(num_arr)
    num_arr = [''.join(i) for i in num_arr if len(i) == len(string)]
    print(num_arr)
    print(num_arr)
    res_arr = []
    for i in num_arr:
        temp = ''
        for j in i:
            temp += string[int(j)]
        if temp not in res_arr: res_arr.append(temp)
    return res_arr
print(permutations('abc'))

string = 'abcd'
init_nums = [str(i) for i in range(1, len(string)+1)]
num_arr = list(itertools.product(init_nums, repeat=len(init_nums)))
print(num_arr)
num_arr = [''.join(i) for i in num_arr]

print(num_arr)

list(itertools.permutations(string, len(string)))


def permutations(string):
    import itertools

    init_arr = set(itertools.permutations(string, len(string)))
    init_arr = [''.join(i) for i in init_arr]
    init_arr.sort()
    #print(init_arr)
    #res_arr = []
    #for i in init_arr:
       # if i not in res_arr: res_arr.append(i)

    return init_arr

print(permutations('aabb'))

text = 'Quis    custodiet  ipsos  custodes ?'
str_list = text.split()
str_list = [i.capitalize() for i in str_list]
print(' '.join(str_list))

str_05 = '- x + 1 = 9 - 2'
i = 0
while i < len(str_05):
    if str_05[i] == '-':
        str_05 = str_05[:i+1] + str_05[(i+2):]
    if str_05[i] == '+':
        str_05 = str_05[:i] + str_05[(i + 1):]
    i += 1

list_05 = str_05.split('=')
if 'x' in list_05[0]:
    x_part = list_05[0].split()
    not_x_part = list_05[1].split()
else:
    x_part = list_05[1].split()
    not_x_part = list_05[0].split()
not_x_part = [int(i) for i in not_x_part]
negative_flag = False
for i in x_part:
    if 'x' not in i:
        not_x_part.append(-int(i))
    else:
        negative_flag = '-' in i
res_sum = 0
for i in not_x_part:
    res_sum += i
#str_05 = [i for i in str_05 if i != ' ']
#print(str_05)
#str_05 = ''.join([i for i in str_05 if i != ' '])
#list_05 = [i for i in str_05 if i not in '+-=']
#list_05 = str_05.split('=')


        #str_05.pop(i+1)
#str_05 = ''.join([i for i in str_05 if i not in '-+'])
print(x_part)
print(not_x_part)
print(negative_flag)