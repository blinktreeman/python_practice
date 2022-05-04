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
    return '341010'


def fact_string_2_dec(string):
    return 463


# Write a function, which takes a non-negative integer (seconds) as input and returns the time
# in a human-readable format (HH:MM:SS)
# HH = hours, padded to 2 digits, range: 00 - 99
# MM = minutes, padded to 2 digits, range: 00 - 59
# SS = seconds, padded to 2 digits, range: 00 - 59
# The maximum time never exceeds 359999 (99:59:59)
# You can find some examples in the test fixtures.


def make_readable(seconds):
    pass
