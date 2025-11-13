import matplotlib
import matplotlib.pyplot as plt
import numpy as np

matplotlib.rcParams['font.sans-serif'] = ['SimHei']      # 指定默认字体
matplotlib.rcParams['font.family'] = 'sans-serif'
matplotlib.rcParams['axes.unicode_minus'] = False 

def is_prime(num):
    if num == 1 or num == 2:
        return True
    elif num <= 0 or num % 2 == 0:
        return False

    for j in range(2, 1 + int(np.ceil(np.sqrt(num)))):
        if num % j == 0:
            return False
    return True


Upper = 828

for i in range(1, Upper + 1):
    print(i, " ", end="")
    if not is_prime(i):  # 特定条件
        continue

    print("hey its a prime number")
    print("we love prime numbers")

print("Done")

x = np.arange(1, Upper + 1)

# 计算 π(x)
y_pi = []
cnt = 0
for xi in x:
    if is_prime(xi):
        cnt += 1
    y_pi.append(cnt)

# 计算 x/log(x)
# 为避免 log(1)=0 引发问题，我们从 x>=2 开始计算
y_approx = np.zeros_like(x, dtype=float)
mask = x >= 2
y_approx[mask] = x[mask] / np.log(x[mask])
# 绘图
plt.figure(figsize=(10, 6))
plt.plot(
    x, y_pi, "-o", markersize=3, linewidth=1, label="π(x)：质数累计数", color="blue"
)
plt.plot(x[mask], y_approx[mask], "--", linewidth=2, label="x / log(x)", color="red")

plt.xlabel("n")
plt.ylabel("累计值")
plt.title(f"1 到 {Upper} 的 π(x) 与 x/log(x) 对比")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.autoscale()
plt.show()
