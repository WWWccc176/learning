import pandas as pd
import matplotlib.pyplot as plt

# 1. 读取 Excel
#    如果 time 列是日期格式，可以加上 parse_dates 参数
df = pd.read_excel(
    "the velocity of M1 money stock.xlsx",
    sheet_name="the velocity of M1 money stock",
    parse_dates=["time"]
)

# 2. 确认列名
#    假设列名正好是 'time' 和 'the velocity of M1 money stock'
print(df.columns)

# 3. 绘制折线图
plt.figure(figsize=(10, 6))
plt.plot(df["time"], df["the velocity of M1 money stock"], marker="o", linestyle="-")
plt.xlabel("Time")
plt.ylabel("Velocity of M1 Money Stock")
plt.title("Time vs Velocity of M1 Money Stock")
plt.grid(True)
plt.xticks(rotation=45)    # x 轴刻度倾斜，防止重叠
plt.tight_layout()         # 自动调整子图参数，防止标签被截断
plt.savefig('M1_velocity_trend.png', dpi=300)
plt.show()