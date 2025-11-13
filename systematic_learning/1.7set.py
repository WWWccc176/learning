# 性质同数学的set(无序，互异，确定)
a = {3, 3, 2, 3, 1, 4, 5, 6, 4, 2}
print(a)

print(set("banana"))

b = {1, 2, 3}
c = {3, 4, 5}

print(a | b)           # {1, 2, 3, 4, 5} 交
print(a & b)           # {3} 并
print(a - b)           # {1, 2} 差
print(a ^ b)           # {1, 2, 4, 5} 交+去重
print(a.issubset({1, 2, 3, 4}))  # 子集
