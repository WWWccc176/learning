a = "zxcv"
b = "hello,{}"
print(b.format(a))

format_string = "{artist} sang {song} in {year}"
print(format_string.format(artist="Paloma Faith", song="Guilty", year=2017))

# 冒号是规范符，不等号，尖号是左右居中
print("|{:<25}|".format("left aligned"))
print("|{:>25}|".format("right aligned"))
print("|{:^25}|".format("centered"))
print("{:,}".format(1234567890))  # 三位计点
print("{:,}".format(1234567890.0))
