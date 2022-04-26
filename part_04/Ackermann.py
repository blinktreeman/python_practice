# Написать программу вычисления функции Аккермана
#              | n + 1,                    m = 0;
#  A(m, n) =   | A(m - 1, 1),              m > 0, n = 0;
#              | A(m - 1, A(m, n - 1))     m > 0, n > 0.

from threading import Thread


def Ackermann(m, n):
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        thread = Thread(target=Ackermann, args=(m - 1, 1))
        thread.start()
        res = thread.get()
        return res
    elif m > 0 and n > 0:
        temp = m
        n = Ackermann(m, n - 1)
        return Ackermann(temp - 1, n)

print(Ackermann(3, 5))