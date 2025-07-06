import numpy as np

n = int(input("Input the shape of the matrix:"))

one = np.ones((n, n), dtype=int)


for i in range(0, n):
    for j in range(0, n):
        if (i + j) % 2 != 0:
            one[i, j] = 0

print(one)
