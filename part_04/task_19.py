# Составить список простых множителей натурального числа N


def prime_number(a):
    for i in list_mult:
        if i!=1 and a!=i and a%i == 0:
            return False
    return True


init_number = int(input('Задайте целое число '))
# Все множители
list_mult = [i for i in range(1, init_number) if not init_number%i]
# Простые числа в list_mult
list_prime = [i for i in list_mult if prime_number(i)]

print('Простые множители числа {}: {}' .format(init_number, list_prime))

# Output:
# Задайте целое число 30030
# Простые множители числа 30030: [1, 2, 3, 5, 7, 11, 13]
