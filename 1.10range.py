import numpy as np

a = np.arange(0, 10, 1)  # (起，终，间隔)不含重点
print(a)

b = np.linspace(0, 10, 10)  # 浮点数
print(b)

print(a[3])
print(b[2:])
print(b[-1])

a[:3] = 1
print(a)

b[1:4]=3
print(b)