count = 0

while count < 10:
    print(count, " ", end="")  # end=是抑制输出后换行，引号内可以填任意的字符
    count += 1

print()  # not part of the while loop, 换行
print("Done")
