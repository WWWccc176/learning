# 矩阵以及显示其性质的方法
import numpy as np

a = np.array([[1, 4, 3], [9, 2, 7]])
print(a)

print(a.shape)
print(a.size)

print(a[0, 1])  # 编号从0开始
print(a[:, [0, 2]])
