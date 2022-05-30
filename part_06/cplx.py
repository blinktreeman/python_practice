x = complex(1, 2)
y = complex(3, 4)


def init(complex_a, complex_b):
    global x
    global y
    x = complex(complex_a)
    y = complex(complex_b)
    return (x, y)


def sum():
    return x + y


def minus():
    return x - y


def mult():
    return x * y


def div():
    return x / y


init('2+4j','3-7j')

print(sum())
print(minus())
print(mult())
print(div())