add_lambda = lambda x, y: x + y
print(add_lambda(3, 5))


words = ["apple", "kiwi", "banana", "pear"]
sorted_words = sorted(words, key=lambda s: len(s))  # 冒号后面就是函数
print(sorted_words)


def create_multiplier(n):
    return lambda x: x * n


double = create_multiplier(2)  # 这是两个函数
triple = create_multiplier(3)

print(double(5))  # 输出 10
print(triple(5))  # 输出 15
