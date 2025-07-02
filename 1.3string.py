# 多行字符用三层引号
print(
    """Hello
    world"""
)

a = "asdf"
b = "qwer"
c = "I'm a new Python learner."

print(type(a))
print(a + " " + b)

# 打印某一串字符
print(c[:7])

d = a * 10
print(d)

# 按照字符串里面的空格进行 分隔
print(c.split(" "))

# 统计某一个字符的数量
print(c.count("e"))

# 替换
e = d.replace("s", "a")
print(e)

# 查找(第一个)
print(e.find("aa"))

# 只有首字母是大写
print(" ".isalpha())
