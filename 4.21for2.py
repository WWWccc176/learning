import math


def is_prime(n):
    if n <= 0:
        raise ValueError("numbershould be greater than 0")
    if n % 2 == 0:
        return False
    if n == 2:
        return True

    maxDivisor = math.isqrt(n)
    for i in range(3, maxDivisor + 1, 2):
        if n % i == 0:
            return False
    return True


for i in range(1, 50):
    print(i, " ", end="")
    if not is_prime(i):  # 特定条件
        continue

    print("hey its a prime number")
    print("we love prime numbers")
print("Done")
