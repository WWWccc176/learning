import numpy as np


def plusOne(f, x):
    return f(x) + 1


print(plusOne(np.sin, np.pi / 2))
print(plusOne(np.cos, np.pi / 2))
print(plusOne(np.sqrt, 25))


def power(a, b, c):
    return a**b + c


# 复合函数：power(sqrt(x), 2, 1)
def composite(x):
    sqrt_x = np.sqrt(x)
    return power(sqrt_x, 2, 1)


print(composite(9))

def print_hello():
    print('Hello')