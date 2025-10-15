import random
import string
import time
import sys

target_text = "Hello World! I'm Python."

# 定义一个干净的字符集
charset = string.ascii_letters + string.digits + string.punctuation + " "

current_list = [random.choice(charset) for _ in range(len(target_text))]
print("--- 开始模拟同步破解效果 ---")
print("".join(current_list))
time.sleep(1)

while "".join(current_list) != target_text:

    output_list = []

    for i in range(len(target_text)):
        # 如果当前位置的字符已经等于目标字符了
        if current_list[i] == target_text[i]:
            # 就直接“锁定”这个正确的字符
            output_list.append(target_text[i])
        else:
            # 否则，就为这个位置生成一个新的随机字符，实现“滚动”效果
            output_list.append(random.choice(charset))

    # 更新当前列表为我们刚刚生成的新一帧的列表
    current_list = output_list

    # --- 4. 打印当前帧 ---
    sys.stdout.write("".join(current_list) + "\n")
    # sys.stdout.write("".join(current_list) + '\r')#强制刷新更新字符
    sys.stdout.flush()

    # 短暂延迟，控制动画速度
    time.sleep(0.025)

print("".join(current_list))
print("---破解完成---")
