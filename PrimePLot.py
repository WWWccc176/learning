import matplotlib.pyplot as plt
import random
import math

# 1. 实现一个能够处理超大数字的质数判断程序
# 使用米勒-拉宾素性检验 (Miller-Rabin Primality Test)
# 因为对于 10^999 这样的数字，常规的试除法是绝对不可能完成的。
# k 是测试的轮数，轮数越多，结果越可靠。对于大数，k=10 已经非常可靠。
def is_prime(n, k=10):
    """
    使用米勒-拉宾算法判断一个大数n是否为质数。
    """
    # 处理基本情况
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False

    # 将 n-1 分解为 2^s * d 的形式
    d, s = n - 1, 0
    while d % 2 == 0:
        d //= 2
        s += 1

    # 进行 k 轮测试
    for _ in range(k):
        # 随机选择一个见证数 a
        a = random.randrange(2, n - 1)
        x = pow(a, d, n) # 计算 a^d mod n

        if x == 1 or x == n - 1:
            continue

        # 进行 s-1 次平方测试
        for _ in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            # 如果循环正常结束（没有break），说明 n 是合数
            return False
            
    # 如果通过所有 k 轮测试，则 n 极有可能是质数
    return True

# --- 主绘图逻辑 ---

# 2. 建立一个极坐标系
# 我们在一个实际的、可见的范围内进行绘图，以展示效果
# 遍历到 10^999 是不可能的，但我们的 is_prime 函数可以判断那么大的数
PLOT_RANGE_MAX = 20000 

print(f"将在 1 到 {PLOT_RANGE_MAX} 的范围内寻找质数并绘图...")

# 存储质数的角度和半径
# 对于 r*e^(i*r)，在极坐标中：
# 半径 (radius) = r
# 角度 (angle) = r (单位是弧度)
thetas = [] # 角度列表
radii = []  # 半径列表

# 3. 遍历数字，判断是否为质数，如果是则记录坐标
for r in range(2, PLOT_RANGE_MAX + 1):
    if is_prime(r):
        # 只有质数才能被描点
        thetas.append(r)
        radii.append(r)

print(f"找到了 {len(radii)} 个质数，开始绘图...")

# 创建一个图形和子图，并指定为极坐标投影
fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})

# 使用散点图在极坐标上描点
ax.scatter(thetas, radii, s=1.5, alpha=0.8) # s是点的大小, alpha是透明度

# 设置图表标题
ax.set_title(f'Prime Numbers Spiral up to {PLOT_RANGE_MAX}\nPoint(r, θ) = (prime, prime)', va='bottom')

# 显示图形
plt.show()

# --- 额外演示：测试一个非常大的数 ---
print("\n--- 大数测试 ---")
try:
    # 一个接近 10^50 的数，这是一个已知的质数 (梅森素数 M167)
    large_prime_candidate = pow(2, 167) - 1
    print(f"测试一个大数: 2^167 - 1 (有 {len(str(large_prime_candidate))} 位)")
    if is_prime(large_prime_candidate):
        print("结果: 这是一个质数。")
    else:
        print("结果: 这是一个合数。")

    # 一个普通的大合数
    large_composite = (pow(2, 100) - 1) * (pow(2, 100) - 3)
    print(f"\n测试一个大合数 (有 {len(str(large_composite))} 位)")
    if is_prime(large_composite):
        print("结果: 这是一个质数。")
    else:
        print("结果: 这是一个合数。")

except Exception as e:
    print(f"大数测试出错: {e}")
