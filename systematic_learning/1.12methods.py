#这些methods都生成浮点数
import numpy as np

a = np.zeros((2, 2))
a[0, 0] = 1
a[0, 1] = 2
a[1, 0] = 3
a[1, 1] = 4

print(a)

b = a
c = a

b = b + 4
c = c**2
d=b.T

print(b)
print(c)
print(b + c)  # 元素之间进行运算
print(d)

e = [1, 4, 9, 16]
print(np.sqrt(e))

x = np.array([1, 2, 4, 5, 9, 3])
y = np.array([0, 2, 8, 1, 2, 4])
print(x<y)

f=y[y>x]
print(f)