# Base64 Numeric Translator
# Our standard numbering system is (Base 10). That includes 0 through 9.
# Binary is (Base 2), only 1’s and 0’s. And Hexadecimal is (Base 16) (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F).
# A hexadecimal “F” has a (Base 10) value of 15.
# (Base 64) has 64 individual characters which translate in value in (Base 10) from between 0 to 63.
# ####Write a method that will convert a string from (Base 64) to it's (Base 10) integer value.
# The (Base 64) characters from least to greatest will be
# ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/
# Where 'A' is equal to 0 and '/' is equal to 63.
# Just as in standard (Base 10) when you get to the highest individual integer 9 the next number adds an additional
# place and starts at the beginning 10; so also (Base 64) when you get to the 63rd digit '/'
# and the next number adds an additional place and starts at the beginning "BA".
# Example:
# base64_to_base10("/") # => 63
# base64_to_base10("BA") # => 64
# base64_to_base10("BB") # => 65
# base64_to_base10("BC") # => 66
# Write a method base64_to_base10 that will take a string (Base 64) number and output
# it's (Base 10) value as an integer.
import math


def base64_to_decimal(num64):
    base_64_chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
    decimal_num = 0
    for i in range(len(num64)):
        decimal_num += 64 ** (len(num64) - 1 - i) * base_64_chars.index(num64[i])
    return decimal_num


# Given a string of words, you need to find the highest scoring word.
# Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.
# You need to return the highest scoring word as a string.
# If two words score the same, return the word that appears earliest in the original string.
# All letters will be lowercase and all inputs will be valid.


def high(x):
    # Code here
    return 'none'


# Coding decimal numbers with factorials is a way of writing out numbers in a base system that depends on factorials,
# rather than powers of numbers.
# In this system, the last digit is always 0 and is in base 0!.
# The digit before that is either 0 or 1 and is in base 1!.
# he digit before that is either 0, 1, or 2 and is in base 2!, etc.
# More generally, the nth-to-last digit is always 0, 1, 2, ..., n and is in base n!.
# Read more about it at: http://en.wikipedia.org/wiki/Factorial_number_system
# Example
# The decimal number 463 is encoded as "341010", because:
# 463 = 3×5! + 4×4! + 1×3! + 0×2! + 1×1! + 0×0!
# If we are limited to digits 0..9, the biggest number we can encode is 10!-1 (= 3628799).
# So we extend 0..9 with letters A..Z. With these 36 digits we can now encode numbers up to 36!-1 (= 3.72 × 1041)
# Task
# We will need two functions. The first one will receive a decimal number and return a string with the
# factorial representation.
# The second one will receive a string with a factorial representation and produce the decimal representation.
# Given numbers will always be positive.


def dec_2_fact_string(nb):
    letters = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    out_string = ''
    count = 0
    while nb // math.factorial(count) > 0:
        count += 1
    for i in range(count - 1, -1, -1):
        out_string += letters[nb // math.factorial(i)]
        nb %= math.factorial(i)
    return out_string


def fact_string_2_dec(string):
    letters = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    nums = [math.factorial(i) * int(letters.index(string[-(i + 1)])) for i in range(len(string))]
    return sum(nums)


# Write a function, which takes a non-negative integer (seconds) as input and returns the time
# in a human-readable format (HH:MM:SS)
# HH = hours, padded to 2 digits, range: 00 - 99
# MM = minutes, padded to 2 digits, range: 00 - 59
# SS = seconds, padded to 2 digits, range: 00 - 59
# The maximum time never exceeds 359999 (99:59:59)
# You can find some examples in the test fixtures.


def make_readable(seconds):
    ss = seconds % 60
    if ss < 10: ss = '0' + str(ss)
    mm = seconds // 60 % 60
    if mm < 10: mm = '0' + str(mm)
    hh = seconds // 60 // 60
    if hh < 10: hh = '0' + str(hh)
    return f'{hh}:{mm}:{ss}'


cache = {0: 0, 1: 1}


def fibo(n):
    if n in cache:
        return cache[n]
    else:
        cache[n] = fibo(n - 1) + fibo(n - 2)
    return cache[n]


def perimeter(n):
    return sum([fibo(i) for i in range(n+2)]) * 4


#print(perimeter(5))

def dec_to_bin(n):
    bin_str = ''
    for i in range(3, -1, -1):
        if n // 2**i > 0:
            n %= 2**i
            bin_str += '1'
        else:
            bin_str += '0'
    return bin_str


str_pi = '141592653589793238462643383279502884197169399375105820974944592307816406286208998628034825\
34211706798214808651328230664709384460955058223172535940812848111745028410270193852110555964462294895493038196\
44288109756659334461284756482337867831652712019091456485669234603486104543266482133936072602491412737245870066\
06315588174881520920962829254091715364367892590360011330530548820466521384146951941511609433057270365759591953\
09218611738193261179310511854807446237996274956735188575272489122793818301194912983367336244065664308602139494\
63952247371907021798609437027705392171762931767523846748184676694051320005681271452635608277857713427577896091\
73637178721468440901224953430146549585371050792279689258923542019956112129021960864034418159813629774771309960\
51870721134999999837297804995105973173281609631859502445945534690830264252230825334468503526193118817101000313\
78387528865875332083814206171776691473035982534904287554687311595628638823537875937519577818577805321712268066\
130019278766111959092164201989'

#str_pi = str(math.pi)[2:]
list_pi = ''.join([dec_to_bin(int(i)) for i in str_pi])
list_pi = ''.join([' ' if i=='0' else '█' for i in list_pi])
#print(str_pi)
#print(list_pi)
#n = 17*4
#for i in range(0, len(list_pi), n):
#    print(list_pi[i:n+i])


# A format for expressing an ordered list of integers is to use a comma separated list of either
#
# individual integers
# or a range of integers denoted by the starting integer separated from the end integer in the range by a dash, '-'.
# The range includes all integers in the interval including both endpoints. It is not considered a range unless it
# spans at least 3 numbers. For example "12,13,15-17"
# Complete the solution so that it takes a list of integers in increasing order and returns a correctly
# formatted string in the range format.

# solution([-10, -9, -8, -6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20])
# # returns "-10--8,-6,-3-1,3-5,7-11,14,15,17-20"


def solution(args):
    group_list = [[args[0]]]
    count = 0
    res_count = 0
    for i in range(1, len(args)):
        if args[i] - group_list[count][res_count] == 1:
            group_list[count].append(args[i])
            res_count += 1
        else:
            res_count = 0
            count += 1
            group_list.append([0])
            group_list[count][res_count] = args[i]
    res_list = []
    for i in group_list:
        if len(i) < 3:
            for j in i:
                res_list.append(str(j))
        else:
            res_list.append(f'{i[0]}-{i[-1]}')

    return ','.join(res_list)


init_list = [-10, -9, -8, -6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20]
print(solution(init_list))

#fibo_list = [fib = lambda x: x if x in {0, 1} else fib(x-1) + fib(x-2) for i in range(10)]